import os
import sys

from dotenv import load_dotenv

load_dotenv()


dev = {
    'app': {
        'host': os.getenv('DEV_APP_HOST'),
        'port': int(os.getenv('DEV_APP_PORT')),
    },
    'db': {
        'host': os.getenv('DEV_DB_HOST'),
        'port': int(os.getenv('DEV_DB_PORT')),
        'name': os.getenv('DEV_DB_NAME'),
    }
}

prod = {
    'app': {
        'host': os.getenv('PROD_APP_HOST'),
        'port': int(os.getenv('PROD_APP_PORT')),
    },
    'db': {
        'host': os.getenv('PROD_DB_HOST'),
        'port': int(os.getenv('PROD_DB_PORT')),
        'name': os.getenv('PROD_DB_NAME'),
    }
}

cfg = {
    'dev': dev,
    'prod': prod,
}

index_env = 1

try:
    env = sys.argv[index_env]
    if env not in (None, 'dev', 'prod'):
        env = 'dev'
except IndexError:
    env = 'dev'

CONFIG = cfg[env]
