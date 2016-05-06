import requests
import elementtree.ElementTree as ET
import xml.parsers.expat
import csv

cnt = 1
payload = {'limit': '200', 'page' : cnt}
bcinvn = {}

def obtainProduct(url, payload, topLevel, bcinvn):
	cnt = 1
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
					bcinvn[itmsku] = qty

			cnt = cnt + 1
			payload = {'limit': '200', 'page' : cnt}

	return bcinvn

print "Grabbing SKU's From Option Set Products"

bcinvn = obtainProduct('products/skus', payload, 'sku', bcinvn)

print "Grabbing SKU's From Option Set Products COMPLETED"

print "Grabbing SKU's From Single SKU Products"

bcinvn = obtainProduct('products', payload, 'product', bcinvn)

print "Grabbing SKU's From Single SKU Products COMPLETED"
print len(bcinvn)
