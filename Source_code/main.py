from predict import get_user_input
from API import get_rate_by_location, calculate_risk
from Population import return_population, return_locations
from login import *
from save_search import insert_new_data, get_user_data
from area_advice import provide_advice
from yes_no_input import get_yes_no_input


def run():
    """
    This function acts as the main body of the COVID calculator app. It works by calling the imported functions as
    previously defined in other files, and also by defining its own logic.
    """

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

        valid_nations = ['england', 'wales', 'scotland', 'northern ireland']

        if level == "nation" and location not in valid_nations :
            print("Error: The location you have selected is not a nation. Please try again.")
        elif level == "utla" and location in valid_nations:
            print("Error: The location you have selected is not an UTLA. Please try again.")
        else:
            break

    if location is None:
        print("Sorry you have exceeded the maximum number of attempts. You will now be logged out.")
        exit(-1)
    else:
        print("Fetching data for {}...".format(location.title()))

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


if __name__ == '__main__':
    run()

