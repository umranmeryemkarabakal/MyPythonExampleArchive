programlama_dilleri = ["python", "c", "c++", "matlab"]
sonuc = "python" in programlama_dilleri
print(sonuc)

sonuc = max(programlama_dilleri) # alfabetik olarak
print(sonuc)

sonuc = min(programlama_dilleri) # alfabetik olarak
print(sonuc)

programlama_dilleri.insert(0, "java")
print(programlama_dilleri)

programlama_dilleri.insert(-1, "javascript")
print(programlama_dilleri)

programlama_dilleri.insert(-2, "R")
print(programlama_dilleri)

programlama_dilleri.insert(len(programlama_dilleri), "go")
print(programlama_dilleri)

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
    },}
dict2list = students_dict["101"].items()
print("dict to list: ", dict2list)

students_dict.popitem()
print("son eklenen elemani silinmiş dict", students_dict)

ex_set = {"kizilelma", "akinci", "soloturk"}
print("ornek set: ", ex_set)
ex_set.update({"turkyildizlari"})
ex_set.discard("hurkuş")
ex_set.add("hurkus")
#ex_set.remove("f22")
print("guncellenmis ornek set: ", ex_set)

list1 = ["green", "black"]
list2 = ["green", "black"]

list1=list2

list1[0] = "white"

print(f"1.liste: {list1}, 2.liste: {list2}")

list1 = ["green", "black"]
list2 = list1.copy()
print(f"1.liste: {list1}, 2.liste: {list2}")

list1 = ["green", "black"]
list2 = list(list1)
print(f"1.liste: {list1}, 2.liste: {list2}")