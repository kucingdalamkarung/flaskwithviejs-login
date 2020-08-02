import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

# change connection string to your own 
SQLALCHEMY_DATABASE_URI = '<Your connection Sring>'