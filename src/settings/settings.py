"""Application configuration."""
import os
from autotech_sdk.database.mongo import MongoConfig


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('URL_BUILDER_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))   # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = "simple"   # Can be "memcached", "redis", etc.


class ProdConfig(Config):
    """Production configuration."""

    MONGO_DB_SETTINGS = MongoConfig(
        mongo_uri=os.environ.get("MONGO_URL", "mongodb://localhost:27017"),
        db_name=os.environ.get("DB_NAME", "prodDB")
    )


class DevConfig(Config):
    """Development configuration."""

    DB_PATH = None
    MONGO_DB_SETTINGS = MongoConfig(
        mongo_uri=os.environ.get("MONGO_URL", "mongodb://localhost:27017"),
        db_name=os.environ.get("DB_NAME", "devDB")
    )

    CACHE_TYPE = 'simple'   # Can be "memcached", "redis", etc


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    MONGO_DB_SETTINGS = MongoConfig(
        mongo_uri=os.environ.get("MONGO_URL", "mongodb://localhost:27017"),
        db_name=os.environ.get("DB_NAME", "testDB")
    )
