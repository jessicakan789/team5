from predict import get_user_input
from API import get_rate_by_location, calculate_risk
from Population import return_population
from User import register_or_login, sign_in
from dbconnection import _connect_to_db
from user_update import insert_new_data, get_user_data


# These local encoded_password = password.encode()
#             hash_password = hashlib.md5(encoded_password).hexdigest()tions would be fetched from the database of upper-tier local authorities
locations = ['salford', 'barnet', 'barnsley', 'bath', 'bolton', 'blackpool', 'camden', 'dorset', 'sefton', 'sandwell']


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('Please use this information as one part of your own personal risk assessment')
    print('For personalised risk information you can visit OurRisk.CoV | COVID-19 Phenomics (covid19-phenomics.org) ')
    print('If you consider yourself to be high risk, please visit https://www.nhs.uk/conditions/coronavirus-covid-19/people-at-higher-risk/advice-for-people-at-high-risk/')
    print('for further information.')
    print('############################')
    print()

    register_or_login()

    try:
        level = input("Choose Nations or UTLA(Your Local Authority): ")
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

    print(location.title())
    rate = get_rate_by_location(level.lower(), location.title())
    pop = return_population(location.title())
    risk = rate/pop*10000
    calculate_risk(risk)
    print()

    print("UK")
    uk_rate = get_rate_by_location("overview", None)
    uk_pop = return_population("UNITED KINGDOM")
    uk_risk = uk_rate/uk_pop*10000
    calculate_risk(uk_risk)

    try:
        store_data = input('Do you want to store your latest information? y/n :')
        if store_data.isnumeric():
            raise ValueError

    except ValueError:
        print("Sorry wrong input format. Please try again")
        exit()


    else:
        if store_data == 'y':
            username = input('To save your information, please type in your username again ')
            get_user_data(username)
            insert_new_data(username, location, risk)
        elif store_data == 'n':
            print('No worries! Hope to see you soon!')
        else:
            print("Sorry that is not recognised, please try again some other time")






if __name__ == '__main__':
    run()


# Example
# black pool