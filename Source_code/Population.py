from dbconnection import _connect_to_db

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
        FROM cutdownpopulation
        WHERE Area = '{}'
        """.format(input.upper())

        cursor.execute(query)

        result = cursor.fetchall()[0][0]
        print("population: ", result)
        cursor.close()

        return result

    except Exception:
        print('Sorry there has been an error')
        return False


# print(return_population('SoMerset'))

#  FETCH LOCATIONS FROM DATABASE AND STORE IN LIST
def return_locations():
    try:
        db_name = 'population'
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        query = """
        SELECT Area
        FROM cutdownpopulation
        """

        cursor.execute(query)

        result = cursor.fetchall()
        result_list = [x[0].lower() for x in result]
        cursor.close()

        return result_list

    except TypeError:
        print('Sorry there has been an error')
        return False
