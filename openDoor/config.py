import os
pin = {'up': 23, 'down': 24, 'ctrl': 25, 'led': 22}
action = {'on': False, 'off': True, }

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# secends
SESSION_DURATION = 2592000
REQUIRED_LOGIN_URLS = [
    '/user/add',
    '/',
]
STATIC_FILE_URLS = [
    '/static/css',
    '/static/js',
]
