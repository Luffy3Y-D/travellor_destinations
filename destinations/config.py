import os


class Config(object):
    DEBUG = os.environ.get("DEBUG")
    TESTING = False
    SESSION_COOKIE_SECURE = True
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
