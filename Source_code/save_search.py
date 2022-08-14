from dbconnection import _connect_to_db


def populate_table(username):
    """
    Inserts a new entry into the user_area_data table in the population database. Should be used when a new account
    is created, to prepare for future functionality.

    :param username: (type: str)
    The username belonging to the account for which an entry is being made.

    :return: None
    """

    user = {'username': username}
    db_name = 'population'
    db_connection = _connect_to_db(db_name)
    cursor = db_connection.cursor()
    query = """Insert into user_area_data ({}) Values ('{}')""".format(
        'username', user['username'], )
    cursor.execute(query)
    db_connection.commit()
    cursor.close()


def insert_new_data(username, location, risk):
    """
    Stores data in the user_area_data in the population database. Specifically, stores the area and rate that the
    user has checked using the app against their username. This can then be compared within any future uses.

    :param username: (type: str)
    The username of the user whose data is being stored.
    :param location: (type: str)
    The location searched by the user.
    :param risk: (type: float)
    The numerical risk calculated for the user based on COVID cases in their location.

    :return:
    True/False (type: bool): A signifier of whether data was successfully saved in the database.
    """
    try:
        db_name = 'population'
        db_location = location
        db_rate = float(risk * 100000)

        info = {'username': username, 'last_area' : db_location, 'last_rate' : db_rate}
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
        
        UPDATE user_area_data SET
           last_area = '{}', last_rate = '{}'
            WHERE username = '{}'
            """.format(

            info['last_area'], info['last_rate'], info['username'])
        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        print('Your latest area and rate information is saved to your account. Thanks for using the Covid Calculator. '
              'See you soon!')
        return True

    except ValueError:
        return False

    except Exception as exc:
        print(exc)
        return False


def get_user_data(username):
    """
    Gets the last searched location and corresponding rate as stored in the user_area_data table in the population
    database.

    :param username: (type: str)
    The username belonging to the account whose data we are fetching.

    :return:
    True/False (type: bool): A signifier of whether data was successfully retrieved from the database.
    """
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
            SELECT last_area, last_rate FROM user_area_data where username = '{}'
            """.format(username)
        cursor.execute(query)
        for i in cursor:
            last_area = i[0]
            last_rate = i[1]
        cursor.close()
        db_connection.close()

        if last_area is not None:
            print('The last location you searched for was {} and the local rate then was {} people / 100000'.format(
                last_area, last_rate))
        return True

    except Exception as exc:
        print(exc)
        return False

