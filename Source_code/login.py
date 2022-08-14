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
    """
    Class to store data belonging to User accounts.

    Attributes: Username (type: str), Password (type: str), Location (type: str)
    Username: The username belonging to an account.
    Password: The password belonging ot an account.
    Location: The last used location stored in the account.

    """

    _existing_users = get_usernames()

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.location = None
        self.hint = None


class NewUser(User):
    """
    Class to store data/define methods belonging to new users i.e. those without an existing account.
    """

    # Underscore before these variable names denote that they are private members
    _is_Successful = False
    _common_passwords = ['Password123!', 'password', 'abc123!']
    _regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

    def is_unique(self):
        # This method is used to check whether a username has already been taken.
        # We require all usernames to be unique.
        if self.username in self._existing_users:
            raise UsernameExistsError
        return True

    def common_passwords_checker(self):
        # This method is used to check whether a password is a particularly 'common' one.
        # This avoids weak passwords, and encourages users to have better account security.
        if self.password in self._common_passwords:
            raise CommonPasswordError
        return True

    def password_regex(self):
        # This method is used to check whether the password follows the predefined regex rules.
        # This regex is stored in the private _regex attribute.
        if not re.fullmatch(self._regex, self.password):
            raise RegexError
        return True

    def make_new_user(self):
        # This method can be called to store a new users account details to the database.
        # The method performs all necessary checks, ensuring that the username is unique, and the password follows
        # necessary rules.
        # If any rules are invalid, appropriate Exceptions are raised, and the User is presented with an error message.

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
    """
    Class to store data/define methods belonging to existing users i.e. those with an account.
    """

    def login(self):
        # This method can be used to validate the user's login details matches those stored within the database.
        # The user will be presented within a message to say login was successful, or a reason as to why the
        # login failed.

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
        # This method can be used to update the location attribute belonging to an existing user.
        self.location = location


def register_or_login():
    """
    This function should be called to act as the 'Start' page for the COVID calculator app.
    This gives the user the option of logging in or making an account.

    :return:
    status (type: tuple) -
    A tuple containing a boolean True/False value in the first index. This signifies whether the login/registration
    was completed successfully. The second index stores the account username.

    """

    account_exists = get_yes_no_input("Do you already have an account? y/n")

    if account_exists:
        print("Please enter your Log-In details... ")
        status = existing_user_login()

    elif not account_exists:
        print("Please register to user the Covid Calculator app... ")
        status = make_new_user()

    return status


def make_new_user():
    """
    This function allows the user to make a new account. The function will ask the user to make an account repeatedly
    until valid account details have been given and the account has been successfully registered, through storing
    the details in the database.

    :return:

    Returns a tuple containing isSuccess (type: bool), and username (type: str)
    isSuccess is an indicator as to whether the account was successfully created.
    username is the (prospective) username of the account being created.
    """
    isSuccess = False
    while not isSuccess:
        username = input("Username: ")
        password = input("Password: ")

        new_user = NewUser(username,password)
        isSuccess = new_user.make_new_user()
    return isSuccess, username


def existing_user_login():
    """
    This function allows the user to log-in to an existing account. The function will give the user 3 attempts to
    access an account. If these 3 attempts are exceeded, the program will terminate prematurely.
    The details provided by the user are stored in an ExistingUser class instance, and then compared with the stored
    account details in the database.

    :return:

    Returns a tuple containing isSuccess (type: bool) in the first index. This is an indicator as to whether the log-in
    was successful. The second index stores the username (type: str) variable, which is the username of the account
    trying to be logged into.
    """
    isSuccess = False
    attempts = 0
    while not isSuccess and attempts < 3:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        login_user = ExistingUser(username,password)
        isSuccess = login_user.login()

        if not isSuccess:
            attempts += 1
            print("You have {} attempts left.".format(3-attempts))

    if attempts >= 3:
        print("Sorry, you have exceeded the maximum number of attempts.")

    return isSuccess, username


