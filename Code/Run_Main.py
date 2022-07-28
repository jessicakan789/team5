from team5.Code.Get_Location import *
from team5.Code.API import *

def main():

    # TO DO: FETCH LOCATIONS FROM DATABASE AND STORE IN LIST AS FOLLOWS

    locations = ['salford', 'barnet', 'barnsley', 'bath', 'bolton', 'blackpool', 'camden', 'dorset', 'sefton',
                 'sandwell']

    location = get_user_input(locations)
    rate = get_cases_by_location(location,'utla')

    print("There are {} registered COVID cases in your area".format(rate))



# Run the main code
main()