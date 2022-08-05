from dbconnection import _connect_to_db


def provide_advice(area):
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

        elif region[0] == 'Scotland':
            with open('ScotlandAdvice.txt', 'r') as Scotland:
                for x in Scotland:
                    print(x)

        elif region[0] == 'Wales':
            with open('WalesAdvice.txt', 'r') as Wales:
                for x in Wales:
                    print(x)

        elif region[0] == 'Northern Ireland':
            with open('NIAdvice.txt', 'r') as NI:
                for x in NI:
                    print(x)



#provide_advice('Northern Ireland')




