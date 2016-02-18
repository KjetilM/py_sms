__author__ = 'Kjetil'
#import http, urllib
#import re
import xml.etree.ElementTree as ET
def BuildSession(eClient,ePW,eAP = None ,eSD = None):
    SessionElement = ET.Element('SESSION')
    client = ET.SubElement(SessionElement,'CLIENT')
    PW = ET.SubElement(SessionElement,'PW')
    client.text = eClient
    PW.text = ePW
    if SessionElement is not None:
        return SessionElement

def AddMessage(**kwargs):
    MessageElement = ET.Element('MSG')
    for key,value in kwargs.items():
        if value != None or key != 'self' or key != 'arguments':
            addElement = ET.SubElement(MessageElement,key)
            addElement.text = str(value)

    #ET.dump( MessageElement)
    if MessageElement is not None:
        return MessageElement





