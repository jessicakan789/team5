import requests
import json


def get_rate_by_location(level, location):
    """
    Fetches COVID cases data from the NHS API for a given location.

    :param level: (type: str)
    The level of location in use - Either 'UTLA' (Upper-Tier Local Authority) or 'Nation'
    :param location: (type: str)
    The name of the location in use
    :return:
    IF SUCCESSFUL :

    latest: (type: float)
    The number of COVID cases in the given location over the most recent 7 day period.

    ELSE:

    False (type: bool)
    """
    try:
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

        if level == "overview":
            result = requests.get(
                'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=overview&structure=',
                params=structure_params
            )
        else:
            result = requests.get(
                'https://api.coronavirus.data.gov.uk/v1/data?filters=areaName={};areaType={}&structure='
                .format(location, level),
                params=structure_params
            )

        latest = 0

        for i in range(0, 7):
            latest += int(result.json()['data'][i]['dailyCases'])

        print('Number of positive tests in this area in the last 7 days:', latest)

        return latest

    except (KeyError, requests.exceptions.JSONDecodeError):
        print("Sorry area type or area name not recognised.")
        return False


def calculate_risk(risk):
    """
    Outputs the appropriate message to the user depending on their calculated risk, and produces simple classifications
    to group users into "high", "medium" and "low" risk categories.

    :param risk: (type: float)
    A numerical value to approximate the user's risk of catching COVID, depending on current positive-test results in
    their area.

    :return:

    "high", "medium", or "low" (type: str)

    These return values are classifications of the users risk based on current positive-test results in their area.
    """
    if risk < 10:  # CDC COVID-19 Community Levels
        print("The rate of COVID in your area is {} in 100,000 people".format(round(risk * 100000)))
        print("Your risk is LOW")
        return "low"
    elif 10 <= risk <= 19.9:
        print("The rate of COVID in your area is {} in 100,000 people".format(round(risk * 100000)))
        print("Your risk is MEDIUM")
        return "medium"
    else:
        print("The rate of COVID in your area is {} in 100,000 people".format(round(risk * 100000)))
        print("Your risk is HIGH")
        return "high"

