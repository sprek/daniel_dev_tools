import sqlite3

DATABASE = 'users.db'

def create_db(filename=DATABASE):
    con = sqlite3.connect(filename)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS user")
        cur.execute("CREATE TABLE user (id_num INT, name TEXT)")
    con.close()
if __name__ == '__main__':
    create_db()
