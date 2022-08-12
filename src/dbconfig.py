import os

WEB_PASSWORD = os.environ.get('WEB_PASSWORD')
RUN_ENV = os.environ.get('RUN_ENV')
USER = "root"
PASSWORD = '' if RUN_ENV == 'WEB' else input("Please enter your password")
HOST = "localhost"