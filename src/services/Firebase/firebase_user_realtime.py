import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from datetime import datetime
from datetime import timedelta
#other type of timestamp is firestore.SERVER_TIMESTAMP

cred = credentials.Certificate("serviceAccountKey.json")

# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dw-bk-1d.firebaseio.com'
# })

ref = db.reference()

mach_ref = ref.child('Machine')

# blk59_washer_1_ref = mach_ref.child('blk59_washer_1')

# starttime = datetime.now().timestamp()
# endtime = starttime + 2400
# time_data = {'start_time': starttime , 'end_time': endtime}
# blk59_washer_1_ref.set({
#         'Availability': 'True'
#         })

# blk59_washer_1_ref.push('data_log').set({
#         '1': one
#         })

# blk59_washer_1_datalog_ref = blk59_washer_1_ref.child('data_log')
# blk59_washer_1_datalog_no_ref = blk59_washer_1_datalog_ref.child('1')
# blk59_washer_1_datalog_no_ref.set(time_data)


#UPDATE

def update_availability_used(blocknumber,machine_type,ID): #blocknumber has to be in 'blk--'' format
    machines = mach_ref.keys()
    machines = list(machines)
    for mac_ID in machines:
        machine_details = mac_ID.split('_')
        if blocknumber == machine_details[0]:
            if machine_type.lower() == machine_details[1]:
                if int(ID) == int(machine_details[2]):
                    mach_ref.child(mac_ID).update({
                        'Availability': 'False'
                    })

                    
            

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

update_datalog('Block55', 'Washer', '01')                    
                    
# def finished_cycle(timenow):
#     machines = machines.keys()
#     machines = list(machines)
#     for mac_ID in machines:
#         machine_details = mac_ID.split('_')
#         query = mach_ref.document(docid).collection('data_log').where('end_time', '==', datetime.now().timestamp).stream()
#         for data in query:
#             mach_ref.child(mac_ID).update({
#                 'Availability': 'True'
#             })
    
    
#RETRIEVE
    
def get_available_mach(blocknumber, machine_type):
    avail_mach = []
    machines = mach_ref.order_by_key().get()
    machines = list(machines) 
    for mac_ID in machines: 
        availability = mach_ref.child(mac_ID).order_by_child('availability').get().items()
        key, val = availability
        if key[1] == True:
            machine_details = mac_ID.split('_')
            avail_mach.append(machine_details[2])
                
    if avail_mach == []:
        return 'None'
    else:
        return avail_mach
    
get_available_mach('Block55', 'Washer')
    
    