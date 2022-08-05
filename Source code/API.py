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
    if risk <= 0.0005:
        print("In this area in the last 7 days, {} in 10000 people have tested positive for Covid-19."
              "This is the same as {} people in a packed Wembley Stadium or {} people at the Glastonbury"
              " Festival".format(round(risk), round(risk * 9), round(risk * 20)))
        print("Overall risk in your area is LOW")
    elif 0.0005 < risk <= 0.001:
        print("In this area in the last 7 days, {} in 10000 people have tested positive for Covid-19."
              "This is the same as {} people in a packed Wembley Stadium or {} people at the Glastonbury"
              " Festival".format(round(risk), round(risk * 9), round(risk * 20)))
        print("Overall risk in your area is MEDIUM")
    else:
        print("In this area in the last 7 days, {} in 10000 people have tested positive for Covid-19."
              "This is the same as {} people in a packed Wembley Stadium or {} people at the Glastonbury"
              " Festival".format(round(risk), round(risk * 9), round(risk * 20)))
        print("Overall risk in your area is HIGH")

#print(calculate_risk(0.0006))