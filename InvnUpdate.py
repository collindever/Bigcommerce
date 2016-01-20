import csv
import datetime
import requests
from grabsku import bcinvn
from bcorders import order_inventory
from sprdshtimprt import rpinvn

old_product = {}
new_product = {}
update_invn = {}

rpinvnSet = set(rpinvn.keys())
bcinvnSet = set(bcinvn.keys())



d = datetime.date.today()

for sku in rpinvnSet.intersection(bcinvnSet):
	update_invn[sku] = rpinvn[sku]
	if sku in order_inventory:
		update_invn[sku] = update_invn[sku] - order_inventory[sku]


for sku in bcinvnSet.difference(rpinvnSet):
	old_product[sku] = bcinvn[sku]

for sku in rpinvnSet.difference(bcinvnSet):
	new_product[sku] = rpinvn[sku]
	
with open('%s.csv' % (d), 'w+') as f:
	w = csv.writer(f)
	headers = ['Product SKU', 'Stock Level']
	w.writerow(headers)
	for row in update_invn.iteritems():	
		w.writerow(row)
f.close()

with open('oldproduct.csv', 'w+') as f:
	w = csv.writer(f)
	for row in old_product.iteritems():	
		w.writerow(row)
f.close()

with open('newproduct.csv', 'w+') as f:
	w = csv.writer(f)
	for row in new_product.iteritems():	
		w.writerow(row)
f.close()
