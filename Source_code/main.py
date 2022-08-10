from predict import get_user_input
from API import get_rate_by_location, calculate_risk
from Population import return_population, return_locations
from login import *
from save_search import insert_new_data, get_user_data
from area_advice import provide_advice
from yes_no_input import get_yes_no_input


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('Please use this information as one part of your own personal risk assessment')
    print('For personalised risk information you can visit OurRisk.CoV | COVID-19 Phenomics (covid19-phenomics.org) ')
    print('If you consider yourself to be high risk, please visit '
          'https://www.nhs.uk/conditions/coronavirus-covid-19/people-at-higher-risk/advice-for-people-at-high-risk/')
    print('for further information.')
    print('############################')
    print()

    login_status, user = register_or_login()

    if not login_status:
        exit(-1)

    while True:
        try:
            level = input("Choose Nation or UTLA (Your Local Authority): ").strip().lower()

            if level != "utla" and level != "nation":
                raise ValueError

            break

        except ValueError:
            print("Sorry wrong input format. Please try again")
            continue

    locations = return_locations()
    location = get_user_input(locations, level)  # RETURNS MATCHED WORD

    print()

    print(location.title())
    rate = get_rate_by_location(level.lower(), location.title())
    pop = return_population(location.title())
    risk = rate/pop
    calculate_risk(risk)
    print()

    print("UK")
    uk_rate = get_rate_by_location("overview", None)
    uk_pop = return_population("UNITED KINGDOM")
    uk_risk = uk_rate/uk_pop
    calculate_risk(uk_risk)

    advice = get_yes_no_input('Would you like your national advice? y/n : ')

    if advice:
        provide_advice(location)            # need to use location to get nation from DB

    store_data = get_yes_no_input('Do you want to store your latest information? y/n : ')

    if store_data:
        username = input('To save your information, please type in your username again: ')
        if username.strip() == user:
            get_user_data(username)
            insert_new_data(username, location, risk)
        else:
            print("This input does not match! Data could not be saved.")
    else:
        print('No worries! Hope to see you soon!')

    # try:
    #     store_data = input('Do you want to store your latest information? y/n : ')
    #     if store_data.isnumeric():
    #         raise ValueError
    #
    # except ValueError:
    #     print("Sorry wrong input format. Please try again")
    #     exit()
    #
    # else:
    #     if store_data == 'y':
    #         username = input('To save your information, please type in your username again: ')
    #         if username.strip() == user:
    #             get_user_data(username)
    #             insert_new_data(username, location, risk)
    #         else:
    #             print("This input does not match! Data could not be saved.")
    #     elif store_data == 'n':
    #         print('No worries! Hope to see you soon!')
    #     else:
    #         print("Sorry that is not recognised, please try again some other time")


if __name__ == '__main__':
    run()

# Example
# black pool
