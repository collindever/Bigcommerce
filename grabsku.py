import requests
import elementtree.ElementTree as ET
import xml.parsers.expat
import csv

bcinvn = {}

def obtainProduct(url, topLevel):
	cnt = 1
	payload = {'limit': '200', 'page' : cnt}
	invn = {}
	
	while cnt != -1:
		try:
			r = requests.get('https://STORE URL/api/v2/%s' %url, params=payload, auth=('API ID', 'API PASSWORD'))
			tree = ET.fromstring(r.content)
		except xml.parsers.expat.ExpatError, e:
			cnt = -1

		else:
			for product in tree.findall('%s' %topLevel):
				if product.find('sku').text is not None:
					itmsku = int(product.find('sku').text)
					qty = int(product.find('inventory_level').text)
					invn[itmsku] = qty

			cnt = cnt + 1
			payload = {'limit': '200', 'page' : cnt}

	return invn

print "Grabbing SKU's From Option Set Products"

bcinvn.update(obtainProduct('products/skus', 'sku'))

print "Grabbing SKU's From Option Set Products COMPLETED"

print "Grabbing SKU's From Single SKU Products"

bcinvn.update(obtainProduct('products', 'product'))

print "Grabbing SKU's From Single SKU Products COMPLETED"
print len(bcinvn)
