import unittest
from dbconnection import _connect_to_db


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = "<class 'mysql.connector.connection_cext.CMySQLConnection'>"
        actual = str(type(_connect_to_db("population")))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
