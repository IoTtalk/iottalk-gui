import logging

from pony import orm as pony

import config

log = logging.getLogger('iottalk-gui')


def define_entities(db):
    pass


def db_init(db=None):
    '''
    Database init.

    We will create sqlite3 db file in config.DB_DIR.

    Also, we will generate mapping for pony orm.

    :param db: the pony database instance. if None, we generate a new one.
    '''
    db = db if db else pony.Database()
    if db.provider is not None:
        log.warning('db %r has binded already.', db)
        return

    define_entities(db)
    db.bind(config.DB_CONF['type'], config.DB_CONF['path'], create_db=True)
    db.generate_mapping(create_tables=True)

    return db
