class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/cit_flask'
    SECRET_KEY = 'mysecretkey'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig
    }