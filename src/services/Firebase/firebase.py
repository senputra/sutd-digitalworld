import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from datetime import datetime
from datetime import timedelta
#other type of timestamp is firestore.SERVER_TIMESTAMP

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()



machine_ref = db.collection('Machine')

machine_type_washer_ref = machine_ref.document('Washer')
washer_numbers_ref = machine_type_washer_ref.collection('No.')
washer_01 = washer_numbers_ref.document('01')
washer_01.set({
        'ID': '57/01',  #Constant
        'StartTime': datetime.now(),
        'EndTime': datetime.now() + timedelta(seconds = 37*60),
        'Used': False
        })
washer_02 = washer_numbers_ref.document('02')
washer_02.set({
        'ID': '59/01',  #Constant
        'StartTime': datetime.now(),
        'EndTime': datetime.now() + timedelta(seconds = 37*60),
        'Used': False
        })
washer_03 = washer_numbers_ref.document('03')
washer_03.set({
        'ID': '57/03'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 37*60)
        'Used': False
        })
washer_04 = washer_numbers_ref.document('04')
washer_04.set({
        'ID': '57/02'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 37*60)
        'Used': False
        })
washer_05 = washer_numbers_ref.document('05')
washer_05.set({
        'ID': '55/01'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 37*60)
        'Used': False
        })

machine_type_dryer_ref = machine_ref.document('Dryer')
dryer_numbers_ref = machine_type_dryer_ref.collection('No.')
dryer_01 = dryer_numbers_ref.document('01')
dryer_01.set({
        'ID': '57/01'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 30*60)
        'Used': False
        })
dryer_02 = dryer_numbers_ref.document('02')
dryer_02.set({
        'ID': '57/02'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 30*60)
        'Used': False
        })
dryer_03 = dryer_numbers_ref.document('03')
dryer_03.set({
        'ID': '59/01'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 30*60)
        'Used': False
        })
dryer_04 = dryer_numbers_ref.document('04')
dryer_04.set({
        'ID': '59/02'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 30*60)
        'Used': False
        })
dryer_05 = dryer_numbers_ref.document('05')
dryer_05.set({
        'ID': '57/05'  #Constant
        'StartTime': datetime.now()
        'EndTime': datetime.now() + timedelta(seconds = 30*60)
        'Used': False
        })


#UPDATE

def update_use(machine_type,ID):
    
    if lower(machine_type) == 'washer':
        for i in list(washer_numbers_ref.get()): #get document(e.g. washer_01, washer_02)
            i_dict = i.get()                     #get dictionary from document
            if i_dict.get('ID') == str(ID):
                i.dict['StartTime'] = datetime.now()
                i.dict['EndTime'] = datetime.now() + timedelta(seconds = 37*60)
                i.dict['Used'] = True
                break
            
    elif lower(machine_type) == 'dryer':
        for i in list(dryer_numbers_ref.get()): #get document(e.g. dryer_01, dryer_02)
            i_dict = i.get()                     #get dictionary from document
            if i_dict.get('ID') == str(ID):
                i.dict['StartTime'] = datetime.now()
                i.dict['EndTime'] = datetime.now() + timedelta(seconds = 30*60)
                i.dict['Used'] = True
                break
            
    return 'Thanks for Using'


def finished_cycle(timenow):
    ## how do i do this -.-
    
    
#RETRIEVE INFO
    
def mach_not_in_use(machine_type, location):
    
    if lower(machine_type) == 'washer':
        for i in list(washer_numbers_ref.get()): #get document(e.g. washer_01, washer_02)
            i_dict = i.get()                     #get dictionary from document
            if int(i_dict['ID'][:2]) == int(location):                
                not_used_lst = []
                if i_dict.get('Used') == False:
                    not_used_lst.append(i.dict['ID'])
                    
        return not_used_lst
                    
    elif lower(machine_type) == 'dryer':
        for i in list(dryer_numbers_ref.get()): #get document(e.g. dryer_01, dryer_02)
            i_dict = i.get()                     #get dictionary from document
            if int(i_dict['ID'][:2]) == int(location):
                not_used_lst = []
                if i_dict.get('Used') == False:
                    not_used_lst.append(i.dict['ID'])
                    
        return not_used_lst
                    
    if not_used_lst == []:  ## Can i do this?
        return 'All Machines Are Used'            
 
data_log = .document('data_log')               
'StartTime': datetime.now()
'EndTime': datetime.now() + timedelta(seconds = 30*60)    
            
    
#     

# washer_no.update({
#     u'Status': u'used'
# })

# dryer_no.update({
#     u'Status': u'not used'
# })

# firebase_admin.db.Query.order_by_key('washer')



