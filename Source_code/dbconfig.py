"""
This file must contain the MySQL connection information on your PC.

The Password variable has been set up so that the User is prompted to enter this before running the main program.
If this Password is incorrect, the program will exit prematurely as it cannot function without a connection to the
database.
"""


USER = "root"
PASSWORD = input("Please input your SQL password: ")
HOST = "localhost"
