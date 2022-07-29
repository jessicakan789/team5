from dbconnection import _connect_to_db
import re


def register_or_login():
    try:
        answer = input("Have you already got an account? y/n ")
        if answer == "y":
            sign_in()
        else:
            create_user()
    except ValueError:
        print("Sorry please try again")


def sign_in():
    username = input("Please input your username: ")
    user_list = get_usernames()

    attempts = 0
    while attempts < 2:  # 3 attempts in total
        if username in user_list:
            password = input("Please input your password: ")
            print("Successful login!")
            return True
        else:
            print("Sorry username not found. Please try again.")
            username = input("Please input your username: ")
            attempts += 1

    print("Failed to login.")
    return False


def get_usernames():
    user_list = []
    db_name = 'population'
    db_connection = _connect_to_db(db_name)
    cursor = db_connection.cursor()
    query = """
    SELECT username from user_info
    """

    cursor.execute(query)
    for i in cursor:
        user_list.append(i[0])

    cursor.close()
    return user_list


def create_user():
    username = input('Please type in a Username: ')
    user_list = get_usernames()

    attempts = 0
    while attempts < 2:  # 3 attempts in total
        if username in user_list:
            print('Sorry that name is already taken. Please try again.')
            attempts += 1
            username = input('Please type in a Username: ')

        else:
            print("Your password must have at least 8 letters, an uppercase letter, lowercase letter, "
                  "and special character.")
            password = input("Please input your password: ")
            regex = ["[0-9]", "[a-z]", "[A-Z]", "[?/!£$%^&*()'\",{}\\+=#~<>|`.@-]"]
            valid = False
            counter = 0
            if len(password) >= 8:
                for i in regex:
                    if re.findall(i, password):
                        counter += 1
                if counter == 4:
                    valid = True

            if valid:
                stored_password = hash(password)
                new_user = {'username': username, 'password': stored_password}
                db_name = 'population'
                db_connection = _connect_to_db(db_name)
                cursor = db_connection.cursor()
                query = """Insert into user_info ({}) Values ('{}', '{}')""".format(
                    ', '.join(new_user.keys()), new_user['username'], new_user['password'])
                cursor.execute(query)
                db_connection.commit()
                print('Welcome!')
                cursor.close()

            else:
                print("Invalid password. Please try again.")

    if attempts == 2:
        print("Failed to create user account.")





