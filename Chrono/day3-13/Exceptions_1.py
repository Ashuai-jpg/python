#Exceptions
import os

# try:
#     """some lines of code"""
# except<ERROR1>:
#     """handler <EOFError>"""
# except<ERROR2>:
#     """ERROR2"""
# else:
#     """no exceptions were raised, the code ran successfully"""
# finally:
#     """do something in any case"""

try:    
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divede by zero')
finally:
    result = 1

print(result) #1 


"""costomize your exceptions"""
try:
    raise Exception('An error') #raise an exception intentionally
except Exception as error:
    print(error)


class DogNotFoundException(Exception):
    print("inside")
    pass
try:
    raise DogNotFoundException() #raise an exception intentionally
except DogNotFoundException:
    print("Dog not found")

def working_with_file():
    name = os.path.abspath(__file__) #get the absolute filename with path preceded
    print(name)
    try:
        file = open(name, 'r')
        content = file.read()
        print(content)
    finally:
        file.close()

working_with_file()

