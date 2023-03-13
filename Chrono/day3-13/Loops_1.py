#Loops


condition =True
count = 1
while count < 10: #while Loop
    count += 1
    print("The condition is True")

items = [1,2,3,4,5]

for item in items:# for Loop
    print(item)


for index, item in enumerate(items):# Loop with enumerate fun which provide additional index of items in iteration
    if index == 2: #miss the item with index of 2, that is (index==2, item==3)
        continue
    print(index, item) 
     