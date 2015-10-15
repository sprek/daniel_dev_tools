import unittest, os, tempfile, sqlite3
import user, create_db

TEST_USER_VALUES1 = [1, 'daniel']

def clear_tables(db):
    cur = db.cursor()
    cur.execute('DELETE FROM user')
    db.commit()

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd = tempfile.mkstemp()
        create_db.create_db(self.db_fd[1])
        self.db = sqlite3.connect(self.db_fd[1])

    def tearDown(self):
        os.close(self.db_fd[0])
        os.remove(self.db_fd[1])

    def test_user_db(self):
        clear_tables(self.db)
        # insert user
        test_user = user.User (*TEST_USER_VALUES1)
        user.insert_user_into_db(test_user, self.db)
        get_user = user.get_user_from_db_by_name(test_user.name, self.db)
        assert(get_user == test_user)

if __name__ == '__main__':
    unittest.main(verbosity=2)
