import requests
import elementtree.ElementTree as ET
import xml.parsers.expat
import csv
import threading

bcinvn = {}

class Sku_List(threading.Thread):
	def __init__(self, url, topLevel, name='SKUS'):
		threading.Thread.__init__(self) 
		self.name = name
		self.url = url
		self.topLevel = topLevel
		self.cnt = 0
		self.invn = {}


	def run(self):
		SKUS_TO_GRAB = True

		while SKUS_TO_GRAB is True:
			
			self.cnt = self.cnt + 1
			payload = {'limit': '200', 'page' : self.cnt}
			
			try:
				r = requests.get('STORE URL%s' %self.url, params=payload, auth=('API ID', 'API PASSWORD'))
				tree = ET.fromstring(r.content)
			
			except xml.parsers.expat.ExpatError, e:
				SKUS_TO_GRAB = False

			else:
				for product in tree.findall('%s' %self.topLevel):
					if product.find('sku').text is not None:
						itmsku = int(product.find('sku').text)
						qty = int(product.find('inventory_level').text)
						self.invn[itmsku] = qty

		return self.invn

threads = []
skuThread = Sku_List('products/skus', 'sku', 'skus')
productThread = Sku_List('products', 'product', 'products')

skuThread.start()
threads.append(skuThread)

productThread.start()
threads.append(productThread)

print 'Threads Declared'

for t in threads:
	t.join()
print 'Exiting Threads'

bcinvn.update(skuThread.invn)
bcinvn.update(productThread.invn)

print 'SKUS GRABBED'
print len(bcinvn)
