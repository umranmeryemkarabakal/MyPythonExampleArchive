title = "Python ile Programlama Dersleri"

print("degisken icindeki toplam karakter sayisi: ", len(title))
print("degisken icerisindeki 'Python' kelimesi: ", title[0:6])
print("degiskenin ilk 5 ve son 5 karakteri: " + title[5] + "+" + title[-5])
print("degiskenin tersten yazilisi: ", title[-1])

input_name = input("ogrenci ismi giriniz: ")
input_first_grades = float(input("ilk notunuzu giriniz: "))
input_second_grades = float(input("ikinci notunuzu giriniz: "))

average_grades = (input_first_grades+input_second_grades) / 2

text = "{name} isimli ogrencinin 1.notu {first} 2. notu {second} ve ortalaması {average} olarak hesaplanmıştır".format(name = input_name,
                                                                                                                       first = input_first_grades,
                                                                                                                       second = input_second_grades,
                                                                                                                       average = average_grades)
print(text)