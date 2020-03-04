#!/usr/bin/env python
# coding: utf-8

# # Class Booking for backend
# 

# In[1]:


import firebase_admin
import time
import numpy as np
from firebase_admin import credentials
from firebase_admin import db

'''
structure:
        machine 
            mac_ID: string #string format: Location_Type_Machine number
                availability: boolean
                datalog: dictionary = {'start_timestamp': , 'end_timestamp'}     
                    
'''
class Booking:
    __root = None
    def __init__(self):
        # Vectorizing all fucntions to perform action on multiple machines
        self.manage_Machine = np.vectorize(self.__manage_Machine)
        self.change_Availability = np.vectorize(self.__change_Availability)
        # Establishing connection to firebase RT Database
        
        while type(self.__root) == type(None): #modify to use try catch instead
            try:
                cred = credentials.Certificate("serviceAccountKey.json")
                firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://dw-bk-1d.firebaseio.com'
                })
                self.__root = db.reference().child("Machine")
                print(type(self.__root))
            except:
                print("serviceAccountKey.json is not setup properly")
                time.sleep(0.5)
                
    # Splice a full ID into substrings: Location, Type and No_ID
    def ID_splicer(self, full_ID):
        if type(full_ID) == list:
            Location= list()
            Type = list()
            ID = list()
            for string in full_ID:
                if type(string) != str:
                    raise Exception("Invalid argument, please use a list of IDs with only strings")
                    break
                else:
                    temp = string.split('_')
                    if len(temp) != 3:
                        raise Exception("Invalid ID formot, your ID format should be: Location_Type_No.ID ")
                    else:
                        Location.append(temp[0])
                        Type.append(temp[1])
                        ID.append(temp[2])
            Location = np.array(Location)
            Type = np.array(Type)
            ID = np.array(ID)
            return Location,Type, ID
        elif type(full_ID) == str:
            Location, Type, ID = full_ID.split('_')
            return Location, Type, ID

    
    # Retreiving existing machines from database            
    def __getMachines(self):
        machines = self.__root.order_by_key().get()
        if machines != None:
            machines = machines.keys()
        return machines
            
    # Adding/removing a machine 
    def __manage_Machine(self, edit: str, Location: str, Type: str, no_ID: str ): 
        # Managing Queries: 
        existing_Machine = self.__getMachines()
        mac_ID = Location + "_"  + Type + "_" + no_ID
        if edit == "del" and existing_Machine != None:
            # Deleting all machines with specified Type and Location
            if Location != "" and Type != "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Location) != -1 and machine.find(Type) != -1:
                        self.__root.child(machine).delete()
                        
            # Deleting all machines in specified Location
            elif Location != "" and Type == "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Location) != -1 :
                        self.__root.child(machine).delete()
            # Deleting all mmachines belong to specified Type    
            elif Location == "" and Type != "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Type) != -1:
                        self.__root.child(machine).delete()
                        
            # Deleting the machine with the specified full ID of Location_Type_ID 
            elif mac_ID in existing_Machine:
                self.__root.child(mac_ID).delete()
                #if mac_ID not in existing_Machine:
                #    print("deleted: ", mac_ID) # for debugging only
                
        elif edit == "add":
            if existing_Machine == None:
                    self.__root.child(mac_ID).child("availability").set(False)
                    self.__root.child(mac_ID).child("datalog").set("")
            elif mac_ID not in existing_Machine and Location != "" and Type != "" and no_ID != "":
                    self.__root.child(mac_ID).child("availability").set(False)
                    self.__root.child(mac_ID).child("datalog").set("")
        else:
            raise Exception("Invalid action. manage_Machine can only 'del' or 'add' machines ")
    
    # Change machine availability
    def __change_Availability(self, Location: str, Type: str, no_ID: str , status: bool):
        existing_Machine = self.__getMachines()
        mac_ID = Location + "_"  + Type + "_" + no_ID

        if status != False and status != True:
            raise Exception("Invalid value for machine availability")
        
        if existing_Machine != None:

            # Change availability all machines with specified Type and Location
            if Location != "" and Type != "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Location) != -1 and machine.find(Type) != -1:
                        self.__root.child(machine).child("availability").set(bool(status))
            
            # Change availability all machines with specified Location  
            elif Location != "" and Type == "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Location) != -1 :
                        self.__root.child(machine).child("availability").set(bool(status))
            
            # Change availability all machines with specified Type
            elif Location == "" and Type != "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Type) != -1:
                        self.__root.child(machine).child("availability").set(bool(status))
            
            # Change availability the machine with specified full ID of Location_Type_ID  
            elif mac_ID in existing_Machine:
                self.__root.child(mac_ID).child("availability").set(bool(status))
                
            else:
                raise Exception("Invalid ID. The specified machine ID does not exist")
        else:
            raise Exception("Fail to retrieve machines from firebase")


# # Warning!!! Only run this cell ONCE. If you fked up, restart kernel and clear outputs
# 

# In[2]:


a = Booking()


# # Sample code for usage of methods in class Booking(). Please read the comment lines for instructions to use the methods

# In[11]:


# Machine ID list, format of each ID is: Location_Type_ID
mac = ["Block57_Dryer_01", "Block57_Dryer_02", "Block57_Dryer_03", "Block55_Dryer_01", "Block55_Washer_01"]
# Splice the full IDs in the above list into Location, Type and ID lists
Loc, Type, ID = a.ID_splicer(mac)
print(Loc)
print(Type)
print(ID)

# Adding new machines
a.manage_Machine("add",Loc,Type, ID)


# # Debugging booking methods: U can pass in lists as arguments/parameters for all methods.

# In[12]:


# Run one method code line AT A TIME, uncomment the method u WANT to run

status = True # your status must be either True or False

# Change availability status of all machines in the machine ID list 
#a.change_Availability(Loc, Type, ID, status)

# Change availability status of all Washers in database
#a.change_Availability("", "Dryer", "", status)

# Change availability status of all machines in Block57
#a.change_Availability("Block57", "", "", status)

# Change availability status of all Dryers in Block 57
#a.change_Availability("Block57", "Dryer", "", status)

# Change availability status of  01 and 03 in block 57
dryer_57_ID = ["01","03"]
a.change_Availability("Block57", "Dryer", dryer_57_ID, status)


# In[13]:


# Run one method code line AT A TIME, uncomment the method u WANT to run

# Tip: After u have deleted successfully, u can re-run the a.manage_Machine() cell to re-add new machines 
# then run this cell again for debugging
# DEBUGGING: Run dele

# Delete all machines in the machine ID list
#a.manage_Machine("del",Loc,Type, ID)

# Delete all Washers in database
#a.manage_Machine("del","","Washer", "")

# Delete all Dryers in database
#a.manage_Machine("del","","Dryer", "")

# Delete all machines in Block57:
#a.manage_Machine("del","Block57","", "")

# Delete all Dryers in Block57:
#a.manage_Machine("del","Block57","Dryer", "")

#Delete Dryers 01 and 03 in Block57
dryer_57_ID = ["01","03"]
a.manage_Machine("del","Block57","Dryer", dryer_57_ID)


# In[ ]:




