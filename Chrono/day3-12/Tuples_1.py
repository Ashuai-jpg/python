#Tuples
names = ("Roger", "Guy","JB")

#useful cases
names[-1] #get the item in Tuple by index
names.index("Roger") #get the index in Tuple using ".index("item")"
len(names) #get the length of a Tuples

print("Roger" in names)
print(sorted(names))
newTuple = names + ("Jin", "Ping", 2952, True)
print(newTuple)