from predict import get_user_input
from API import get_rate_by_location

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

    get_rate_by_location(location.title())

    print()
    print('Keep smiling and carry on!')


if __name__ == '__main__':
    run()


# Example
# black pool
