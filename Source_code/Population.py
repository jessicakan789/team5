from dbconnection import _connect_to_db


def return_population(input):
    """
    Fetches the population of the given input location from cutdownpopulation table in the population database.

    :param input: (type: str)
    This should be the location that we are getting the population of.

    :return:
    Either returns result (type: int) which is the fetched population number.
    Otherwise, returns False (type: bool) which signifies that the population couldn't be fetched.
    """

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
        print("The overall population of {} is {}. ".format(input, result))
        cursor.close()

        return result

    except Exception:
        print('Sorry there has been an error')
        return False


def return_locations():
    """
    Fetches the locations as stored within the cutdownpopulation table in the database.

    Note that this table has been edited to only contain locations compatible with the API.

    :return:
    result_list (type: list)
    This is a list of all locations stored within the database. The locations are str types.
    """

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
