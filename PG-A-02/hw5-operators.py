a,b,c = 4, 8, (12,2)

number1 = int(input("birinci sayiyi giriniz: "))
number2 = int(input("ikinci sayiyi giriniz: "))

number = number1*number2

c = c[0] + c[1]
sum = a + b + c
sub = abs(number-sum)
print("sayilarin  carpiminin toplaminin farki: ", sub)

print("cnin bye kalansiz bolumu: ",c//b)

print("a,b,c toplaminin mod 7si: ", sum%7)

print("binin a kuvveti: ", b**a)

x, *y, z = (2,4,6,8,13)

print(f"x: {x}, y: {y}, z: {z}")
print("znin kupu: ", z**3)

x, y, *z = (2,4,6,8,13)
sum_z = 0
for i in z:
    sum_z +=i

print("z degerlerinin toplami: ", sum_z)





num1 = int(input("ilk sayiyi giriniz: "))
num2 = int(input("ikinci sayiyi giriniz: "))

if num1 > num2 :
    print(f"girilen ilk sayi daha büyüktür. {num1}>{num2}")
elif num2 > num1:
    print(f"girilen ikinci sayi daha büyüktür. {num1}>{num2}")
else:
    print("iki sayi birbirine esittir.")

if num1%2 == 0:
    print("girilen ilk sayi çift sayidir.")
elif num2%2==0:
    print("girilen ikinci sayi çift sayidir")

not_1 = int(input("ilk sayiyi giriniz: "))
not_2 = int(input("ikinci sayiyi giriniz: "))
not_3 = int(input("ucuncu sayiyi giriniz: "))

average = round((not_1+not_2+not_3) /3)
if average >= 50:
    print("basarili")
else:
    print("basarisiz")





yas = 19
veli_izni = True
if (yas >= 18) or (veli_izni==True):
    print("bir iste calisabilir")

ders_notu = 80

if (ders_notu>=50 and ders_notu<=100):
    print("gecti")
else:
    print("kaldi")

ortalama = 70
zayif_sayisi = 0
if (zayif_sayisi<=50 and zayif_sayisi==0):
    print("tesekkur belgesi alabilir")


egitim= "lisans"
sigara_icme = False

if (egitim == "onlisans" or egitim == "lisans") and not(sigara_icme):
    print("ise girebilir.")

username = "umran34"
email = "umranmeryem19@gmail.com"
parola = "umran"

if (username == "umran34" or email == "umranmeryem19@gmail.com" )and parola=="umran":
    print("giris basarili")