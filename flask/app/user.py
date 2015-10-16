import sqlite3

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
    return _get_users_from_db_result(db_result)

def get_user_from_db_by_name(name, db):
    cur = db.cursor()
    db_result = cur.execute("SELECT * FROM user where name = ?", (name,))
    users = _get_users_from_db_result(db_result)
    if len(users) == 0:
        return None
    return users[0]

def insert_user_into_db(user, db):
    cur = db.cursor()
    attr_list = ','.join(_list_user_attributes())
    val_list = ','.join(list(len(_list_user_attributes()) * '?'))
    cur.execute("INSERT INTO user (" + attr_list + ") VALUES (" + val_list + ")",
                _get_user_vals(user))
    db.commit()

def _get_users_from_db_result(db_result):
    args_dict = {}
    cols = _list_columns_from_result(db_result)
    results = db_result.fetchall()
    users = []
    for result in results:
        for i, val in enumerate(result):
            args_dict[cols[i]] = val
        users.append(User(**args_dict))
    return users

def _list_user_attributes():
    return sorted(User().__dict__.keys())

def _list_columns_from_result(result):
    return list(map(lambda x: x[0], result.description))

def _get_user_vals(user):
    vals = []
    for attr in sorted(User().__dict__.keys()):
        vals.append(getattr(user, attr))
    return vals
