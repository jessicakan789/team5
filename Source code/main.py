from predict import get_user_input
from API import get_rate_by_location, calculate_risk
from Population import return_population
from User import register_or_login, sign_in
from dbconnection import _connect_to_db
from db_insert import insert_new_data


# These local encoded_password = password.encode()
#             hash_password = hashlib.md5(encoded_password).hexdigest()tions would be fetched from the database of upper-tier local authorities
locations = ['salford', 'barnet', 'barnsley', 'bath', 'bolton', 'blackpool', 'camden', 'dorset', 'sefton', 'sandwell']


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('############################')
    print()

    register_or_login()


    try:
        level = input("Choose Nations or UTLA: ")
        if level.isnumeric():
            raise ValueError

        location = get_user_input(locations)  # RETURNS MATCHED WORD
        if location.isnumeric():
            raise ValueError

    except ValueError:
        print("Sorry wrong input format. Please try again")
        exit()

    except KeyError:
        print("Sorry area type or area name not recognised.")

    print()

    print(location)
    rate = get_rate_by_location(level.lower(), location.title())
    pop = return_population(location.title())
    risk = rate/pop*1000
    calculate_risk(risk)
    print()
    insert_new_data(location, risk)


    print("UK")
    uk_rate = get_rate_by_location("overview", None)
    uk_pop = return_population("UNITED KINGDOM")
    uk_risk = uk_rate/uk_pop*1000
    calculate_risk(uk_risk)
    print()
    print('Keep smiling and carry on!')








if __name__ == '__main__':
    run()


# Example
# black pool