x, y, name, isStudent = (1, 2.3, "Pınar", True)

#200/700
print("my name is {s} {n:5.4}".format(n=result, s=name))

# string methods
message = "hello world.i am student"
print(message) # hello world.i am student

list_message = message.split(".") 
print(list_message) # ['hello world', 'i am student']
new_message = " ".join(list_message)
print(new_message) # hello world i am student

new_message_1 = message.replace("student", "teacher") 
print(new_message_1) # hello world.i am teacher

new_message_2 = message.center(40)
print(new_message_2) #          hello world.i am student

new_message_3 = message.strip() # başındaki ve sonundaki boşlukları kaldırır
print(new_message_3) # hello world.i am student

new_message_4 = "   " +  message.lstrip() # sol kısımdaki boşlukları kaldırır
print(new_message_4) # hello world.i am student

new_message_5 = message.rstrip() + " " # sağ kısımdaki boşlukları kaldırır
print(new_message_5) # hello world.i am student

# 0, 9 arası indekste w karakterinin sayısı
print(message.count("w", 0, 10)) # 1

my_list = [1,2,3,4,5,6]
print(my_list) # [1, 2, 3, 4, 5, 6] 

del my_list[-3] 
print(my_list) # [1, 2, 3, 5, 6]

my_list.reverse() # listeyi tersine çevir
print(my_list) # [6, 5, 3, 2, 1]

sehirler = ["istanbul", "sakarya", "kocaeli"]
plakalar = [34,54,41]
print(plakalar[sehirler.index("sakarya")]) # 54
print(sehirler.index("sakarya")) # 1
print(plakalar[1]) # 54

plakalar =  {"istanbul":34, "sakarya":54, "kocaeli":41}
print(plakalar["istanbul"]) # 34

users = { 
    'umran' : {
        "id" : "111",
        "name" : "Umran",
        "surname" : "karabakal"
    },
    'meryem' : {
        "id" : "2",
        "name" : "Meryem",
        "surname" : "karabakal"
    }
}

print(users["umran"]["id"]) # 111
print(users["umran"]) # {'id': '111', 'name': 'Umran', 'surname': 'karabakal'}
print(users) # {'umran': {'id': '111', 'name': 'Umran', 'surname': 'karabakal'}, 'meryem': {'id': '2', 'name': 'Meryem', 'surname': 'karabakal'}}

# reference type
x = ["hello", "world"] 
y = ["hello", "world"]
x = y
y[1] = "python"
print(x[1]) # python


x = ["hello", "world"]
y = ["hello", "world"]
x = y
y = ["hello", "python"]
print(x, y) # ['hello', 'world'] ['hello', 'python']

x = 5
y = 10
x = y
y = 20
print(x,y) # 10 20

# value type
x = 5
y = 10
x = y
x = 20
print(x, y) # 20 10

values = 1,2,3,4,5
x, *y, z = values
print(x, y, z) # 1 [2, 3, 4] 5

nmbr = True + False + 8
print(nmbr) # 9

# identity operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x == y) # True
print(x == z) # True 

# adres karşılaştırmasıdır
print(x is y) # True
print(x is z) # False
print(y is not z) # True

# membership operator : in

x = ["apple","banana"]
print("apple" in x) # True
print("apple" not in x) # False


import datetime

tarih = "2025/1/12"
tarih = tarih.split('/') 
trafigeCikis = datetime.datetime(int(tarih[0]), int (tarih [1]), int (tarih [2])) 
simdi = datetime.datetime.now() 

fark = simdi - trafigeCikis

print(type(fark)) # <class 'datetime.timedelta'>
print(fark) # 5 days, 21:00:33.596757
days = fark.days
print(days) # 5

d = {"k1":1, "k2":2, "k3":3}

for key, value in d.items():
    print(key, value) # k1 1 , k2 2 , k3 3 


name = ' ' # False

while not name.strip():
    name = input("isim giriniz: ") # 
print(name)

urunler = []
adet = int(input("kac adet urun gireceksiniz: "))
i = 0

while i < adet:
    name = input("ürün ismi: ")
    price = input("ürün fiyatı: ")

    urunler.append({
        "name": name,
        "price": price})
    
    i +=1

for urun in urunler:
    print(urun["name"], urun["price"]) # apple 100 , banana 50

print(list(range(5,200,20))) # [5, 25, 45, 65, 85, 105, 125, 145, 165, 185]

gretting = "hello world"
for item in enumerate(gretting):
    print(item) 

"""
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
(5, ' ')
(6, 'w')
(7, 'o')
(8, 'r')
(9, 'l')
(10, 'd')
"""

list_1 = [1, 2, 3, 4, 5]
list_2 = ["a","b","c","d","e"]

print(list(zip(list_1, list_2))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

list_3 = [100,200,300,400,500]
for item in zip(list_1, list_2, list_3):
    print(item)

"""
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)
(4, 'd', 400)
(5, 'e', 500)
"""

# list comprehension
numbers = [ x for x in range(20) if x % 2 == 0]
print(numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

numbers = [ x if x%2==0 else "tek" for x in range(10)]
print(numbers) # [0, 'tek', 2, 'tek', 4, 'tek', 6, 'tek', 8, 'tek']

numbers = [x**2 for x in range(10)] 
print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

my_string = "meryem"
my_list = [letter for letter in my_string] # ['m', 'e', 'r', 'y', 'e', 'm']
print(my_list)

numbers = [x for x in range(3) for y in range(3)]
print(numbers) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers) 

"""
[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
"""
