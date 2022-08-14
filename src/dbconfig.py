import os

WEB_PASSWORD = os.environ.get('WEB_PASSWORD')
RUN_ENV = os.environ.get('RUN_ENV')
USER = "root"
PASSWORD = '' if RUN_ENV == 'WEB' else input("Please enter your password")
HOST = "localhost"

# import operating system
# from the os env, get the WEB_PASSWORD
# if WEB in the RUN_ENV then run else ask for SQL password.
