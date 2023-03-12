#Dictionaries
dog = {
    "name": "Guy_z",
    "age" : 22,
    "Job" : "Backend Developer",
    "hobby": "Oshi"
}

#some essentials
dog["age"] = 23 #Change the value of a item or add a new item while there is no such.
del dog["hobby"] 
dog.copy() #Just a copy of Dic.
print(dog)
print(dog["age"])
print("color" in dog) #output: False

#get the keys in the Dictionaries and also can get the value by swap the "key" to "value". Ooutput: dict_keys(['name', 'age', 'Job', 'hobby'])
print(dog.keys()) 
print("keys are:"+ str(list(dog.keys()))) #pure keys in Bracket.

#get the value by passing the key and it will return a default value if there is no such.
print(dog.get("hobby", "Zhuang Bomb")) 