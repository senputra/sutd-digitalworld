import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from datetime import datetime
from datetime import timedelta

cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred)

db = firestore.client()



washer_ref = db.collection(u'machine').document(u'washer')

washer_no = washer_ref.collection(u'identity').document(u'01')
washer_no.set({
    u'Status': u'input',
    u'Time': firestore.SERVER_TIMESTAMP,
    u'EndTime': datetime.now() + timedelta(seconds=2220)
})





dryer_ref = db.collection(u'machine').document(u'dryer')


dryer_no = dryer_ref.collection(u'identity').document(u'01')
dryer_no.set({
    u'Status': u'input',
    u'Time': firestore.SERVER_TIMESTAMP,
    u'EndTime': datetime.now() + timedelta(seconds=1800)
})



washer_no.update({
    u'Status': u'used'
})

dryer_no.update({
    u'Status': u'not used'
})

firebase_admin.db.Query.order_by_key('washer')