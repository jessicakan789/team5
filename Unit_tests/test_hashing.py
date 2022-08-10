import unittest
from hashing import hash_password


class HashTest(unittest.TestCase):
    def test_hash_password(self):
        expected = "6f1ed002ab5595859014ebf0951522d9"
        actual = hash_password("blah")
        self.assertEqual(expected, actual)

    def test_hash_error(self):
        with self.assertRaises(AttributeError):
            hash_password(1234)  # AttributeError: 'int' object has no attribute 'encode'


if __name__ == '__main__':
    unittest.main()
