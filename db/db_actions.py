from pymongo import MongoClient
import os
from pprint import pprint
class mongoActions:

    def __init__(self,collectionection):
        self.client = MongoClient(serverSelectionTimeoutMS=1)
        self.db=self.client.test_database
        self.collection = self.db[collectionection]
        self.yes = {'yes','y', 'ye'}

    def getConnection(self):
        os.system('clear')
        print("Check connection...")
        try:
            self.client.server_info()
            return True
        except:
            return False

    def showUser(self):
        """Search an users by name"""
        os.system('clear')
        if self.collection.count() > 0:
            self.name = input("Who are you looking for? Insert a name: ")
            print(self.collection.find_one({"name": self.name}))
        else:
            print("There's no one in this collectionection!")
        print("\n\n\n")


    def insertUser(self):
        """Insert a new user"""
        os.system('clear')
        self.name = input("InsertName: ")
        try:
            self.collection.insert({"name": self.name})
            print("User added correctly!")
        except Exception as e:
            print(e)
        print("\n\n\n")


    def showAllUsers(self):
        """Find all user in the collectionection"""
        os.system('clear')
        if self.collection.count() > 0:
            print("Users found:")
            for item in self.collection.find():
                pprint(item)
        else:
            print("No user found")

        print("\n\n\n")


    def deleteUser(self):
        """Delete an user by the name"""
        os.system('clear')
        if self.collection.count() > 0:
            self.name = input("Who would you remove?")
            try:
                self.collection.remove({"name": self.name})
                print("User remove correctly!")
            except Exception as e:
                print(e)
        else:
            print("You can't remove. The collectionection is empty.")

        print("\n\n\n")


    def countUsers(self):
        """Returns the count of document inside Users"""
        os.system('clear')
        self.countUser = self.collection.count()
        if self.countUser > 0:
            print("\nThere's {0} user/s".format(self.collection.count()))
        else:
            print("No user found...")

        print("\n\n\n")

    def updateUserItem(self):
        """Update the data of a user"""
        os.system('clear')
        self.name = input("Who needs to be upgraded?")
        if len(self.collection.find({"name":self.name}))>0:
            self.collection.update({"name": self.name},{$set:{"su"}})




    def dropcollectionection(self):
        """Delete the collectionection"""
        os.system('clear')
        self.choice = input("Are you sure?").lower()
        if self.choice in self.yes:
           try:
               self.collection.remove()
               print("collectionection Removed")
           except:
               print("Error collectionection not removed")
        else:
            pass
