import requests
import json


def get_rate_by_location(location, level):
    structure = {
        "date": "date",
        "name": "areaName",
        "code": "areaCode",
        "dailyCases": "newCasesByPublishDate",
        "cumulativeCases": "cumCasesByPublishDate",
        "dailyDeaths": "newDeaths28DaysByPublishDate",
        "cumulativeDeaths": "cumDeaths28DaysByPublishDate"
    }

    structure_params = {
        "structure": json.dumps(structure, separators=(",", ":"))
    }

    result = requests.get(
        'https://api.coronavirus.data.gov.uk/v1/data?filters=areaName={};areaType={}&structure='
        .format(location, level),
        params=structure_params
    )

    latest = result.json()['data'][0]['dailyCases']
    print('dailyCases:', latest)

    if latest <= 100:
        print("Your risk of getting COVID is LOW")
        print("We recommend you wash your hands frequently")
    if 100 < latest <= 400:
        print("Your risk of getting COVID is MEDIUM")
        print("We recommend you wear a mask")
    if latest > 400:
        print("Your risk of getting COVID is HIGH")
        print("We recommend you take a LFD")


def run():
    print('############################')
    print('Hello, welcome to the COVID calculator')
    print('############################')
    print()

    try:
        location = input('What is your location? ')
        if location.isnumeric():
            raise ValueError

        level = input('How specific would you like the area to be? ')
        if level.isnumeric():
            raise ValueError

    except ValueError:
        print("Sorry wrong input format. Please try again")
        exit()

    print()

    get_rate_by_location(location.title(), level)

    print()
    print('Keep smiling and carry on!')


if __name__ == '__main__':
    run()

# Example
# bath and north east somerset
# utla
