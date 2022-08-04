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

    # Note: cases are only reported every 7 days.
    # Only indexes 0, 7, 14 etc. have new data
    # It is hence a waste of time to sum over other days...

    current_weeks_cases = result.json()['data'][0]['dailyCases']

    # Sum over last 2 weeks maybe? You can be infectious for up to 10 days, so this may
    # be the most cautious approach?
    current_fortnights_cases = sum([int(result.json()['data'][i]['dailyCases']) for i in [0,7]])


    return current_fortnights_cases


#  print(get_cases_by_location('fife','utla'))

