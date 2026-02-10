# get ve set

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private değişken
        self.__age = age    # Private değişken

    # Getter (Okuma işlemi için)
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter (Değiştirme işlemi için)
    def set_age(self, new_age):
        if new_age > 0:  # Yaş negatif olamaz
            self.__age = new_age
        else:
            print("Hata: Yaş negatif olamaz!")

# Kullanım
person = Person("Ahmet", 25)
print(person.get_name())  # Çıktı: Ahmet
print(person.get_age())   # Çıktı: 25

person.set_age(30)  # Yaşı güncelle
print(person.get_age())  # Çıktı: 30

person.set_age(-5)  # Hata verecek
