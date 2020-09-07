import os

# uncomment the line below for postgres database url from environment variable
# postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}
# postgres_uri = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    domains = ['xmpp.ru', 'jabber.ru']
    recaptcha_secret = os.getenv('RECAPTCHA_SECRET', 'XXX')


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = postgres_uri


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)


def config():
    return config_by_name[os.getenv('ENV') or 'dev']


key = Config.SECRET_KEY
