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
        FROM population2020
        WHERE Area = '{}'
        """.format(input.upper())

        cursor.execute(query)

        for i in cursor:
            num = i[0]
            print("population: ", num)
        cursor.close()

        return num

    except Exception:
        print('Sorry there has been an error')
        exit(1)


# print(return_population('SoMerset'))
