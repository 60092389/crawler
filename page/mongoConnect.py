'''
Created on 2017. 7. 25.

@author: dslc
'''

import pymongo


connection = pymongo.MongoClient('192.168.1.28', 27017)
db = connection.gaduda
#collection = db.crawling_furniture
collection = db.fur_test