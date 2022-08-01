# COVID Calculator

## Team 5 Code First Girls
Maysa, Louise, Emily, and Jess K

![image](https://user-images.githubusercontent.com/83308735/180663618-639532f5-18b1-4b8b-9bff-473e6c09f40d.png)

## Description

The COVID calculator is an application that allows users to put in location information and returns data about covid 
rates using an API and database. The COVID calculator gives the user simple advice to follow to reduce their risk of 
catching covid based on percentage risk or some scale of our own. Also, it compares local rates to nationwide rates to 
give users some context to their local rate.

## How to use

1. Create database by running [SQL file](https://github.com/jessicakan789/team5/blob/main/Database/UpdatedDBThursday.sql)
2. Download [source code](https://github.com/jessicakan789/team5/tree/main/Source%20code)
3. Run "main.py" from source code
4. Create an account or sign-in
5. Choose an area type and an area name:
[list of areas](https://github.com/jessicakan789/team5/blob/main/utla_area_names.txt)
6. Find out how likely you are to get COVID


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


