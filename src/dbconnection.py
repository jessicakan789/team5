from concurrent.futures import process
import mysql.connector
from dbconfig import HOST, USER


# Create a database connection
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        # password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# #check connection works
# #print(_connect_to_db(population))
#
# db_name = 'population'
# db_connection = _connect_to_db(db_name)
# cursor = db_connection.cursor()
# print("Connected to database")
#
# # query = """
# # SELECT Population
# # FROM 2020population
# # WHERE Area = 'UNITED KINGDOM'
# # """
#
#
# query = """
# SELECT Population
# FROM 2020population
# WHERE Area = 'SOMERSET'
# """
#
# cursor.execute(query)
# for row in cursor:
#     num = row[0]
#     print(num)
#     print(type(num))
