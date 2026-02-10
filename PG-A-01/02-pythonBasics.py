
sayi = int(input("Bir sayı giriniz: "))

if sayi == 1:
    asalmi = False

else: 
    for i in range(2,sayi):
        if sayi % i == 0:
            asalmi = False
            break
    else:
        asalmi = True

if asalmi:
    print("Asal")
else:
    print("Asal degil")

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi %i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(12)) # [2, 3, 4, 6]

def square(num): return num **2

numbers = [1,3,5,7,9,11,13]

for item in map(square, numbers):
    print(item)

"""
1
9
25
49
81
121
169
"""

#list(map(square, numbers))
print(result) # [1, 9, 25, 49, 81, 121, 169]

#list(map(lambda num: num**2, numbers))
print(result)    # [1, 9, 25, 49, 81, 121, 169]

square = lambda num: num**2
print(square(5)) # 25

def check_even(num): return num % 2 == 0

numbers = [12, 51, 25, 76, 41, 27, 98]
#list(filter(check_even, numbers))
print(result) # [12, 76, 98]

check_even = lambda num: num % 2 == 0
#list(filter(lambda num: num % 2 == 0, numbers))
print(result) # [12, 76, 98]



mylist = [1,2,3]
myString = 'my string'

print(len(mylist)) # 3
print(len(myString)) # 9
print(type(mylist)) # <class 'list'>
print(type(myString)) # <class 'strs'>

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('film objesi silindi')

m = Movie('film adı','yönetmen adı',120)

print(str(mylist))
print(str(m))
print(len(mylist))
print(len(m))

