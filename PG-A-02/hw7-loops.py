numbers = [3, 5, 7, 2, 12, 32, 45]

sum=0
for i in numbers:
    print(i)
    if i%3==0:
        print("{i} 3e tam bolunur.")
    sum +=i

urunler = ["samsung s24", "samsung s22", "iphone 15", "iphone 14"]

index = 0
for i in urunler:
    print(i)
    if i.find("samsung") >-1:
        index +=1

print(f"{index} tane samsung marka telefon var")





urunler = [
    {"urunAdi": "Hp Victus 1", 
     "fiyat": 32999},
    {"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi":"Apple Macbook", "fiyat": 49999}, 
    {"urunAdi":"Huawei Matebook", "fiyat": 26999},
    {"urunAdi":"Casper Nirvana", "fiyat": 20000},
    {"urunAdi": "Hp Victus 2", 
     "fiyat": 42999},
]

key = input("fiyatini gormek istediginiz urun anahtarini giriniz: ")

sum = 0
for i in urunler:
    print(f"{i["urunAdi"]} marka bilgisayar {i["fiyat"]} fiyatindadir")

    sum += int(i["fiyat"])

    if i["fiyat"] >= 25000 and i["fiyat"] < 40000:
        print(f"{i["urunAdi"]} belirtilen fiyat araligindadir")

    if i["urunAdi"].lower().find(key.lower() ) > -1 :
        print(f"bulunan modeller: {i['urunAdi']}")

print("toplam fiyat: ", sum)







start = int(input("baslangic degerini giriniz: "))
end = int(input("bitis degerini giriniz: "))

while start <= end:
    if start %2==0:
        print(start)
    start +=1

val = 100
while val>=1:
    print(val)
    val -= 1

"""
numbers = [int(input(f"{i+1}. sayıyı giriniz: ")) for i in range(5)]
"""


my_list = []
i = 1
while i <= 5:
    num = int(input(f"{i}. sayıyı giriniz: "))
    my_list.append(num)
    i += 1
sort_list = sorted(my_list)

print("Girilen sayılar:", sort_list)

username = ""

while not username:
    username = input("kullanici adi giriniz: ")

print("kullanici adi: ", username)

""
add = "y"
students = []
while add == "y":
    studentNo = input("ogrenci no: ")
    studentName= input("ogrenci adi: ")
    studentSurname = input("ogrenci soyadi: ") 

    students.append({
        "studentNo": studentNo,
        "studentName": studentName,
        "studentSurname": studentSurname
    })

    add = input("ogrenci eklemeye devam edilsin mi ? ")

for student in students:
    print(f"{student['ogrenciNo']} numarali ogrencinin adi: {student['studentName']}, soyadi: {student['studentSurname']}")


