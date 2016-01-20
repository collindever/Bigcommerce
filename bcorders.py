import requests
import elementtree.ElementTree as ET

order_items = []
filename = 'lastupdate.txt'
target = open(filename, 'r')
last_id = target.read()
target.close()

payload = {'min_id': last_id, 'limit' : '250'}

print "Importing Orders Since Last Update"

r = requests.get('https://<STORE URL>/api/v2/orders', params=payload, auth=(<USER ID>, <API KEY>))

tree = ET.fromstring(r.content)   

for order in tree.findall('order'):
	payment_status = order.find('payment_status').text
	if payment_status == 'captured':
		order_id = order.find('id').text
		order_items.append( order_id )

max = len(order_items)
cnt = 0
order_inventory = {}

while cnt < max:
	r = requests.get('https://<STORE URL>/api/v2/orders/%s/products.xml' % order_items[cnt], auth=(<USER ID>, <API KEY>))
		
	tree = ET.fromstring(r.content)
	
	for product in tree.findall('product'):
		if (product.find('sku').text) is None:
			cnt = cnt + 1
		else:
			itmsku = int(product.find('sku').text)
			qty = int(product.find('quantity').text) 
			if itmsku in order_inventory:
				order_inventory[itmsku] = order_inventory[itmsku] + qty	
			else:
				order_inventory[itmsku] = qty
		cnt = cnt + 1

cnt = cnt - 1
newest_order = order_items[cnt]

print "Importing Orders Since Last Update COMPLETE"

filename = 'lastupdate.txt'
target = open(filename, 'w')
target.truncate()
target.write(newest_order)
target.close
