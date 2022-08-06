from dbconnection import _connect_to_db
import re
import hashlib
# username = 'Louise'
# new_user_2 = {'username' : username}
# db_name = 'population'
# db_connection = _connect_to_db(db_name)
# cursor = db_connection.cursor()
# query_2 = "Insert into user_area_data ('username') Values ('{}',)", (new_user_2['username'],)
# cursor.execute(query_2)
# db_connection.commit()
# cursor.close()


# new_user_2 = {'username' : username}
                # db_name = 'population'
                # db_connection = _connect_to_db(db_name)
                # cursor = db_connection.cursor()
                # query_2 = """Insert into user_area_data ('username') Values ('{}')""".format(new_user_2['username'])
                # cursor.execute(query_2)
                # db_connection.commit()
                # cursor.close()


def insert_new_data(username, location, risk):
    db_name = 'population'
    db_location = location
    db_rate = float(risk)

    info = {'username': username, 'last_area' : db_location, 'last_rate' : db_rate}
    db_connection = _connect_to_db(db_name)
    cursor = db_connection.cursor()
    # query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
    #     ', '.join(record.keys()),
    #     record['OrderDate'],
    #     record['Region'],
    #     record['Rep'],
    #     record['Item'],
    #     record['Units'],
    #     record['UnitCost'],
    #     record['Total'],
    #)
    query = ("""INSERT INTO user_area_data ({}) VALUES ('{}', '{}', '{}')""".format(', '.join(info.keys()),
                                                        info['username'], info['last_area'], info['last_rate'],))
    # query = ("""UPDATE user_info SET
    #        last_area = '{}', last_rate = '{}'
    #         WHERE username = '{}'""".format(
    # info['last_area'], info['last_rate'], info['username']))
    cursor.execute(query)
    db_connection.commit()
    cursor.close()
#
insert_new_data('LouisePoole15', 'somerset', 1.4)