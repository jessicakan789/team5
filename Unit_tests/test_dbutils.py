import unittest
from db_utils import get_password, add_new_user


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
        actual = get_password("blah")  # user does not exist so returns empty string
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
