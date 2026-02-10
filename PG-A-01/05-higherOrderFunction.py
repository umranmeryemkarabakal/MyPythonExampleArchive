# Higher-Order Functions - Yüksek seviyeli fonksiyonlar
# fonksiyonları parametre olarak gönderme

def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b  

def bolme(a,b):
    return a/b    

def islem(f1, f2, f3, f4, islem_adi):
    
    if islem_adi == "toplama":
        print(f1(2,3))

    elif islem_adi == "cikarma":
        print(f2(2,3))

    elif islem_adi == "carpma":
        print(f3(2,3))

    elif islem_adi == "bolme":
        print(f4(2,3))

    else:
        print("geçersiz islem")


islem(toplama, cikarma, carpma, bolme, "toplama")
