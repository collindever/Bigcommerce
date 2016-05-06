import requests
import elementtree.ElementTree as ET
import xml.parsers.expat
import csv

cnt =  1
payload = {'limit': '200', 'page' : cnt}
inventory = {}

while cnt != -1:
	try:
		r = requests.get('https://STORE URL/api/v2/products/skus', params=payload, auth=('USER ID', 'API KEY'))

		tree = ET.fromstring(r.content)   

	except xml.parsers.expat.ExpatError, e:
		cnt = -1

	else:
		for sku in tree.findall('sku'):
			itmsku = sku.find('sku').text
			qty = sku.find('inventory_level').text
			inventory[itmsku] = qty

		cnt = cnt + 1
		payload = {'limit': '200', 'page' : cnt}

	finally:
		print len(inventory)

cnt =  1
payload = {'limit': '200', 'page' : cnt}

while cnt != -1:
	try:
		r = requests.get('https://STORE URL/api/v2/products', params=payload, auth=('USER ID', 'API KEY'))

		tree = ET.fromstring(r.content)   

	except xml.parsers.expat.ExpatError, e:
		cnt = -1

	else:
		for product in tree.findall('product'):
			itmsku = product.find('sku').text
			qty = product.find('inventory_level').text
			inventory[itmsku] = qty

		cnt = cnt + 1
		payload = {'limit': '200', 'page' : cnt}
	
print len(inventory)
