import mysql.connector
from hashing import hash_password
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


# To connect to the database
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# This fetches all locations from the database and returns a list
def get_locations():
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        # print("Connected to database")

        query = """
            SELECT Area FROM cutdownpopulation
        """
        cursor.execute(query)

        result = cursor.fetchall()
        result_list = [x[0] for x in result]
        # print("Locations retrieved")

    except Exception:
        raise DbConnectionError("Failed to get all locations from the database")

    else:
        if db_connection:
            db_connection.close()
            # print("Database connection closed.")
            return result_list


# This fetches the population count of a specific location from the database
def get_population(location):
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        # print("Connected to database")

        query = """
            SELECT Population FROM cutdownpopulation WHERE Area = '{}'
        """.format(location)

        cursor.execute(query)

        result = cursor.fetchall()[0][0]

        # print("Population count retrieved")

    except Exception:
        raise DbConnectionError("Failed to read population count from the database")

    else:
        if db_connection:
            db_connection.close()
            # print("Database connection closed.")
            return result

def get_existing_users():
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        # print("Connected to database")

        query = """
            SELECT username FROM user_info
        """

        cursor.execute(query)

        result = cursor.fetchall()
        result_list = [x[0] for x in result]

        # print("Usernames retrieved")

    except Exception:
        raise DbConnectionError("Failed to read usernames from the database")

    else:
        if db_connection:
            db_connection.close()
            # print("Database connection closed.")
            return result_list

def get_password(username):
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        # print("Connected to database")

        try:
            query = """
                SELECT password FROM user_info WHERE username = '{}'
             """.format(username)
        except Exception:
            print("Username doesn't exist!")

        cursor.execute(query)

        result = cursor.fetchall()[0][0]

        # print("Password retrieved")

    except Exception:
        raise DbConnectionError("Failed to get password from the database")

    else:
        if db_connection:
            db_connection.close()
            # print("Database connection closed.")
            return result

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
            # print("Database connection closed.")


# print(get_locations())
# print(get_population("Salford"))
# print(get_password('David'))
# print(add_new_user('emily2','password'))
print(get_existing_users())