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
    return data_model.get_objects_from_db(User, db)

def get_user_from_db_by_name(name, db):
    return data_model.get_object_from_db_by_key(User, "name", name, db)

def insert_user_into_db(user, db):
    data_model.insert_object_into_db(user, db)

def clear_table(db):
    data_model.clear_table(User, db)

