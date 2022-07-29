from dbconfig import USER, PASSWORD, HOST
import mysql.connector


# Create a database connection
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
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


"""
function to query db and return information
makes input case insensitive
returns a tuple so this is -> int
"""


def return_population(input):
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
        SELECT Population
        FROM population2020
        WHERE Area = '{}'
        """.format(input.upper())

        cursor.execute(query)

        for i in cursor:
            num = i[0]
            print("population: ")
            print(num)
        cursor.close()

        return num

    except Exception:
        print('Sorry there has been an error')
        exit(1)


# print(return_population('SoMerset'))






