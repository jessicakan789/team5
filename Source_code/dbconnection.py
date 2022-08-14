import mysql.connector
from dbconfig import HOST, USER, PASSWORD


def _connect_to_db(db_name):
    """
    Sets up a connection to the database.

    :param db_name: (type: str)
    The name of the database that is being connected to. For the COVID Calculator app this is the 'population' database.
    :return:

    cnx: (type: MySQL connector Class - <class 'mysql.connector.connection_cext.CMySQLConnection'>)
    The connection object for the database.

    """
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

