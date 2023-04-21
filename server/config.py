import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'mysql+pymysql://lanceraleigh:1N%23xplicavel@localhost/lancentric'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
