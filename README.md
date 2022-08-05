# COVID Calculator

## Team 5 Code First Girls
Maysa, Louise, Emily, and Jess K

![image](https://user-images.githubusercontent.com/83308735/180663618-639532f5-18b1-4b8b-9bff-473e6c09f40d.png)

## Description

The COVID calculator is an application that allows users to put in location information and returns data about COVID 
rates using an API and database. The COVID calculator gives the user simple advice to follow to reduce their risk of 
catching COVID based on risk. Also, it compares local rates to nationwide rates to 
give users some context to their local rate.

## How to use

1. Create database by running [SQL file](https://github.com/jessicakan789/team5/tree/main/Database)
2. Download [source code](https://github.com/jessicakan789/team5/tree/main/Source%20code)
3. Run "main.py" from source code
4. Create an account or sign-in
5. Choose an area type and an area name:
[list of areas](https://github.com/jessicakan789/team5/tree/main/Research/area_names.txt)
6. Find out how likely you are to get COVID


## File descriptions

| File | Description |
| ------- | -------------------------- |
| main.py | Runs the program |
| API.py | Connects to the API and fetches COVID rate info |
| predict.py | Predicts what area name user desires |
| dbconfig.py | Holds SQL login details |
| dbconnection.py | Connects to SQL database about population and account info |
| Population.py | Allows user to access population database info |
| login.py | Allows user to login/create account |
| area_advice.py | Gives user government advice for their nation |
| save_search.py | Saves location and risk from previous search |

## Unit tests
To run unit tests in PyCharm please follow these steps:
1. In PyCharm right click on Source code --> Mark Directory as --> Sources Root
2. In PyCharm right click on Unit tests --> Mark Directory as --> Test Sources Root
3. Right click on Unit tests --> Run
