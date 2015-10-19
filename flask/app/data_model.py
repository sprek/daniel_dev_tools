""" data_model
This class contains helper functions for interacting with an
sqlite3 database using a data model pattern.

Assumes that the class_name passed in to the functions has
member variables whose names match the columns in the database table
"""

def get_objects_from_db_result(class_name, db_result):
    """
    input: class_name - Class
           db_result -  sqlite3 result from a "select *" type query
    returns: list of Class objects
    """
    args_dict = {}
    cols = list_columns_from_result(db_result)
    results = db_result.fetchall()
    objects = []
    for result in results:
        for i, val in enumerate(result):
            args_dict[cols[i]] = val
        objects.append(class_name(**args_dict))
    return objects

def list_class_attributes(class_name):
    """
    input: class_name - Class
    returns: alphabetically sorted member variables for class_name
    """
    return sorted(class_name().__dict__.keys())

def list_columns_from_result(result):
    """
    input: result - sqlite3 result from a query
    returns: a list of the names for each column in the result input
             the order of the column names matches the order of the result input
    """
    return list(map(lambda x: x[0], result.description))

def get_class_vals(obj):
    """
    input: obj - object of type Class
    returns: list of member variable values of obj, sorted alphabetically by
             member variable name
    """
    vals = []
    for attr in sorted(type(obj).__dict__.keys()):
        vals.append(getattr(obj, attr))
    return vals

# --------------------------------------------------
# Database access functions

def get_objects_from_db(class_name, db):
    """
    input: class_name - Class
           table_name - string of table in database
           db - database
    returns: list of class_name objects in database
    """
    table_name = class_name.__name__.lower()
    cur = db.cursor()
    db_result = cur.execute("SELECT * FROM " + table_name)
    return get_objects_from_db_result(class_name, db_result)

def get_object_from_db_by_key(class_name, key_name, key_val, db):
    """
    input: class_name - Class
           key_name - string of name of key column
           key_val - value of the key
           db - database
    returns: class_name object that matches the item in the database,
             or None if not found
    """
    cur = db.cursor()
    table_name = class_name.__name__.lower()
    db_result = cur.execute("SELECT * FROM " + table_name + " where " + key_name + " = ?",
                            (key_val,))
    objects = get_objects_from_db_result(class_name, db_result)
    if len(objects) == 0:
        return None
    return objects[0]

def insert_object_into_db (obj, db):
    """
    input: obj - object to insert into database
           db - database
    """
    cur = db.cursor()
    table_name = type(obj).__name__.lower()
    attr_list = ','.join(list_class_attributes(type(obj)))
    val_list = ','.join(list(len(list_class_attributes(type(obj))) * '?'))
    cur.execute("INSERT INTO " + table_name + " (" + attr_list + ") VALUES (" + val_list + ")",
                get_class_vals(obj))
    db.commit()

def clear_table (class_name, db):
    """
    input: class_name - Class
    returns: db - database
    """
    table_name = class_name.__name__.lower()
    cur = db.cursor()
    cur.execute('DELETE FROM ' + table_name)
    db.commit()
