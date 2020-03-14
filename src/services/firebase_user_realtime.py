import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dw-bk-1d.firebaseio.com'
})

ref = db.reference()

mach_ref = ref.child('Machine')
                 
  

'''
    input are all strings
    blocknumber --- 'block55' or 'block57' or 'block59'
    machine_type --- 'washer' or 'dryer'
    ID --- '01', '02', ..., '14', ...
    
'''

          
def update_datalog(blocknumber,machine_type,ID): 
    time = datetime.now().timestamp()
    time_str = str(int(time))
    starttime = datetime.now().timestamp()
    if machine_type.lower() == 'washer':
        endtime = starttime + 2400
    elif machine_type.lower() == 'dryer':
        endtime = starttime + 1800
    data = {'start_time': starttime, 'end_time': endtime}
    
    machines = mach_ref.order_by_key().get()
    machines = list(machines)
    for mac_ID in machines:
        machine_details = mac_ID.split('_')
        if blocknumber == machine_details[0]:
            if machine_type == machine_details[1]:
                if ID == machine_details[2]:
                    mach_ref.child(mac_ID).child("datalog").child(time_str).set(data) #add a document with data to 'data_log' collection (random id allocation)

#update_datalog('Block55', 'Washer', '01')                    
          

    
def get_available_mach(blocknumber, machine_type):
    machines_availability = {'True': {}, 'False': {}, 'Spoiled': {}}
    avail_mach = []
    unavail_mach = []
    spoiled_mach = []
    machines = mach_ref.order_by_key().get()
    machines = list(machines) 
    for mac_ID in machines: 
        availability = mach_ref.child(mac_ID).order_by_child('availability').get().items()
        key, val = availability
        machine_details = mac_ID.split('_')
        if blocknumber == machine_details[0]:
            if machine_type == machine_details[1]:
                if key[1] == 'True':
                    avail_mach.append(machine_details[2])
                    
                elif key[1] == 'Spoiled':
                    spoiled_mach.append(machine_details[2])
                    
                elif key[1] == 'False':
                    unavail_mach.append(machine_details[2])
                    
    machines_availability['True'] = avail_mach
    machines_availability['False'] = unavail_mach
    machines_availability['Spoiled'] = spoiled_mach
   
    return machines_availability
    
#get_available_mach('Block57', 'Dryer')


