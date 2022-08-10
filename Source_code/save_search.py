from dbconnection import _connect_to_db


def populate_table(username):

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
        print('Last time you searched for was {} and the local rate then was {} people / 100000'.format(
            last_area, last_rate))
        return True

    # except (_mysql_connector.MySQLInterfaceError, mysql.connector.errors.ProgrammingError, UnboundLocalError):
    #     return False

    except Exception as exc:
        print(exc)
        return False

