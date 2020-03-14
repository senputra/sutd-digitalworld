import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from datetime import datetime
from datetime import timedelta
#other type of timestamp is firestore.SERVER_TIMESTAMP

cred = credentials.Certificate("/Users/coconut/Project/sutd-digitalworld/src/services/serviceAccountKey.json")

# # firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dw-bk-1d.firebaseio.com'
# })

#-------------------------------------------------------------------------------------------------------------
##CLOUD

# mach_ref = firestore.client().collection('machine')
# blk59_washer_1_ref = mach_ref.document('blk59_washer_1')

# starttime = datetime.now().timestamp()
# endtime = starttime + 2400
# time_data = {'start_time': starttime , 'end_time': endtime}
# blk59_washer_1_ref.set({
#         'Availability': True
#         })
# blk59_washer_1_datalog_ref = blk59_washer_1_ref.collection('data_log')
# blk59_washer_1_datalog_no_ref = blk59_washer_1_datalog_ref.document('1')
# blk59_washer_1_datalog_no_ref.set(time_data)


#UPDATE

def update_availability_used(blocknumber,machine_type,ID): #blocknumber has to be in 'blk--'' format
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        doc_id_lst = docid.split('_')
        if blocknumber == doc_id_lst[0]:
            if machine_type.lower() == doc_id_lst[1]:
                if int(ID) == int(doc_id_lst[2]):
                    mach_ref.document(docid).update({
                        'Availability': 'False'
                    })
                    
update_availability_used('blk59', 'washer', 1)
            

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

update_datalog('blk59', 'washer', 1)



def finished_cycle(timenow):
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        query = mach_ref.document(docid).collection('data_log').where('end_time', '==', datetime.now().timestamp()).stream()
        for data in query:
            mach_ref.document(docid).update({
                'Availability': 'True'
            })

finished_cycle('i')       

    
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


get_available_mach('blk59', 'washer')



#-----------------------------------------------------------------------------------------------------------------------
##REALTIME

ref = db.reference()

mach_ref = ref.child('machine')

blk59_washer_1_ref = mach_ref.child('blk59_washer_1')
blk59_washer_1_datalog_ref = blk59_washer_1_ref.child('data_log')
blk59_washer_1_datalog_no_ref = blk59_washer_1_datalog_ref.child('1')
starttime = datetime.now()
endtime = starttime + timedelta(seconds = 40*60)
blk59_washer_1_datalog_no_ref.set = ({
        'StartTime': starttime ,
        'EndTime': endtime
        })
blk59_washer_1_ref.push().set({
        'Availability': True
        })


#UPDATE

def update_availability_used(blocknumber,machine_type,ID): #blocknumber has to be in 'blk--'' format
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        doc_id = str(doc.id)
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if machine_type.lower() == doc_id_lst[1]:
                if int(ID) == doc_id_lst[2]:
                    docid.update({
                        'Availability': False
                    })
            

def update_datalog(blocknumber,machine_type,ID):
    starttime = datetime.now
    if machine_type.lower() == 'washer':
        endtime = starttime + timedelta(seconds = 40*60)
    elif machine_type.lower() == 'dryer':
        endtime = starttime + timedelta(seconds = 30*60)
    data = {'start_time': starttime, 'end_time': endtime}
    
    docs = mach_ref.stream()
    for doc in docs:
        doc_id = str(doc.id)
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if machine_type.lower() == doc_id_lst[1]:
                if int(ID) == doc_id_lst[2]:
                    doc.collection('data_log').add(data) #add a document with data to 'data_log' collection (random id allocation)


def finished_cycle(timenow):
    """
    When the time now equals 
    """
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        done = []
        query = blk59_washer_1_datalog_ref.where('end_time', '==', datetime.now())
        done.append(query)
        if done != []:
            docid.update({
                    'Availability': True
                    })

    
#RETRIEVE
    
def get_available_mach(blocknumber, machine_type):
    query = mach_ref.where('availability', '==', True)
    all_avail_mach = list(query) ##i'm assuming that query returns all the documents' id
    avail_mach = []
    for doc_id in all_avail_mach: 
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if machine_type.lower() == doc_id_lst[1]:
                avail_mach.append(doc_id_lst[2])
                
    if avail_mach == []:
        return None
    else:
        return avail_mach
          
    

# firebase_admin.db.Query.order_by_key('washer')



