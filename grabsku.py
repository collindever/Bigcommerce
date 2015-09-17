import requests
import elementtree.ElementTree as ET

cnt = 1
payload = {'limit': '250', 'page' : cnt}   #adds ?limit=250&page=cnt to the end of the GET request
r = requests.get('https://STORE URL/api/v2/products/skus', params=payload, auth=('USER ID', 'API TOKEN'))  #get request pulls pages of 250 SKUS

tree = ET.fromstring(r.content)   #imports the raw binary data from the site into Element Tree to read XML data

for sku in tree.findall('sku'):   
	itmsku = sku.find('sku').text
	qty = sku.find('inventory_level').text
	print itmsku, qty
