import sqlite3

def create_db(filename='database.db'):
    con = sqlite3.connect(filename)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS user")
        cur.execute("CREATE TABLE user (id_num INT, name TEXT)")
        #cur.execute("INSERT INTO user (id_num) VALUES (5)")
    con.close()

if __name__ == '__main__':
    create_db()
