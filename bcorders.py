import datetime
import time
import requests
import elementtree.ElementTree as ET

order_items = []
filename = 'lastupdate.txt'
target = open(filename, 'r')
last_id = target.read()
target.close()

print last_id

payload = {'min_id': last_id}

print payload

r = requests.get('STORE URL/api/v2/orders', params=payload, auth=(USER ID, API KEY))

tree = ET.fromstring(r.content)   
print tree

for order in tree.findall('order'):
	payment_status = order.find('payment_status').text
	if payment_status == 'captured':
		order_id = order.find('id').text
		print order_id
		order_items.append( order_id )
print  order_items

#time = datetime.datetime.fromtimestamp(
		#int(t)).strftime('%a%%2C%d+%b+%Y+%H%%3A%M%%3A%S+%%2B0000')

#target = open(filename, 'w')
#target.truncate()
#target.write(time)
#target.close
