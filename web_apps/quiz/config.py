class Config(object):
        DEBUG = True
        TESTING = False
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/cit_flask'
        SECRET_KEY = 'mysecretkey'