from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from API import get_rate_by_location, calculate_risk
from Population import return_population

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Route
# Function read_location handles the location that is passed in.

@app.post("/locations/{location_id}")
def read_location(location_id: str):
    level = 'nation'
    nations = ['England', 'Northern', 'Ireland', 'Scotland', 'Wales']
    if location_id not in nations:
        level = 'utla'
    rate = get_rate_by_location(level, location_id)

    if rate == False:
        raise HTTPException(status_code=404, detail='UTLA not found.')
    population = return_population(location_id)

    if population == False:
        raise HTTPException(status_code=404, detail='UTLA not found.')

    risk = rate / population
    result = calculate_risk(risk)

    return {"cases": result}
