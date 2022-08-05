import unittest
from login import get_password


class PasswordTest(unittest.TestCase):
    def test_user_exists(self):
        expected = "a64eb7c6abe8010318b2f15cd7178699"  # the hash of password "L0u1sep00le@"
        actual = get_password("LouisePoole1")
        self.assertEqual(expected, actual)

    def test_no_user(self):
        with self.assertRaises(UnboundLocalError):  # unencoded_password does not exist as user does not exist
            get_password("blah")  # user does not exist


if __name__ == '__main__':
    unittest.main()
