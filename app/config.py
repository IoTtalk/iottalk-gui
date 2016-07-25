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
STATIC_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'node_modules'),
)
