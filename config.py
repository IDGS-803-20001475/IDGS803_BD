import os 
from sqlalchemy import create_engine


class Config(object):
    SECRET_KET='SUPER_SECRET_KEY'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://yair:Balones12?@127.0.0.1/idgs803"
    SQLALCHEMY_TRACK_MODIFICATION=False