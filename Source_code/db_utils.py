from dbconnection import _connect_to_db
from hashing import hash_password


class DbConnectionError(Exception):
    """ To be raised if connection to the database cannot be established. """
    pass


def get_usernames():
    """
    Fetches usernames currently stored within the user_info table in the population database.

    Raises a DbConnectionError Exception if connection to the database cannot be established, meaning that usernames
    cannot be read. Otherwise, returns list of usernames in database.

    :param:

    None

    :return:

    user_list: (type: list)
    A list of all usernames stored in the user_info table. These usernames are strings.
    """
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
        SELECT username from user_info
        """

        cursor.execute(query)
        result = cursor.fetchall()
        user_list = [x[0] for x in result]

        cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from database.")

    finally:
        if db_connection:
            db_connection.close()
            return user_list


def get_password(username):
    """
    Gets the hashed password as stored in the user_info table in the population database corresponding to a specific
    (existing) username.
    Raises a DbConnectionError Exception if connection to database cannot be established.

    :param username: (type: str)
    The string username belonging to the account for which we want the password.

    :return:
    final_password: (type: str)
    The hashed password corresponding to the user account with the given username.
    """
    try:
        final_password = ''
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
            SELECT password FROM user_info where username = '{}'
            """.format(username)

        cursor.execute(query)

        for i in cursor:
            password = i[0]  # accesses bytearray in tuple
            unencoded_password = password.decode()  # decodes bytearray into string

        final_password = ''

        for x in unencoded_password:
            if x.isalnum():
                final_password = final_password + x  # removes binary data from start and end of decoded bytearray

    except Exception:
        raise DbConnectionError("Failed to read data from database.")

    finally:
        if db_connection:
            db_connection.close()
            return final_password


def add_new_user(username,password):
    """
    Adds a new user by writing data to the user_info table in the population database.

    :param username: (type: str)
    The string username value belonging to the new user account to be added.
    :param password: (type: str)
    The string password value belonging to the new user account to be added. This password should not be hashed when
    passed in. The hashing is done inside this function, utilising the external hash_password function.

    :return:

    True/False: (type: bool)
    A boolean value to signify whether the new user's account details were successfully stored in the database.
    """
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()

        query = """
            INSERT INTO user_info (username, password)
            VALUES ('{}','{}')
        """.format(username,hash_password(password))

        cursor.execute(query)
        db_connection.commit()
        cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from database.")

    finally:
        if db_connection:
            db_connection.close()
        return True

    return False



