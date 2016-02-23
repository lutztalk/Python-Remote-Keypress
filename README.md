# 8841 Cisco IP phone 
A quick and simple python script I took from samiamsam.com and tweaked to work with 8841 model Cisco IP phones.

http://samiamsam.com/2014/04/16/cisco-uc-devops-series-remotely-deleting-the-itl-cert-from-a-7900-series-phone/

Instructions

-On the CUCM your devices are registered to, create an application user with the "Standard CTI Enabled" Permissions. Once created, assign all devices you are wanting to control to its list of "Controlled Devices".

-Fill in the phoneiplist.csv with the IPs you want to run the script against. Execute 'python 8841-KeyPress-Template.py' from the same directory as your phoneiplist.csv file. This script supports up to 2000 IPs in the CSV.
