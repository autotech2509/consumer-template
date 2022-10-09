from flask import Flask
from pymongo import MongoClient
import copy

from pymongo.database import Database

global_mongodb_client: MongoClient = None
mongo_config: dict = None


class MongoConfigParam:
    MONGO_URI = 'MONGO_URI'
    DB_NAME = "DB_NAME"


class MongoDBInit(object):
    app = None

    @staticmethod
    def init_client(mongo_uri=None, config=None):
        global global_mongodb_client
        global mongo_config

        if mongo_config is None and config is not None:
            mongo_config = copy.deepcopy(config)

        if mongo_uri is None:
            mongo_uri = mongo_config.get(MongoConfigParam.MONGO_URI)

        if global_mongodb_client is None:
            global_mongodb_client = MongoClient(mongo_uri, connect=False)

        from src.database.mongo.setup_collection import setup_collection_model
        setup_collection_model()

    @staticmethod
    def init_app(app: Flask):
        global global_mongodb_client
        global mongo_config

        if mongo_config is None:
            mongo_config = copy.deepcopy(app.config["MONGO_DB_SETTINGS"])

        if global_mongodb_client is None:
            global_mongodb_client = MongoClient(mongo_config.get(MongoConfigParam.MONGO_URI))

        from src.database.mongo.setup_collection import setup_collection_model
        setup_collection_model()

    @staticmethod
    def get_db(db_name=None, mongo_uri: dict = None) -> Database:
        assert global_mongodb_client is not None, "You must call MongoDBInit.init_app(app) or " \
                                                  "MongoDBInit.init_client first"
        if db_name is None:
            assert mongo_config is not None, "no config provided."
            db_name = mongo_config.get(MongoConfigParam.DB_NAME)

        if mongo_uri is None:
            return global_mongodb_client.get_database(db_name)

        return MongoClient(mongo_uri, connect=False).get_database(db_name)

    @staticmethod
    def get_mongo_db_client() -> MongoClient:
        assert global_mongodb_client is not None, "You must call MongoDBInit.init_app(app) or " \
                                                  "MongoDBInit.init_client first"
        return global_mongodb_client
