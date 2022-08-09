from dbconnection import _connect_to_db
from hashing import hash_password


class DbConnectionError(Exception):
    pass

def get_usernames():
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
            # print("Database connection closed.")
            return user_list


def get_password(username):
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
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        # print("Connected to database")

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

def area_info_usernames():
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
        SELECT username from user_area_data
        """

        cursor.execute(query)
        result = cursor.fetchall()
        user_area_data_list = [x[0] for x in result]

        cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from database.")
    finally:
        if db_connection:
            db_connection.close()
            # print("Database connection closed.")
            return user_area_data_list



