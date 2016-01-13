from lxml import etree
from lxml.etree import tostring
from copy import deepcopy
import requests
import time
from StringIO import StringIO
_79xx_keynavlist = ['Key:Applications','Key:KeyPad5','Key:KeyPad4','Key:KeyPad4','Key:Soft3','Key:Soft1']
key = 'XML'
keynav = {key : []}
for keypress in _79xx_keynavlist:
    ph_nav = etree.Element('CiscoIPPhoneExecute')
    exeit_e = etree.SubElement(ph_nav, 'ExecuteItem')
    exeit_e.set('Priority','0')
    exeit_e.set('URL',keypress)
    phnavstr = etree.tostring(ph_nav,pretty_print=True)
    print phnavstr
    keynav[key] = keynav[key]+[phnavstr]

key_action = deepcopy(keynav)

url = 'http://192.168.5.197/CGI/Execute'
user='phonecontrol'
pwd='phonecontrol'
headers={'content-type':'application/xml'}
counter = 0
for xml in keynav[key]:
    key_press = {}
    key_press[key] = xml
    r = requests.post(url,headers=headers,data=key_press,auth=(user,pwd))
    key_action[key].remove(xml)
    if(counter == 4):
        break
    counter += 1
for i in range(1,3):
    counter = 1
    for action in key_action[key]:
        keyact = {}
        keyact[key] = action
        r = requests.post(url,headers=headers,data=keyact,auth=(user,pwd))
        if counter != 3:
            time.sleep(50.0/1000.0)
        else:
            time.sleep(2)
        counter += 1
