""" user
Provides the User class that matches the "user" table in the database
"""

import data_model

class User:
    def __init__(self, id_num=-1, name=''):
        self.id_num = id_num
        self.name   = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

def get_user_ids_from_db(db):
    return list(map(lambda x: x.id_num, get_users_from_db(db)))

def get_users_from_db(db):
    cur = db.cursor()
    db_result = cur.execute("SELECT * FROM user")
    return data_model.get_objects_from_db_result(User, db_result)

def get_user_from_db_by_name(name, db):
    cur = db.cursor()
    db_result = cur.execute("SELECT * FROM user where name = ?", (name,))
    users = data_model.get_objects_from_db_result(User, db_result)
    if len(users) == 0:
        return None
    return users[0]

def insert_user_into_db(user, db):
    cur = db.cursor()
    attr_list = ','.join(data_model.list_class_attributes(User))
    val_list = ','.join(list(len(data_model.list_class_attributes(User)) * '?'))
    cur.execute("INSERT INTO user (" + attr_list + ") VALUES (" + val_list + ")",
                data_model.get_class_vals(User, user))
    db.commit()

def clear_table(db):
    cur = db.cursor()
    cur.execute('DELETE FROM user')
    db.commit()

