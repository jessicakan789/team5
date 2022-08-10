import re
from db_utils import *
from save_search import populate_table
from yes_no_input import get_yes_no_input


class UsernameExistsError(Exception):
    """To be raised when username already exists"""
    pass


class CommonPasswordError(Exception):
    """To be raised if password is too easy to guess, based on list of common passwords"""
    pass


class RegexError(Exception):
    """To be raised if password doesn't satisfy REGEX conditions"""


class User:

    _existing_users = get_usernames()

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.location = None
        self.hint = None


class NewUser(User):

    # Underscore before these variable names denote that they are private members
    _is_Successful = False
    _common_passwords = ['Password123!', 'password', 'abc123!']
    _regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

    def is_unique(self):  # existing users would need to be fetched from database
        if self.username in self._existing_users:
            raise UsernameExistsError
        return True

    def common_passwords_checker(self):
        if self.password in self._common_passwords:
            raise CommonPasswordError
        return True

    def password_regex(self):
        if not re.fullmatch(self._regex, self.password):
            raise RegexError
        return True

    def make_new_user(self):
        try:
            if self.is_unique() and self.common_passwords_checker() and self.password_regex():
                add_new_user(self.username, self.password)
                populate_table(self.username)
                self._is_Successful = True
        except UsernameExistsError:
            print("Sorry, this username already exists. Please try again.")
        except CommonPasswordError:
            print("Your password is commonly used, and so may be easier to guess. Please try again.")
        except RegexError:
            print("Your password must be at-least 8 characters long, "
                  "containing at-least 1 uppercase letter, 1 lowercase letter, 1 number"
                  "and 1 special character!")
        else:
            print('New user account made. Welcome!')
        finally:
            return self._is_Successful


class ExistingUser(User):

    def login(self):
        if self.username in self._existing_users:
            if hash_password(self.password) == get_password(self.username):
                print("LOGIN SUCCESSFUL")
                return True
            else:
                print("LOGIN FAILED: Incorrect password")
        else:
            print("LOGIN FAILED: Username unrecognised")
        return False

    def add_location(self, location):
        self.location = location

    def add_hint(self):
        # hint and memorable word? in case forgot password?
        pass

    def forgot_password(self):
        # use hint to reset password
        pass


def register_or_login():

    account_exists = get_yes_no_input("Do you already have an account? y/n")

    if account_exists:
        status = existing_user_login()

    elif not account_exists:
        status = make_new_user()

    return status



def make_new_user():
    isSuccess = False
    while not isSuccess:
        username = input("Username: ")
        password = input("Password: ")

        new_user = NewUser(username,password)
        isSuccess = new_user.make_new_user()
    return isSuccess, username


def existing_user_login():
    isSuccess = False
    attempts = 0
    while not isSuccess and attempts < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        login_user = ExistingUser(username,password)
        isSuccess = login_user.login()

        attempts += 1

        if not isSuccess:
            print("You have {} attempts left.".format(3-attempts))

    if attempts >= 3:
        print("Sorry, you have exceeded the maximum number of attempts.")

    return isSuccess, username


