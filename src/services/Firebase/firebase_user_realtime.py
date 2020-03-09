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

# ref = db.reference()

# mach_ref = ref.child('machine')

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
    machines = machines.keys()
    for doc in docs:
        docid = doc.id
        doc_id_lst = docid.split('_')
        if blocknumber == doc_id_lst[0]:
            if machine_type.lower() == doc_id_lst[1]:
                if int(ID) == int(doc_id_lst[2]):
                    mach_ref.document(docid).update({
                        'Availability': 'False'
                    })

                    
test_dict = { "geeks" : 7, "for" : 1, "geeks" : 2 } 
lst = list(test_dict.keys())
# accessing 2nd element using keys() 
print (lst[1])
            

def update_datalog(blocknumber,machine_type,ID):
    time = datetime.now().timestamp()
    time_str = str(time)
    starttime = datetime.now().timestamp()
    if machine_type.lower() == 'washer':
        endtime = starttime + 2400
    elif machine_type.lower() == 'dryer':
        endtime = starttime + 1800
    data = {'start_time': starttime, 'end_time': endtime}
    
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        doc_id_lst = docid.split('_')
        if blocknumber == doc_id_lst[0]:
            if machine_type.lower() == doc_id_lst[1]:
                if int(ID) == int(doc_id_lst[2]):
                    mach_ref.document(docid).collection('data_log').document(time_str).set(data) #add a document with data to 'data_log' collection (random id allocation)

                    
                    
def finished_cycle(timenow):
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        query = mach_ref.document(docid).collection('data_log').where('end_time', '==', datetime.now().timestamp).stream()
        for data in query:
            mach_ref.document(docid).update({
                'Availability': 'True'
            })
    
    
#RETRIEVE
    
def get_available_mach(blocknumber, machine_type):
    docs = mach_ref.where('Availability', '==', 'True').stream()
    avail_mach = []
    for doc in docs: 
        docid = doc.id
        print(mach_ref.document(docid).get())
        doc_id_lst = docid.split('_')
        if blocknumber == doc_id_lst[0]:
            if machine_type.lower() == doc_id_lst[1]:
                avail_mach.append(doc_id_lst[2])
                
    if avail_mach == []:
        return 'None'
    else:
        return avail_mach