import pickle
'''student1 = ["Raushan", "Rakesh","Jyoti", "Rekha"]
file_object=open('Student.dat', 'ab')
pickle.dump(student1,file_object)
file_object.close()'''

f = open('Student.dat', 'rb')
r = pickle.load(f)
print(r)
