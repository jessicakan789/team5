# LOGIN PAGE
import re

username_password_dict = dict()  # store in database - import function from dbconnection.py


def register_or_login():
    try:
        answer = input("Have you already got an account? y/n ")
        if answer == "y":
            sign_in()
        else:
            create_new_account()
    except ValueError:
        print("Sorry please try again")


def create_new_account():
    print("Your username must have at least 8 letters.")
    name = input("Please input your username: ")
    if len(name) >= 8:
        username = name
    else:
        print("Invalid username. Please try again.")

    print("Your password must have at least 8 letters, an uppercase letter, lowercase letter, and special character.")
    word = input("Please input your password: ")
    regex = ["[0-9]", "[a-z]", "[A-Z]", "[?/!£$%^&*()'\",{}\\+=#~<>|`.@-]"]
    valid = False
    counter = 0
    if len(word) >= 8:
        for i in regex:
            if re.findall(i, word):
                counter += 1
        if counter == 4:
            valid = True

    if valid:
        password = word
        username_password_dict[username] = password
    else:
        print("Invalid password. Please try again.")


def sign_in():
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    attempts = 0
    while attempts < 2:  # 3 attempts in total
        if username_password_dict[username] == password:
            print("Successful login!")
            return
        else:
            print("Please try again.")
            username = input("Please input your username: ")
            password = input("Please input your password: ")
            attempts += 1


register_or_login()
