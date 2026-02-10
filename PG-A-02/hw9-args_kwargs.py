# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
    {
        "ad":"Sadık Turan",
        "hesapNo": "12345",
        "bakiye": 20000,
        "ekHesap": 5000,
        "username":"sadikturan",
        "password":"1234"
    },
    {
        "ad":"Efe Turan",
        "hesapNo": "12345",
        "bakiye": 30000,
        "ekHesap": 10000,
        "username":"efeturan",
        "password":"1234"
    }
]

def menu(hesap):
    print("\n")

    print(f"merhaba, {hesap["ad"]}")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    else:
        print("yanlış seçim")

    menu(hesap)

def paraYatirma(hesap):
    pass

def bakiyeSorgula(hesap):
    print(f"bakiye: {hesap["bakiye"]}")
    print(f"ek bakiye: {hesap["ekHesap"]}")

def paraCekme(hesap):
    miktar = float(input("çekmek istediğiniz miktar: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimIzmi = input("ek hesap kullanılsın mı? (e/h): ")

            if ekHesapKullanimIzmi == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("paranızı alabilirsiniz")
            else:
                print("üzgünüz bakiyeniz yetersiz")
        else:
                print("üzgünüz bakiyeniz yetersiz")

def login():
    username = input("username: ")
    password = input("parola: ")

    isLoggedIn = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not(isLoggedIn):
        print("username yada parola yanlış")

login()





# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 

def yazdir(text, adet):
    return text * adet

# print(yazdir("Merhaba ", 5))

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    return f"alan: {alan} çevre: {cevre}"

sonuc = hesapla(3,5)
sonuc = hesapla(4,5)

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazı"
    
sonuc = yaziTura()

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if(sayi > 1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayilariBul(10,30)

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if(sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(20))
