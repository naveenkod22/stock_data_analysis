import logging
import datetime
import configparser
from sqlalchemy import create_engine

def database_connection(user = 'naveen', host = 'localhost', database = 'stock_database'):
    """
    Creates a connection to the PostgreSQL database
    by default it connects to the database with the following credentials:
        user = 'naveen'
        host = 'localhost'
        database = 'stock_database'
    Returns: engine
    
    """
    config = configparser.ConfigParser()
    config.read('./scripts/config.ini')
    password = config.get('postgresql', 'password')
    port = config.get('postgresql', 'port')
    user = user
    host = host
    database = database
    conn = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'\
                           .format(user = user, password = password, host = host, port = port, database = database)).connect()

    return conn

def log(message):
    """Logs messages to a file called logs.log"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.info("; {message} ; {timestamp}".format(message=message, timestamp=timestamp))