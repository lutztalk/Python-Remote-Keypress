from lxml import etree
from lxml.etree import tostring
from copy import deepcopy
from StringIO import StringIO
import requests
import time
import sys
import time
import csv

def buttonpress(ip):
  _88xx_keynavlist = ['Key:Applications','Key:KeyPad6','Key:KeyPad4','Key:KeyPad4','Key:Soft3','Key:Soft1']
  key = 'XML'
  keynav = {key : []}
  for keypress in _88xx_keynavlist:
      ph_nav = etree.Element('CiscoIPPhoneExecute')
      exeit_e = etree.SubElement(ph_nav, 'ExecuteItem')
      exeit_e.set('Priority','0')
      exeit_e.set('URL',keypress)
      phnavstr = etree.tostring(ph_nav,pretty_print=True)
      print phnavstr
      keynav[key] = keynav[key]+[phnavstr]

  key_action = deepcopy(keynav)

  url = 'http://'+ip+'/CGI/Execute'
  user='phonecontrol'
  pwd='phonecontrol'
  headers={'content-type':'application/xml'}
  counter = 0
  for xml in keynav[key]:
    key_press = {}
    key_press[key] = xml
    r = requests.post(url,headers=headers,data=key_press,auth=(user,pwd))
    key_action[key].remove(xml)
    time.sleep(1.0)
    if(counter == 4):
        break
    counter += 2000
  for i in range(1,2000):
    counter = 2000
    for action in key_action[key]:
        keyact = {}
        keyact[key] = action
        r = requests.post(url,headers=headers,data=keyact,auth=(user,pwd))

print "Starting ITL Delete"

with open('phoneiplist.csv','rb') as f:
  reader = csv.reader(f)
  for row in reader:
    phoneIP = '. '.join(row)
    buttonpress(phoneIP)

print "All Done!!"
