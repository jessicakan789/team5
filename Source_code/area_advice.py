from dbconnection import _connect_to_db


def provide_advice(area):
    """
    This function connects to the database to identify the nation that the search area is in. It returns the
    relevant text file, containing COVID advice, depending on the nation identified.

    :param area: (type: str)
    The location for which we would live to identify the nation of. i.e. if the area = 'Leeds', the nation is 'England'.

    :return:
    If successful, returns a string value corresponding to the nation identified.

    Otherwise, returns False (type: bool) to signify that the nation could not be identified.
    """
    db_name = 'population'
    db_connection = _connect_to_db(db_name)
    cursor = db_connection.cursor()
    query = """
            SELECT Nation FROM cutdownpopulation where Area = '{}'
            """.format(area)
    cursor.execute(query)
    for region in cursor:
        print(region)

        if region[0] == 'England':
            with open('EnglandAdvice.txt', 'r') as England:
                for x in England:
                    print(x)
            return "England"

        elif region[0] == 'Scotland':
            with open('ScotlandAdvice.txt', 'r') as Scotland:
                for x in Scotland:
                    print(x)
            return "Scotland"

        elif region[0] == 'Wales':
            with open('WalesAdvice.txt', 'r') as Wales:
                for x in Wales:
                    print(x)
            return "Wales"

        elif region[0] == 'Northern Ireland':
            with open('NIAdvice.txt', 'r') as NI:
                for x in NI:
                    print(x)
            return "Northern Ireland"

    return False





