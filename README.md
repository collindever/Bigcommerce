# Bigcommerce
Attempts at Automating tasks based on the specific Retail Setup I work with

I am working with an older site that runs on a basic auth API and produces XML data.  Most of the Bigcommerce documentation I think is focused on newer versions, there for i have not had any luck with the Python Bigcommerce 0.11.0 library, instead most of this I think will end up relying on the requests library as well as the ElementTree library for working with XML data.

The ulitimate goal will be to create scripts that can be implemented on the server for automation of tasks currently being done by hand.

First goal will be batch inventory update once a day
Second will be real time order updating

The challenge is interlinking the ecommerce software we are using, Bigcommerce, and our POS software RetailPro8

Any and all help is more than appreciated.

SCRIPTS INCLUDE:
    rqtest.py  -- proof of successful connection test, returns time from store
    
    grabsku.py -- This is the script I'm activily working on to work with my particular setup of pulling all the skus and qty levels for a store, importing an excel file of the same formatted info from a POS databse, update the store inventory levels to the POS inventory values, remove whatever was sold in the store since last run. Create a log file for review.
    
    skutofile.py -- A side script that I figure someone might find useful.  Pulls all skus and inventory levels from the store and prints it to a csv file with two columns sku and cooresponding inventory level. 
      
