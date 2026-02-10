students_dict = {
    '101':{
        "Ad":"Yigit",
        "Soyad":"Bilgi",
        "Dyili":2010,
        "Notlar":[40,80,90]
    },
    '102':{
        "Ad":"Ada",
        "Soyad":"Bilgi",
        "Dyili":2012,
        "Notlar":[80,80,80]
    },
    '103':{
        "Ad":"Cinar",
        "Soyad":"Turan",
        "Dyili":2017,
        "Notlar":[70,70,70]
    }
}

student_num = input("ogrenci numarasi giriniz: ")

notlar = students_dict[student_num]["Notlar"]
sum = 0 
for i in notlar:
    sum += i
average = sum/3

print(f"ogrencinin not ortalamasi: {average}")