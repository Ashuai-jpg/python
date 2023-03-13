# def count():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         print(count)

#     increment()

# count() #output: 1
# count() #output: 1
# count() #output: 1

#closure in python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

increment = counter()


print(increment())
print(increment())
print(increment())
