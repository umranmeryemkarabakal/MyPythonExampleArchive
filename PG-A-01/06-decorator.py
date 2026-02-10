# decorator fonksiyonları
# bir fonksiyon, başka bir fonksiyonun girdisi veya çıktısı olabilir.
def my_decoraqtor(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayGretting():
    print("greeting")

@my_decoraqtor
def sayHello():
    print("hello")


sayGretting = my_decoraqtor(sayGretting)
sayGretting()

sayHello()


import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):        
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)        
        finish = time.time()
        print("fonksiyon " + func.__name__  + " " + str(finish-start) + " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))   

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)