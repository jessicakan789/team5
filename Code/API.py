"""
API for CFG Project
NHS COVID API
link for documentation : https://coronavirus.data.gov.uk/details/developers-guide/generic-api

"""
import requests
import json

def get_cases_by_location(location, level):
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

    daily_cases = result.json()['data'][0]['dailyCases']

    return daily_cases


print(get_cases_by_location('fife','utla'))

