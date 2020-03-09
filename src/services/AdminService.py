import firebase_admin
import time
import numpy as np
from firebase_admin import credentials
from firebase_admin import db
from helper import Logger
'''
structure:
        machine 
            mac_ID: string #string format: Location_Type_Machine number
                availability: boolean
                datalog: dictionary = {'start_timestamp': , 'end_timestamp'}     
                    
'''

class AdminService:
    __root = None
    _logger = None
    def __init__(self):
        self._logger = Logger.Logger()
        # Vectorizing all fucntions to perform action on multiple machines
        #self.change_Availability = np.vectorize(self.__change_Availability)
        self.add_machine = np.vectorize(self.__add_Machine, cache = True)
        self.delete_machine = np.vectorize(self.__del_Machine, cache = True)
        self.occupy_machine = np.vectorize(self.__occupy_machine, cache = True)
        self.undo_occupy_machine = np.vectorize(self.__undo_occupy_machine, cache = True)
        self.spoiled_machine = np.vectorize(self.__spoiled_machine, cache = True)
        # Establishing connection to firebase RT Database
        
        while type(self.__root) == type(None): #modify to use try catch instead
            try:
                cred = credentials.Certificate("/Users/coconut/Project/sutd-digitalworld/src/services/serviceAccountKey.json")
                firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://dw-bk-1d.firebaseio.com'
                })
                self.__root = db.reference().child("Machine")
                self._logger.log(type(self.__root))
            except:
                self._logger.log("serviceAccountKey.json is not setup properly")
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
    # Separate into add and delete functions
    def __del_Machine(self,  Location: str, Type: str, no_ID: str ): 
        # Managing Queries: 
        existing_Machine = self.__getMachines()
        mac_ID = Location + "_"  + Type + "_" + no_ID

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
            #    self._logger.log("deleted: ", mac_ID) # for debugging only
                
        
   
    def __add_Machine(self, Location: str, Type: str, no_ID: str):
        existing_Machine = self.__getMachines()
        mac_ID = Location + "_"  + Type + "_" + no_ID
        if existing_Machine == None:
                self.__root.child(mac_ID).child("availability").set(False)
                self.__root.child(mac_ID).child("datalog").set({"1": "a", "2": "b", "3":"c"})
        elif mac_ID not in existing_Machine and Location != "" and Type != "" and no_ID != "":
                self.__root.child(mac_ID).child("availability").set(False)
                self.__root.child(mac_ID).child("datalog").set({"1": "a", "2": "b", "3":"c"})        
    
    #Change machine availability
    def __change_Availability(self, Location: str, Type: str, no_ID: str , status: str):
        existing_Machine = self.__getMachines()
        mac_ID = Location + "_"  + Type + "_" + no_ID

        
        if existing_Machine != None:

            # Change availability all machines with specified Type and Location
            if Location != "" and Type != "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Location) != -1 and machine.find(Type) != -1:
                        self.__root.child(machine).child("availability").set(str(status))
            
            # Change availability all machines with specified Location  
            elif Location != "" and Type == "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Location) != -1 :
                        self.__root.child(machine).child("availability").set(str(status))
            
            # Change availability all machines with specified Type
            elif Location == "" and Type != "" and no_ID == "":
                for machine in existing_Machine:
                    if machine.find(Type) != -1:
                        self.__root.child(machine).child("availability").set(str(status))
            
            # Change availability the machine with specified full ID of Location_Type_ID  
            elif mac_ID in existing_Machine:
                self.__root.child(mac_ID).child("availability").set(str(status))
                
            else:
                raise Exception("Invalid ID. The specified machine ID does not exist")
        else:
            raise Exception("Fail to retrieve machines from firebase")
    
    # Clear latest datalog
    def __clear_latest_datalog(self, Location: str, Type: str, no_ID: str):
        #Search for the latest 
        existing_Machine = self.__getMachines()
        mac_ID = Location + "_"  + Type + "_" + no_ID
        
        if Location != "" and Type != "" and no_ID == "":
            for machine in existing_Machine:
                if machine.find(Location) != -1 and machine.find(Type) != -1:  
                    latest_attempt = list(self.__root.child(machine).child("datalog").order_by_key().limit_to_last(1).get().keys())
                    self._logger.log(latest_attempt)
                    self.__root.child(machine).child("datalog").child(latest_attempt[0]).delete()
                    
        elif Location != "" and Type == "" and no_ID == "":
            for machine in existing_Machine:
                if machine.find(Location) != -1 :
                    latest_attempt = list(self.__root.child(machine).child("datalog").order_by_key().limit_to_last(1).get().keys())
                    self._logger.log(latest_attempt)
                    self.__root.child(machine).child("datalog").child(latest_attempt[0]).delete()
                    
        elif Location == "" and Type != "" and no_ID == "":
            for machine in existing_Machine:
                self._logger.log(machine)
                if machine.find(Type) != -1:
                    latest_attempt = list(self.__root.child(machine).child("datalog").order_by_key().limit_to_last(1).get().keys())
                    self._logger.log(latest_attempt)
                    self.__root.child(machine).child("datalog").child(latest_attempt[0]).delete()
        
        elif mac_ID in existing_Machine:
            latest_attempt = list(self.__root.child(mac_ID).child("datalog").order_by_key().limit_to_last(1).get().keys())
            self._logger.log(latest_attempt)
            self.__root.child(mac_ID).child("datalog").child(latest_attempt[0]).delete()
    
    # Occupy the machine, set availability = "True"
    def __occupy_machine(self, Location: str, Type: str, no_ID: str):
        self.__change_Availability(Location, Type, no_ID , "True")
    
    # Unoccupy the machine, set availability = "False"
    def __undo_occupy_machine(self, Location: str, Type: str, no_ID: str):
        self.__clear_latest_datalog(Location, Type, no_ID)
        self.__change_Availability(Location, Type, no_ID , "False")
    
    # Setting machines to spoiled state
    def __spoiled_machine(self, Location: str, Type: str, no_ID: str):
        self.__change_Availability(Location, Type, no_ID , "Spoiled")