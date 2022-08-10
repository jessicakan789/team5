import unittest
from db_utils import get_password, add_new_user, DbConnectionError


class PasswordTest(unittest.TestCase):
    def test_user_exists(self):
        expected = "a64eb7c6abe8010318b2f15cd7178699"  # the hash of password "L0u1sep00le@"
        actual = get_password("LouisePoole1")
        self.assertEqual(expected, actual)

    # def test_no_user(self):
    #     expected ="a64eb7c6abe8010318b2f15cd7178699"
    #     actual = get_password("LillyPoole")
    #     message = "This user does not exist"
    #     self.assertEqual(expected, actual, message)  # unencoded_password does not exist as user does not exist

    def test_no_user(self):
        expected = ''
        actual = get_password("DoesNotExist")  # user does not exist so returns empty string
        self.assertEqual(expected, actual)


class NewUserTest(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(add_new_user("BlahBlah", "blah"))

    def test_error(self):
        with self.assertRaises(DbConnectionError):
            add_new_user("blah")  # TypeError: add_new_user() missing 1 required positional argument: 'password'


if __name__ == '__main__':
    unittest.main()

