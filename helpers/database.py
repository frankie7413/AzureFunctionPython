import os
import logging
from dotenv import load_dotenv

load_dotenv()

<<<<<<< HEAD

def get_secret(secret):
    secret_value = os.environ.get(secret)
=======
def get_secret(secret):
    secret_value =  os.environ.get(secret)
>>>>>>> 630b7b35db671e83425a33b1e6870e52827766e2

    if secret_value is None:
        logging.info("Did not find secret value: {}!", secret)
        return None

    return secret_value

<<<<<<< HEAD

# dialect+driver://username:password@host:port/database
def connection_string():
    host = get_secret("HOST")
    port = get_secret("PORT")
    database = get_secret("DATABASE")
    username = get_secret("USERNAME")
    password = get_secret("PASSWORD")
=======
# dialect+driver://username:password@host:port/database
def connection_string():
    host = get_secret('HOST')
    port = get_secret('PORT')
    database = get_secret('DATABASE')
    username = get_secret('USERNAME')
    password = get_secret('PASSWORD')
>>>>>>> 630b7b35db671e83425a33b1e6870e52827766e2

    temp = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    print(temp)
    return temp
