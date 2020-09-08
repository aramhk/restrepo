import requests
import xml.etree.ElementTree as ET


URL = 'https://xml2.travelsim.com/tsim_xml/service/xmlgate'

phone = input("Please enter Phone number:")
phone = int(phone)


PARAMS =  {'uname':'QWpT1ErThjyfYqv', 'upass':'PBeXOuiiHBph','plain':1, 'command':'account' }
r= requests.get(url=URL,params=PARAMS)
print(r.text)
root = ET.fromstring(r.text)
oid=root[5].text
orderid= int(oid) + 1


PARAMS1 = {'uname':'QpT1ErTYqv', 'upass':'PeXOuiiBph','plain':1, 'command':'corp','onum':phone ,'corp_minlimit':1,'corp_transaction':4,'corp_maxlimit':50,'aserviceid':24181,'corp_group':1,'corp_enabled':'yes' } 
PARAMS2 = {'uname':'QpT1ErTYqv', 'upass':'PeXOuiiBph','plain':1, 'command':'sbalance','amount': '+1.00' ,'curr':'EUR','orderid':orderid,'onum':phone ,'groupid':1,'aserviceid':24181 }



print('----------------------------------------------------------------------------')
r1 = requests.get(url=URL,params=PARAMS1)
print(r1.text)
print('----------------------------------------------------------------------------')
r2 = requests.get(url=URL,params=PARAMS2)
print(r2.text)
