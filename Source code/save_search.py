from dbconnection import _connect_to_db

def insert_new_data(username, location, risk):
    try:
        db_name = 'population'
        db_location = location
        db_rate = float(risk)*100000

        info = {'username': username, 'last_area' : db_location, 'last_rate' : db_rate}
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = ("""UPDATE user_area_data SET
           last_area = '{}', last_rate = '{}'
            WHERE username = '{}'""".format(
        info['last_area'], info['last_rate'], info['username']))   #saves number of people/100000 in db
        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        db_connection.close()
        print('Your latest area and rate information is saved to your account. Thanks for using the Covid Calculator. '
          'See you soon!')

    except mysql.connector.Error as error:
        print('Failed to insert record into database')


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

    except mysql.connector.Error as error:
        print("Failed to insert record into database")


