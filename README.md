# COVID Calculator

## Team 5 Code First Girls
Maysa, Louise, Emily, and Jess K

![image](https://user-images.githubusercontent.com/83308735/180663618-639532f5-18b1-4b8b-9bff-473e6c09f40d.png)

## Description

The COVID calculator is an application that allows users to put in location information and returns data about covid 
rates using an API and database. The COVID calculator gives the user simple advice to follow to reduce their risk of 
catching covid based on percentage risk or some scale of our own. Also, it compares local rates to nationwide rates to 
give users some context to their local rate.


## Pre-requisites and Dependencies

1. Python(v3.6) - link to installation
a. Clone the repo
b. pip install -r requirements.txt: installs all py dependencies (installs uvicorn and fastAPI)

2. For the frontend Javascript is used so please install these packages
* Install nodejs: https://nodejs.org/en/download/

Change directory to js/covid-calc.
Then run:

    npm install 


## How to use(locally)

1. Create database by running [SQL file](https://github.com/jessicakan789/team5/tree/main/Database)
2. Download [source code](https://github.com/jessicakan789/team5/tree/main/Source%20code)
3. Go to team5/src/js/covid-calc
4. Run "npm start" in the terminal
5. Create an account or sign-in
6. Choose an area type and an area name:
[list of areas](https://github.com/jessicakan789/team5/tree/main/Research/area_names.txt)
7. Find out how likely you are to get COVID-19

How to use(web)



1. Export environment variables to shell in terminal
```sh
export RUN_ENV=WEB
export WEB_PASSWORD = "insert sql password here"
```

2. Run Backend
```sh
cd /src

uvicorn main_server:app
```

3. Run Frontend
```sh
cd /src/js/covid-calc

npm start
```

## File descriptions

| File | Description |
| ------- | -------------------------- |
| main.py | Run the program |
| API.py | Connects to the API and fetches COVID rate info |
| predict.py | Predicts what area name user desires |
| dbconfig.py | Holds SQL login details |
| dbconnection.py | Connects to SQL database about population and account info |
| User.py | Allows user to login/create account |
| Population.py | Allows user to access population database info |
| main.server | Runs webserver
|

## Unit tests
To run unit tests in PyCharm please follow these steps:
1. In PyCharm right click on Source code --> Mark Directory as --> Sources Root
2. In PyCharm right click on Unit tests --> Mark Directory as --> Test Sources Root
3. Right click on Unit tests --> Run
