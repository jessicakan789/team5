from User import sign_in
from dbconnection import _connect_to_db
import mysql.connector
from dbconfig import HOST, USER, PASSWORD


def insert_new_data(location, risk):
    username = sign_in()[1]
    db_name = 'population'
    db_location = location
    db_rate = round(risk, 2)

    info = {'username': username, 'last_area' : db_location, 'last_rate' : db_rate}

    print(db_location, db_rate, username)

    db_connection = _connect_to_db(db_name)

    cursor = db_connection.cursor()

    print('connected to db')

    query = ("""UPDATE user_info SET
           last_area = '{}', last_rate = '{}'
            WHERE username = '{}'""".format(
    info['last_area'], info['last_rate'], info['username']))

    cursor.execute(query)
    db_connection.commit()
    #cursor.rowcount()
    cursor.close()
    db_connection.close()

insert_new_data('barnet', 1.5)