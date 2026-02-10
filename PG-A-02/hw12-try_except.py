
def faktoriel(x):
    x = int(x)
    
    if x<0:
        raise ValueError("negatif olamaz")
    
    sonuc = 1

    for i in range(1, x+1):
        sonuc *= i

    return sonuc

for i in [3,6,7,'2a', -1,-7,9]:
    try:
        x = faktoriel(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)



def parolaKontrol(parola):
    turkce_karakterler = "şçğçüı"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parolada turkce karakter icermez")
    
    print("gecerli parola")

parola = input("parola: ")

try:
    parolaKontrol(parola)

except TypeError as e:
    print(e)





