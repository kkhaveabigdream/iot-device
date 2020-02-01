'''
Created on Jan 28, 2020

@author: sk199
'''
from labs.common.ConfigUtil import ConfigUtil
import logging
from labs.common import ConfigConst
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtpd import SMTPServer
import smtplib

class SmtpClientConnector(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.config = ConfigUtil()
        self.config.loadConfig()
        
        logging.info('Configuration data...\n' + str(ConfigConst.CONFIGFILE))
    
    '''   
    configured via the data stored in ConfigUtil    
    implement an SMTP, sending sensor data to a remote email account
    '''    
    def publishMessage(self,topic,data):
        host        = self.config.getValue(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port        = self.config.getValue(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr    = self.config.getValue(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr      = self.config.getValue(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken   = self.config.getValue(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        
        msg         = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To']   = toAddr
        msg['Subject'] = topic
        msgBody     = str(data)
        
        msg.attach(MIMEText(msgBody))
        
        msgText     = msg.as_string()
        
        SMTPServer  = smtplib.SMTP_SSL(host,port)
        SMTPServer.ehlo()
        SMTPServer.login(fromAddr,authToken)
        SMTPServer.sendmail(fromAddr,toAddr,msgText)
        SMTPServer.close()
        
        