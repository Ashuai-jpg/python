#List Compression

numbers = [1,2,3,4,5]
"""List Compression version"""
numbers_power_2 = [ n**2 for n in numbers]
print(numbers_power_2)

"""for loop version"""
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

"""math lambda version"""
numbers_power_2 = list(map(lambda n : n**2, numbers))
