import requests
import json


def get_rate_by_location(level, location):
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

    print('Number of cases in the last 7 days:', latest)

    return latest


def calculate_risk(risk):
    if risk <= 1:
        print("The risk of getting COVID is LOW")
        print("We recommend you wash your hands frequently")
    elif 1 < risk <= 2:
        print("The risk of getting COVID is MEDIUM")
        print("We recommend you wear a mask")
    else:
        print("The risk of getting COVID is HIGH")
        print("We recommend you take a LFD")
