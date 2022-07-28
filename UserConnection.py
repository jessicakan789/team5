# from dbconnection import _connect_to_db
import _mysql_connector

from dbconfig import USER, PASSWORD, HOST
import mysql.connector

def _connect(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_usernames():
    user_list = []
    db_name = 'population'
    db_connection = _connect(db_name)
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
    if username in user_list:
        print('sorry that name is already taken')

    else:
        password = input('Please type in an password. This has to be at least 8 characters long: ')
        if len(password) < 8:
            print('Please enter a password which is more than 8 characters long')
        else:
            stored_password = hash(password)
            new_user = {'username': username, 'password': stored_password}
            db_name = 'population'
            db_connection = _connect(db_name)
            cursor = db_connection.cursor()
            query = """Insert into user_info ({}) Values ('{}', '{}')""".format(', '.join(new_user.keys()),
                                                                        new_user['username'],
                                                                        new_user['password']
                                                                        )
            cursor.execute(query)
            db_connection.commit()
            print('Welcome!')
            cursor.close()

create_user()




