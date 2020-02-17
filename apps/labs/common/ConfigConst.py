'''
Created on Jan 30, 2020

@author: sk199
'''

DEFAULT_CONFIG_FILE_NAME = '../../../config/ConnectedDevicesConfig.props'

SEPARATOR = '.'
CLOUD = 'cloud'
SMTP = 'smtp'
DEVICE = 'device'

SMTP_CLOUD_SECTION = SMTP + SEPARATOR + CLOUD

HOST_KEY = 'host'
PORT_KEY = 'port'

FROM_ADDRESS_KEY = 'fromAddr'
TO_ADDRESS_KEY = 'toAddr'
USER_AUTH_TOKEN_KEY = 'authToken'

NOMINAL_TEMP    = 'nominalTemp'
NOMINAL_HUMID   = 'nominalHumid'