import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from datetime import datetime
from datetime import timedelta
#other type of timestamp is firestore.SERVER_TIMESTAMP

cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)


#-------------------------------------------------------------------------------------------------------------
##CLOUD
db = firestore.client()

machine_ref = db.collection('machine')
#test if can be added to firestore -- cannott
mach_ref = db.collection('machine')
blk59_washer_1_ref = mach_ref.document('blk59_washer_1')

starttime = datetime.now()
endtime = starttime + timedelta(seconds = 40*60)
time_data = {'StartTime': starttime , 'EndTime': endtime}
blk59_washer_1_ref.set({
        'Availability': True
        })
blk59_washer_1_datalog_ref = blk59_washer_1_ref.collection('data_log')
blk59_washer_1_datalog_no_ref = blk59_washer_1_datalog_ref.document('1')
blk59_washer_1_datalog_no_ref.set(time_data)



mach_ref.document('blk59_washer_1').set({
        'Availability': True
        }).then(function() {
    console.log("Collection added to Firestore!");
    var promises = [];
    promises.push(firebase.firestore().collection().doc().collection().doc().set());
    ;
    Promise.all(promises).then(function() {
      console.log("All subcollections were added!");
    })
    .catch(function(error){
      console.log("Error adding subcollections to Firestore: " + error);
    });
  })
  .catch(function(error){
    console.log("Error adding document to Firestore: " + error);
  });


#UPDATE

def update_availability_used(blocknumber,machine_type,ID): #blocknumber has to be in 'blk--'' format
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        doc_id = str(doc.id)
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if  lower(machine_type) == doc_id_lst[1]:
                if int(ID) == doc_id_lst[2]:
                    docid.update({
                        'Availability': False
                    })
            

def update_datalog(blocknumber,machine_type,ID):
    starttime = datetime.now
    if lower(machine_type) == 'washer':
        endtime = starttime + timedelta(seconds = 40*60)
    elif lower(machine_type) == 'dryer':
        endtime = starttime + timedelta(seconds = 30*60)
    data = {'start_time': starttime, 'end_time': endtime}
    
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        doc_id = str(doc.id)
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if lower(machine_type) == doc_id_lst[1]:
                if int(ID) == doc_id_lst[2]:
                    doc.collection('data_log').add(data) #add a document with data to 'data_log' collection (random id allocation)


def finished_cycle(timenow):
    ## how do i do this -.-
    

    
#RETRIEVE
    
def get_available_mach(blocknumber, machine_type):
    query = mach_ref.where('availability', '==', True)
    all_avail_mach = lst(query) ##i'm assuming that query returns all the documents' id
    avail_mach = []
    for doc_id in all_avail_mach: 
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if lower(machine_type) == doc_id_lst[1]:
                avail_mach.append(doc_id_lst[2])
                
    if avail_mach == []:
        return None
    else:
        return avail_mach



#-----------------------------------------------------------------------------------------------------------------------
##REALTIME
ref = db.reference(...)

mach_ref = ref.child('machine')

blk59_washer_1_ref = mach_ref.child('blk59_washer_1')
blk59_washer_1_datalog_ref = blk59_washer_1_ref.child('data_log')
blk59_washer_1_datalog_no_ref = blk59_washer_1_datalog_ref.child('1')  ##doesnt add collection to document --- also couldnt add document to collection??
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
            if  lower(machine_type) == doc_id_lst[1]:
                if int(ID) == doc_id_lst[2]:
                    docid.update({
                        'Availability': False
                    })
            

def update_datalog(blocknumber,machine_type,ID):
    starttime = datetime.now
    if lower(machine_type) == 'washer':
        endtime = starttime + timedelta(seconds = 40*60)
    elif lower(machine_type) == 'dryer':
        endtime = starttime + timedelta(seconds = 30*60)
    data = {'start_time': starttime, 'end_time': endtime}
    
    docs = mach_ref.stream()
    for doc in docs:
        docid = doc.id
        doc_id = str(doc.id)
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if lower(machine_type) == doc_id_lst[1]:
                if int(ID) == doc_id_lst[2]:
                    doc.collection('data_log').add(data) #add a document with data to 'data_log' collection (random id allocation)


def finished_cycle(timenow):
    ## how do i do this -.-
    

    
#RETRIEVE
    
def get_available_mach(blocknumber, machine_type):
    query = mach_ref.where('availability', '==', True)
    all_avail_mach = lst(query) ##i'm assuming that query returns all the documents' id
    avail_mach = []
    for doc_id in all_avail_mach: 
        doc_id_lst = doc_id.split('_')
        if int(blocknumber) == int(doc_id_lst[0]):
            if lower(machine_type) == doc_id_lst[1]:
                avail_mach.append(doc_id_lst[2])
                
    if avail_mach == []:
        return None
    else:
        return avail_mach
          
    

# firebase_admin.db.Query.order_by_key('washer')



