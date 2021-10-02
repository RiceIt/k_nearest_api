import os


class Config:
    POSTGRESQL_USER = os.environ["POSTGRESQL_USER"]
    POSTGRESQL_PASSWORD = os.environ["POSTGRESQL_PASSWORD"]
    POSTGRESQL_SERVER = os.environ["POSTGRESQL_SERVER"]
    DB_NAME = os.environ["DB_NAME"]
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_SERVER}/{DB_NAME}"