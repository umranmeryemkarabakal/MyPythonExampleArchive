import math

value = math.floor(5.9)
print(value) # 5
value = math.ceil(5.9)
print(value) # 6

import random
names = ["a", "b", "c", "d", "e"]
#random.choice(names)
print(result) # ~d

#random.sample(names, 2)
print(result) # ~['c', 'e']

sayHello = "hello"
del sayHello
#print(sayHello)

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)
try:
    print(factorial("4"))
except Exception as ex:
    print(ex)

    