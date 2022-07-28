import re

class UsernameExistsError(Exception):
    """To be raised when username already exists"""
    pass

class CommonPasswordError(Exception):
    """To be raised if password is too easy to guess, based on list of common passwords"""
    pass

class RegexError(Exception):
    """To be raised if password doesn't satisfy REGEX conditions"""


class User():

    # Underscore before these variable names denote that they are private members
    _is_Successful = False
    _common_passwords = ['password123', 'password', 'abc123']
    _existing_users = ['bob12', 'emily']  # These would be fetched from database in function ...
    _regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.location = None
        self.hint = None

    def is_unique(self):  # existing users would need to be fetched from database
        if self.username in self._existing_users:
            raise UsernameExistsError
        return True

    def common_passwords_checker(self):
        if self.password in self._common_passwords:
            raise CommonPasswordError
        return True

    def password_regex(self):
        if not re.fullmatch(self._regex,self.password):
            raise RegexError
        return True

    def make_new_user(self):
        try:
            if self.is_unique() and self.common_passwords_checker() and self.password_regex():
                # Need an external 'add to database' function ?
                print("Adding to database...")
                self._is_Successful = True
        except UsernameExistsError:
            print("Sorry, this username already exists. Please try again.")
        except CommonPasswordError:
            print("Your password is commonly used, and so may be easier to guess. Please try again.")
        except RegexError:
            print("Your password must be at-least 8 characters long, "
                  "containing at-least 1 uppercase letter, 1 lowercase letter, and 1 number!")
        else:
            print("Database... Success?")
        finally:
            return self._is_Successful

    def add_location(self,location):
        self.location = location

    def add_hint(self):
        # hint and memorable word? incase forgot password?
        pass

    def forgot_password(self):
        # use hint to reset password
        pass

    def encrypt_password(self):
        # hash the password and username before storing
        # may have to use encryption instead as I don't think you can unhash pythons hash() function
        pass

    def decrypt_password(self):
        #unhash
        pass

    # def login(self,login_user,login_pass):
    #     # search for usernmae and password in database ...
    #     pass


# class Admin(User):
    #  an admin class that inherits from user ... ?


def make_new_user():
    isSuccess = False
    while isSuccess==False:
        username = input("Username:")
        password = input("Password:")

        new_user = User(username,password)
        isSuccess = new_user.make_new_user()


def existing_user_login():
    pass



"""
when user has logged in.. then type in location... store this in database?
then automatically display info when logged in...

guest???

forgot password?

memorable info?




"""