__author__ = 'Kjetil'
import urllib.parse as u
import http.client as h
import xml.etree.ElementTree as ET
from xml.etree.cElementTree import Element, ElementTree,Comment
import XMLBuilder as xpars




class sms():
    SMS_messages = []
    SMS_Result = []
    SMS_Batchsize = 3
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "xml-test.pswin.com"
        self.SMS_session = xpars.BuildSession(self.username, self.password)



    def sms_add(self,TEXT ,RCV ,SND = None,RCPREQ = None,OP = None,CLASS = None,TTL = None,CPATAG = None,AGELIMIT = None,SHORTCODE = None,REPLACE = None,DELIVERYTIME = None,ID = None):
        #def __init__(self):
        ID = len(self.SMS_messages)
        arguments = {}


        for key,value in locals().items():
            if value is not None and key != 'self' and key != 'arguments' and self is not None:
                arguments[key] = value
            message = xpars.AddMessage(**arguments)

        sms.SMS_messages.append(message)

    def sms_result (self,ID ,REF ,STATUS,INFO = None):
        arguments = {}
        for key,value in locals().items():
            print(key)
            print(value)


    @property
    def sms_send(self):
        #Build the complete XML pacakge
        print("Number fo messages: %s " % (len(sms.SMS_messages)))
        xml = self.SMS_session
        messagelist = ET.Element('MSGLST')
        xml.append(messagelist)
        print(len(self.SMS_messages))
        while len(self.SMS_messages) != 0:
            current = self.SMS_Batchsize
            while 0 != current:

                #print("Processing Batch: %s" %(current))
                if not len(self.SMS_messages) == 0:
                    currrentBatch = xml.find('MSGLST')
                    currrentBatch.append(self.SMS_messages.pop())
                    current -= 1
                    if 0 == current or len(self.SMS_messages) == 0:
                        ET.dump(xml)
                        self.http_post(xml)
                        currrentBatch.clear()
                    if len(self.SMS_messages) == 0:
                        break



    def http_post(self,xml):
        #Time for HTTP stuff
        connection = h.HTTPConnection(self.url)
        headers = {'Content-type': 'application/xml'}
        xdata = ET.tostring(xml,encoding='ISO-8859-1')
        connection.request('POST','/',str(xdata,encoding='ISO-8859-1'),headers)
        response = connection.getresponse()
        print(response.read().decode(encoding='ISO-8859-1'))
        return response




