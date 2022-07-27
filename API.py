import requests
import json


def get_rate_by_location(location):
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
        'https://api.coronavirus.data.gov.uk/v1/data?filters=areaName={};areaType=utla&structure='
        .format(location),
        params=structure_params
    )

    latest = 0

    for i in range(0, 7):
        latest += int(result.json()['data'][i]['dailyCases'])

    print('weeklyCases:', latest)

    if latest <= 100:
        print("Your risk of getting COVID is LOW")
        print("We recommend you wash your hands frequently")
    if 100 < latest <= 400:
        print("Your risk of getting COVID is MEDIUM")
        print("We recommend you wear a mask")
    if latest > 400:
        print("Your risk of getting COVID is HIGH")
        print("We recommend you take a LFD")
