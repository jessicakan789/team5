from predict import get_user_input
from API import get_rate_by_location, calculate_risk
from Population import return_population, return_locations
from User import register_or_login


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('############################')
    print()

    if not register_or_login():
        exit()

    try:
        level = input("Choose Nations or UTLA: ")
        if (level.isnumeric()) or (level.lower() not in ["nations", "utla"]):
            raise ValueError

        locations = return_locations()
        location = get_user_input(locations)  # RETURNS MATCHED WORD
        if location is None or location.isnumeric():
            raise ValueError

    except ValueError:
        print("Sorry wrong input format. Please try again")
        exit()

    print()

    print(location)
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
    print()
    print('Keep smiling and carry on!')


if __name__ == '__main__':
    run()


# Example
# black pool