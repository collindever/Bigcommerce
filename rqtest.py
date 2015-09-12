import requests
import elementtree.ElementTree as ET

r = requests.get('https://STORE-URL/api/v2/time', auth=('USER IS', 'API TOKEN'))

print r.headers['content-type']

tree = ET.fromstring(r.content)
print "tag=%s, attrib=%s, text=%s" % (tree.tag, tree.attrib, tree.text)

for child in tree:
    print child.tag, child.attrib, child.text
