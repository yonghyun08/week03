from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.dbsparta
# db.users.insert_one({'name': 'ashely','age':28})
# db.users.insert_one({'name': 'tommy','age':30})
# db.users.insert_one({'name': 'eli','age':29})
# db.users.insert_one({'name': 'ashely','age':28})

all_users = list(db.users.find({}))
#print(all_users[0]['name'])

user = db.users.find_one({'name':'ashely'})
#print(user)

db.users.update_many({'name':'tommy'},{'$set':{'age':60}})
#print(all_users)

db.users.delete_many({'name':'ashely'})

