import unittest
from login import *
import random
import string

# Generate random string for use in some unit-tests
def get_random_string():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(8))



class NewUserClassTests(unittest.TestCase):

    def test_is_unique(self):
        while True:
            random_user = get_random_string()
            if random_user not in get_usernames():
                user1 = NewUser(random_user, 'Dinosaur123!')
                self.assertTrue(user1.is_unique())
                break
            else:
                continue

    def test_is_unique_exception(self):
        existing_username = get_usernames()[0]
        user1 = NewUser(existing_username,'Password123!')
        with self.assertRaises(UsernameExistsError):
            user1.is_unique()


    def test_common_passwords_checker(self):
        user1 = NewUser('test_user','Password123!')
        with self.assertRaises(CommonPasswordError):
            user1.common_passwords_checker()

    def test_password_regex_too_short(self):
        user1 = NewUser('test_user', 'Pp123!')
        with self.assertRaises(RegexError):
            user1.password_regex()

    def test_password_regex_no_uppercase(self):
        user1 = NewUser('test_user', 'password123!')
        with self.assertRaises(RegexError):
            user1.password_regex()

    def test_password_regex_no_lowercase(self):
        user1 = NewUser('test_user', 'PASSWORD123!')
        with self.assertRaises(RegexError):
            user1.password_regex()

    def test_password_regex_no_numbers(self):
        user1 = NewUser('test_user', 'Password!')
        with self.assertRaises(RegexError):
            user1.password_regex()

    def test_password_regex_no_special_chars(self):
        user1 = NewUser('test_user', 'Password1234')
        with self.assertRaises(RegexError):
            user1.password_regex()


    def test_password_regex_valid(self):
        user1 = NewUser('test_user','Password123!')
        self.assertTrue(user1.password_regex())


class ExistingUserClassTests(unittest.TestCase):

    def test_login_success(self):
        # This username and password needs to be in the database for test to pass
        existing_username = 'emily2'
        existing_password = 'Pumpkin123!'

        user1 = ExistingUser(existing_username, existing_password)

        self.assertTrue(user1.login())

    def test_login_wrong_password(self):
        existing_username = get_usernames()[0]
        existing_password = get_password(existing_username)

        incorrect_password = existing_password + get_random_string()

        user1 = ExistingUser(existing_username, incorrect_password)

        self.assertFalse(user1.login())

    def test_login_wrong_username(self):
        existing_username = get_usernames()[0]
        existing_password = get_password(existing_username)

        incorrect_username = existing_password + get_random_string()

        user1 = ExistingUser(incorrect_username, existing_password)

        self.assertFalse(user1.login())


if __name__ == '__main__':
    unittest.main()
