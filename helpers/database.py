import os
import logging
from dotenv import load_dotenv

load_dotenv()


def get_secret(secret):
    secret_value = os.environ.get(secret)

    if secret_value is None:
        logging.info("Did not find secret value: {}!", secret)
        return None

    return secret_value


# dialect+driver://username:password@host:port/database
def connection_string():
    host = get_secret("HOST")
    port = get_secret("PORT")
    database = get_secret("DATABASE")
    username = get_secret("USERNAME")
    password = get_secret("PASSWORD")

    temp = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    print(temp)
    return temp
