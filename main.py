from predict import get_user_input
from API import get_rate_by_location
from dbconnection import return_population

# These locations would be fetched from the database of upper-tier local authorities
locations = ['salford', 'barnet', 'barnsley', 'bath', 'bolton', 'blackpool', 'camden', 'dorset', 'sefton', 'sandwell']


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('############################')
    print()

    try:
        location = get_user_input(locations)  # RETURNS MATCHED WORD
        if location.isnumeric():
            raise ValueError

    except ValueError:
        print("Sorry wrong input format. Please try again")
        exit()

    print()

    rate = get_rate_by_location(location.title())
    pop = return_population(location.title())
    risk = rate/pop*1000

    if risk <= 1:
        print("Your risk of getting COVID is LOW")
        print("We recommend you wash your hands frequently")
    if 1 < risk <= 2:
        print("Your risk of getting COVID is MEDIUM")
        print("We recommend you wear a mask")
    if risk > 2:
        print("Your risk of getting COVID is HIGH")
        print("We recommend you take a LFD")

    print()
    print('Keep smiling and carry on!')


if __name__ == '__main__':
    run()


# Example
# black pool