'''
Configuration file for gui server
'''
import os


DEBUG = True

HTTP_PORT = 8080

BASE_DIR = os.path.dirname(__file__)

# template
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# static contents
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# database
DB_DIR = BASE_DIR
DB_CONF = {
    'type': 'sqlite',
    'path': os.path.join(DB_DIR, 'db.sqlite3'),
}
