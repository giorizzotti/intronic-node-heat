from oslo_log import log as logging
from heat.engine import properties
from heat.engine import resource
from gettext import gettext as _
from iotronicclient import client

__author__ = 'Giovanni Rizzotti'

kwargs={
    'os_username': 'admin', 
    'os_user_domain_name': '', 
    'os_cacert': None, 
    'os_tenant_name': 'admin', 
    'os_user_domain_id': 'default', 
    'os_iotronic_api_version': None, 
    'os_password': 'f719b3e7ebe94b5f', 
    'os_cert': None, 
    'os_project_id': '', 
    'retry_interval': 2, 
    'os_tenant_id': '', 
    'os_project_name': 'admin', 
    'os_service_type': '', 
    'os_key': None, 
    'os_project_domain_id': 'default', 
    'insecure': False, 
    'max_retries': 5, 
    'os_endpoint_type': '', 
    'os_region_name': '', 
    'iotronic_url': '', 
    'os_auth_url': 'http://10.0.2.4:35357/v3', 
    'os_auth_token': '', 
    'timeout': 600, 
    'os_project_domain_name': ''}

myclient = client.get_client('1', **kwargs)

LOG = logging.getLogger(__name__)

class IoTronicNode(resource.Resource):    
    """Heat Template Resource for IoTronic Node."""
    PROPERTIES = (
        CREATED_AT,
        UPDATED_AT,
        ID,
        UUID,
        CODE,
        STATUS,
        NAME,
        DEVICE,
        SESSION,
        MOBILE,
        EXTRA) = (
        'created_at',
        'updated_at',
        'id',
        'uuid',
        'code',
        'status',
        'name',
        'device',
        'session',
        'mobile',
        'extra')

    properties_schema = {
        CREATED_AT: properties.Schema(
            properties.Schema.STRING,
            _('The date and time when the node infos were created.'),
            required=False,
            update_allowed=True
        ),

        UPDATED_AT: properties.Schema(
            properties.Schema.STRING,
            _('The date and time when the node infos were updated.'),
            required=False,
            update_allowed=True
        ),

        ID: properties.Schema(
            properties.Schema.INTEGER,
            _('The unique id for the node.'),
            required=True,
            update_allowed=False
        ),

        UUID: properties.Schema(
            properties.Schema.STRING,
            _('The unique id for the node.'),
            required=True,
            update_allowed=False
        ),

        CODE: properties.Schema(
            properties.Schema.STRING,
            _('The code of the node.'),
            required=True,
            update_allowed=True
        ),

        STATUS: properties.Schema(
            properties.Schema.STRING,
            _('The generic node status.'),
            required=False,
            update_allowed=True
        ),

        NAME: properties.Schema(
            properties.Schema.STRING,
            _('The name of the node.'),
            required=False,
            update_allowed=True
        ),

        DEVICE: properties.Schema(
            properties.Schema.STRING,
            _('The typology of the node.'),
            required=False,
            update_allowed=True
        ),

        SESSION: properties.Schema(
            properties.Schema.STRING,
            _('The WAMP session ID of a CONNECTED node.'),
            required=False,
            update_allowed=True
        ),

        MOBILE: properties.Schema(
            properties.Schema.INTEGER,
            _('If true, the node is mobile. If false, the node is fixed.'),
            required=False,
            update_allowed=True
        ),

        EXTRA: properties.Schema(
            properties.Schema.STRING,
            _('List of metadata defined by the user.'),
            required=False,
            update_allowed=True
        )
    }

    def handle_create(self):
        created_at = self.properties.get(self.CREATED_AT),
        updated_at=self.properties.get(self.UPDATED_AT),
        id=self.properties.get(self.ID),
        uuid=self.properties.get(self.UUID),
        code=self.properties.get(self.CODE),
        status=self.properties.get(self.STATUS),
        name=self.properties.get(self.NAME),
        device=self.properties.get(self.DEVICE),
        session=self.properties.get(self.SESSION),
        mobile=self.properties.get(self.MOBILE),
        extra=self.properties.get(self.EXTRA)
        
        LOG.error("NODE CREATED: %s %s", created_at, name)

        LOG.error(myclient.node.list())     


def resource_mapping():
    mappings = {}
    mappings['OS::IoTronic::Node'] = IoTronicNode
    return mappings