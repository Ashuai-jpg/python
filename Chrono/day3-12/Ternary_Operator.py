def is_adult(age):
    return True if age > 18 else False

inputAge =  int(input("Enter your age: "))

if is_adult(inputAge):
    print("So you are an adult")
else:
    print("You are not an adult")