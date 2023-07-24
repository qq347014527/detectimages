from peewee import *

database = MySQLDatabase('safedb', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '10.151.18.163', 'port': 3306, 'user': 'admin', 'password': 'Eroot123!@#'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database


class CcppAiAxPeoples(BaseModel):
    time = DateField()
    in_Num = DateField()
    out_Num = DateField()

    class Meta:
        table_name = 'ccpp_ai_ax_peoples'



class ActEvtLog(BaseModel):
    data_ = TextField(column_name='DATA_', null=True)
    execution_id_ = CharField(column_name='EXECUTION_ID_', null=True)
    is_processed_ = IntegerField(column_name='IS_PROCESSED_', constraints=[SQL("DEFAULT 0")], null=True)
    lock_owner_ = CharField(column_name='LOCK_OWNER_', null=True)
    lock_time_ = DateTimeField(column_name='LOCK_TIME_', null=True)
    log_nr_ = BigAutoField(column_name='LOG_NR_')
    proc_def_id_ = CharField(column_name='PROC_DEF_ID_', null=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', null=True)
    time_stamp_ = DateTimeField(column_name='TIME_STAMP_')
    type_ = CharField(column_name='TYPE_', null=True)
    user_id_ = CharField(column_name='USER_ID_', null=True)

    class Meta:
        table_name = 'act_evt_log'

class ActEvtLogCopy(BaseModel):
    data_ = TextField(column_name='DATA_', null=True)
    execution_id_ = CharField(column_name='EXECUTION_ID_', null=True)
    is_processed_ = IntegerField(column_name='IS_PROCESSED_', constraints=[SQL("DEFAULT 0")], null=True)
    lock_owner_ = CharField(column_name='LOCK_OWNER_', null=True)
    lock_time_ = DateTimeField(column_name='LOCK_TIME_', null=True)
    log_nr_ = BigAutoField(column_name='LOG_NR_')
    proc_def_id_ = CharField(column_name='PROC_DEF_ID_', null=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', null=True)
    time_stamp_ = DateTimeField(column_name='TIME_STAMP_')
    type_ = CharField(column_name='TYPE_', null=True)
    user_id_ = CharField(column_name='USER_ID_', null=True)

    class Meta:
        table_name = 'act_evt_log_copy'

class ActReDeployment(BaseModel):
    category_ = CharField(column_name='CATEGORY_', null=True)
    deploy_time_ = DateTimeField(column_name='DEPLOY_TIME_', null=True)
    engine_version_ = CharField(column_name='ENGINE_VERSION_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    key_ = CharField(column_name='KEY_', null=True)
    name_ = CharField(column_name='NAME_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'act_re_deployment'

class ActGeBytearray(BaseModel):
    bytes_ = TextField(column_name='BYTES_', null=True)
    deployment_id_ = ForeignKeyField(column_name='DEPLOYMENT_ID_', field='id_', model=ActReDeployment, null=True)
    generated_ = IntegerField(column_name='GENERATED_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    name_ = CharField(column_name='NAME_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)

    class Meta:
        table_name = 'act_ge_bytearray'

class ActGeProperty(BaseModel):
    name_ = CharField(column_name='NAME_', primary_key=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    value_ = CharField(column_name='VALUE_', null=True)

    class Meta:
        table_name = 'act_ge_property'

class ActHiActinst(BaseModel):
    act_id_ = CharField(column_name='ACT_ID_')
    act_name_ = CharField(column_name='ACT_NAME_', null=True)
    act_type_ = CharField(column_name='ACT_TYPE_')
    assignee_ = CharField(column_name='ASSIGNEE_', null=True)
    call_proc_inst_id_ = CharField(column_name='CALL_PROC_INST_ID_', null=True)
    delete_reason_ = CharField(column_name='DELETE_REASON_', null=True)
    duration_ = BigIntegerField(column_name='DURATION_', null=True)
    end_time_ = DateTimeField(column_name='END_TIME_', index=True, null=True)
    execution_id_ = CharField(column_name='EXECUTION_ID_')
    id_ = CharField(column_name='ID_', primary_key=True)
    proc_def_id_ = CharField(column_name='PROC_DEF_ID_')
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_')
    start_time_ = DateTimeField(column_name='START_TIME_', index=True)
    task_id_ = CharField(column_name='TASK_ID_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'act_hi_actinst'
        indexes = (
            (('execution_id_', 'act_id_'), False),
            (('proc_inst_id_', 'act_id_'), False),
        )

class ActHiAttachment(BaseModel):
    content_id_ = CharField(column_name='CONTENT_ID_', null=True)
    description_ = CharField(column_name='DESCRIPTION_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    name_ = CharField(column_name='NAME_', null=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', null=True)
    time_ = DateTimeField(column_name='TIME_', null=True)
    type_ = CharField(column_name='TYPE_', null=True)
    url_ = CharField(column_name='URL_', null=True)
    user_id_ = CharField(column_name='USER_ID_', null=True)

    class Meta:
        table_name = 'act_hi_attachment'

class ActHiComment(BaseModel):
    action_ = CharField(column_name='ACTION_', null=True)
    full_msg_ = TextField(column_name='FULL_MSG_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    message_ = CharField(column_name='MESSAGE_', null=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', null=True)
    time_ = DateTimeField(column_name='TIME_')
    type_ = CharField(column_name='TYPE_', null=True)
    user_id_ = CharField(column_name='USER_ID_', null=True)

    class Meta:
        table_name = 'act_hi_comment'

class ActHiDetail(BaseModel):
    act_inst_id_ = CharField(column_name='ACT_INST_ID_', index=True, null=True)
    bytearray_id_ = CharField(column_name='BYTEARRAY_ID_', null=True)
    double_ = FloatField(column_name='DOUBLE_', null=True)
    execution_id_ = CharField(column_name='EXECUTION_ID_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    long_ = BigIntegerField(column_name='LONG_', null=True)
    name_ = CharField(column_name='NAME_', index=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', index=True, null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', index=True, null=True)
    text2_ = CharField(column_name='TEXT2_', null=True)
    text_ = CharField(column_name='TEXT_', null=True)
    time_ = DateTimeField(column_name='TIME_', index=True)
    type_ = CharField(column_name='TYPE_')
    var_type_ = CharField(column_name='VAR_TYPE_', null=True)

    class Meta:
        table_name = 'act_hi_detail'

class ActHiIdentitylink(BaseModel):
    group_id_ = CharField(column_name='GROUP_ID_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', index=True, null=True)
    task_id_ = CharField(column_name='TASK_ID_', index=True, null=True)
    type_ = CharField(column_name='TYPE_', null=True)
    user_id_ = CharField(column_name='USER_ID_', index=True, null=True)

    class Meta:
        table_name = 'act_hi_identitylink'

class ActHiProcinst(BaseModel):
    business_key_ = CharField(column_name='BUSINESS_KEY_', index=True, null=True)
    delete_reason_ = CharField(column_name='DELETE_REASON_', null=True)
    duration_ = BigIntegerField(column_name='DURATION_', null=True)
    end_act_id_ = CharField(column_name='END_ACT_ID_', null=True)
    end_time_ = DateTimeField(column_name='END_TIME_', index=True, null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    name_ = CharField(column_name='NAME_', null=True)
    proc_def_id_ = CharField(column_name='PROC_DEF_ID_')
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', unique=True)
    start_act_id_ = CharField(column_name='START_ACT_ID_', null=True)
    start_time_ = DateTimeField(column_name='START_TIME_')
    start_user_id_ = CharField(column_name='START_USER_ID_', null=True)
    super_process_instance_id_ = CharField(column_name='SUPER_PROCESS_INSTANCE_ID_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'act_hi_procinst'

class ActHiTaskinst(BaseModel):
    assignee_ = CharField(column_name='ASSIGNEE_', null=True)
    category_ = CharField(column_name='CATEGORY_', null=True)
    claim_time_ = DateTimeField(column_name='CLAIM_TIME_', null=True)
    delete_reason_ = CharField(column_name='DELETE_REASON_', null=True)
    description_ = CharField(column_name='DESCRIPTION_', null=True)
    due_date_ = DateTimeField(column_name='DUE_DATE_', null=True)
    duration_ = BigIntegerField(column_name='DURATION_', null=True)
    end_time_ = DateTimeField(column_name='END_TIME_', null=True)
    execution_id_ = CharField(column_name='EXECUTION_ID_', null=True)
    form_key_ = CharField(column_name='FORM_KEY_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    name_ = CharField(column_name='NAME_', null=True)
    owner_ = CharField(column_name='OWNER_', null=True)
    parent_task_id_ = CharField(column_name='PARENT_TASK_ID_', null=True)
    priority_ = IntegerField(column_name='PRIORITY_', null=True)
    proc_def_id_ = CharField(column_name='PROC_DEF_ID_', null=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', index=True, null=True)
    start_time_ = DateTimeField(column_name='START_TIME_')
    task_def_key_ = CharField(column_name='TASK_DEF_KEY_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'act_hi_taskinst'

class ActHiVarinst(BaseModel):
    bytearray_id_ = CharField(column_name='BYTEARRAY_ID_', null=True)
    create_time_ = DateTimeField(column_name='CREATE_TIME_', null=True)
    double_ = FloatField(column_name='DOUBLE_', null=True)
    execution_id_ = CharField(column_name='EXECUTION_ID_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    last_updated_time_ = DateTimeField(column_name='LAST_UPDATED_TIME_', null=True)
    long_ = BigIntegerField(column_name='LONG_', null=True)
    name_ = CharField(column_name='NAME_')
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', index=True, null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', index=True, null=True)
    text2_ = CharField(column_name='TEXT2_', null=True)
    text_ = CharField(column_name='TEXT_', null=True)
    var_type_ = CharField(column_name='VAR_TYPE_', null=True)

    class Meta:
        table_name = 'act_hi_varinst'
        indexes = (
            (('name_', 'var_type_'), False),
        )

class ActIdGroup(BaseModel):
    id_ = CharField(column_name='ID_', primary_key=True)
    name_ = CharField(column_name='NAME_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    type_ = CharField(column_name='TYPE_', null=True)

    class Meta:
        table_name = 'act_id_group'

class ActIdInfo(BaseModel):
    id_ = CharField(column_name='ID_', primary_key=True)
    key_ = CharField(column_name='KEY_', null=True)
    parent_id_ = CharField(column_name='PARENT_ID_', null=True)
    password_ = TextField(column_name='PASSWORD_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    type_ = CharField(column_name='TYPE_', null=True)
    user_id_ = CharField(column_name='USER_ID_', null=True)
    value_ = CharField(column_name='VALUE_', null=True)

    class Meta:
        table_name = 'act_id_info'

class ActIdUser(BaseModel):
    email_ = CharField(column_name='EMAIL_', null=True)
    first_ = CharField(column_name='FIRST_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    last_ = CharField(column_name='LAST_', null=True)
    picture_id_ = CharField(column_name='PICTURE_ID_', null=True)
    pwd_ = CharField(column_name='PWD_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)

    class Meta:
        table_name = 'act_id_user'

class ActIdMembership(BaseModel):
    group_id_ = ForeignKeyField(column_name='GROUP_ID_', field='id_', model=ActIdGroup)
    user_id_ = ForeignKeyField(column_name='USER_ID_', field='id_', model=ActIdUser)

    class Meta:
        table_name = 'act_id_membership'
        indexes = (
            (('user_id_', 'group_id_'), True),
        )
        primary_key = CompositeKey('group_id_', 'user_id_')

class ActReProcdef(BaseModel):
    category_ = CharField(column_name='CATEGORY_', null=True)
    deployment_id_ = CharField(column_name='DEPLOYMENT_ID_', null=True)
    description_ = CharField(column_name='DESCRIPTION_', null=True)
    dgrm_resource_name_ = CharField(column_name='DGRM_RESOURCE_NAME_', null=True)
    engine_version_ = CharField(column_name='ENGINE_VERSION_', null=True)
    has_graphical_notation_ = IntegerField(column_name='HAS_GRAPHICAL_NOTATION_', null=True)
    has_start_form_key_ = IntegerField(column_name='HAS_START_FORM_KEY_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    key_ = CharField(column_name='KEY_')
    name_ = CharField(column_name='NAME_', null=True)
    resource_name_ = CharField(column_name='RESOURCE_NAME_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    suspension_state_ = IntegerField(column_name='SUSPENSION_STATE_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    version_ = IntegerField(column_name='VERSION_')

    class Meta:
        table_name = 'act_re_procdef'
        indexes = (
            (('key_', 'version_', 'tenant_id_'), True),
        )

class ActProcdefInfo(BaseModel):
    id_ = CharField(column_name='ID_', primary_key=True)
    info_json_id_ = ForeignKeyField(column_name='INFO_JSON_ID_', field='id_', model=ActGeBytearray, null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef)
    rev_ = IntegerField(column_name='REV_', null=True)

    class Meta:
        table_name = 'act_procdef_info'

class ActReModel(BaseModel):
    category_ = CharField(column_name='CATEGORY_', null=True)
    create_time_ = DateTimeField(column_name='CREATE_TIME_', null=True)
    deployment_id_ = ForeignKeyField(column_name='DEPLOYMENT_ID_', field='id_', model=ActReDeployment, null=True)
    editor_source_extra_value_id_ = ForeignKeyField(column_name='EDITOR_SOURCE_EXTRA_VALUE_ID_', field='id_', model=ActGeBytearray, null=True)
    editor_source_value_id_ = ForeignKeyField(backref='act_ge_bytearray_editor_source_value_id__set', column_name='EDITOR_SOURCE_VALUE_ID_', field='id_', model=ActGeBytearray, null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    key_ = CharField(column_name='KEY_', null=True)
    last_update_time_ = DateTimeField(column_name='LAST_UPDATE_TIME_', null=True)
    meta_info_ = CharField(column_name='META_INFO_', null=True)
    name_ = CharField(column_name='NAME_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    version_ = IntegerField(column_name='VERSION_', null=True)

    class Meta:
        table_name = 'act_re_model'

class ActRuExecution(BaseModel):
    act_id_ = CharField(column_name='ACT_ID_', null=True)
    business_key_ = CharField(column_name='BUSINESS_KEY_', index=True, null=True)
    cached_ent_state_ = IntegerField(column_name='CACHED_ENT_STATE_', null=True)
    deadletter_job_count_ = IntegerField(column_name='DEADLETTER_JOB_COUNT_', null=True)
    evt_subscr_count_ = IntegerField(column_name='EVT_SUBSCR_COUNT_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    id_link_count_ = IntegerField(column_name='ID_LINK_COUNT_', null=True)
    is_active_ = IntegerField(column_name='IS_ACTIVE_', null=True)
    is_concurrent_ = IntegerField(column_name='IS_CONCURRENT_', null=True)
    is_count_enabled_ = IntegerField(column_name='IS_COUNT_ENABLED_', null=True)
    is_event_scope_ = IntegerField(column_name='IS_EVENT_SCOPE_', null=True)
    is_mi_root_ = IntegerField(column_name='IS_MI_ROOT_', null=True)
    is_scope_ = IntegerField(column_name='IS_SCOPE_', null=True)
    job_count_ = IntegerField(column_name='JOB_COUNT_', null=True)
    lock_time_ = DateTimeField(column_name='LOCK_TIME_', null=True)
    name_ = CharField(column_name='NAME_', null=True)
    parent_id_ = ForeignKeyField(column_name='PARENT_ID_', field='id_', model='self', null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    proc_inst_id_ = ForeignKeyField(backref='act_ru_execution_proc_inst_id__set', column_name='PROC_INST_ID_', field='id_', model='self', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    root_proc_inst_id_ = CharField(column_name='ROOT_PROC_INST_ID_', index=True, null=True)
    start_time_ = DateTimeField(column_name='START_TIME_', null=True)
    start_user_id_ = CharField(column_name='START_USER_ID_', null=True)
    super_exec_ = ForeignKeyField(backref='act_ru_execution_super_exec__set', column_name='SUPER_EXEC_', field='id_', model='self', null=True)
    suspension_state_ = IntegerField(column_name='SUSPENSION_STATE_', null=True)
    susp_job_count_ = IntegerField(column_name='SUSP_JOB_COUNT_', null=True)
    task_count_ = IntegerField(column_name='TASK_COUNT_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    timer_job_count_ = IntegerField(column_name='TIMER_JOB_COUNT_', null=True)
    var_count_ = IntegerField(column_name='VAR_COUNT_', null=True)

    class Meta:
        table_name = 'act_ru_execution'

class ActRuDeadletterJob(BaseModel):
    duedate_ = DateTimeField(column_name='DUEDATE_', null=True)
    exception_msg_ = CharField(column_name='EXCEPTION_MSG_', null=True)
    exception_stack_id_ = ForeignKeyField(column_name='EXCEPTION_STACK_ID_', field='id_', model=ActGeBytearray, null=True)
    exclusive_ = IntegerField(column_name='EXCLUSIVE_', null=True)
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    handler_cfg_ = CharField(column_name='HANDLER_CFG_', null=True)
    handler_type_ = CharField(column_name='HANDLER_TYPE_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    process_instance_id_ = ForeignKeyField(backref='act_ru_execution_process_instance_id__set', column_name='PROCESS_INSTANCE_ID_', field='id_', model=ActRuExecution, null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    repeat_ = CharField(column_name='REPEAT_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    type_ = CharField(column_name='TYPE_')

    class Meta:
        table_name = 'act_ru_deadletter_job'

class ActRuEventSubscr(BaseModel):
    activity_id_ = CharField(column_name='ACTIVITY_ID_', null=True)
    configuration_ = CharField(column_name='CONFIGURATION_', index=True, null=True)
    created_ = DateTimeField(column_name='CREATED_', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(3)")])
    event_name_ = CharField(column_name='EVENT_NAME_', null=True)
    event_type_ = CharField(column_name='EVENT_TYPE_')
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    proc_def_id_ = CharField(column_name='PROC_DEF_ID_', null=True)
    proc_inst_id_ = CharField(column_name='PROC_INST_ID_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'act_ru_event_subscr'

class ActRuTask(BaseModel):
    assignee_ = CharField(column_name='ASSIGNEE_', null=True)
    category_ = CharField(column_name='CATEGORY_', null=True)
    claim_time_ = DateTimeField(column_name='CLAIM_TIME_', null=True)
    create_time_ = DateTimeField(column_name='CREATE_TIME_', index=True, null=True)
    delegation_ = CharField(column_name='DELEGATION_', null=True)
    description_ = CharField(column_name='DESCRIPTION_', null=True)
    due_date_ = DateTimeField(column_name='DUE_DATE_', null=True)
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    form_key_ = CharField(column_name='FORM_KEY_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    name_ = CharField(column_name='NAME_', null=True)
    owner_ = CharField(column_name='OWNER_', null=True)
    parent_task_id_ = CharField(column_name='PARENT_TASK_ID_', null=True)
    priority_ = IntegerField(column_name='PRIORITY_', null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    proc_inst_id_ = ForeignKeyField(backref='act_ru_execution_proc_inst_id__set', column_name='PROC_INST_ID_', field='id_', model=ActRuExecution, null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    suspension_state_ = IntegerField(column_name='SUSPENSION_STATE_', null=True)
    task_def_key_ = CharField(column_name='TASK_DEF_KEY_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'act_ru_task'

class ActRuIdentitylink(BaseModel):
    group_id_ = CharField(column_name='GROUP_ID_', index=True, null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    proc_inst_id_ = ForeignKeyField(column_name='PROC_INST_ID_', field='id_', model=ActRuExecution, null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    task_id_ = ForeignKeyField(column_name='TASK_ID_', field='id_', model=ActRuTask, null=True)
    type_ = CharField(column_name='TYPE_', null=True)
    user_id_ = CharField(column_name='USER_ID_', index=True, null=True)

    class Meta:
        table_name = 'act_ru_identitylink'

class ActRuJob(BaseModel):
    duedate_ = DateTimeField(column_name='DUEDATE_', null=True)
    exception_msg_ = CharField(column_name='EXCEPTION_MSG_', null=True)
    exception_stack_id_ = ForeignKeyField(column_name='EXCEPTION_STACK_ID_', field='id_', model=ActGeBytearray, null=True)
    exclusive_ = IntegerField(column_name='EXCLUSIVE_', null=True)
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    handler_cfg_ = CharField(column_name='HANDLER_CFG_', null=True)
    handler_type_ = CharField(column_name='HANDLER_TYPE_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    lock_exp_time_ = DateTimeField(column_name='LOCK_EXP_TIME_', null=True)
    lock_owner_ = CharField(column_name='LOCK_OWNER_', null=True)
    process_instance_id_ = ForeignKeyField(backref='act_ru_execution_process_instance_id__set', column_name='PROCESS_INSTANCE_ID_', field='id_', model=ActRuExecution, null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    repeat_ = CharField(column_name='REPEAT_', null=True)
    retries_ = IntegerField(column_name='RETRIES_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    type_ = CharField(column_name='TYPE_')

    class Meta:
        table_name = 'act_ru_job'

class ActRuSuspendedJob(BaseModel):
    duedate_ = DateTimeField(column_name='DUEDATE_', null=True)
    exception_msg_ = CharField(column_name='EXCEPTION_MSG_', null=True)
    exception_stack_id_ = ForeignKeyField(column_name='EXCEPTION_STACK_ID_', field='id_', model=ActGeBytearray, null=True)
    exclusive_ = IntegerField(column_name='EXCLUSIVE_', null=True)
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    handler_cfg_ = CharField(column_name='HANDLER_CFG_', null=True)
    handler_type_ = CharField(column_name='HANDLER_TYPE_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    process_instance_id_ = ForeignKeyField(backref='act_ru_execution_process_instance_id__set', column_name='PROCESS_INSTANCE_ID_', field='id_', model=ActRuExecution, null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    repeat_ = CharField(column_name='REPEAT_', null=True)
    retries_ = IntegerField(column_name='RETRIES_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    type_ = CharField(column_name='TYPE_')

    class Meta:
        table_name = 'act_ru_suspended_job'

class ActRuTimerJob(BaseModel):
    duedate_ = DateTimeField(column_name='DUEDATE_', null=True)
    exception_msg_ = CharField(column_name='EXCEPTION_MSG_', null=True)
    exception_stack_id_ = ForeignKeyField(column_name='EXCEPTION_STACK_ID_', field='id_', model=ActGeBytearray, null=True)
    exclusive_ = IntegerField(column_name='EXCLUSIVE_', null=True)
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    handler_cfg_ = CharField(column_name='HANDLER_CFG_', null=True)
    handler_type_ = CharField(column_name='HANDLER_TYPE_', null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    lock_exp_time_ = DateTimeField(column_name='LOCK_EXP_TIME_', null=True)
    lock_owner_ = CharField(column_name='LOCK_OWNER_', null=True)
    process_instance_id_ = ForeignKeyField(backref='act_ru_execution_process_instance_id__set', column_name='PROCESS_INSTANCE_ID_', field='id_', model=ActRuExecution, null=True)
    proc_def_id_ = ForeignKeyField(column_name='PROC_DEF_ID_', field='id_', model=ActReProcdef, null=True)
    repeat_ = CharField(column_name='REPEAT_', null=True)
    retries_ = IntegerField(column_name='RETRIES_', null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    tenant_id_ = CharField(column_name='TENANT_ID_', constraints=[SQL("DEFAULT ''")], null=True)
    type_ = CharField(column_name='TYPE_')

    class Meta:
        table_name = 'act_ru_timer_job'

class ActRuVariable(BaseModel):
    bytearray_id_ = ForeignKeyField(column_name='BYTEARRAY_ID_', field='id_', model=ActGeBytearray, null=True)
    double_ = FloatField(column_name='DOUBLE_', null=True)
    execution_id_ = ForeignKeyField(column_name='EXECUTION_ID_', field='id_', model=ActRuExecution, null=True)
    id_ = CharField(column_name='ID_', primary_key=True)
    long_ = BigIntegerField(column_name='LONG_', null=True)
    name_ = CharField(column_name='NAME_')
    proc_inst_id_ = ForeignKeyField(backref='act_ru_execution_proc_inst_id__set', column_name='PROC_INST_ID_', field='id_', model=ActRuExecution, null=True)
    rev_ = IntegerField(column_name='REV_', null=True)
    task_id_ = CharField(column_name='TASK_ID_', index=True, null=True)
    text2_ = CharField(column_name='TEXT2_', null=True)
    text_ = CharField(column_name='TEXT_', null=True)
    type_ = CharField(column_name='TYPE_')

    class Meta:
        table_name = 'act_ru_variable'

class AeCurrentlog(BaseModel):
    client = CharField(column_name='CLIENT', null=True)
    id = CharField(column_name='ID', primary_key=True)
    logdate = DateTimeField(column_name='LOGDATE', null=True)
    logempid = CharField(column_name='LOGEMPID', null=True)
    logempname = CharField(column_name='LOGEMPNAME', null=True)
    logexception = CharField(column_name='LOGEXCEPTION', null=True)
    logip = CharField(column_name='LOGIP', null=True)
    logmessage = CharField(column_name='LOGMESSAGE', null=True)
    logobject = CharField(column_name='LOGOBJECT', null=True)
    logposition = CharField(column_name='LOGPOSITION', null=True)
    logtype = CharField(column_name='LOGTYPE', null=True)
    objecttype = CharField(column_name='OBJECTTYPE', null=True)
    parameter = CharField(column_name='PARAMETER', null=True)
    procd = CharField(column_name='PROCD', null=True)
    result = CharField(column_name='RESULT', null=True)
    val = CharField(column_name='VAL', null=True)

    class Meta:
        table_name = 'ae_currentlog'

class AeHelp(BaseModel):
    id = CharField(column_name='ID')
    content = CharField(null=True)
    file_source = CharField(null=True)
    is_active = CharField(constraints=[SQL("DEFAULT '1'")], null=True)
    seq = IntegerField()
    title = CharField(null=True)

    class Meta:
        table_name = 'ae_help'
        indexes = (
            (('seq', 'id'), True),
        )
        primary_key = CompositeKey('id', 'seq')

class AeJtCheck(BaseModel):
    user_code = CharField(column_name='USER_CODE', primary_key=True)
    user_name = CharField(column_name='USER_NAME', null=True)

    class Meta:
        table_name = 'ae_jt_check'

class AeSendlog(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    checkcode = CharField(column_name='CHECKCODE', null=True)
    content = CharField(column_name='CONTENT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    issend = CharField(column_name='ISSEND', constraints=[SQL("DEFAULT '1'")], null=True)
    mobile_url = CharField(column_name='MOBILE_URL', null=True)
    pc_url = CharField(column_name='PC_URL', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    result = CharField(column_name='RESULT', null=True)
    sendtime = DateTimeField(column_name='SENDTIME', null=True)
    title = CharField(column_name='TITLE', null=True)

    class Meta:
        table_name = 'ae_sendlog'

class Alarm(BaseModel):
    alarm_close = CharField(null=True)
    alarm_file = CharField(null=True)
    alarm_level = CharField(null=True)
    alarm_state = CharField(null=True)
    alarm_time = DateTimeField(null=True)
    alarm_type = CharField(null=True)
    cluster = CharField(null=True)
    device_id = CharField(null=True)
    device_loc = CharField(null=True)
    device_name = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'alarm'

class AlgorithmWeight(BaseModel):
    i_id = AutoField(column_name='I_ID')
    accident = FloatField()
    amount = FloatField()
    anti_violation = FloatField()
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    drill = FloatField()
    duty = FloatField()
    education = FloatField()
    hazard = FloatField()

    class Meta:
        table_name = 'algorithm_weight'

class BFunctionSwitch(BaseModel):
    send_switch = CharField(column_name='SEND_SWITCH', null=True)
    switch_1 = CharField(column_name='SWITCH_1', null=True)
    switch_2 = CharField(column_name='SWITCH_2', null=True)
    switch_3 = CharField(column_name='SWITCH_3', null=True)
    switch_4 = CharField(column_name='SWITCH_4', null=True)
    switch_5 = CharField(column_name='SWITCH_5', null=True)
    switch_6 = CharField(column_name='SWITCH_6', null=True)
    switch_7 = CharField(column_name='SWITCH_7', null=True)
    switch_8 = CharField(column_name='SWITCH_8', null=True)
    work_remind = CharField(column_name='WORK_REMIND', null=True)

    class Meta:
        table_name = 'b_function_switch'
        primary_key = False

class BcCategorylist(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    code = CharField(column_name='CODE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    isall = CharField(column_name='ISALL', constraints=[SQL("DEFAULT '0'")], null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    name = CharField(column_name='NAME', null=True)
    seq = IntegerField(column_name='SEQ', null=True)

    class Meta:
        table_name = 'bc_categorylist'

class CAcAccident(BaseModel):
    accident_category = CharField(column_name='ACCIDENT_CATEGORY', null=True)
    accident_course = CharField(column_name='ACCIDENT_COURSE', null=True)
    accident_date = DateTimeField(column_name='ACCIDENT_DATE', null=True)
    accident_death = IntegerField(column_name='ACCIDENT_DEATH', null=True)
    accident_minor = IntegerField(column_name='ACCIDENT_MINOR', null=True)
    accident_name = CharField(column_name='ACCIDENT_NAME', null=True)
    accident_org = CharField(column_name='ACCIDENT_ORG', null=True)
    accident_org_id = CharField(column_name='ACCIDENT_ORG_ID', null=True)
    accident_property = CharField(column_name='ACCIDENT_PROPERTY', null=True)
    accident_reason = CharField(column_name='ACCIDENT_REASON', null=True)
    accident_serious = IntegerField(column_name='ACCIDENT_SERIOUS', null=True)
    accident_type = CharField(column_name='ACCIDENT_TYPE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ac_accident'

class CAcAccidentfile(BaseModel):
    accident_id = CharField(column_name='ACCIDENT_ID', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)

    class Meta:
        table_name = 'c_ac_accidentfile'

class CCockpitAc1(BaseModel):
    cnt = IntegerField(column_name='CNT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    month = CharField(column_name='MONTH', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_cockpit_ac_1'

class CCockpitDs1(BaseModel):
    cnt = IntegerField(column_name='CNT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)

    class Meta:
        table_name = 'c_cockpit_ds_1'

class CCockpitDs2(BaseModel):
    cnt = IntegerField(column_name='CNT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)

    class Meta:
        table_name = 'c_cockpit_ds_2'

class CCockpitDt1(BaseModel):
    cnt_c = IntegerField(column_name='CNT_C', null=True)
    cnt_t = IntegerField(column_name='CNT_T', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    rate = DecimalField(column_name='RATE', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_cockpit_dt_1'

class CCockpitTable(BaseModel):
    ac_cnt_1 = IntegerField(column_name='AC_CNT_1', null=True)
    ac_cnt_2 = IntegerField(column_name='AC_CNT_2', null=True)
    ac_cnt_3 = IntegerField(column_name='AC_CNT_3', null=True)
    category = CharField(column_name='CATEGORY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ds_cnt_1 = IntegerField(column_name='DS_CNT_1', null=True)
    ds_cnt_2 = IntegerField(column_name='DS_CNT_2', null=True)
    dt_cnt_1 = IntegerField(column_name='DT_CNT_1', null=True)
    dt_cnt_2 = IntegerField(column_name='DT_CNT_2', null=True)
    em_cnt_1 = IntegerField(column_name='EM_CNT_1', null=True)
    em_cnt_2 = IntegerField(column_name='EM_CNT_2', null=True)
    em_cnt_3 = IntegerField(column_name='EM_CNT_3', null=True)
    em_cnt_4 = IntegerField(column_name='EM_CNT_4', null=True)
    hd_cnt_1 = IntegerField(column_name='HD_CNT_1', null=True)
    hd_cnt_2 = IntegerField(column_name='HD_CNT_2', null=True)
    hd_cnt_3 = IntegerField(column_name='HD_CNT_3', null=True)
    id = AutoField(column_name='ID')
    month = CharField(column_name='MONTH', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    se_cnt_1 = IntegerField(column_name='SE_CNT_1', null=True)
    se_cnt_2 = IntegerField(column_name='SE_CNT_2', null=True)
    se_cnt_3 = IntegerField(column_name='SE_CNT_3', null=True)
    su_cnt_1 = IntegerField(column_name='SU_CNT_1', null=True)
    su_cnt_2 = IntegerField(column_name='SU_CNT_2', null=True)
    tr_cnt_1 = IntegerField(column_name='TR_CNT_1', null=True)
    tr_cnt_2 = IntegerField(column_name='TR_CNT_2', null=True)
    tr_cnt_3 = IntegerField(column_name='TR_CNT_3', null=True)
    vi_cnt_1 = IntegerField(column_name='VI_CNT_1', null=True)
    vi_cnt_2 = IntegerField(column_name='VI_CNT_2', null=True)
    vi_cnt_3 = IntegerField(column_name='VI_CNT_3', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_cockpit_table'

class CCockpitTr1(BaseModel):
    cnt = IntegerField(column_name='CNT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_cockpit_tr_1'

class CCockpitTr2(BaseModel):
    cnt = IntegerField(column_name='CNT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)

    class Meta:
        table_name = 'c_cockpit_tr_2'

class CCockpitVi1(BaseModel):
    cnt = IntegerField(column_name='CNT', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = AutoField(column_name='ID')
    month = CharField(column_name='MONTH', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_cockpit_vi_1'

class CDsControl(BaseModel):
    accident = CharField(column_name='ACCIDENT', null=True)
    control_level = CharField(column_name='CONTROL_LEVEL', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    dange_source = CharField(column_name='DANGE_SOURCE', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    inherent_risk_level = CharField(column_name='INHERENT_RISK_LEVEL', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    item_c_score = DecimalField(column_name='ITEM_C_SCORE', null=True)
    item_d_score = DecimalField(column_name='ITEM_D_SCORE', null=True)
    item_e_score = DecimalField(column_name='ITEM_E_SCORE', null=True)
    item_l_score = DecimalField(column_name='ITEM_L_SCORE', null=True)
    job_active = CharField(column_name='JOB_ACTIVE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    measure = CharField(column_name='MEASURE', null=True)
    production = CharField(column_name='PRODUCTION', null=True)
    remnant_risk_level = CharField(column_name='REMNANT_RISK_LEVEL', null=True)
    safety = CharField(column_name='SAFETY', null=True)
    score_method = CharField(column_name='SCORE_METHOD', null=True)
    team = CharField(column_name='TEAM', null=True)
    technology = CharField(column_name='TECHNOLOGY', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ds_control'

class CDsDsdist(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    dist_cell = CharField(column_name='DIST_CELL', null=True)
    ds_num = IntegerField(column_name='DS_NUM', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    job_num = IntegerField(column_name='JOB_NUM', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    level01_ds_num = IntegerField(column_name='LEVEL01_DS_NUM', null=True)
    level02_ds_num = IntegerField(column_name='LEVEL02_DS_NUM', null=True)
    level03_ds_num = IntegerField(column_name='LEVEL03_DS_NUM', null=True)
    level04_ds_num = IntegerField(column_name='LEVEL04_DS_NUM', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ds_dsdist'

class CDsImportds(BaseModel):
    affect = CharField(column_name='AFFECT', null=True)
    contact_psn_name = CharField(column_name='CONTACT_PSN_NAME', null=True)
    contact_tele_no = CharField(column_name='CONTACT_TELE_NO', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    defend_dist = CharField(column_name='DEFEND_DIST', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_address = CharField(column_name='DEPT_ADDRESS', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    dept_type = CharField(column_name='DEPT_TYPE', null=True)
    device = CharField(column_name='DEVICE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    importds_address = CharField(column_name='IMPORTDS_ADDRESS', null=True)
    importds_level = CharField(column_name='IMPORTDS_LEVEL', null=True)
    importds_name = CharField(column_name='IMPORTDS_NAME', null=True)
    importds_type = CharField(column_name='IMPORTDS_TYPE', null=True)
    importds_use_date = DateField(column_name='IMPORTDS_USE_DATE', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    lat = CharField(column_name='LAT', null=True)
    lng = CharField(column_name='LNG', null=True)
    matt_property = CharField(column_name='MATT_PROPERTY', null=True)
    safe_equip = CharField(column_name='SAFE_EQUIP', null=True)
    storage = DecimalField(column_name='STORAGE', null=True)
    succor_info = CharField(column_name='SUCCOR_INFO', null=True)
    succor_linker_name = CharField(column_name='SUCCOR_LINKER_NAME', null=True)
    succor_tele_no = CharField(column_name='SUCCOR_TELE_NO', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ds_importds'

class CDsRiskplan(BaseModel):
    accident = CharField(column_name='ACCIDENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dange_source = CharField(column_name='DANGE_SOURCE', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    job_active = CharField(column_name='JOB_ACTIVE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    remark = CharField(column_name='REMARK', null=True)
    riskplan_item = CharField(column_name='RISKPLAN_ITEM', null=True)
    risk_level = CharField(column_name='RISK_LEVEL', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ds_riskplan'

class CDsRiskscore(BaseModel):
    accident = CharField(column_name='ACCIDENT', null=True)
    control_measure = CharField(column_name='CONTROL_MEASURE', null=True)
    correlation = CharField(column_name='CORRELATION', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dange_source = CharField(column_name='DANGE_SOURCE', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    dist_cell = CharField(column_name='DIST_CELL', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    item_c_score = DecimalField(column_name='ITEM_C_SCORE', null=True)
    item_d_score = DecimalField(column_name='ITEM_D_SCORE', null=True)
    item_e_score = DecimalField(column_name='ITEM_E_SCORE', null=True)
    item_l_score = DecimalField(column_name='ITEM_L_SCORE', null=True)
    job_active = CharField(column_name='JOB_ACTIVE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    remark = CharField(column_name='REMARK', null=True)
    risk_level = CharField(column_name='RISK_LEVEL', null=True)
    score_method = CharField(column_name='SCORE_METHOD', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ds_riskscore'

class CDtComment(BaseModel):
    commentdate = DateTimeField(column_name='COMMENTDATE', null=True)
    comment_psn = CharField(column_name='COMMENT_PSN', null=True)
    comment_psn_id = CharField(column_name='COMMENT_PSN_ID', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    journal_id = CharField(column_name='JOURNAL_ID', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    opinion = CharField(column_name='OPINION', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    valuation = CharField(column_name='VALUATION', null=True)

    class Meta:
        table_name = 'c_dt_comment'
        indexes = (
            (('journal_id', 'created_by'), False),
        )

class CDtCommentCopy20230129(BaseModel):
    commentdate = DateTimeField(column_name='COMMENTDATE', null=True)
    comment_psn = CharField(column_name='COMMENT_PSN', null=True)
    comment_psn_id = CharField(column_name='COMMENT_PSN_ID', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    journal_id = CharField(column_name='JOURNAL_ID', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    opinion = CharField(column_name='OPINION', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    valuation = CharField(column_name='VALUATION', null=True)

    class Meta:
        table_name = 'c_dt_comment_copy20230129'
        indexes = (
            (('journal_id', 'created_by'), False),
        )

class CDtCommentinpsn(BaseModel):
    commented_org = CharField(column_name='COMMENTED_ORG', null=True)
    commented_org_id = CharField(column_name='COMMENTED_ORG_ID', null=True)
    commented_psn = CharField(column_name='COMMENTED_PSN', null=True)
    commented_psn_id = CharField(column_name='COMMENTED_PSN_ID')
    commented_psn_no = CharField(column_name='COMMENTED_PSN_NO', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID')
    id = CharField(null=True)

    class Meta:
        table_name = 'c_dt_commentinpsn'
        indexes = (
            (('psn_id', 'commented_psn_id'), True),
        )
        primary_key = CompositeKey('commented_psn_id', 'psn_id')

class CDtDatacapture(BaseModel):
    circle = CharField(null=True)
    duty = CharField(null=True)
    dutyid = CharField(null=True)
    frequency = CharField(null=True)
    gwzz = CharField(null=True)
    lvsx = CharField(null=True)
    org = CharField(null=True)
    percode = CharField(null=True)
    pername = CharField(null=True)
    year = IntegerField(null=True)

    class Meta:
        table_name = 'c_dt_datacapture'

class CDtDutylist(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    pos_duty = CharField(column_name='POS_DUTY', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_dt_dutylist'

class CDtDutylistCopy(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    pos_duty = CharField(column_name='POS_DUTY', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_dt_dutylist_copy'

class CDtDutylistCopy202301040931(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    pos_duty = CharField(column_name='POS_DUTY', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_dt_dutylist_copy202301040931'

class CDtDutylistCycle(BaseModel):
    begintime = DateTimeField(null=True)
    cycle = CharField(null=True)
    cycle_main = CharField(null=True)
    cycle_num = IntegerField(null=True)
    endtime = DateTimeField(null=True)
    id = CharField(primary_key=True)
    year = IntegerField(null=True)

    class Meta:
        table_name = 'c_dt_dutylist_cycle'

class CDtDutylistCycleCopy202301040931(BaseModel):
    begintime = DateTimeField(null=True)
    cycle = CharField(null=True)
    cycle_main = CharField(null=True)
    cycle_num = IntegerField(null=True)
    endtime = DateTimeField(null=True)
    id = CharField(primary_key=True)
    year = IntegerField(null=True)

    class Meta:
        table_name = 'c_dt_dutylist_cycle_copy202301040931'

class CDtDutylistCycleMain(BaseModel):
    cycle = CharField(null=True)
    id = CharField(primary_key=True)
    year = IntegerField(null=True)
    zqs = IntegerField(null=True)

    class Meta:
        table_name = 'c_dt_dutylist_cycle_main'

class CDtDutylistCycleMainCopy202301040931(BaseModel):
    cycle = CharField(null=True)
    id = CharField(primary_key=True)
    year = IntegerField(null=True)
    zqs = IntegerField(null=True)

    class Meta:
        table_name = 'c_dt_dutylist_cycle_main_copy202301040931'

class CDtDutylistQc(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    pos_duty = CharField(column_name='POS_DUTY', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_dt_dutylist_qc'

class CDtDutymatter(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    cycle_main = CharField(column_name='CYCLE_MAIN', null=True)
    detail = CharField(column_name='DETAIL', null=True)
    duty_id = CharField(column_name='DUTY_ID', index=True, null=True)
    frequency = DecimalField(column_name='FREQUENCY', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_dt_dutymatter'

class CDtDutymatterCopy202301040931(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    cycle_main = CharField(column_name='CYCLE_MAIN', null=True)
    detail = CharField(column_name='DETAIL', null=True)
    duty_id = CharField(column_name='DUTY_ID', index=True, null=True)
    frequency = DecimalField(column_name='FREQUENCY', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_dt_dutymatter_copy202301040931'

class CDtDutymatterQc(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    detail = CharField(column_name='DETAIL', null=True)
    duty_id = CharField(column_name='DUTY_ID', null=True)
    frequency = DecimalField(column_name='FREQUENCY', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '修订中'")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_dt_dutymatter_qc'

class CDtDutyreason(BaseModel):
    cnt = CharField(column_name='CNT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    duty_id = CharField(column_name='DUTY_ID', null=True)
    end_date = CharField(column_name='END_DATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', null=True)
    is_complete = CharField(column_name='IS_COMPLETE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    matter_id = CharField(column_name='MATTER_ID', index=True, null=True)
    period = CharField(column_name='PERIOD', null=True)
    reason = CharField(column_name='REASON', null=True)
    sp_date = DateTimeField(column_name='SP_DATE', null=True)
    sp_per = CharField(column_name='SP_PER', null=True)
    start_date = CharField(column_name='START_DATE', null=True)
    tj_date = DateTimeField(column_name='TJ_DATE', null=True)
    tj_per = CharField(column_name='TJ_PER', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    memo = CharField(null=True)
    status = CharField(null=True)

    class Meta:
        table_name = 'c_dt_dutyreason'

class CDtJournal(BaseModel):
    completion = CharField(column_name='COMPLETION')
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle_pid = CharField(column_name='CYCLE_PID', null=True)
    entourage = CharField(column_name='ENTOURAGE', null=True)
    hd_id = CharField(column_name='HD_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    matterdate = DateTimeField(column_name='MATTERDATE', null=True)
    matter_id = CharField(column_name='MATTER_ID', null=True)
    place = CharField(column_name='PLACE', null=True)
    title = CharField(column_name='TITLE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_dt_journal'
        indexes = (
            (('is_active', 'matterdate'), False),
        )

class CDtJournalfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    journal_id = CharField(column_name='JOURNAL_ID', null=True)

    class Meta:
        table_name = 'c_dt_journalfile'

class CDtJournalfj(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    journal_id = CharField(column_name='JOURNAL_ID', null=True)

    class Meta:
        table_name = 'c_dt_journalfj'

class CDtJournalhd(BaseModel):
    hd_desc = CharField(column_name='HD_DESC', null=True)
    hd_id = CharField(column_name='HD_ID')
    journal_id = CharField(column_name='JOURNAL_ID')

    class Meta:
        table_name = 'c_dt_journalhd'
        primary_key = False

class CDtReason(BaseModel):
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'c_dt_reason'

class CDtStatisticOrg(BaseModel):
    id = IntegerField(column_name='ID', null=True)
    description = CharField(null=True)
    level = CharField(null=True)
    org_code = CharField(null=True)
    org_name = CharField(null=True)

    class Meta:
        table_name = 'c_dt_statistic_org'
        primary_key = False

class CEmEmergplay(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    director = CharField(column_name='DIRECTOR', null=True)
    eval_date = DateField(column_name='EVAL_DATE', null=True)
    eval_mind = CharField(column_name='EVAL_MIND', null=True)
    eval_org = CharField(column_name='EVAL_ORG', null=True)
    eval_org_id = CharField(column_name='EVAL_ORG_ID', null=True)
    eval_person = CharField(column_name='EVAL_PERSON', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    outlay = DecimalField(column_name='OUTLAY', null=True)
    play_content = CharField(column_name='PLAY_CONTENT', null=True)
    play_date = DateField(column_name='PLAY_DATE', null=True)
    play_level = CharField(column_name='PLAY_LEVEL', null=True)
    play_name = CharField(column_name='PLAY_NAME', null=True)
    play_org = CharField(column_name='PLAY_ORG', null=True)
    play_org_id = CharField(column_name='PLAY_ORG_ID', null=True)
    play_plan_num = IntegerField(column_name='PLAY_PLAN_NUM')
    play_psn_num = IntegerField(column_name='PLAY_PSN_NUM', null=True)
    play_style = CharField(column_name='PLAY_STYLE', null=True)
    prof_num = IntegerField(column_name='PROF_NUM', null=True)
    trade_type = CharField(column_name='TRADE_TYPE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_em_emergplay'

class CEmEmergplayfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    play_id = CharField(column_name='PLAY_ID', null=True)

    class Meta:
        table_name = 'c_em_emergplayfile'

class CEmEquipment(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    day_charge = CharField(column_name='DAY_CHARGE', null=True)
    day_charge_id = CharField(column_name='DAY_CHARGE_ID', null=True)
    day_mobile = CharField(column_name='DAY_MOBILE', null=True)
    day_tel = CharField(column_name='DAY_TEL', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    lat = CharField(column_name='LAT', null=True)
    lng = CharField(column_name='LNG', null=True)
    manage_org = CharField(column_name='MANAGE_ORG', null=True)
    manage_org_id = CharField(column_name='MANAGE_ORG_ID', null=True)
    model = CharField(column_name='MODEL', null=True)
    name = CharField(column_name='NAME', null=True)
    night_charge = CharField(column_name='NIGHT_CHARGE', null=True)
    night_charge_id = CharField(column_name='NIGHT_CHARGE_ID', null=True)
    night_mobile = CharField(column_name='NIGHT_MOBILE', null=True)
    night_tel = CharField(column_name='NIGHT_TEL', null=True)
    place = CharField(column_name='PLACE', null=True)
    quantity = IntegerField(column_name='QUANTITY', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_em_equipment'

class CEmPlan(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    director = CharField(column_name='DIRECTOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    level = CharField(column_name='LEVEL', null=True)
    month = CharField(column_name='MONTH', null=True)
    name = CharField(column_name='NAME', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_em_plan'

class CEmScenarios(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    description = CharField(column_name='DESCRIPTION', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    scenarios_date = DateField(column_name='SCENARIOS_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_em_scenarios'

class CEmScenariosfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    scenarios_id = CharField(column_name='SCENARIOS_ID', null=True)

    class Meta:
        table_name = 'c_em_scenariosfile'

class CFile(BaseModel):
    created = CharField(column_name='CREATED', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateField(column_name='CREATED_DATE', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    source = CharField(column_name='SOURCE', null=True)

    class Meta:
        table_name = 'c_file'

class CHdChargeinorg(BaseModel):
    org_id = CharField(column_name='ORG_ID')
    org_name = CharField(column_name='ORG_NAME', null=True)
    psn_id = CharField(column_name='PSN_ID')
    psn_name = CharField(column_name='PSN_NAME', null=True)

    class Meta:
        table_name = 'c_hd_chargeinorg'
        indexes = (
            (('org_id', 'psn_id'), True),
        )
        primary_key = CompositeKey('org_id', 'psn_id')

class CHdHiddendangerfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    hd_id = CharField(column_name='HD_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)

    class Meta:
        table_name = 'c_hd_hiddendangerfile'

class CHdHiddendangerinfo(BaseModel):
    charge = CharField(column_name='CHARGE', null=True)
    charge_id = CharField(column_name='CHARGE_ID', null=True)
    checker = CharField(column_name='CHECKER', null=True)
    checker_id = CharField(column_name='CHECKER_ID', null=True)
    check_date = DateField(column_name='CHECK_DATE', null=True)
    client = CharField(column_name='CLIENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    hd_desc = CharField(column_name='HD_DESC', null=True)
    hd_level = CharField(column_name='HD_LEVEL', null=True)
    hd_money = DecimalField(column_name='HD_MONEY', null=True)
    hd_org = CharField(column_name='HD_ORG', null=True)
    hd_org_id = CharField(column_name='HD_ORG_ID', null=True)
    hd_reason = CharField(column_name='HD_REASON', null=True)
    hd_source = CharField(column_name='HD_SOURCE', null=True)
    hd_status = CharField(column_name='HD_STATUS', null=True)
    hd_type = CharField(column_name='HD_TYPE', null=True)
    hd_type_self = CharField(column_name='HD_TYPE_SELF', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_exam = CharField(column_name='IS_EXAM', constraints=[SQL("DEFAULT '0'")], null=True)
    is_neaten = CharField(column_name='IS_NEATEN', constraints=[SQL("DEFAULT '0'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    lat = CharField(column_name='LAT', null=True)
    lng = CharField(column_name='LNG', null=True)
    neate_type = CharField(column_name='NEATE_TYPE', null=True)
    temp_measure = CharField(column_name='TEMP_MEASURE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_hd_hiddendangerinfo'

class CHdHiddendangerinfoCopy(BaseModel):
    charge = CharField(column_name='CHARGE', null=True)
    charge_id = CharField(column_name='CHARGE_ID', null=True)
    checker = CharField(column_name='CHECKER', null=True)
    checker_id = CharField(column_name='CHECKER_ID', null=True)
    check_date = DateField(column_name='CHECK_DATE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    hd_desc = CharField(column_name='HD_DESC', null=True)
    hd_level = CharField(column_name='HD_LEVEL', null=True)
    hd_money = DecimalField(column_name='HD_MONEY', null=True)
    hd_org = CharField(column_name='HD_ORG', null=True)
    hd_org_id = CharField(column_name='HD_ORG_ID', null=True)
    hd_reason = CharField(column_name='HD_REASON', null=True)
    hd_source = CharField(column_name='HD_SOURCE', null=True)
    hd_status = CharField(column_name='HD_STATUS', null=True)
    hd_type = CharField(column_name='HD_TYPE', null=True)
    hd_type_self = CharField(column_name='HD_TYPE_SELF', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_exam = CharField(column_name='IS_EXAM', constraints=[SQL("DEFAULT '0'")], null=True)
    is_neaten = CharField(column_name='IS_NEATEN', constraints=[SQL("DEFAULT '0'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    neate_type = CharField(column_name='NEATE_TYPE', null=True)
    temp_measure = CharField(column_name='TEMP_MEASURE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_hd_hiddendangerinfo_copy'

class CHdHidexaminfo(BaseModel):
    charge = CharField(column_name='CHARGE', null=True)
    charge_exam_date = DateTimeField(column_name='CHARGE_EXAM_DATE', null=True)
    charge_exam_info = CharField(column_name='CHARGE_EXAM_INFO', null=True)
    charge_id = CharField(column_name='CHARGE_ID', null=True)
    charge_is_exam_complete = CharField(column_name='CHARGE_IS_EXAM_COMPLETE', constraints=[SQL("DEFAULT '0'")], null=True)
    charge_is_exam_pass = CharField(column_name='CHARGE_IS_EXAM_PASS', null=True)
    checker = CharField(column_name='CHECKER', null=True)
    checker_exam_date = DateTimeField(column_name='CHECKER_EXAM_DATE', null=True)
    checker_exam_info = CharField(column_name='CHECKER_EXAM_INFO', null=True)
    checker_id = CharField(column_name='CHECKER_ID', null=True)
    checker_is_exam_complete = CharField(column_name='CHECKER_IS_EXAM_COMPLETE', constraints=[SQL("DEFAULT '0'")], null=True)
    checker_is_exam_pass = CharField(column_name='CHECKER_IS_EXAM_PASS', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    hd_id = CharField(column_name='HD_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_hd_hidexaminfo'

class CHdHidneateninfo(BaseModel):
    client = CharField(column_name='CLIENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    delay_limit_date = DateField(column_name='DELAY_LIMIT_DATE', null=True)
    hd_id = CharField(column_name='HD_ID', index=True, null=True)
    hd_reason = CharField(column_name='HD_REASON', null=True)
    id = CharField(column_name='ID', primary_key=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    neaten_date = DateField(column_name='NEATEN_DATE', null=True)
    neaten_dept = CharField(column_name='NEATEN_DEPT', null=True)
    neaten_dept_id = CharField(column_name='NEATEN_DEPT_ID', null=True)
    neaten_fund = DecimalField(column_name='NEATEN_FUND', null=True)
    neaten_limit_date = DateField(column_name='NEATEN_LIMIT_DATE', null=True)
    neaten_measure = CharField(column_name='NEATEN_MEASURE', null=True)
    neaten_nopass_reason = CharField(column_name='NEATEN_NOPASS_REASON', null=True)
    neaten_psn = CharField(column_name='NEATEN_PSN', null=True)
    neaten_psn_id = CharField(column_name='NEATEN_PSN_ID', null=True)
    neaten_result = CharField(column_name='NEATEN_RESULT', null=True)
    neaten_suggest = CharField(column_name='NEATEN_SUGGEST', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_hd_hidneateninfo'

class CHdInstance(BaseModel):
    action_time = DateTimeField(column_name='ACTION_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    aft_status = CharField(column_name='AFT_STATUS', null=True)
    bef_status = CharField(column_name='BEF_STATUS', null=True)
    deal_action = CharField(column_name='DEAL_ACTION', null=True)
    deal_psn = CharField(column_name='DEAL_PSN', null=True)
    deal_psn_id = CharField(column_name='DEAL_PSN_ID', null=True)
    hd_id = CharField(column_name='HD_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    remark = CharField(column_name='REMARK', null=True)
    seq = IntegerField(column_name='SEQ', null=True)

    class Meta:
        table_name = 'c_hd_instance'

class CHdLeaderinfo(BaseModel):
    id = CharField(column_name='ID')
    usercode = CharField(column_name='USERCODE')
    username = CharField(column_name='USERNAME', null=True)

    class Meta:
        table_name = 'c_hd_leaderinfo'
        primary_key = False

class CHdManage(BaseModel):
    org_code = CharField(column_name='ORG_CODE', primary_key=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    psn_name = CharField(column_name='PSN_NAME', null=True)

    class Meta:
        table_name = 'c_hd_manage'

class CHdUrgenotice(BaseModel):
    area_name = CharField(column_name='AREA_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    duty_org = CharField(column_name='DUTY_ORG', null=True)
    duty_org_id = CharField(column_name='DUTY_ORG_ID', null=True)
    duty_psn_name = CharField(column_name='DUTY_PSN_NAME', null=True)
    event_desc = CharField(column_name='EVENT_DESC', null=True)
    fact_complete_date = DateField(column_name='FACT_COMPLETE_DATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    neaten_psn = CharField(column_name='NEATEN_PSN', null=True)
    neaten_psn_name = CharField(column_name='NEATEN_PSN_NAME', null=True)
    neaten_schema = CharField(column_name='NEATEN_SCHEMA', null=True)
    notice_date = DateField(column_name='NOTICE_DATE', null=True)
    notice_no = CharField(column_name='NOTICE_NO', null=True)
    plan_neaten_date = DateField(column_name='PLAN_NEATEN_DATE', null=True)
    standard = CharField(column_name='STANDARD', null=True)
    temp_measure = CharField(column_name='TEMP_MEASURE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    urge_status = CharField(column_name='URGE_STATUS', null=True)
    urge_type = CharField(column_name='URGE_TYPE', null=True)

    class Meta:
        table_name = 'c_hd_urgenotice'

class CHdUrgenoticeSeq(BaseModel):
    month = CharField(column_name='MONTH')
    seq = IntegerField(column_name='SEQ', null=True)
    year = CharField(column_name='YEAR')

    class Meta:
        table_name = 'c_hd_urgenotice_seq'
        primary_key = False

class CHdUrgenoticefile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    notice_id = CharField(column_name='NOTICE_ID', null=True)

    class Meta:
        table_name = 'c_hd_urgenoticefile'

class CLrLawrule(BaseModel):
    act_date = DateTimeField(column_name='ACT_DATE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    fileno = CharField(column_name='FILENO', null=True)
    hand_dept = CharField(column_name='HAND_DEPT', null=True)
    hand_dept_id = CharField(column_name='HAND_DEPT_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    kind = CharField(column_name='KIND', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    level = CharField(column_name='LEVEL', null=True)
    name = CharField(column_name='NAME', null=True)
    pub_date = DateTimeField(column_name='PUB_DATE', null=True)
    pub_org_name = CharField(column_name='PUB_ORG_NAME', null=True)
    remark = CharField(column_name='REMARK', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_lr_lawrule'

class CLrLawrulefile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    rule_id = CharField(column_name='RULE_ID', null=True)

    class Meta:
        table_name = 'c_lr_lawrulefile'

class CLrLawrulefitdept(BaseModel):
    fit_dept = CharField(column_name='FIT_DEPT', null=True)
    fit_dept_id = CharField(column_name='FIT_DEPT_ID')
    rule_id = CharField(column_name='RULE_ID')

    class Meta:
        table_name = 'c_lr_lawrulefitdept'
        indexes = (
            (('rule_id', 'fit_dept_id'), True),
        )
        primary_key = CompositeKey('fit_dept_id', 'rule_id')

class CLrLawrulepic(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    rule_id = CharField(column_name='RULE_ID', null=True)

    class Meta:
        table_name = 'c_lr_lawrulepic'

class CNaNews(BaseModel):
    abstract = CharField(column_name='ABSTRACT', null=True)
    content = TextField(column_name='CONTENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_draft = CharField(column_name='IS_DRAFT', constraints=[SQL("DEFAULT '0'")], null=True)
    is_recommend = CharField(column_name='IS_RECOMMEND', constraints=[SQL("DEFAULT '0'")], null=True)
    is_top = CharField(column_name='IS_TOP', constraints=[SQL("DEFAULT '0'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    pub_date = DateField(column_name='PUB_DATE', null=True)
    pub_dept = CharField(column_name='PUB_DEPT', null=True)
    pub_dept_id = CharField(column_name='PUB_DEPT_ID', null=True)
    title = CharField(column_name='TITLE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_na_news'
        primary_key = False

class CNaNewsfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    news_id = CharField(column_name='NEWS_ID', null=True)

    class Meta:
        table_name = 'c_na_newsfile'

class CNaNewspic(BaseModel):
    description = CharField(column_name='DESCRIPTION', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    news_id = CharField(column_name='NEWS_ID', null=True)
    seq = IntegerField(column_name='SEQ', null=True)

    class Meta:
        table_name = 'c_na_newspic'

class CNaNotice(BaseModel):
    abstract = CharField(column_name='ABSTRACT', null=True)
    content = TextField(column_name='CONTENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_draft = CharField(column_name='IS_DRAFT', constraints=[SQL("DEFAULT '0'")], null=True)
    is_recommend = CharField(column_name='IS_RECOMMEND', constraints=[SQL("DEFAULT '0'")], null=True)
    is_top = CharField(column_name='IS_TOP', constraints=[SQL("DEFAULT '0'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    pub_date = DateField(column_name='PUB_DATE', null=True)
    pub_dept = CharField(column_name='PUB_DEPT', null=True)
    pub_dept_id = CharField(column_name='PUB_DEPT_ID', null=True)
    title = CharField(column_name='TITLE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_na_notice'

class CNaNoticefile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    rule_id = CharField(column_name='RULE_ID', null=True)

    class Meta:
        table_name = 'c_na_noticefile'

class CNaNoticefitdept(BaseModel):
    fit_dept = CharField(column_name='FIT_DEPT', null=True)
    fit_dept_id = CharField(column_name='FIT_DEPT_ID')
    notice_id = CharField(column_name='NOTICE_ID')

    class Meta:
        table_name = 'c_na_noticefitdept'
        indexes = (
            (('notice_id', 'fit_dept_id'), True),
        )
        primary_key = CompositeKey('fit_dept_id', 'notice_id')

class CNaNoticepic(BaseModel):
    description = CharField(column_name='DESCRIPTION', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    rule_id = CharField(column_name='RULE_ID', null=True)
    seq = IntegerField(column_name='SEQ', null=True)

    class Meta:
        table_name = 'c_na_noticepic'

class CPfDanger(BaseModel):
    contact_num = IntegerField(column_name='CONTACT_NUM', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    job_danger = CharField(column_name='JOB_DANGER', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    process_num = IntegerField(column_name='PROCESS_NUM', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_pf_danger'

class CPfDangerdoc(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    fact_num = IntegerField(column_name='FACT_NUM', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    job_danger = CharField(column_name='JOB_DANGER', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    pass_num = IntegerField(column_name='PASS_NUM', null=True)
    plan_num = IntegerField(column_name='PLAN_NUM', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = IntegerField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_pf_dangerdoc'

class CPfDangerplace(BaseModel):
    danger_id = CharField(column_name='DANGER_ID')
    danger_place = CharField(column_name='DANGER_PLACE', null=True)
    id = CharField(column_name='ID', primary_key=True)

    class Meta:
        table_name = 'c_pf_dangerplace'

class CPfHealth(BaseModel):
    check_type = CharField(column_name='CHECK_TYPE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    fact_num = IntegerField(column_name='FACT_NUM', null=True)
    forbid_num = IntegerField(column_name='FORBID_NUM', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    job_danger = CharField(column_name='JOB_DANGER', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    plan_num = IntegerField(column_name='PLAN_NUM', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = IntegerField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_pf_health'

class CSeCrane(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    check_status = CharField(column_name='CHECK_STATUS', null=True)
    check_unit = CharField(column_name='CHECK_UNIT', null=True)
    code = CharField(column_name='CODE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    equ_name = CharField(column_name='EQU_NAME', null=True)
    equ_type = CharField(column_name='EQU_TYPE', null=True)
    height = CharField(column_name='HEIGHT', null=True)
    id = AutoField(column_name='ID')
    install_date = DateField(column_name='INSTALL_DATE', null=True)
    install_unit = CharField(column_name='INSTALL_UNIT', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_auxiliayhook = CharField(column_name='IS_AUXILIAYHOOK', null=True)
    is_auxiliaypole = CharField(column_name='IS_AUXILIAYPOLE', null=True)
    is_clampexist = CharField(column_name='IS_CLAMPEXIST', null=True)
    is_doublecab = CharField(column_name='IS_DOUBLECAB', null=True)
    is_doublecar = CharField(column_name='IS_DOUBLECAR', null=True)
    is_elecsuckerexist = CharField(column_name='IS_ELECSUCKEREXIST', null=True)
    is_explosion_proof = CharField(column_name='IS_EXPLOSION_PROOF', null=True)
    is_grabexist = CharField(column_name='IS_GRABEXIST', null=True)
    is_metallurgy = CharField(column_name='IS_METALLURGY', null=True)
    is_rakeexist = CharField(column_name='IS_RAKEEXIST', null=True)
    last_checkdate = DateField(column_name='LAST_CHECKDATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    lifting_t = CharField(column_name='LIFTING_T', null=True)
    location = CharField(column_name='LOCATION', null=True)
    manufacturer = CharField(column_name='MANUFACTURER', null=True)
    model = CharField(column_name='MODEL', null=True)
    next_checkdate = DateField(column_name='NEXT_CHECKDATE', null=True)
    owner = CharField(column_name='OWNER', null=True)
    owner_id = CharField(column_name='OWNER_ID', null=True)
    registration_code = CharField(column_name='REGISTRATION_CODE', null=True)
    registration_no = CharField(column_name='REGISTRATION_NO', null=True)
    result = CharField(column_name='RESULT', null=True)
    span = CharField(column_name='SPAN', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    user = CharField(column_name='USER', null=True)
    user_id = CharField(column_name='USER_ID', null=True)

    class Meta:
        table_name = 'c_se_crane'

class CSePipe(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    check_status = CharField(column_name='CHECK_STATUS', null=True)
    check_unit = CharField(column_name='CHECK_UNIT', null=True)
    code = CharField(column_name='CODE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    diameter = CharField(column_name='DIAMETER', null=True)
    equ_name = CharField(column_name='EQU_NAME', null=True)
    equ_status = CharField(column_name='EQU_STATUS', null=True)
    gb50160 = CharField(column_name='GB50160', null=True)
    gb5044 = CharField(column_name='GB5044', null=True)
    id = AutoField(column_name='ID')
    install_date = DateField(column_name='INSTALL_DATE', null=True)
    install_unit = CharField(column_name='INSTALL_UNIT', null=True)
    isundergrand = CharField(column_name='ISUNDERGRAND', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_checkdate = DateField(column_name='LAST_CHECKDATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    location = CharField(column_name='LOCATION', null=True)
    material = CharField(column_name='MATERIAL', null=True)
    medium = CharField(column_name='MEDIUM', null=True)
    next_checkdate = DateField(column_name='NEXT_CHECKDATE', null=True)
    owner = CharField(column_name='OWNER', null=True)
    owner_id = CharField(column_name='OWNER_ID', null=True)
    pipe_length = CharField(column_name='PIPE_LENGTH', null=True)
    pressure = CharField(column_name='PRESSURE', null=True)
    registration_code = CharField(column_name='REGISTRATION_CODE', null=True)
    registration_no = CharField(column_name='REGISTRATION_NO', null=True)
    result = CharField(column_name='RESULT', null=True)
    temprature = CharField(column_name='TEMPRATURE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    user = CharField(column_name='USER', null=True)
    user_id = CharField(column_name='USER_ID', null=True)

    class Meta:
        table_name = 'c_se_pipe'

class CSePlan(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    cnt_1 = DecimalField(column_name='CNT_1', null=True)
    cnt_10 = DecimalField(column_name='CNT_10', null=True)
    cnt_11 = DecimalField(column_name='CNT_11', null=True)
    cnt_12 = DecimalField(column_name='CNT_12', null=True)
    cnt_2 = DecimalField(column_name='CNT_2', null=True)
    cnt_3 = DecimalField(column_name='CNT_3', null=True)
    cnt_4 = DecimalField(column_name='CNT_4', null=True)
    cnt_5 = DecimalField(column_name='CNT_5', null=True)
    cnt_6 = DecimalField(column_name='CNT_6', null=True)
    cnt_7 = DecimalField(column_name='CNT_7', null=True)
    cnt_8 = DecimalField(column_name='CNT_8', null=True)
    cnt_9 = DecimalField(column_name='CNT_9', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_se_plan'

class CSeVessel(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    check_status = CharField(column_name='CHECK_STATUS', null=True)
    check_unit = CharField(column_name='CHECK_UNIT', null=True)
    code = CharField(column_name='CODE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    cycle = CharField(column_name='CYCLE', null=True)
    design_pressure = CharField(column_name='DESIGN_PRESSURE', null=True)
    equ_name = CharField(column_name='EQU_NAME', null=True)
    equ_status = CharField(column_name='EQU_STATUS', null=True)
    height = CharField(column_name='HEIGHT', null=True)
    id = AutoField(column_name='ID')
    install_date = DateField(column_name='INSTALL_DATE', null=True)
    install_unit = CharField(column_name='INSTALL_UNIT', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_checkdate = DateField(column_name='LAST_CHECKDATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    last_ycheckdate = DateField(column_name='LAST_YCHECKDATE', null=True)
    location = CharField(column_name='LOCATION', null=True)
    manufacturer = CharField(column_name='MANUFACTURER', null=True)
    model = CharField(column_name='MODEL', null=True)
    next_checkdate = DateField(column_name='NEXT_CHECKDATE', null=True)
    next_ycheckdate = DateField(column_name='NEXT_YCHECKDATE', null=True)
    owner = CharField(column_name='OWNER', null=True)
    owner_id = CharField(column_name='OWNER_ID', null=True)
    rated_pressure = CharField(column_name='RATED_PRESSURE', null=True)
    registration_code = CharField(column_name='REGISTRATION_CODE', null=True)
    registration_no = CharField(column_name='REGISTRATION_NO', null=True)
    result = CharField(column_name='RESULT', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    user = CharField(column_name='USER', null=True)
    user_id = CharField(column_name='USER_ID', null=True)
    vessel_shape = CharField(column_name='VESSEL_SHAPE', null=True)
    vessel_type = CharField(column_name='VESSEL_TYPE', null=True)
    volume = CharField(column_name='VOLUME', null=True)
    ycheck_status = CharField(column_name='YCHECK_STATUS', null=True)
    ycycle = CharField(column_name='YCYCLE', null=True)
    yresult = CharField(column_name='YRESULT', null=True)

    class Meta:
        table_name = 'c_se_vessel'

class CTrManagertrain(BaseModel):
    cert_end_validate = DateField(column_name='CERT_END_VALIDATE', null=True)
    cert_no = CharField(column_name='CERT_NO', null=True)
    cert_start_validate = DateField(column_name='CERT_START_VALIDATE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    diploma = CharField(column_name='DIPLOMA', null=True)
    duty = CharField(column_name='DUTY', null=True)
    end_train_date = DateField(column_name='END_TRAIN_DATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    issue_org = CharField(column_name='ISSUE_ORG', constraints=[SQL("DEFAULT ''")])
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    org_type = CharField(column_name='ORG_TYPE', null=True)
    qual_type = CharField(column_name='QUAL_TYPE', null=True)
    reaudit_one = CharField(column_name='REAUDIT_ONE', null=True)
    reaudit_two = CharField(column_name='REAUDIT_TWO', null=True)
    sex = CharField(column_name='SEX', null=True)
    start_train_date = DateField(column_name='START_TRAIN_DATE', null=True)
    title = CharField(column_name='TITLE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_tr_managertrain'

class CTrManagertrainfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    train_id = CharField(column_name='TRAIN_ID', null=True)

    class Meta:
        table_name = 'c_tr_managertrainfile'

class CTrSpeccert(BaseModel):
    birthday = CharField(column_name='BIRTHDAY', null=True)
    cert_end_validate = DateField(column_name='CERT_END_VALIDATE', null=True)
    cert_no = CharField(column_name='CERT_NO', null=True)
    cert_start_validate = DateField(column_name='CERT_START_VALIDATE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    diploma = CharField(column_name='DIPLOMA', null=True)
    id = CharField(column_name='ID', primary_key=True)
    id_card = CharField(column_name='ID_CARD', null=True)
    issue_org = CharField(column_name='ISSUE_ORG', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    job_type = CharField(column_name='JOB_TYPE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    reaudit_date = DateField(column_name='REAUDIT_DATE', null=True)
    sex = CharField(column_name='SEX', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    work_item = CharField(column_name='WORK_ITEM', null=True)

    class Meta:
        table_name = 'c_tr_speccert'

class CTrTrainacct(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    content = CharField(column_name='CONTENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    level = CharField(column_name='LEVEL', null=True)
    name = CharField(column_name='NAME', null=True)
    object = CharField(column_name='OBJECT', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    place = CharField(column_name='PLACE', null=True)
    plam_num = IntegerField(column_name='PLAM_NUM', null=True)
    plan_hour = DecimalField(column_name='PLAN_HOUR', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    teacher = CharField(column_name='TEACHER', null=True)
    train_hour = DecimalField(column_name='TRAIN_HOUR', null=True)
    train_num = IntegerField(column_name='TRAIN_NUM', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_tr_trainacct'

class CTrTrainacctfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    id = CharField(column_name='ID', primary_key=True)
    train_id = CharField(column_name='TRAIN_ID', null=True)

    class Meta:
        table_name = 'c_tr_trainacctfile'

class CTsControlplan(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    month1 = IntegerField(column_name='MONTH1', null=True)
    month10 = IntegerField(column_name='MONTH10', null=True)
    month11 = IntegerField(column_name='MONTH11', null=True)
    month12 = IntegerField(column_name='MONTH12', null=True)
    month2 = IntegerField(column_name='MONTH2', null=True)
    month3 = IntegerField(column_name='MONTH3', null=True)
    month4 = IntegerField(column_name='MONTH4', null=True)
    month5 = IntegerField(column_name='MONTH5', null=True)
    month6 = IntegerField(column_name='MONTH6', null=True)
    month7 = IntegerField(column_name='MONTH7', null=True)
    month8 = IntegerField(column_name='MONTH8', null=True)
    month9 = IntegerField(column_name='MONTH9', null=True)
    special_type = CharField(column_name='SPECIAL_TYPE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    year = IntegerField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_ts_controlplan'

class CTsGroupexam(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dept = CharField(column_name='DEPT', null=True)
    dept_id = CharField(column_name='DEPT_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    nopass_content = CharField(column_name='NOPASS_CONTENT', null=True)
    pass_date = DateTimeField(column_name='PASS_DATE', null=True)
    pass_point = DecimalField(column_name='PASS_POINT', null=True)
    team_group = CharField(column_name='TEAM_GROUP', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'c_ts_groupexam'

class CTsGroupexamfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_path = CharField(column_name='FILE_PATH', null=True)
    groupexam_id = CharField(column_name='GROUPEXAM_ID', null=True)
    id = CharField(column_name='ID', null=True)

    class Meta:
        table_name = 'c_ts_groupexamfile'
        primary_key = False

class CViolatingfile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    id = CharField(column_name='ID', primary_key=True)
    vio_id = CharField(column_name='VIO_ID', null=True)

    class Meta:
        table_name = 'c_violatingfile'

class CWiAcpara(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    death_1 = IntegerField(column_name='DEATH_1', null=True)
    death_2 = IntegerField(column_name='DEATH_2', null=True)
    death_3 = IntegerField(column_name='DEATH_3', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = AutoField(column_name='ID')
    minor_1 = IntegerField(column_name='MINOR_1', null=True)
    minor_2 = IntegerField(column_name='MINOR_2', null=True)
    minor_3 = IntegerField(column_name='MINOR_3', null=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    serious_1 = IntegerField(column_name='SERIOUS_1', null=True)
    serious_2 = IntegerField(column_name='SERIOUS_2', null=True)
    serious_3 = IntegerField(column_name='SERIOUS_3', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    target = DecimalField(column_name='TARGET', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_wi_acpara'

class CWiDtpara(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    cnt_complete = IntegerField(column_name='CNT_COMPLETE', null=True)
    cnt_total = IntegerField(column_name='CNT_TOTAL', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_wi_dtpara'

class CWiEmpara(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    rate_1 = DecimalField(column_name='RATE_1', null=True)
    rate_2 = DecimalField(column_name='RATE_2', null=True)
    rate_3 = DecimalField(column_name='RATE_3', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_wi_empara'

class CWiHdpara(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)
    solved_general_harzard = IntegerField(null=True)
    solved_severe_hazard = IntegerField(null=True)
    total_general_hazard = IntegerField(null=True)
    total_severe_hazard = IntegerField(null=True)

    class Meta:
        table_name = 'c_wi_hdpara'

class CWiIncidentsHistory(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    enddate = DateTimeField(column_name='ENDDATE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    startdate = DateTimeField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)
    fire_smoothing = DecimalField(null=True)
    other_smoothing = DecimalField(null=True)
    production_smoothing = DecimalField(null=True)

    class Meta:
        table_name = 'c_wi_incidents_history'

class CWiTargetstat(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    forecast_1 = CharField(column_name='FORECAST_1', constraints=[SQL("DEFAULT '注意'")], null=True)
    forecast_2 = CharField(column_name='FORECAST_2', constraints=[SQL("DEFAULT '注意'")], null=True)
    forecast_3 = CharField(column_name='FORECAST_3', constraints=[SQL("DEFAULT '注意'")], null=True)
    forecast_4 = CharField(column_name='FORECAST_4', constraints=[SQL("DEFAULT '注意'")], null=True)
    forecast_5 = CharField(column_name='FORECAST_5', constraints=[SQL("DEFAULT '注意'")], null=True)
    forecast_6 = CharField(column_name='FORECAST_6', constraints=[SQL("DEFAULT '注意'")], null=True)
    forecast_7 = CharField(column_name='FORECAST_7', constraints=[SQL("DEFAULT '注意'")], null=True)
    id = CharField(column_name='ID', primary_key=True)
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    result_1 = DecimalField(column_name='RESULT_1', null=True)
    result_2 = DecimalField(column_name='RESULT_2', null=True)
    result_2_actual = DecimalField(column_name='RESULT_2_ACTUAL', null=True)
    result_3 = DecimalField(column_name='RESULT_3', null=True)
    result_4 = DecimalField(column_name='RESULT_4', null=True)
    result_5 = DecimalField(column_name='RESULT_5', null=True)
    result_6 = DecimalField(column_name='RESULT_6', null=True)
    result_7 = DecimalField(column_name='RESULT_7', null=True)
    result_7_actual = DecimalField(column_name='RESULT_7_ACTUAL', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_wi_targetstat'

class CWiTrpara(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    gen_rate_1 = DecimalField(column_name='GEN_RATE_1', null=True)
    gen_rate_2 = DecimalField(column_name='GEN_RATE_2', null=True)
    gen_rate_3 = DecimalField(column_name='GEN_RATE_3', null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    sp_rate_1 = DecimalField(column_name='SP_RATE_1', null=True)
    sp_rate_2 = DecimalField(column_name='SP_RATE_2', null=True)
    sp_rate_3 = DecimalField(column_name='SP_RATE_3', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_wi_trpara'

class CWiVipara(BaseModel):
    category = CharField(column_name='CATEGORY', null=True)
    cnt_1 = IntegerField(column_name='CNT_1', null=True)
    cnt_2 = IntegerField(column_name='CNT_2', null=True)
    cnt_3 = IntegerField(column_name='CNT_3', null=True)
    enddate = DateField(column_name='ENDDATE', null=True)
    id = AutoField(column_name='ID')
    org = CharField(column_name='ORG', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    period = CharField(column_name='PERIOD', null=True)
    psn = CharField(column_name='PSN', null=True)
    psn_id = CharField(column_name='PSN_ID', null=True)
    startdate = DateField(column_name='STARTDATE', null=True)
    year = CharField(column_name='YEAR', null=True)

    class Meta:
        table_name = 'c_wi_vipara'

class CWiWordReport(BaseModel):
    content = TextField(column_name='CONTENT', null=True)
    id = CharField(column_name='ID', primary_key=True)
    month = CharField(column_name='MONTH', null=True)
    org = CharField(column_name='ORG', constraints=[SQL("DEFAULT '大型厂'")], null=True)
    org_id = CharField(column_name='ORG_ID', constraints=[SQL("DEFAULT '0021811'")], null=True)
    year = CharField(column_name='YEAR', null=True)
    gen_time = DateTimeField(null=True)

    class Meta:
        table_name = 'c_wi_word_report'

class CaseInfo(BaseModel):
    card_no = CharField(column_name='CARD_NO', null=True)
    case_info_id = IntegerField(column_name='CASE_INFO_ID', null=True)
    file_id = CharField(column_name='FILE_ID', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    tel = CharField(column_name='TEL', null=True)
    user_name = CharField(column_name='USER_NAME', null=True)
    user_no = CharField(column_name='USER_NO', null=True)

    class Meta:
        table_name = 'case_info'

class CaseMain(BaseModel):
    activiti_key = CharField(column_name='ACTIVITI_KEY', null=True)
    activiti_stat = CharField(column_name='ACTIVITI_STAT', null=True)
    actual_commencement_date = DateTimeField(column_name='ACTUAL_COMMENCEMENT_DATE', null=True)
    approval_comments = TextField(column_name='APPROVAL_COMMENTS', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    estimated_completion_date = DateTimeField(column_name='ESTIMATED_COMPLETION_DATE', null=True)
    file_url = TextField(column_name='FILE_URL', null=True)
    id = AutoField(column_name='ID')
    ind_unique = CharField(column_name='IND_UNIQUE', null=True)
    item_code = CharField(column_name='ITEM_CODE', null=True)
    item_name = CharField(column_name='ITEM_NAME', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    leader_level = CharField(column_name='LEADER_LEVEL', null=True)
    main_leader_sign = CharField(column_name='MAIN_LEADER_SIGN', null=True)
    make_case = CharField(column_name='MAKE_CASE', null=True)
    operation_content = CharField(column_name='OPERATION_CONTENT', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    person_liable = CharField(column_name='PERSON_LIABLE', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    supplier_name = CharField(column_name='SUPPLIER_NAME', null=True)
    tel = CharField(column_name='TEL', null=True)
    work_area = CharField(column_name='WORK_AREA', null=True)

    class Meta:
        table_name = 'case_main'

class Ceshi(BaseModel):
    code = CharField(primary_key=True)

    class Meta:
        table_name = 'ceshi'

class FlowProcessConfiguration(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    deployment_id = CharField(column_name='DEPLOYMENT_ID', null=True)
    deployment_time = DateTimeField(column_name='DEPLOYMENT_TIME', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    flow_id = CharField(column_name='FLOW_ID', null=True)
    flow_name = CharField(column_name='FLOW_NAME', null=True)
    id = AutoField(column_name='ID')
    is_delete = IntegerField(column_name='IS_DELETE', constraints=[SQL("DEFAULT 0")], null=True)
    is_interface = CharField(column_name='IS_INTERFACE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    source_system_code = CharField(column_name='SOURCE_SYSTEM_CODE', null=True)

    class Meta:
        table_name = 'flow_process_configuration'

class JxCxoutorgReport(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    jx_date = DateField(column_name='JX_DATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    out_org_name = CharField(null=True)
    pro_name = CharField(null=True)
    remarks = TextField(null=True)
    user_pro_name = TextField(null=True)
    user_pro_num = IntegerField(null=True)

    class Meta:
        table_name = 'jx_cxoutorg_report'

class JxJobFiling(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    dh_bw = CharField(column_name='DH_BW', null=True)
    dh_date_begin = DateTimeField(column_name='DH_DATE_BEGIN', null=True)
    dh_date_end = DateTimeField(column_name='DH_DATE_END', null=True)
    dh_fs = CharField(column_name='DH_FS', null=True)
    dh_no = CharField(column_name='DH_NO', null=True)
    dh_type = CharField(column_name='DH_TYPE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    lxr_tel = CharField(column_name='LXR_TEL', null=True)
    memo = CharField(column_name='MEMO', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    zxdept = CharField(column_name='ZXDEPT', null=True)
    zysx = CharField(column_name='ZYSX', null=True)
    is_active = CharField(constraints=[SQL("DEFAULT '1'")], null=True)

    class Meta:
        table_name = 'jx_job_filing'

class JxOutorgReport(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    jx_date = DateField(column_name='JX_DATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    in_org_name = CharField(null=True)
    in_user_num = IntegerField(null=True)
    in_work_name = CharField(null=True)
    long_org_name = CharField(null=True)
    long_user_num = IntegerField(null=True)
    long_work_name = CharField(null=True)
    out_org_name = CharField(null=True)
    out_user_num = IntegerField(null=True)
    out_work_name = CharField(null=True)
    short_org_name = CharField(null=True)
    short_user_name = TextField(null=True)
    short_user_num = IntegerField(null=True)
    short_work_name = CharField(null=True)

    class Meta:
        table_name = 'jx_outorg_report'

class JxOverhaulReport(BaseModel):
    area_code = CharField(column_name='AREA_CODE', null=True)
    area_name = CharField(column_name='AREA_NAME', null=True)
    content = TextField(column_name='CONTENT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    jx = CharField(column_name='JX', null=True)
    jx_date = DateTimeField(column_name='JX_DATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    memo = CharField(column_name='MEMO', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    regulators = CharField(column_name='REGULATORS', null=True)
    responsible = CharField(column_name='RESPONSIBLE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    wx_pro = CharField(column_name='WX_PRO', null=True)

    class Meta:
        table_name = 'jx_overhaul_report'

class JxOverhaulSendHis(BaseModel):
    id = CharField(column_name='ID', primary_key=True)
    danger_type = CharField(null=True)
    send_date = DateTimeField(null=True)
    send_mes = CharField(null=True)
    user_code = CharField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'jx_overhaul_send_his'

class JxSendManagerUserDic(BaseModel):
    check_org_code = CharField(column_name='CHECK_ORG_CODE', null=True)
    check_org_name = CharField(column_name='CHECK_ORG_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    danger_type = CharField(null=True)
    is_delete = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    user_code = CharField(null=True)
    user_id = IntegerField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'jx_send_manager_user_dic'

class OmEmployee(BaseModel):
    birthday = CharField(column_name='BIRTHDAY', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    diploma_code = CharField(column_name='DIPLOMA_CODE', null=True)
    duty_code = CharField(column_name='DUTY_CODE', null=True)
    email = CharField(column_name='EMAIL', null=True)
    enter_org_id = CharField(column_name='ENTER_ORG_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    id_card = CharField(column_name='ID_CARD', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_dimission = CharField(column_name='IS_DIMISSION', constraints=[SQL("DEFAULT '0'")], null=True)
    is_operator = CharField(column_name='IS_OPERATOR', constraints=[SQL("DEFAULT '0'")], null=True)
    job_number = CharField(column_name='JOB_NUMBER', null=True)
    job_type_code = CharField(column_name='JOB_TYPE_CODE', null=True)
    lphone = CharField(column_name='LPHONE', null=True)
    maddress = CharField(column_name='MADDRESS', null=True)
    mphone = CharField(column_name='MPHONE', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    other_contact = CharField(column_name='OTHER_CONTACT', null=True)
    person_name = CharField(column_name='PERSON_NAME', null=True)
    politics_code = CharField(column_name='POLITICS_CODE', null=True)
    position_id = CharField(column_name='POSITION_ID', null=True)
    postal_code = CharField(column_name='POSTAL_CODE', null=True)
    qq_code = CharField(column_name='QQ_CODE', null=True)
    resume = CharField(column_name='RESUME', null=True)
    safety_duty_code = CharField(column_name='SAFETY_DUTY_CODE', null=True)
    school = CharField(column_name='SCHOOL', null=True)
    sepc_subject = CharField(column_name='SEPC_SUBJECT', null=True)
    sex = CharField(column_name='SEX', null=True)
    tiny_sign = CharField(column_name='TINY_SIGN', null=True)
    title_code = CharField(column_name='TITLE_CODE', null=True)
    type_code = CharField(column_name='TYPE_CODE', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'om_employee'

class OmOrganization(BaseModel):
    contactor = CharField(column_name='CONTACTOR', null=True)
    contactor_email = CharField(column_name='CONTACTOR_EMAIL', null=True)
    contactor_fax = CharField(column_name='CONTACTOR_FAX', null=True)
    contactor_tel = CharField(column_name='CONTACTOR_TEL', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    depttype_code = CharField(column_name='DEPTTYPE_CODE', null=True)
    dstr_code = CharField(column_name='DSTR_CODE', null=True)
    dstr_level = CharField(column_name='DSTR_LEVEL', null=True)
    extend_01 = CharField(column_name='EXTEND_01', null=True)
    extend_02 = CharField(column_name='EXTEND_02', null=True)
    extend_03 = CharField(column_name='EXTEND_03', null=True)
    ext_org_id = CharField(column_name='EXT_ORG_ID', null=True)
    ext_p_org_id = CharField(column_name='EXT_P_ORG_ID', null=True)
    hd_psn = CharField(column_name='HD_PSN', null=True)
    hd_psn_id = CharField(column_name='HD_PSN_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    inner_id = CharField(column_name='INNER_ID', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_dept = CharField(column_name='IS_DEPT', null=True)
    order_index = IntegerField(column_name='ORDER_INDEX', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    principal = CharField(column_name='PRINCIPAL', null=True)
    p_org_id = CharField(column_name='P_ORG_ID', null=True)
    simple_name = CharField(column_name='SIMPLE_NAME', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'om_organization'

class OmOrganizationCopy(BaseModel):
    contactor = CharField(column_name='CONTACTOR', null=True)
    contactor_email = CharField(column_name='CONTACTOR_EMAIL', null=True)
    contactor_fax = CharField(column_name='CONTACTOR_FAX', null=True)
    contactor_tel = CharField(column_name='CONTACTOR_TEL', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    depttype_code = CharField(column_name='DEPTTYPE_CODE', null=True)
    dstr_code = CharField(column_name='DSTR_CODE', null=True)
    dstr_level = CharField(column_name='DSTR_LEVEL', null=True)
    extend_01 = CharField(column_name='EXTEND_01', null=True)
    extend_02 = CharField(column_name='EXTEND_02', null=True)
    extend_03 = CharField(column_name='EXTEND_03', null=True)
    ext_org_id = CharField(column_name='EXT_ORG_ID', null=True)
    ext_p_org_id = CharField(column_name='EXT_P_ORG_ID', null=True)
    hd_psn = CharField(column_name='HD_PSN', null=True)
    hd_psn_id = CharField(column_name='HD_PSN_ID', null=True)
    id = CharField(column_name='ID', primary_key=True)
    inner_id = CharField(column_name='INNER_ID', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    is_dept = CharField(column_name='IS_DEPT', null=True)
    order_index = IntegerField(column_name='ORDER_INDEX', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    principal = CharField(column_name='PRINCIPAL', null=True)
    p_org_id = CharField(column_name='P_ORG_ID', null=True)
    simple_name = CharField(column_name='SIMPLE_NAME', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'om_organization_copy'

class PhoneStorage(BaseModel):
    asid = IntegerField()

    class Meta:
        table_name = 'phone_storage'

class Poi(BaseModel):
    address = CharField(null=True)
    city_code = CharField(null=True)
    id = BigIntegerField(null=True)
    insert_date = DateTimeField(null=True)
    lat = CharField(null=True)
    lng = CharField(null=True)
    name = CharField(null=True)
    tel = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'poi'
        primary_key = False

class ProjMain(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    cw_bill_code = CharField(column_name='CW_BILL_CODE', null=True)
    cw_bill_type_code = CharField(column_name='CW_BILL_TYPE_CODE', null=True)
    cw_bill_type_name = CharField(column_name='CW_BILL_TYPE_NAME', null=True)
    cw_contract_bz_code = CharField(column_name='CW_CONTRACT_BZ_CODE', null=True)
    cw_contract_bz_name = CharField(column_name='CW_CONTRACT_BZ_NAME', null=True)
    cw_contract_code = CharField(column_name='CW_CONTRACT_CODE', null=True)
    cw_contract_exam_opinion = CharField(column_name='CW_CONTRACT_EXAM_OPINION', null=True)
    cw_contract_exam_result = CharField(column_name='CW_CONTRACT_EXAM_RESULT', null=True)
    cw_contract_porp_code = CharField(column_name='CW_CONTRACT_PORP_CODE', null=True)
    cw_contract_porp_name = CharField(column_name='CW_CONTRACT_PORP_NAME', null=True)
    cw_if_ret_desc = CharField(column_name='CW_IF_RET_DESC', null=True)
    cw_if_ret_type = CharField(column_name='CW_IF_RET_TYPE', null=True)
    cw_if_send_date = DateTimeField(column_name='CW_IF_SEND_DATE', null=True)
    cw_if_send_status = CharField(column_name='CW_IF_SEND_STATUS', null=True)
    cw_org_code = CharField(column_name='CW_ORG_CODE', null=True)
    cw_org_name = CharField(column_name='CW_ORG_NAME', null=True)
    cw_super_org_code = CharField(column_name='CW_SUPER_ORG_CODE', null=True)
    cw_super_org_name = CharField(column_name='CW_SUPER_ORG_NAME', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    person_farmer_num = IntegerField(column_name='PERSON_FARMER_NUM', null=True)
    process_inst_id = CharField(column_name='PROCESS_INST_ID', null=True)
    proj_code = CharField(column_name='PROJ_CODE', unique=True)
    proj_contract_prop_code = CharField(column_name='PROJ_CONTRACT_PROP_CODE', null=True)
    proj_contract_prop_name = CharField(column_name='PROJ_CONTRACT_PROP_NAME', null=True)
    proj_create_org_code = CharField(column_name='PROJ_CREATE_ORG_CODE', null=True)
    proj_create_org_name = CharField(column_name='PROJ_CREATE_ORG_NAME', null=True)
    proj_his_code = CharField(column_name='PROJ_HIS_CODE', null=True)
    proj_manage_opinion = CharField(column_name='PROJ_MANAGE_OPINION', null=True)
    proj_manage_org_code = CharField(column_name='PROJ_MANAGE_ORG_CODE', null=True)
    proj_manage_org_name = CharField(column_name='PROJ_MANAGE_ORG_NAME', null=True)
    proj_manage_req_desc = CharField(column_name='PROJ_MANAGE_REQ_DESC', null=True)
    proj_money = DecimalField(column_name='PROJ_MONEY', null=True)
    proj_money_bz = CharField(column_name='PROJ_MONEY_BZ', null=True)
    proj_money_cal_remark = CharField(column_name='PROJ_MONEY_CAL_REMARK', null=True)
    proj_name = CharField(column_name='PROJ_NAME')
    proj_org_code = CharField(column_name='PROJ_ORG_CODE', null=True)
    proj_org_name = CharField(column_name='PROJ_ORG_NAME', null=True)
    proj_other_money = DecimalField(column_name='PROJ_OTHER_MONEY', null=True)
    proj_person_count = IntegerField(column_name='PROJ_PERSON_COUNT', null=True)
    proj_person_money = DecimalField(column_name='PROJ_PERSON_MONEY', null=True)
    proj_person_out_count = IntegerField(column_name='PROJ_PERSON_OUT_COUNT', null=True)
    proj_person_rate = DecimalField(column_name='PROJ_PERSON_RATE', null=True)
    proj_plan_amount = DecimalField(column_name='PROJ_PLAN_AMOUNT', null=True)
    proj_plan_begin_date = DateField(column_name='PROJ_PLAN_BEGIN_DATE', null=True)
    proj_plan_end_date = DateField(column_name='PROJ_PLAN_END_DATE', null=True)
    proj_plan_limit = IntegerField(column_name='PROJ_PLAN_LIMIT', null=True)
    proj_plan_limit_unit = CharField(column_name='PROJ_PLAN_LIMIT_UNIT', null=True)
    proj_price_remark = CharField(column_name='PROJ_PRICE_REMARK', null=True)
    proj_remark = CharField(column_name='PROJ_REMARK', null=True)
    proj_result_code = CharField(column_name='PROJ_RESULT_CODE', null=True)
    proj_result_name = CharField(column_name='PROJ_RESULT_NAME', null=True)
    proj_status_code = CharField(column_name='PROJ_STATUS_CODE', constraints=[SQL("DEFAULT '编辑'")], null=True)
    proj_status_name = CharField(column_name='PROJ_STATUS_NAME', constraints=[SQL("DEFAULT '编辑'")], null=True)
    proj_supplier_prop_code = CharField(column_name='PROJ_SUPPLIER_PROP_CODE', null=True)
    proj_supplier_prop_name = CharField(column_name='PROJ_SUPPLIER_PROP_NAME', null=True)
    proj_supplier_req_desc = CharField(column_name='PROJ_SUPPLIER_REQ_DESC', null=True)
    proj_tax_kind_code = CharField(column_name='PROJ_TAX_KIND_CODE', null=True)
    proj_tax_kind_name = CharField(column_name='PROJ_TAX_KIND_NAME', null=True)
    proj_tax_rate = DecimalField(column_name='PROJ_TAX_RATE', null=True)
    proj_type_code = CharField(column_name='PROJ_TYPE_CODE', null=True)
    proj_type_code2 = CharField(column_name='PROJ_TYPE_CODE2', null=True)
    proj_type_name = CharField(column_name='PROJ_TYPE_NAME', null=True)
    proj_type_name2 = CharField(column_name='PROJ_TYPE_NAME2', null=True)
    proj_work_content = CharField(column_name='PROJ_WORK_CONTENT', null=True)
    proj_year = IntegerField(column_name='PROJ_YEAR', null=True)
    proj_yg_class_code = CharField(column_name='PROJ_YG_CLASS_CODE', null=True)
    proj_yg_class_name = CharField(column_name='PROJ_YG_CLASS_NAME', null=True)
    proj_yg_org_code = CharField(column_name='PROJ_YG_ORG_CODE', null=True)
    proj_yg_org_name = CharField(column_name='PROJ_YG_ORG_NAME', null=True)
    proj_zb_type_code = CharField(column_name='PROJ_ZB_TYPE_CODE', null=True)
    proj_zb_type_name = CharField(column_name='PROJ_ZB_TYPE_NAME', null=True)
    proj_zr_type_code = CharField(column_name='PROJ_ZR_TYPE_CODE', null=True)
    proj_zr_type_name = CharField(column_name='PROJ_ZR_TYPE_NAME', null=True)
    proj_zz_date = DateField(column_name='PROJ_ZZ_DATE', null=True)
    sap_buy_code = CharField(column_name='SAP_BUY_CODE', null=True)
    sap_order_id = CharField(column_name='SAP_ORDER_ID', null=True)
    sap_proj_code = CharField(column_name='SAP_PROJ_CODE', null=True)
    sap_proj_money_notax = DecimalField(column_name='SAP_PROJ_MONEY_NOTAX', null=True)
    sap_proj_money_tax = DecimalField(column_name='SAP_PROJ_MONEY_TAX', null=True)
    sap_proj_name = CharField(column_name='SAP_PROJ_NAME', null=True)
    sap_scope = CharField(column_name='SAP_SCOPE', null=True)
    sap_tax_rate = DecimalField(column_name='SAP_TAX_RATE', null=True)
    sjrs = IntegerField(column_name='SJRS', null=True)
    ykt_if_date = DateTimeField(column_name='YKT_IF_DATE', null=True)
    ykt_if_ret_msg = CharField(column_name='YKT_IF_RET_MSG', null=True)
    ykt_if_status = CharField(column_name='YKT_IF_STATUS', constraints=[SQL("DEFAULT '0'")], null=True)
    cw_contract_prop_code = CharField(constraints=[SQL("DEFAULT ''")])
    cw_if_send_status_desc = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'proj_main'
        indexes = (
            (('proj_year', 'proj_plan_begin_date', 'proj_plan_end_date', 'proj_type_code', 'proj_yg_class_code', 'proj_person_count', 'proj_supplier_prop_code', 'cw_contract_exam_result'), False),
        )

class ProjMainCopy1(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    cw_bill_code = CharField(column_name='CW_BILL_CODE', null=True)
    cw_bill_type_code = CharField(column_name='CW_BILL_TYPE_CODE', null=True)
    cw_bill_type_name = CharField(column_name='CW_BILL_TYPE_NAME', null=True)
    cw_contract_bz_code = CharField(column_name='CW_CONTRACT_BZ_CODE', null=True)
    cw_contract_bz_name = CharField(column_name='CW_CONTRACT_BZ_NAME', null=True)
    cw_contract_code = CharField(column_name='CW_CONTRACT_CODE', null=True)
    cw_contract_exam_opinion = CharField(column_name='CW_CONTRACT_EXAM_OPINION', null=True)
    cw_contract_exam_result = CharField(column_name='CW_CONTRACT_EXAM_RESULT', null=True)
    cw_contract_porp_code = CharField(column_name='CW_CONTRACT_PORP_CODE', null=True)
    cw_contract_porp_name = CharField(column_name='CW_CONTRACT_PORP_NAME', null=True)
    cw_if_ret_desc = CharField(column_name='CW_IF_RET_DESC', null=True)
    cw_if_ret_type = CharField(column_name='CW_IF_RET_TYPE', null=True)
    cw_if_send_date = DateTimeField(column_name='CW_IF_SEND_DATE', null=True)
    cw_if_send_status = CharField(column_name='CW_IF_SEND_STATUS', null=True)
    cw_org_code = CharField(column_name='CW_ORG_CODE', null=True)
    cw_org_name = CharField(column_name='CW_ORG_NAME', null=True)
    cw_super_org_code = CharField(column_name='CW_SUPER_ORG_CODE', null=True)
    cw_super_org_name = CharField(column_name='CW_SUPER_ORG_NAME', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    person_farmer_num = IntegerField(column_name='PERSON_FARMER_NUM', null=True)
    process_inst_id = CharField(column_name='PROCESS_INST_ID', null=True)
    proj_code = CharField(column_name='PROJ_CODE', unique=True)
    proj_contract_prop_code = CharField(column_name='PROJ_CONTRACT_PROP_CODE', null=True)
    proj_contract_prop_name = CharField(column_name='PROJ_CONTRACT_PROP_NAME', null=True)
    proj_create_org_code = CharField(column_name='PROJ_CREATE_ORG_CODE', null=True)
    proj_create_org_name = CharField(column_name='PROJ_CREATE_ORG_NAME', null=True)
    proj_his_code = CharField(column_name='PROJ_HIS_CODE', null=True)
    proj_manage_opinion = CharField(column_name='PROJ_MANAGE_OPINION', null=True)
    proj_manage_org_code = CharField(column_name='PROJ_MANAGE_ORG_CODE', null=True)
    proj_manage_org_name = CharField(column_name='PROJ_MANAGE_ORG_NAME', null=True)
    proj_manage_req_desc = CharField(column_name='PROJ_MANAGE_REQ_DESC', null=True)
    proj_money = DecimalField(column_name='PROJ_MONEY', null=True)
    proj_money_bz = CharField(column_name='PROJ_MONEY_BZ', null=True)
    proj_money_cal_remark = CharField(column_name='PROJ_MONEY_CAL_REMARK', null=True)
    proj_name = CharField(column_name='PROJ_NAME')
    proj_org_code = CharField(column_name='PROJ_ORG_CODE', null=True)
    proj_org_name = CharField(column_name='PROJ_ORG_NAME', null=True)
    proj_other_money = DecimalField(column_name='PROJ_OTHER_MONEY', null=True)
    proj_person_count = IntegerField(column_name='PROJ_PERSON_COUNT', null=True)
    proj_person_money = DecimalField(column_name='PROJ_PERSON_MONEY', null=True)
    proj_person_out_count = IntegerField(column_name='PROJ_PERSON_OUT_COUNT', null=True)
    proj_person_rate = DecimalField(column_name='PROJ_PERSON_RATE', null=True)
    proj_plan_amount = DecimalField(column_name='PROJ_PLAN_AMOUNT', null=True)
    proj_plan_begin_date = DateField(column_name='PROJ_PLAN_BEGIN_DATE', null=True)
    proj_plan_end_date = DateField(column_name='PROJ_PLAN_END_DATE', null=True)
    proj_plan_limit = IntegerField(column_name='PROJ_PLAN_LIMIT', null=True)
    proj_plan_limit_unit = CharField(column_name='PROJ_PLAN_LIMIT_UNIT', null=True)
    proj_price_remark = CharField(column_name='PROJ_PRICE_REMARK', null=True)
    proj_remark = CharField(column_name='PROJ_REMARK', null=True)
    proj_result_code = CharField(column_name='PROJ_RESULT_CODE', null=True)
    proj_result_name = CharField(column_name='PROJ_RESULT_NAME', null=True)
    proj_status_code = CharField(column_name='PROJ_STATUS_CODE', constraints=[SQL("DEFAULT '编辑'")], null=True)
    proj_status_name = CharField(column_name='PROJ_STATUS_NAME', constraints=[SQL("DEFAULT '编辑'")], null=True)
    proj_supplier_prop_code = CharField(column_name='PROJ_SUPPLIER_PROP_CODE', null=True)
    proj_supplier_prop_name = CharField(column_name='PROJ_SUPPLIER_PROP_NAME', null=True)
    proj_supplier_req_desc = CharField(column_name='PROJ_SUPPLIER_REQ_DESC', null=True)
    proj_tax_kind_code = CharField(column_name='PROJ_TAX_KIND_CODE', null=True)
    proj_tax_kind_name = CharField(column_name='PROJ_TAX_KIND_NAME', null=True)
    proj_tax_rate = DecimalField(column_name='PROJ_TAX_RATE', null=True)
    proj_type_code = CharField(column_name='PROJ_TYPE_CODE', null=True)
    proj_type_code2 = CharField(column_name='PROJ_TYPE_CODE2', null=True)
    proj_type_name = CharField(column_name='PROJ_TYPE_NAME', null=True)
    proj_type_name2 = CharField(column_name='PROJ_TYPE_NAME2', null=True)
    proj_work_content = CharField(column_name='PROJ_WORK_CONTENT', null=True)
    proj_year = IntegerField(column_name='PROJ_YEAR', null=True)
    proj_yg_class_code = CharField(column_name='PROJ_YG_CLASS_CODE', null=True)
    proj_yg_class_name = CharField(column_name='PROJ_YG_CLASS_NAME', null=True)
    proj_yg_org_code = CharField(column_name='PROJ_YG_ORG_CODE', null=True)
    proj_yg_org_name = CharField(column_name='PROJ_YG_ORG_NAME', null=True)
    proj_zb_type_code = CharField(column_name='PROJ_ZB_TYPE_CODE', null=True)
    proj_zb_type_name = CharField(column_name='PROJ_ZB_TYPE_NAME', null=True)
    proj_zr_type_code = CharField(column_name='PROJ_ZR_TYPE_CODE', null=True)
    proj_zr_type_name = CharField(column_name='PROJ_ZR_TYPE_NAME', null=True)
    proj_zz_date = DateField(column_name='PROJ_ZZ_DATE', null=True)
    sap_buy_code = CharField(column_name='SAP_BUY_CODE', null=True)
    sap_order_id = CharField(column_name='SAP_ORDER_ID', null=True)
    sap_proj_code = CharField(column_name='SAP_PROJ_CODE', null=True)
    sap_proj_money_notax = DecimalField(column_name='SAP_PROJ_MONEY_NOTAX', null=True)
    sap_proj_money_tax = DecimalField(column_name='SAP_PROJ_MONEY_TAX', null=True)
    sap_proj_name = CharField(column_name='SAP_PROJ_NAME', null=True)
    sap_scope = CharField(column_name='SAP_SCOPE', null=True)
    sap_tax_rate = DecimalField(column_name='SAP_TAX_RATE', null=True)
    sjrs = IntegerField(column_name='SJRS', null=True)
    ykt_if_date = DateTimeField(column_name='YKT_IF_DATE', null=True)
    ykt_if_ret_msg = CharField(column_name='YKT_IF_RET_MSG', null=True)
    ykt_if_status = CharField(column_name='YKT_IF_STATUS', constraints=[SQL("DEFAULT '0'")], null=True)

    class Meta:
        table_name = 'proj_main_copy1'
        indexes = (
            (('proj_year', 'proj_plan_begin_date', 'proj_plan_end_date', 'proj_type_code', 'proj_yg_class_code', 'proj_person_count', 'proj_supplier_prop_code', 'cw_contract_exam_result'), False),
        )

class ProjSupplier(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    proj_code = CharField(column_name='PROJ_CODE', null=True)
    proj_supplier_code = CharField(column_name='PROJ_SUPPLIER_CODE', null=True)
    proj_supplier_date = DateTimeField(column_name='PROJ_SUPPLIER_DATE', null=True)
    proj_supplier_id = CharField(column_name='PROJ_SUPPLIER_ID', unique=True)
    proj_supplier_link_phone = CharField(column_name='PROJ_SUPPLIER_LINK_PHONE', null=True)
    proj_supplier_link_user = CharField(column_name='PROJ_SUPPLIER_LINK_USER', null=True)
    proj_supplier_name = CharField(column_name='PROJ_SUPPLIER_NAME', null=True)
    proj_supplier_remark = CharField(column_name='PROJ_SUPPLIER_REMARK', null=True)
    proj_supplier_status_code = CharField(column_name='PROJ_SUPPLIER_STATUS_CODE', null=True)
    proj_supplier_status_name = CharField(column_name='PROJ_SUPPLIER_STATUS_NAME', null=True)
    proj_zb_code = CharField(column_name='PROJ_ZB_CODE', null=True)

    class Meta:
        table_name = 'proj_supplier'

class ProjSupplierPerson(BaseModel):
    apply_id = CharField(column_name='APPLY_ID', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    entry_date = DateField(column_name='ENTRY_DATE', null=True)
    id = AutoField(column_name='ID')
    is_table = CharField(column_name='IS_TABLE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    person_id = CharField(column_name='PERSON_ID', index=True, null=True)
    proj_person_id = CharField(column_name='PROJ_PERSON_ID', unique=True)
    proj_person_status_code = CharField(column_name='PROJ_PERSON_STATUS_CODE', null=True)
    proj_person_status_name = CharField(column_name='PROJ_PERSON_STATUS_NAME', null=True)
    proj_remark = CharField(column_name='PROJ_REMARK', null=True)
    proj_supplier_id = CharField(column_name='PROJ_SUPPLIER_ID')
    quit_date = DateField(column_name='QUIT_DATE', null=True)
    ykt_if_date = DateField(column_name='YKT_IF_DATE', null=True)
    ykt_if_ret_msg = CharField(column_name='YKT_IF_RET_MSG', null=True)
    ykt_if_status = CharField(column_name='YKT_IF_STATUS', null=True)
    ykt_pic_if_date = DateTimeField(column_name='YKT_PIC_IF_DATE', null=True)
    ykt_pic_if_ret_msg = CharField(column_name='YKT_PIC_IF_RET_MSG', null=True)
    ykt_pic_if_status = CharField(column_name='YKT_PIC_IF_STATUS', null=True)

    class Meta:
        table_name = 'proj_supplier_person'

class ProjTemp(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    cw_bill_code = CharField(column_name='CW_BILL_CODE', null=True)
    cw_bill_type_code = CharField(column_name='CW_BILL_TYPE_CODE', null=True)
    cw_bill_type_name = CharField(column_name='CW_BILL_TYPE_NAME', null=True)
    cw_contract_bz_code = CharField(column_name='CW_CONTRACT_BZ_CODE', null=True)
    cw_contract_bz_name = CharField(column_name='CW_CONTRACT_BZ_NAME', null=True)
    cw_contract_code = CharField(column_name='CW_CONTRACT_CODE', null=True)
    cw_contract_exam_opinion = CharField(column_name='CW_CONTRACT_EXAM_OPINION', null=True)
    cw_contract_exam_result = CharField(column_name='CW_CONTRACT_EXAM_RESULT', null=True)
    cw_contract_porp_code = CharField(column_name='CW_CONTRACT_PORP_CODE', null=True)
    cw_contract_porp_name = CharField(column_name='CW_CONTRACT_PORP_NAME', null=True)
    cw_if_ret_desc = CharField(column_name='CW_IF_RET_DESC', null=True)
    cw_if_ret_type = CharField(column_name='CW_IF_RET_TYPE', null=True)
    cw_if_send_date = DateTimeField(column_name='CW_IF_SEND_DATE', null=True)
    cw_if_send_status = CharField(column_name='CW_IF_SEND_STATUS', null=True)
    cw_org_code = CharField(column_name='CW_ORG_CODE', null=True)
    cw_org_name = CharField(column_name='CW_ORG_NAME', null=True)
    cw_super_org_code = CharField(column_name='CW_SUPER_ORG_CODE', null=True)
    cw_super_org_name = CharField(column_name='CW_SUPER_ORG_NAME', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    person_farmer_num = IntegerField(column_name='PERSON_FARMER_NUM', null=True)
    process_inst_id = CharField(column_name='PROCESS_INST_ID', null=True)
    proj_code = CharField(column_name='PROJ_CODE', unique=True)
    proj_contract_prop_code = CharField(column_name='PROJ_CONTRACT_PROP_CODE', null=True)
    proj_contract_prop_name = CharField(column_name='PROJ_CONTRACT_PROP_NAME', null=True)
    proj_create_org_code = CharField(column_name='PROJ_CREATE_ORG_CODE', null=True)
    proj_create_org_name = CharField(column_name='PROJ_CREATE_ORG_NAME', null=True)
    proj_his_code = CharField(column_name='PROJ_HIS_CODE', null=True)
    proj_manage_opinion = CharField(column_name='PROJ_MANAGE_OPINION', null=True)
    proj_manage_org_code = CharField(column_name='PROJ_MANAGE_ORG_CODE', null=True)
    proj_manage_org_name = CharField(column_name='PROJ_MANAGE_ORG_NAME', null=True)
    proj_manage_req_desc = CharField(column_name='PROJ_MANAGE_REQ_DESC', null=True)
    proj_money = DecimalField(column_name='PROJ_MONEY', null=True)
    proj_money_bz = CharField(column_name='PROJ_MONEY_BZ', null=True)
    proj_money_cal_remark = CharField(column_name='PROJ_MONEY_CAL_REMARK', null=True)
    proj_name = CharField(column_name='PROJ_NAME')
    proj_org_code = CharField(column_name='PROJ_ORG_CODE', null=True)
    proj_org_name = CharField(column_name='PROJ_ORG_NAME', null=True)
    proj_other_money = DecimalField(column_name='PROJ_OTHER_MONEY', null=True)
    proj_person_count = IntegerField(column_name='PROJ_PERSON_COUNT', null=True)
    proj_person_money = DecimalField(column_name='PROJ_PERSON_MONEY', null=True)
    proj_person_out_count = IntegerField(column_name='PROJ_PERSON_OUT_COUNT', null=True)
    proj_person_rate = DecimalField(column_name='PROJ_PERSON_RATE', null=True)
    proj_plan_amount = DecimalField(column_name='PROJ_PLAN_AMOUNT', null=True)
    proj_plan_begin_date = DateField(column_name='PROJ_PLAN_BEGIN_DATE', null=True)
    proj_plan_end_date = DateField(column_name='PROJ_PLAN_END_DATE', null=True)
    proj_plan_limit = IntegerField(column_name='PROJ_PLAN_LIMIT', null=True)
    proj_plan_limit_unit = CharField(column_name='PROJ_PLAN_LIMIT_UNIT', null=True)
    proj_price_remark = CharField(column_name='PROJ_PRICE_REMARK', null=True)
    proj_remark = CharField(column_name='PROJ_REMARK', null=True)
    proj_result_code = CharField(column_name='PROJ_RESULT_CODE', null=True)
    proj_result_name = CharField(column_name='PROJ_RESULT_NAME', null=True)
    proj_status_code = CharField(column_name='PROJ_STATUS_CODE', constraints=[SQL("DEFAULT '编辑'")], null=True)
    proj_status_name = CharField(column_name='PROJ_STATUS_NAME', constraints=[SQL("DEFAULT '编辑'")], null=True)
    proj_supplier_prop_code = CharField(column_name='PROJ_SUPPLIER_PROP_CODE', null=True)
    proj_supplier_prop_name = CharField(column_name='PROJ_SUPPLIER_PROP_NAME', null=True)
    proj_supplier_req_desc = CharField(column_name='PROJ_SUPPLIER_REQ_DESC', null=True)
    proj_tax_kind_code = CharField(column_name='PROJ_TAX_KIND_CODE', null=True)
    proj_tax_kind_name = CharField(column_name='PROJ_TAX_KIND_NAME', null=True)
    proj_tax_rate = DecimalField(column_name='PROJ_TAX_RATE', null=True)
    proj_type_code = CharField(column_name='PROJ_TYPE_CODE', null=True)
    proj_type_code2 = CharField(column_name='PROJ_TYPE_CODE2', null=True)
    proj_type_name = CharField(column_name='PROJ_TYPE_NAME', null=True)
    proj_type_name2 = CharField(column_name='PROJ_TYPE_NAME2', null=True)
    proj_work_content = CharField(column_name='PROJ_WORK_CONTENT', null=True)
    proj_year = IntegerField(column_name='PROJ_YEAR', null=True)
    proj_yg_class_code = CharField(column_name='PROJ_YG_CLASS_CODE', null=True)
    proj_yg_class_name = CharField(column_name='PROJ_YG_CLASS_NAME', null=True)
    proj_yg_org_code = CharField(column_name='PROJ_YG_ORG_CODE', null=True)
    proj_yg_org_name = CharField(column_name='PROJ_YG_ORG_NAME', null=True)
    proj_zb_type_code = CharField(column_name='PROJ_ZB_TYPE_CODE', null=True)
    proj_zb_type_name = CharField(column_name='PROJ_ZB_TYPE_NAME', null=True)
    proj_zr_type_code = CharField(column_name='PROJ_ZR_TYPE_CODE', null=True)
    proj_zr_type_name = CharField(column_name='PROJ_ZR_TYPE_NAME', null=True)
    proj_zz_date = DateField(column_name='PROJ_ZZ_DATE', null=True)
    sap_buy_code = CharField(column_name='SAP_BUY_CODE', null=True)
    sap_order_id = CharField(column_name='SAP_ORDER_ID', null=True)
    sap_proj_code = CharField(column_name='SAP_PROJ_CODE', null=True)
    sap_proj_money_notax = DecimalField(column_name='SAP_PROJ_MONEY_NOTAX', null=True)
    sap_proj_money_tax = DecimalField(column_name='SAP_PROJ_MONEY_TAX', null=True)
    sap_proj_name = CharField(column_name='SAP_PROJ_NAME', null=True)
    sap_scope = CharField(column_name='SAP_SCOPE', null=True)
    sap_tax_rate = DecimalField(column_name='SAP_TAX_RATE', null=True)
    sjrs = IntegerField(column_name='SJRS', null=True)
    ykt_if_date = DateTimeField(column_name='YKT_IF_DATE', null=True)
    ykt_if_ret_msg = CharField(column_name='YKT_IF_RET_MSG', null=True)
    ykt_if_status = CharField(column_name='YKT_IF_STATUS', constraints=[SQL("DEFAULT '0'")], null=True)

    class Meta:
        table_name = 'proj_temp'
        indexes = (
            (('proj_year', 'proj_plan_begin_date', 'proj_plan_end_date', 'proj_type_code', 'proj_yg_class_code', 'proj_person_count', 'proj_supplier_prop_code', 'cw_contract_exam_result'), False),
        )

class ProjTempSupplierPerson(BaseModel):
    apply_id = CharField(column_name='APPLY_ID', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    entry_date = DateField(column_name='ENTRY_DATE', null=True)
    id = AutoField(column_name='ID')
    is_table = CharField(column_name='IS_TABLE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    person_id = CharField(column_name='PERSON_ID', null=True)
    proj_person_id = CharField(column_name='PROJ_PERSON_ID', unique=True)
    proj_person_status_code = CharField(column_name='PROJ_PERSON_STATUS_CODE', null=True)
    proj_person_status_name = CharField(column_name='PROJ_PERSON_STATUS_NAME', null=True)
    proj_remark = CharField(column_name='PROJ_REMARK', null=True)
    proj_supplier_id = CharField(column_name='PROJ_SUPPLIER_ID')
    quit_date = DateField(column_name='QUIT_DATE', null=True)
    ykt_if_date = DateField(column_name='YKT_IF_DATE', null=True)
    ykt_if_ret_msg = CharField(column_name='YKT_IF_RET_MSG', null=True)
    ykt_if_status = CharField(column_name='YKT_IF_STATUS', null=True)
    ykt_pic_if_date = DateTimeField(column_name='YKT_PIC_IF_DATE', null=True)
    ykt_pic_if_ret_msg = CharField(column_name='YKT_PIC_IF_RET_MSG', null=True)
    ykt_pic_if_status = CharField(column_name='YKT_PIC_IF_STATUS', null=True)

    class Meta:
        table_name = 'proj_temp_supplier_person'

class ProjectDayReport(BaseModel):
    construction_unit_name = CharField(column_name='CONSTRUCTION_UNIT_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    leader_level = CharField(column_name='LEADER_LEVEL', null=True)
    main_leader_sign = CharField(column_name='MAIN_LEADER_SIGN', null=True)
    make_case = CharField(column_name='MAKE_CASE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    plan_begin_date = DateField(column_name='PLAN_BEGIN_DATE', null=True)
    plan_end_date = DateField(column_name='PLAN_END_DATE', null=True)
    project_name = CharField(column_name='PROJECT_NAME', null=True)
    project_user = CharField(column_name='PROJECT_USER', null=True)
    report_date = DateField(column_name='REPORT_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'project_day_report'

class ProjectDayReportCopy(BaseModel):
    construction_unit_name = CharField(column_name='CONSTRUCTION_UNIT_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    leader_level = CharField(column_name='LEADER_LEVEL', null=True)
    main_leader_sign = CharField(column_name='MAIN_LEADER_SIGN', null=True)
    make_case = CharField(column_name='MAKE_CASE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    plan_begin_date = DateField(column_name='PLAN_BEGIN_DATE', null=True)
    plan_end_date = DateField(column_name='PLAN_END_DATE', null=True)
    project_name = CharField(column_name='PROJECT_NAME', null=True)
    report_date = DateField(column_name='REPORT_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'project_day_report_copy'

class ProjectDayReportCopy1(BaseModel):
    construction_unit_name = CharField(column_name='CONSTRUCTION_UNIT_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    leader_level = CharField(column_name='LEADER_LEVEL', null=True)
    main_leader_sign = CharField(column_name='MAIN_LEADER_SIGN', null=True)
    make_case = CharField(column_name='MAKE_CASE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    plan_begin_date = DateField(column_name='PLAN_BEGIN_DATE', null=True)
    plan_end_date = DateField(column_name='PLAN_END_DATE', null=True)
    project_name = CharField(column_name='PROJECT_NAME', null=True)
    project_user = CharField(column_name='PROJECT_USER', null=True)
    report_date = DateField(column_name='REPORT_DATE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'project_day_report_copy1'

class RelateDailySettlement(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    item_code = CharField(column_name='ITEM_CODE', null=True)
    item_name = CharField(column_name='ITEM_NAME', null=True)
    jx_date = DateField(column_name='JX_DATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    pro_type = CharField(column_name='PRO_TYPE', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    supplier_name = CharField(column_name='SUPPLIER_NAME', null=True)
    user_num = IntegerField(column_name='USER_NUM', null=True)

    class Meta:
        table_name = 'relate_daily_settlement'

class RelateProject(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    item_code = CharField(column_name='ITEM_CODE', null=True)
    item_name = CharField(column_name='ITEM_NAME', null=True)
    jx_date = DateField(column_name='JX_DATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    pro_type = CharField(column_name='PRO_TYPE', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    supplier_name = CharField(column_name='SUPPLIER_NAME', null=True)
    user_num = IntegerField(column_name='USER_NUM', null=True)

    class Meta:
        table_name = 'relate_project'

class SafetyAttendance(BaseModel):
    by = CharField(null=True)
    by1 = CharField(null=True)
    by2 = CharField(null=True)
    by3 = CharField(null=True)
    by4 = CharField(null=True)
    check_address = TextField(null=True)
    check_time = DateTimeField(null=True)
    id = CharField(primary_key=True)
    sex = CharField(null=True)
    user_code = CharField(null=True)
    user_id_card = CharField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'safety_attendance'

class SafetyCaseTime(BaseModel):
    activiti_key = CharField(column_name='ACTIVITI_KEY', null=True)
    activiti_stat = CharField(column_name='ACTIVITI_STAT', null=True)
    charge_person_and_information = CharField(column_name='CHARGE_PERSON_AND_INFORMATION', null=True)
    construction_content = TextField(column_name='CONSTRUCTION_CONTENT', null=True)
    construction_unit_name = CharField(column_name='CONSTRUCTION_UNIT_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    estimated_risk = CharField(column_name='ESTIMATED_RISK', null=True)
    formation_unit_code = CharField(column_name='FORMATION_UNIT_CODE', null=True)
    formation_unit_name = CharField(column_name='FORMATION_UNIT_NAME', null=True)
    id = AutoField(column_name='ID')
    ind_unique = CharField(column_name='IND_UNIQUE', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    item_code = CharField(column_name='ITEM_CODE', null=True)
    item_name = CharField(column_name='ITEM_NAME', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    leader_level = CharField(column_name='LEADER_LEVEL', null=True)
    main_leader_sign = CharField(column_name='MAIN_LEADER_SIGN', null=True)
    make_case = CharField(column_name='MAKE_CASE', null=True)
    operation_users = TextField(column_name='OPERATION_USERS', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    plan_begin_date = DateTimeField(column_name='PLAN_BEGIN_DATE', null=True)
    plan_end_date = DateTimeField(column_name='PLAN_END_DATE', null=True)
    project_name = CharField(column_name='PROJECT_NAME', null=True)
    report_date = DateField(column_name='REPORT_DATE', null=True)
    specific_measures = CharField(column_name='SPECIFIC_MEASURES', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    work_area = CharField(column_name='WORK_AREA', null=True)

    class Meta:
        table_name = 'safety_case_time'

class SafetyDailySettlement(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    in_org_name = CharField(column_name='IN_ORG_NAME', null=True)
    in_user_num = IntegerField(column_name='IN_USER_NUM', null=True)
    in_work_name = CharField(column_name='IN_WORK_NAME', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT ''")], null=True)
    jx_date = DateField(column_name='JX_DATE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    long_org_name = CharField(column_name='LONG_ORG_NAME', null=True)
    long_user_num = IntegerField(column_name='LONG_USER_NUM', null=True)
    long_work_name = CharField(column_name='LONG_WORK_NAME', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    out_org_name = CharField(column_name='OUT_ORG_NAME', null=True)
    out_user_num = IntegerField(column_name='OUT_USER_NUM', null=True)
    out_work_name = CharField(column_name='OUT_WORK_NAME', null=True)
    short_org_name = CharField(column_name='SHORT_ORG_NAME', null=True)
    short_user_name = TextField(column_name='SHORT_USER_NAME', null=True)
    short_user_num = IntegerField(column_name='SHORT_USER_NUM', null=True)
    short_work_name = CharField(column_name='SHORT_WORK_NAME', null=True)

    class Meta:
        table_name = 'safety_daily_settlement'

class SupplierOrg(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    id = AutoField(column_name='ID')
    is_delete = CharField(column_name='IS_DELETE', constraints=[SQL("DEFAULT '0'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    org_type = CharField(column_name='ORG_TYPE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 'supplier_org'

class SupplierPerson(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    person_addr = CharField(column_name='PERSON_ADDR', null=True)
    person_addr_city = CharField(column_name='PERSON_ADDR_CITY', null=True)
    person_addr_country = CharField(column_name='PERSON_ADDR_COUNTRY', null=True)
    person_addr_county = CharField(column_name='PERSON_ADDR_COUNTY', null=True)
    person_addr_province = CharField(column_name='PERSON_ADDR_PROVINCE', null=True)
    person_birth = CharField(column_name='PERSON_BIRTH', null=True)
    person_birth_country = CharField(column_name='PERSON_BIRTH_COUNTRY', null=True)
    person_code = CharField(column_name='PERSON_CODE', null=True)
    person_country = CharField(column_name='PERSON_COUNTRY', null=True)
    person_duty_desc = CharField(column_name='PERSON_DUTY_DESC', null=True)
    person_ei_code = CharField(column_name='PERSON_EI_CODE', null=True)
    person_farmer_code = CharField(column_name='PERSON_FARMER_CODE', null=True)
    person_farmer_name = CharField(column_name='PERSON_FARMER_NAME', null=True)
    person_health = CharField(column_name='PERSON_HEALTH', null=True)
    person_health_desc = CharField(column_name='PERSON_HEALTH_DESC', null=True)
    person_hk = CharField(column_name='PERSON_HK', null=True)
    person_hk_desc = CharField(column_name='PERSON_HK_DESC', null=True)
    person_id = CharField(column_name='PERSON_ID', unique=True)
    person_id_code = CharField(column_name='PERSON_ID_CODE', null=True)
    person_jg = CharField(column_name='PERSON_JG', null=True)
    person_kind_of_work_code = CharField(column_name='PERSON_KIND_OF_WORK_CODE', null=True)
    person_kind_of_work_name = CharField(column_name='PERSON_KIND_OF_WORK_NAME', null=True)
    person_marry = CharField(column_name='PERSON_MARRY', null=True)
    person_mz = CharField(column_name='PERSON_MZ', null=True)
    person_mz_name = CharField(column_name='PERSON_MZ_NAME', null=True)
    person_name = CharField(column_name='PERSON_NAME', null=True)
    person_phone = CharField(column_name='PERSON_PHONE', null=True)
    person_photo_file_id = CharField(column_name='PERSON_PHOTO_FILE_ID', null=True)
    person_post_code = CharField(column_name='PERSON_POST_CODE', null=True)
    person_post_code2 = CharField(column_name='PERSON_POST_CODE2', null=True)
    person_post_name = CharField(column_name='PERSON_POST_NAME', null=True)
    person_post_name2 = CharField(column_name='PERSON_POST_NAME2', null=True)
    person_post_name_new = CharField(column_name='PERSON_POST_NAME_NEW', null=True)
    person_prop_code = CharField(column_name='PERSON_PROP_CODE', null=True)
    person_prop_name = CharField(column_name='PERSON_PROP_NAME', null=True)
    person_remark = CharField(column_name='PERSON_REMARK', null=True)
    person_sex = CharField(column_name='PERSON_SEX', null=True)
    person_sf = CharField(column_name='PERSON_SF', null=True)
    person_sf_desc = CharField(column_name='PERSON_SF_DESC', null=True)
    person_status_code = CharField(column_name='PERSON_STATUS_CODE', null=True)
    person_status_desc = CharField(column_name='PERSON_STATUS_DESC', null=True)
    person_xl = CharField(column_name='PERSON_XL', null=True)
    person_xl_name = CharField(column_name='PERSON_XL_NAME', null=True)
    person_zz = CharField(column_name='PERSON_ZZ', null=True)
    person_zz_desc = CharField(column_name='PERSON_ZZ_DESC', null=True)
    proj_year = IntegerField(column_name='PROJ_YEAR', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)

    class Meta:
        table_name = 'supplier_person'

class Suppliers(BaseModel):
    addr = CharField(column_name='ADDR', null=True)
    bank_account_code = CharField(column_name='BANK_ACCOUNT_CODE', null=True)
    bank_name = CharField(column_name='BANK_NAME', null=True)
    city_code = CharField(column_name='CITY_CODE', null=True)
    city_name = CharField(column_name='CITY_NAME', null=True)
    country_code = CharField(column_name='COUNTRY_CODE', null=True)
    country_name = CharField(column_name='COUNTRY_NAME', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    fq_flag = CharField(column_name='FQ_FLAG', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    link_czcode = CharField(column_name='LINK_CZCODE', null=True)
    link_person = CharField(column_name='LINK_PERSON', null=True)
    link_person_code = CharField(column_name='LINK_PERSON_CODE', null=True)
    link_phonecode = CharField(column_name='LINK_PHONECODE', null=True)
    link_type = CharField(column_name='LINK_TYPE', null=True)
    province_code = CharField(column_name='PROVINCE_CODE', null=True)
    province_name = CharField(column_name='PROVINCE_NAME', null=True)
    rel_code = CharField(column_name='REL_CODE', null=True)
    rel_name = CharField(column_name='REL_NAME', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    supplier_fr = CharField(column_name='SUPPLIER_FR', null=True)
    supplier_level_code = CharField(column_name='SUPPLIER_LEVEL_CODE', null=True)
    supplier_level_name = CharField(column_name='SUPPLIER_LEVEL_NAME', null=True)
    supplier_name = CharField(column_name='SUPPLIER_NAME', null=True)
    supplier_status_code = CharField(column_name='SUPPLIER_STATUS_CODE', null=True)
    supplier_status_name = CharField(column_name='SUPPLIER_STATUS_NAME', null=True)
    supplier_zzdj = CharField(column_name='SUPPLIER_ZZDJ', null=True)
    tax_code = CharField(column_name='TAX_CODE', null=True)
    type_code = CharField(column_name='TYPE_CODE', null=True)
    type_desc = CharField(column_name='TYPE_DESC', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    xz_code = CharField(column_name='XZ_CODE', null=True)
    xz_desc = CharField(column_name='XZ_DESC', null=True)
    yyzz = CharField(column_name='YYZZ', null=True)

    class Meta:
        table_name = 'suppliers'

class SuppliersAdmit(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_org = CharField(column_name='CREATOR_ORG', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    level = CharField(column_name='LEVEL', null=True)
    memo = CharField(column_name='MEMO', null=True)
    score = DecimalField(column_name='SCORE', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    supplier_name = CharField(column_name='SUPPLIER_NAME', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    xz_code = CharField(column_name='XZ_CODE', null=True)
    xz_name = CharField(column_name='XZ_NAME', null=True)
    zr_date = DateField(column_name='ZR_DATE', null=True)

    class Meta:
        table_name = 'suppliers_admit'

class SuppliersAdmitFile(BaseModel):
    admit_id = CharField(column_name='ADMIT_ID', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    id = CharField(column_name='ID', primary_key=True)

    class Meta:
        table_name = 'suppliers_admit_file'

class SuppliersDailyPerson(BaseModel):
    id = CharField(column_name='ID', primary_key=True)
    person_code = CharField(column_name='PERSON_CODE', null=True)
    person_id = CharField(column_name='PERSON_ID', null=True)
    person_name = CharField(column_name='PERSON_NAME', null=True)
    proj_code = CharField(column_name='PROJ_CODE', null=True)
    proj_name = CharField(column_name='PROJ_NAME', null=True)
    proj_supplier_id = CharField(column_name='PROJ_SUPPLIER_ID', null=True)
    proj_type = CharField(column_name='PROJ_TYPE', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    suppliers_daily_id = CharField(null=True)

    class Meta:
        table_name = 'suppliers_daily_person'

class SuppliersDailyProj(BaseModel):
    id = CharField(column_name='ID', primary_key=True)
    proj_code = CharField(column_name='PROJ_CODE', null=True)
    proj_name = CharField(column_name='PROJ_NAME', null=True)
    proj_supplier_id = CharField(column_name='PROJ_SUPPLIER_ID', null=True)
    proj_type = CharField(column_name='PROJ_TYPE', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    suppliers_daily_id = CharField(null=True)

    class Meta:
        table_name = 'suppliers_daily_proj'

class SuppliersDailySupervise(BaseModel):
    amount = FloatField(column_name='AMOUNT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_org = CharField(column_name='CREATOR_ORG', null=True)
    creator_org_name = CharField(column_name='CREATOR_ORG_NAME', null=True)
    gl_amount = FloatField(column_name='GL_AMOUNT', null=True)
    gl_khmx = CharField(column_name='GL_KHMX', null=True)
    id = CharField(column_name='ID', primary_key=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    jc_date = DateTimeField(column_name='JC_DATE', null=True)
    khqk = CharField(column_name='KHQK', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    question_type = CharField(column_name='QUESTION_TYPE', null=True)
    ques_memo = CharField(column_name='QUES_MEMO', null=True)
    supplier_code = CharField(column_name='SUPPLIER_CODE', null=True)
    supplier_name = CharField(column_name='SUPPLIER_NAME', null=True)
    type_level = CharField(column_name='TYPE_LEVEL', null=True)
    type_type = CharField(column_name='TYPE_TYPE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    zgbm = CharField(column_name='ZGBM', null=True)
    zgbm_name = CharField(column_name='ZGBM_NAME', null=True)
    zynr = CharField(column_name='ZYNR', null=True)
    zy_type = CharField(column_name='ZY_TYPE', null=True)

    class Meta:
        table_name = 'suppliers_daily_supervise'

class SuppliersDailySuperviseFile(BaseModel):
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    id = CharField(column_name='ID', primary_key=True)
    sup_id = CharField(column_name='SUP_ID', null=True)

    class Meta:
        table_name = 'suppliers_daily_supervise_file'

class TManageOrgs(BaseModel):
    aedtm = DateField(column_name='AEDTM', null=True)
    begda = DateField(column_name='BEGDA', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    endda = DateField(column_name='ENDDA', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    status = CharField(column_name='STATUS', null=True)
    uname = CharField(column_name='UNAME', null=True)
    zz_bm = CharField(column_name='ZZ_BM', null=True)
    zz_bm_n = CharField(column_name='ZZ_BM_N', null=True)
    zz_bm_p = CharField(column_name='ZZ_BM_P', null=True)
    zz_dxlb = CharField(column_name='ZZ_DXLB', null=True)
    zz_ms = CharField(column_name='ZZ_MS', null=True)
    zz_xh = IntegerField(column_name='ZZ_XH', null=True)

    class Meta:
        table_name = 't_manage_orgs'

class TManageUsers(BaseModel):
    begda = DateField(column_name='BEGDA', null=True)
    birthday = DateField(column_name='BIRTHDAY', null=True)
    bzdm = CharField(column_name='BZDM', null=True)
    bzmc = CharField(column_name='BZMC', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    cssj = DateField(column_name='CSSJ', null=True)
    endda = DateField(column_name='ENDDA', null=True)
    gwdm = CharField(column_name='GWDM', null=True)
    gwmc = CharField(column_name='GWMC', null=True)
    id = AutoField(column_name='ID')
    index_data_code = CharField(column_name='INDEX_DATA_CODE', null=True)
    index_data_name = CharField(column_name='INDEX_DATA_NAME', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    mobile = CharField(column_name='MOBILE', null=True)
    open_id = CharField(column_name='OPEN_ID', null=True)
    orgeh = CharField(column_name='ORGEH', null=True)
    org_data_code = CharField(column_name='ORG_DATA_CODE', null=True)
    org_data_name = CharField(column_name='ORG_DATA_NAME', null=True)
    password = CharField(column_name='PASSWORD', null=True)
    pernr = CharField(column_name='PERNR', null=True)
    persg = CharField(column_name='PERSG', null=True)
    pgtxt = CharField(column_name='PGTXT', null=True)
    rylb = CharField(column_name='RYLB', null=True)
    rylbdm = CharField(column_name='RYLBDM', null=True)
    rzqssj = DateField(column_name='RZQSSJ', null=True)
    zwdm = CharField(column_name='ZWDM', null=True)
    zwmc = CharField(column_name='ZWMC', null=True)
    zz_gwlb = CharField(column_name='ZZ_GWLB', null=True)
    zz_gyzt = CharField(column_name='ZZ_GYZT', null=True)
    zz_xm = CharField(column_name='ZZ_XM', null=True)
    zz_ygzt = CharField(column_name='ZZ_YGZT', null=True)

    class Meta:
        table_name = 't_manage_users'

class TMdmImport(BaseModel):
    end_date = DateField(column_name='END_DATE', null=True)
    import_type = CharField(column_name='IMPORT_TYPE', primary_key=True)

    class Meta:
        table_name = 't_mdm_import'

class TSecurityMenu(BaseModel):
    id = CharField(column_name='ID', primary_key=True)
    identifier = CharField(column_name='IDENTIFIER', null=True)
    img = CharField(column_name='IMG', null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    lefa = IntegerField(column_name='LEFA', null=True)
    memo = CharField(column_name='MEMO', null=True)
    menuname = CharField(column_name='MENUNAME', null=True)
    orderby = IntegerField(column_name='ORDERBY', constraints=[SQL("DEFAULT 0")])
    orderby_all = IntegerField(column_name='ORDERBY_ALL', null=True)
    parentid = CharField(column_name='PARENTID', null=True)
    url = CharField(column_name='URL', null=True)
    model = IntegerField(null=True)

    class Meta:
        table_name = 't_security_menu'

class TSecurityOrgs(BaseModel):
    area_type = CharField(column_name='AREA_TYPE', null=True)
    begda = DateField(column_name='BEGDA', null=True)
    code = CharField(column_name='CODE', index=True, null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    description = TextField(column_name='DESCRIPTION', null=True)
    endda = DateField(column_name='ENDDA', null=True)
    factory_level = CharField(column_name='FACTORY_LEVEL', null=True)
    hd_psn = CharField(column_name='HD_PSN', null=True)
    hd_psn_id = CharField(column_name='HD_PSN_ID', null=True)
    id = AutoField(column_name='ID')
    id_org_1 = CharField(column_name='ID_ORG_1', null=True)
    id_org_2 = CharField(column_name='ID_ORG_2', null=True)
    id_org_3 = CharField(column_name='ID_ORG_3', null=True)
    id_org_4 = CharField(column_name='ID_ORG_4', null=True)
    id_org_5 = CharField(column_name='ID_ORG_5', null=True)
    id_org_6 = CharField(column_name='ID_ORG_6', null=True)
    id_org_7 = CharField(column_name='ID_ORG_7', null=True)
    id_org_8 = CharField(column_name='ID_ORG_8', null=True)
    id_org_9 = CharField(column_name='ID_ORG_9', null=True)
    is_active = IntegerField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT 1")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    lat = CharField(column_name='LAT', null=True)
    level = IntegerField(column_name='LEVEL', constraints=[SQL("DEFAULT 0")])
    lng = CharField(column_name='LNG', null=True)
    name = CharField(column_name='NAME')
    org_type = CharField(column_name='ORG_TYPE', constraints=[SQL("DEFAULT '02'")], null=True)
    parent_code = CharField(column_name='PARENT_CODE', index=True, null=True)
    parent_id = IntegerField(column_name='PARENT_ID', null=True)
    iu_pxh = CharField(null=True)
    status = CharField(null=True)

    class Meta:
        table_name = 't_security_orgs'

class TSecurityPermissionUsers(BaseModel):
    code = CharField(column_name='CODE', index=True, null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    description = CharField(column_name='DESCRIPTION', null=True)
    disabled = CharField(column_name='DISABLED', null=True)
    id = CharField(column_name='ID', primary_key=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME', null=True)

    class Meta:
        table_name = 't_security_permission_users'

class TSecurityPermissions(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    description = TextField(column_name='DESCRIPTION', null=True)
    disabled = IntegerField(column_name='DISABLED', constraints=[SQL("DEFAULT 0")])
    id = AutoField(column_name='ID')
    identifier = CharField(column_name='IDENTIFIER', unique=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME')

    class Meta:
        table_name = 't_security_permissions'

class TSecurityPost(BaseModel):
    code = CharField(column_name='CODE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    description = CharField(column_name='DESCRIPTION', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME', null=True)
    org_code = CharField(column_name='ORG_CODE', null=True)
    updator = CharField(column_name='UPDATOR', null=True)

    class Meta:
        table_name = 't_security_post'

class TSecurityRoleMenuMap(BaseModel):
    menu_id = CharField(column_name='menuId')
    role_id = IntegerField(column_name='roleId')

    class Meta:
        table_name = 't_security_role_menu_map'
        primary_key = False

class TSecurityRolePermissionMap(BaseModel):
    permission_id = IntegerField(column_name='PERMISSION_ID')
    role_id = IntegerField(column_name='ROLE_ID')

    class Meta:
        table_name = 't_security_role_permission_map'
        primary_key = False

class TSecurityRoles(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    description = TextField(column_name='DESCRIPTION', null=True)
    disabled = IntegerField(column_name='DISABLED', constraints=[SQL("DEFAULT 0")])
    id = AutoField(column_name='ID')
    identifier = CharField(column_name='IDENTIFIER', unique=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME')

    class Meta:
        table_name = 't_security_roles'

class TSecurityUserRoleMap(BaseModel):
    role_id = IntegerField(column_name='ROLE_ID')
    user_id = IntegerField(column_name='USER_ID')

    class Meta:
        table_name = 't_security_user_role_map'
        indexes = (
            (('user_id', 'role_id'), True),
        )
        primary_key = CompositeKey('role_id', 'user_id')

class TSecurityUsers(BaseModel):
    begda = DateField(column_name='BEGDA', null=True)
    check_org_code = CharField(column_name='CHECK_ORG_CODE', null=True)
    code = CharField(column_name='CODE', index=True, null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    description = TextField(column_name='DESCRIPTION', null=True)
    disabled = IntegerField(column_name='DISABLED', constraints=[SQL("DEFAULT 0")])
    email = CharField(column_name='EMAIL', null=True)
    endda = DateField(column_name='ENDDA', null=True)
    id = AutoField(column_name='ID')
    is_ldap = IntegerField(column_name='IS_LDAP', constraints=[SQL("DEFAULT 0")], null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    login_name = CharField(column_name='LOGIN_NAME', unique=True)
    mobile = CharField(column_name='MOBILE', null=True)
    name = CharField(column_name='NAME')
    org_code = CharField(column_name='ORG_CODE', index=True, null=True)
    org_id = IntegerField(column_name='ORG_ID', null=True)
    org_upcode = CharField(column_name='ORG_UPCODE', null=True)
    password = CharField(column_name='PASSWORD', null=True)
    postcode = CharField(column_name='POSTCODE', null=True)

    class Meta:
        table_name = 't_security_users'

class TSecurityUsersCopy(BaseModel):
    begda = DateField(column_name='BEGDA', null=True)
    code = CharField(column_name='CODE', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    description = TextField(column_name='DESCRIPTION', null=True)
    disabled = IntegerField(column_name='DISABLED', constraints=[SQL("DEFAULT 0")])
    email = CharField(column_name='EMAIL', null=True)
    endda = DateField(column_name='ENDDA', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    login_name = CharField(column_name='LOGIN_NAME', unique=True)
    mobile = CharField(column_name='MOBILE', null=True)
    name = CharField(column_name='NAME')
    org_code = CharField(column_name='ORG_CODE', null=True)
    org_id = IntegerField(column_name='ORG_ID', null=True)
    org_upcode = CharField(column_name='ORG_UPCODE', null=True)
    password = CharField(column_name='PASSWORD', null=True)

    class Meta:
        table_name = 't_security_users_copy'

class TblLearnExamPlan(BaseModel):
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    end_time = DateTimeField(column_name='END_TIME')
    exam_name = CharField(column_name='EXAM_NAME')
    exam_time = IntegerField(column_name='EXAM_TIME')
    exam_users = IntegerField(column_name='EXAM_USERS', constraints=[SQL("DEFAULT 0")], null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    org_id = CharField(column_name='ORG_ID', null=True)
    papers_ab = CharField(column_name='PAPERS_AB')
    papers_id = IntegerField(column_name='PAPERS_ID')
    papers_name = CharField(column_name='PAPERS_NAME')
    pass_score = IntegerField(column_name='PASS_SCORE')
    real_users = IntegerField(column_name='REAL_USERS', constraints=[SQL("DEFAULT 0")], null=True)
    remarks = CharField(column_name='REMARKS', null=True)
    speciality_id = CharField(column_name='SPECIALITY_ID')
    start_time = DateTimeField(column_name='START_TIME')
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_exam_plan'

class TblLearnExamUser(BaseModel):
    answer_device = CharField(column_name='ANSWER_DEVICE', null=True)
    answer_end = DateTimeField(column_name='ANSWER_END', null=True)
    answer_start = DateTimeField(column_name='ANSWER_START', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    exam_result = DecimalField(column_name='EXAM_RESULT', constraints=[SQL("DEFAULT 0.0")], null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    judge_right = IntegerField(column_name='JUDGE_RIGHT', constraints=[SQL("DEFAULT 0")], null=True)
    judge_wrong = IntegerField(column_name='JUDGE_WRONG', constraints=[SQL("DEFAULT 0")], null=True)
    multip_right = IntegerField(column_name='MULTIP_RIGHT', constraints=[SQL("DEFAULT 0")], null=True)
    multip_wrong = IntegerField(column_name='MULTIP_WRONG', constraints=[SQL("DEFAULT 0")], null=True)
    papers_id = IntegerField(column_name='PAPERS_ID')
    plan_id = IntegerField(column_name='PLAN_ID', index=True)
    single_right = IntegerField(column_name='SINGLE_RIGHT', constraints=[SQL("DEFAULT 0")], null=True)
    single_wrong = IntegerField(column_name='SINGLE_WRONG', constraints=[SQL("DEFAULT 0")], null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)
    users_id = IntegerField(column_name='USERS_ID', index=True)
    user_answer = CharField(column_name='USER_ANSWER', null=True)

    class Meta:
        table_name = 'tbl_learn_exam_user'

class TblLearnGroup(BaseModel):
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    group_name = CharField(column_name='GROUP_NAME', null=True)
    group_num = IntegerField(column_name='GROUP_NUM', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    org_id = CharField(column_name='ORG_ID', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_group'

class TblLearnGroupUsers(BaseModel):
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    group_id = IntegerField(column_name='GROUP_ID', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    org_id = CharField(column_name='ORG_ID', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)
    user_id = IntegerField(column_name='USER_ID', null=True)
    user_name = CharField(column_name='USER_NAME', null=True)

    class Meta:
        table_name = 'tbl_learn_group_users'

class TblLearnIntegral(BaseModel):
    begin_time = DateTimeField(column_name='BEGIN_TIME', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    end_time = DateTimeField(column_name='END_TIME', null=True)
    factory_level = CharField(column_name='FACTORY_LEVEL', null=True)
    id = AutoField(column_name='ID')
    integral = DecimalField(column_name='INTEGRAL', constraints=[SQL("DEFAULT 0")], null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    knowledge_id = IntegerField(column_name='KNOWLEDGE_ID', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    study_len = IntegerField(column_name='STUDY_LEN', constraints=[SQL("DEFAULT 0")], null=True)
    user_id = CharField(column_name='USER_ID', null=True)
    user_name = CharField(column_name='USER_NAME', null=True)

    class Meta:
        table_name = 'tbl_learn_integral'

class TblLearnKnowledge(BaseModel):
    content = TextField(column_name='CONTENT', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    duration = DecimalField(column_name='DURATION', constraints=[SQL("DEFAULT 0")], null=True)
    file_id = CharField(column_name='FILE_ID', null=True)
    file_name = CharField(column_name='FILE_NAME', null=True)
    file_type = CharField(column_name='FILE_TYPE', null=True)
    id = AutoField(column_name='ID')
    integral = DecimalField(column_name='INTEGRAL', constraints=[SQL("DEFAULT 0")], null=True)
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    org_id = CharField(column_name='ORG_ID', null=True)
    origin = CharField(column_name='ORIGIN', null=True)
    release_time = DateTimeField(column_name='RELEASE_TIME', null=True)
    speciality_id = IntegerField(column_name='SPECIALITY_ID')
    speciality_name = CharField(column_name='SPECIALITY_NAME')
    text_length = DecimalField(column_name='TEXT_LENGTH', constraints=[SQL("DEFAULT 0")], null=True)
    title = CharField(column_name='TITLE')
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_knowledge'

class TblLearnPapers(BaseModel):
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    judge_num = IntegerField(column_name='JUDGE_NUM', constraints=[SQL("DEFAULT 0")])
    judge_score = DecimalField(column_name='JUDGE_SCORE', constraints=[SQL("DEFAULT 0.0")])
    multiple_num = IntegerField(column_name='MULTIPLE_NUM', constraints=[SQL("DEFAULT 0")])
    multiple_score = DecimalField(column_name='MULTIPLE_SCORE', constraints=[SQL("DEFAULT 0.0")])
    org_id = CharField(column_name='ORG_ID', null=True)
    papers_mode = CharField(column_name='PAPERS_MODE', constraints=[SQL("DEFAULT '随机试卷'")])
    papers_name = CharField(column_name='PAPERS_NAME')
    papers_score = IntegerField(column_name='PAPERS_SCORE', constraints=[SQL("DEFAULT 0")])
    remarks = CharField(column_name='REMARKS', null=True)
    single_num = IntegerField(column_name='SINGLE_NUM', constraints=[SQL("DEFAULT 0")])
    single_score = DecimalField(column_name='SINGLE_SCORE', constraints=[SQL("DEFAULT 0.0")])
    speciality_id = CharField(column_name='SPECIALITY_ID')
    speciality_name = CharField(column_name='SPECIALITY_NAME', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_papers'

class TblLearnPapersList(BaseModel):
    answer = CharField(column_name='ANSWER')
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    id = AutoField(column_name='ID')
    option_a = CharField(column_name='OPTION_A', null=True)
    option_b = CharField(column_name='OPTION_B', null=True)
    option_c = CharField(column_name='OPTION_C', null=True)
    option_d = CharField(column_name='OPTION_D', null=True)
    option_e = CharField(column_name='OPTION_E', null=True)
    option_f = CharField(column_name='OPTION_F', null=True)
    option_g = CharField(column_name='OPTION_G', null=True)
    papers_id = IntegerField(column_name='PAPERS_ID')
    question_tilte = CharField(column_name='QUESTION_TILTE')
    question_type = CharField(column_name='QUESTION_TYPE')
    seqno = IntegerField(column_name='SEQNO', constraints=[SQL("DEFAULT 0")])
    speciality_id = IntegerField(column_name='SPECIALITY_ID')
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_papers_list'

class TblLearnQuestion(BaseModel):
    answer = CharField(column_name='ANSWER')
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    option_a = CharField(column_name='OPTION_A', null=True)
    option_b = CharField(column_name='OPTION_B', null=True)
    option_c = CharField(column_name='OPTION_C', null=True)
    option_d = CharField(column_name='OPTION_D', null=True)
    option_e = CharField(column_name='OPTION_E', null=True)
    option_f = CharField(column_name='OPTION_F', null=True)
    option_g = CharField(column_name='OPTION_G', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    question_tilte = CharField(column_name='QUESTION_TILTE')
    question_type = CharField(column_name='QUESTION_TYPE')
    speciality_id = IntegerField(column_name='SPECIALITY_ID')
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_question'

class TblLearnSpeciality(BaseModel):
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    father_id = IntegerField(column_name='FATHER_ID', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    speciality_name = CharField(column_name='SPECIALITY_NAME', null=True)
    tree_level = IntegerField(column_name='TREE_LEVEL', null=True)
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)

    class Meta:
        table_name = 'tbl_learn_speciality'

class TblLearnWrongTopic(BaseModel):
    answer = CharField(column_name='ANSWER')
    create_time = DateTimeField(column_name='CREATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = CharField(column_name='CREATOR', null=True)
    creator_id = CharField(column_name='CREATOR_ID', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")])
    option_a = CharField(column_name='OPTION_A', null=True)
    option_b = CharField(column_name='OPTION_B', null=True)
    option_c = CharField(column_name='OPTION_C', null=True)
    option_d = CharField(column_name='OPTION_D', null=True)
    option_e = CharField(column_name='OPTION_E', null=True)
    option_f = CharField(column_name='OPTION_F', null=True)
    option_g = CharField(column_name='OPTION_G', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    question_id = IntegerField(column_name='QUESTION_ID', null=True)
    question_tilte = CharField(column_name='QUESTION_TILTE')
    question_type = CharField(column_name='QUESTION_TYPE')
    source_id = IntegerField(column_name='SOURCE_ID')
    speciality_id = IntegerField(column_name='SPECIALITY_ID')
    update_time = DateTimeField(column_name='UPDATE_TIME', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updator = CharField(column_name='UPDATOR', null=True)
    updator_id = CharField(column_name='UPDATOR_ID', null=True)
    user_id = IntegerField(column_name='USER_ID', constraints=[SQL("DEFAULT 0")])
    user_name = CharField(column_name='USER_NAME', constraints=[SQL("DEFAULT '0'")])
    wrong_source = CharField(column_name='WRONG_SOURCE')

    class Meta:
        table_name = 'tbl_learn_wrong_topic'

class Test(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    name = CharField(column_name='NAME', null=True)

    class Meta:
        table_name = 'test'

class TestAnalysis(BaseModel):
    date = DateField()
    name = CharField()
    total = IntegerField()

    class Meta:
        table_name = 'test_analysis'

class ViolateLevel(BaseModel):
    category_id = CharField(column_name='CATEGORY_ID', null=True)
    code = CharField(column_name='CODE', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    name = CharField(column_name='NAME', null=True)

    class Meta:
        table_name = 'violate_level'

class ViolateOrgBehavior(BaseModel):
    behavior_code = CharField(column_name='BEHAVIOR_CODE', null=True)
    behavior_name = CharField(column_name='BEHAVIOR_NAME', null=True)
    code = CharField(column_name='CODE', null=True)
    create_time = DateTimeField(column_name='CREATE_TIME', null=True)
    id = AutoField(column_name='ID')
    is_active = CharField(column_name='IS_ACTIVE', constraints=[SQL("DEFAULT '1'")], null=True)
    name = CharField(column_name='NAME', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)

    class Meta:
        table_name = 'violate_org_behavior'

class Violating(BaseModel):
    check_type = CharField(column_name='CHECK_TYPE', null=True)
    clear = CharField(column_name='CLEAR', null=True)
    clear_count = CharField(column_name='CLEAR_COUNT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', index=True, null=True)
    createtor = CharField(column_name='CREATETOR', null=True)
    id = CharField(column_name='ID', primary_key=True)
    import_type = CharField(column_name='IMPORT_TYPE', null=True)
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_by_id = CharField(column_name='LAST_MODIFIED_BY_ID', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    reality_score = CharField(column_name='REALITY_SCORE', null=True)
    remark = CharField(column_name='REMARK', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT '0'")], null=True)
    total_fee = CharField(column_name='TOTAL_FEE', null=True)
    total_score = CharField(column_name='TOTAL_SCORE', null=True)
    valid_score = CharField(column_name='VALID_SCORE', null=True)
    violating_describe = CharField(column_name='VIOLATING_DESCRIBE', null=True)
    violating_examine = CharField(column_name='VIOLATING_EXAMINE', null=True)
    violating_fee = DecimalField(column_name='VIOLATING_FEE', null=True)
    violating_level = CharField(column_name='VIOLATING_LEVEL', null=True)
    violating_score = CharField(column_name='VIOLATING_SCORE', null=True)
    violating_time = DateTimeField(column_name='VIOLATING_TIME', null=True)
    violating_type = CharField(column_name='VIOLATING_TYPE', null=True)
    violating_unit = CharField(column_name='VIOLATING_UNIT', null=True)
    violating_unit_id = CharField(column_name='VIOLATING_UNIT_ID', null=True)
    violating_user = CharField(column_name='VIOLATING_USER', null=True)
    violating_user_id = CharField(column_name='VIOLATING_USER_ID', null=True)

    class Meta:
        table_name = 'violating'

class ViolatingCategory(BaseModel):
    code = CharField(null=True)
    create_time = DateTimeField(null=True)
    name = CharField(null=True)

    class Meta:
        table_name = 'violating_category'

class ViolatingRegulation(BaseModel):
    count = IntegerField(column_name='COUNT', null=True)
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_by_id = CharField(column_name='LAST_MODIFIED_BY_ID', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    org_id = CharField(column_name='ORG_ID', null=True)
    org_name = CharField(column_name='ORG_NAME', null=True)
    score_sum = IntegerField(column_name='SCORE_SUM', null=True)

    class Meta:
        table_name = 'violating_regulation'

class ViolatingStatistic(BaseModel):
    created_by = CharField(column_name='CREATED_BY', null=True)
    created_date = DateTimeField(column_name='CREATED_DATE', null=True)
    fee = DecimalField(column_name='FEE', null=True)
    id = AutoField(column_name='ID')
    last_modified_by = CharField(column_name='LAST_MODIFIED_BY', null=True)
    last_modified_date = DateTimeField(column_name='LAST_MODIFIED_DATE', null=True)
    score = IntegerField(column_name='SCORE', null=True)
    total_score = IntegerField(column_name='TOTAL_SCORE', null=True)
    violating_unit = CharField(column_name='VIOLATING_UNIT', null=True)
    violating_unit_id = CharField(column_name='VIOLATING_UNIT_ID', null=True)
    violating_user = CharField(column_name='VIOLATING_USER', null=True)
    violating_user_id = CharField(column_name='VIOLATING_USER_ID', null=True)
    year = CharField(column_name='YEAR', null=True)
    count = IntegerField(null=True)

    class Meta:
        table_name = 'violating_statistic'

