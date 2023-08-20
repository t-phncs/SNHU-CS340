#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class DatabaseLayer(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
       	USER = 'aacuser1'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31284
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    
        
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
            
            # Complete this create method to implement the R in CRUD

    def read(self, data=None):
        if data is not None:
            find = self.database.animals.find(data,{"_id":False})
            #for query in find:
            	#pprint.pprint(query)
            	#print(query)
        else:
            find = self.database.animals.find({},{"_id":False})
            #raise Exception("Nothing to find, because data parameter is empty")
        return find
        
    
    def update(self, data, new_data):
        if data is not None:
            result = self.database.animals.update_many(data, {"$set": new_data})
            print("updated successful!")
        else:
            return "{}"
        print(result.raw_result())
    
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            print("deleted successful!")
        else:
            return "{}"
        print(result.raw_result())
        
    
  
        
    
        
    







