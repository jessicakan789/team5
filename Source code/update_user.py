from User import sign_in
from dbconnection import _connect_to_db

def insert_new_data(location, risk):
    username = sign_in()
    db_name = 'population'
    db_location = location
    db_rate = round(risk, 2)
    user_name = sign_in()
    info = (db_location, db_rate, user_name)
    print(db_location, db_rate, username)
    db_connection = _connect_to_db(db_name)
    cursor = db_connection.cursor()
    print('connected to db')
    query = ("""INSERT INTO user_info 
           (last_area, last_rate) 
           VALUES ('{}','{}')
            WHERE username = '{}'""".format(
    info['db_location'], info['db_rate'], username))

    cursor.execute(query)
    db_connection.commit()
    cursor.close()