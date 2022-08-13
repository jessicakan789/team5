import requests
import json


def get_rate_by_location(level, location):
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

# print(calculate_risk(6))
