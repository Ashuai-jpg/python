#map() , filter(), reduce()
from functools import reduce

numbers = [1,2,3,4,5,6]

def double(a):
    return a * 2

double = lambda a : a * 2
isEven = lambda n : n % 2 ==0
result1 = map(double, numbers)
result2 = map(lambda a : a * 2, numbers)
result3 = filter(isEven, numbers)
print(list(numbers))
print(list(result1))
print(f"Filterd list :{list(result3)}")



#reduce()

expenses = [
    ("Dinner", 90),
    ("Car repair", 120)
]

# no reduce added
# sum1 = 0
# for expense in expenses:
#     sum += expense[1]

sum2 = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum2)