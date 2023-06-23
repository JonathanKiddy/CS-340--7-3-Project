from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31093
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.(Create)
    def create(self, data):
        if data is not None:
            # Inserts data
            self.database.animals.insert_one(data)  
            return True
        
        else:
            #Exception
            raise Exception("Cannot save, because parameter is empty")
            return False
        
# Create method to impement the R in CRUD.(Read)  
    def read_all(self, data):
        cursor = self.database.animals.find(data, {"_id" : False} ) 
        #Return cursor that points to the documnets
        return cursor
    
    def read(self, data):
        #Return document as a dictonary
        return self.database.animals.find(data) 
    
# Create method to impement the U in CRUD.(Update)
    def update(self, data, updateData):
        if data is not None:
            result = self.database.animals.update_many(data, { "$set" : updateData })
            
        else:
            return "{}"
        print ("Data has been Updated")
        return result.raw_result
        
# Create method to impement the D in CRUD.(Delete) 
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
            
        else:
            return "{}"
        print ("Data Deleted")
        return result.raw_result