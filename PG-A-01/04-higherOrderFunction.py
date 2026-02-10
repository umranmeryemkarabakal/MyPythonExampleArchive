# fonksiyondan fonksiyon gönderme

def usal(number):
    # two = usal(2)
    # three = usal(3)

    def inner(power):
        return number ** power

    return inner


two = usal(2) # number = 2
three = usal(3) # number = 3
print(two) # <function usal.<locals>.inner at 0x000001C7F6F99240>

#two(3) # power = 3 
print(result) # 8
#three(4) # power = 4
print(result) # 81

def yetki_sorgula(page):
    def inner(role):
        if role == 'admin':
            return "{0} rolünün {1} sayfasına ulaşılabilir".format(role, page)
        else:
            return "{0} rolünün {1} sayfasına ulaşılamaz".format(role, page)
        
    return inner

user1 = yetki_sorgula('product edit')
print(user1('admin')) # admin rolünün product edit sayfasına ulaşılabilir
print(user1('user')) # user rolünün product edit sayfasına ulaşamaz

def islem(islemadi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islemadi == 'toplama':
        return toplam
    elif islemadi == 'carpma':
        return carpma
    
toplama = islem("toplama")
sonuc = toplama(1,2,3,4,5)
print(sonuc)

carpma = islem("carpma")
carpma(1,2,3,4,5)
print(sonuc)
