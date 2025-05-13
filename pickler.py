import pickle

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
# type(b) gives <class 'bytes'>;
cool_hash = hash(pickle.dumps(db))
cool_hash_2 = hash(pickle.dumps(db))
cool_hash = hash(3.2)
print(cool_hash)
# print(cool_hash_2)
