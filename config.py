import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '\xe8X\x04u\x16\x81\x8d\xd1\xcc\xd8\xb6\xd8$\xdbk-\xaa_\x0b@3\xe4\xca2'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
