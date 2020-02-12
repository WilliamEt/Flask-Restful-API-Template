# coding: utf-8


class Config(object):
    SECRET_KEY = "A VERY VERY SECRET WORD"
    DATABASE_URI = "postgresql+psycopg2://postgres:password@localhost:5432/test_blog"

    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}