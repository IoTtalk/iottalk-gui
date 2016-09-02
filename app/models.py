import logging

from functools import partial
from operator import contains

from pony import orm as pony

import config
import const

log = logging.getLogger('iottalk-gui')


def ck_enum(enum):
    '''
    :param enum: iterable for check containing or not

    :return: a partial function will be used by pony ``py_check``
    '''
    return partial(contains, enum)


def define_legacy_entities(db):
    '''
    FIXME: Remove this function
    '''
    class DeviceFeature(db.Entity):
        _table_ = 'DeviceFeature'

        id = pony.PrimaryKey(int, auto=True, column='df_id')
        name = pony.Required(str, max_length=255, column='df_name')
        type = pony.Required(str, max_length=6, column='df_type',
                             py_check=ck_enum(const.FEATURE_TYPES))
        category = pony.Required(str, max_length=7, column='df_category',
                                 py_check=ck_enum(const.FEATURE_CATES))
        # param_no = pony.Required(int)
        comment = pony.Optional(pony.LongStr)

        df_object = pony.Set(lambda: DFObject)

    class DevObject(db.Entity):
        _table_ = 'DeviceObject'

        do_id = pony.PrimaryKey(int, auto=True)
        dm_id = pony.ForeignKey(Devicemodel, pony.DO_NOTHING)
        p_id = pony.IntegerField()
        do_idx = pony.IntegerField()
        d_id = pony.ForeignKey(Device, pony.DO_NOTHING, blank=True, null=True)

        df_object = pony.Set(lambda: DFObject)

    class DFObject(db.Entity):
	'''
        FIXME: pony orm provide many-to-many mechanism already
        '''
        _table_ = 'DFObject'

        id = pony.PrimaryKey(int, auto=True, column='dfo_id')
        dev_obj = pony.Required(DevObject, column='do_id')
        feature = pony.Required(DeviceFeature, column='dfo_id')

    class DfModule(db.Entity):
        _table_ = 'DF_Module'

        na_id = pony.ForeignKey('Networkapplication', pony.DO_NOTHING, primary_key=True)
        dfo_id = pony.ForeignKey(DFObject, pony.DO_NOTHING, primary_key=True)
        param_i = pony.IntegerField(primary_key=True)
        idf_type = pony.CharField(max_length=7, blank=True, null=True)
        fn_id = pony.ForeignKey('Function', pony.DO_NOTHING, blank=True, null=True)
        min = pony.TextField(blank=True, null=True)  # This field type is a guess.
        max = pony.TextField(blank=True, null=True)  # This field type is a guess.
        normalization = pony.BooleanField()
        color = pony.CharField(max_length=5)

        # class Meta:
        #     managed = False
        #     unique_together = (('na', 'dfo', 'param_i'),)

    class DfParameter(db.Entity):
        _table_ = 'DF_Parameter'

        dfp_id = pony.IntegerField(primary_key=True)
        df_id = pony.ForeignKey('DeviceFeature', pony.DO_NOTHING, blank=True, null=True)
        mf_id = pony.ForeignKey('DmDf', pony.DO_NOTHING, blank=True, null=True)
        param_i = pony.IntegerField()
        param_type = pony.CharField(max_length=7)
        u_id = pony.ForeignKey('User', pony.DO_NOTHING, blank=True, null=True)
        idf_type = pony.CharField(max_length=7, blank=True, null=True)
        fn_id = pony.ForeignKey('Function', pony.DO_NOTHING, blank=True, null=True)
        min = pony.TextField(blank=True, null=True)  # This field type is a guess.
        max = pony.TextField(blank=True, null=True)  # This field type is a guess.
        normalization = pony.BooleanField()

    class DmDf(db.Entity):
        _table_ = 'DM_DF'

        mf_id = pony.IntegerField(primary_key=True)
        dm_id = pony.ForeignKey('Devicemodel', pony.DO_NOTHING)
        df_id = pony.ForeignKey('DeviceFeature', pony.DO_NOTHING)

    class Device(db.Entity):
        _table_ = 'Device'

        d_id = pony.IntegerField(primary_key=True)
        mac_addr = pony.CharField(max_length=255)
        monitor = pony.CharField(max_length=255)
        d_name = pony.CharField(max_length=255)
        status = pony.CharField(max_length=7)
        u_id = pony.ForeignKey('User', pony.DO_NOTHING, blank=True, null=True)
        dm_id = pony.ForeignKey('Devicemodel', pony.DO_NOTHING)
        is_sim = pony.BooleanField()

    class Devicemodel(db.Entity):
        _table_ = 'DeviceModel'

        dm_id = pony.IntegerField(primary_key=True)
        dm_name = pony.CharField(max_length=255)
        dm_type = pony.CharField(max_length=10)

    class Function(db.Entity):
        _table_ = 'Function'

        fn_id = pony.IntegerField(primary_key=True)
        fn_name = pony.CharField(max_length=255)

    class Functionsdf(db.Entity):
        _table_ = 'FunctionSDF'

        fnsdf_id = pony.IntegerField(primary_key=True)
        fn_id = pony.ForeignKey(Function, pony.DO_NOTHING)
        u_id = pony.ForeignKey('User', pony.DO_NOTHING, blank=True, null=True)
        df_id = pony.ForeignKey(DeviceFeature, pony.DO_NOTHING, blank=True, null=True)
        display = pony.BooleanField()

    class Functionversion(db.Entity):
        _table_ = 'FunctionVersion'

        fnvt_idx = pony.IntegerField(primary_key=True)
        fn_id = pony.ForeignKey(Function, pony.DO_NOTHING)
        u_id = pony.ForeignKey('User', pony.DO_NOTHING, blank=True, null=True)
        completeness = pony.BooleanField()
        date = pony.DateField()
        code = pony.TextField()
        is_switch = pony.BooleanField()
        non_df_args = pony.TextField()

    class MultiplejoinModule(db.Entity):
        _table_ = 'MultipleJoin_Module'

        na_id = pony.ForeignKey('Networkapplication', pony.DO_NOTHING, primary_key=True)
        param_i = pony.IntegerField(primary_key=True)
        fn_id = pony.ForeignKey(Function, pony.DO_NOTHING, blank=True, null=True)
        dfo_id = pony.ForeignKey(DFObject, pony.DO_NOTHING)

        # class Meta:
        #     unique_together = (('na', 'param_i'),)

    class Networkapplication(db.Entity):
        _table_ = 'NetworkApplication'

        na_id = pony.IntegerField(primary_key=True)
        na_name = pony.CharField(max_length=255)
        na_idx = pony.IntegerField()
        p_id = pony.IntegerField()

    class Project(db.Entity):
        _table_ = 'Project'

        p_id = pony.IntegerField(primary_key=True)
        p_name = pony.CharField(max_length=255)
        status = pony.CharField(max_length=3)
        restart = pony.BooleanField()
        exception = pony.TextField()
        sim = pony.CharField(max_length=3)

    class Simulatedidf(db.Entity):
        _table_ = 'SimulatedIDF'

        d_id = pony.ForeignKey(Device, pony.DO_NOTHING, primary_key=True)
        df_id = pony.ForeignKey(DeviceFeature, pony.DO_NOTHING, primary_key=True)
        execution_mode = pony.CharField(max_length=8)
        data = pony.TextField(blank=True, null=True)

        # class Meta:
        #     unique_together = (('d', 'df'),)

    class User(db.Entity):
        _table_ = 'User'

        id = pony.PrimaryKey(int, auto=True, column='u_id')
        name = pony.Required(str, 255, column='u_name')
        passwd = pony.Required(str, 255)


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
    define_legacy_entities(db)
    db.bind(config.DB_CONF['type'], config.DB_CONF['path'], create_db=True)
    db.generate_mapping(create_tables=True)

    return db



