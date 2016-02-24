from lxml import etree
from lxml.etree import tostring
from StringIO import StringIO
import requests
import time
import sys
import time
import csv

def buttonpress(ip):
    _88xx_keynavlist = ['Key:Applications','Key:KeyPad5','Key:KeyPad4','Key:KeyPad4','Key:Soft3']
    key = 'XML'
    keynav = {key : []}
    url = 'http://' + ip + '/CGI/Execute'
    user='phonecontrol'
    pwd='phonecontrol'
    headers={'content-type':'application/xml'}

    for keypress in _88xx_keynavlist:
        ph_nav = etree.Element('CiscoIPPhoneExecute')
        exeit_e = etree.SubElement(ph_nav, 'ExecuteItem')
        exeit_e.set('Priority','0')
        exeit_e.set('URL',keypress)
        phnavstr = etree.tostring(ph_nav,pretty_print=True)
        keynav[key] = keynav[key]+[phnavstr]

    for xml in keynav[key]:
        key_press = {}
        key_press[key] = xml
        r = requests.post(url,headers=headers,data=key_press,auth=(user,pwd))
        time.sleep(1.0)

print "Starting ITL Delete"

with open('phoneiplist.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        phoneIP = '. '.join(row)
        print "Starting ITL delete operation on " + phoneIP
        buttonpress(phoneIP)
        print phoneIP + " completed"

print "All Done!!"
