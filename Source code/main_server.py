from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from API import get_rate_by_location, calculate_risk

app = FastAPI()

origins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {"Hello": "Word"}


@app.post("/locations/{location_id}")
def read_location(location_id: str):
    level = 'nation'
    nations = ['England', 'Northern', 'Ireland', 'Scotland', 'Wales']
    if location_id not in nations:
        level = 'utla'
    result = get_rate_by_location(level, location_id)

    # TODO return risk factor but first find out how risk number is calculated
    return {"cases": result}