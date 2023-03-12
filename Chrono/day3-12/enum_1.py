from enum  import Enum

#To declare a consonant
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(list(State)) 
print(len(State)) 
print(State.ACTIVE.value)
