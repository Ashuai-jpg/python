#lists in short

items = ["Roger",  "damn"]
items[1] = '2' # change the second item in the list to a new value

items.append('shit')
items.extend(['banana'])
items += ["End"] 
items += "Final" #this will append every single letter as a individual item in the list


items.insert(0,'insert_from_0') #add 1 item at a specific index
items[1:1] = ['mutiple_add_1','mutiple_add_2'] #add mutiple items at a specific index

items.sort(key=str.lower)# after this line of code the '.sort()' function will modify the original list
sorted(items, key=str.lower)# While this will no longer modify the original item in the list 


print(items)
print("2" in items)