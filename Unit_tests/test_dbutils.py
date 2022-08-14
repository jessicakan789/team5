import unittest
from db_utils import get_password, add_new_user
from unittest.mock import patch


class PasswordTest(unittest.TestCase):
    def test_user_exists(self):
        expected = "a64eb7c6abe8010318b2f15cd7178699"  # the hash of password "L0u1sep00le@"
        actual = get_password("LouisePoole1")
        self.assertEqual(expected, actual)

    def test_no_user(self):
        expected = ''
        actual = get_password("DoesNotExist")  # user does not exist so returns empty string
        self.assertEqual(expected, actual)


class NewUserTest(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(add_new_user("BlahBlah", "blah"))

    def test_error(self):
        with self.assertRaises(TypeError):
            add_new_user("blah")  # TypeError: add_new_user() missing 1 required positional argument: 'password'

    @patch('db_utils.get_password')
    def test_get_password_true(self, mock_username):
        username = "LouisePoole"
        mock_username.return_value = username
        expected = ('')
        actual = get_password(mock_username)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()

