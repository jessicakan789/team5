from Get_Location import *
from API import *
from loginsystem_oop import *

def main():

    start_page()
    locations = get_locations()

    location = get_user_input(locations)
    cases = get_cases_by_location(location,'utla')

    print("There are {} registered COVID cases in your area".format(cases))

    population = get_population(location)

    rate = cases/population

    if rate > 0.01:
        print("This is approximately {:.2f}% of the people in your area".format(rate))
    else:
        print("This is approximately < 0.01% of the people in your area".format(rate))





# Run the main code
main()