import unittest
from dbconnection import _connect_to_db


class DbConnectionTest(unittest.TestCase):
    def test_connection_works(self):
        expected = "<class 'mysql.connector.connection_cext.CMySQLConnection'>"
        actual = str(type(_connect_to_db("population")))
        self.assertEqual(expected, actual)

    def test_connection_fail(self):
        with self.assertRaises(Exception):
            _connect_to_db("hello")  # database "hello" does not exist


if __name__ == '__main__':
    unittest.main()
