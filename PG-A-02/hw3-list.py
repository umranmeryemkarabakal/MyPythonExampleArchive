markalar = ["toyota", "bmw", "renault", "mercedes"]

print("listenin eleman sayisi: ", len(markalar))

print("listenin ilk elemani: ",markalar[0])
print("listenin son elemani: ",markalar[-1])

markalar[2] = "togg"
print("guncellenmis markalar listesi: ", markalar)

kosul = "togg" in markalar
print("'togg', listenin bir elemani midir", kosul)

print("listenin ilk iki elemani", markalar[:1])

new_liste = markalar + ["ford", "citroen"]
print("ekleme yapilmis liste: ", new_liste)

markalar_yeni = new_liste.pop()
print("son elemani silinmis liste", markalar_yeni)

ogrenci_1 = ["yiğit Bilgi","2010",[70,80,90] ]
ogrenci_2 = ["Ada Bilgi","2011" ,[70,70,80]]
ogrenci_3 = ["Cinar Turwn","2017", [60,60,90]]

print(f"ogrenci_1 {2025- int(ogrenci_1[1])} yasindadir")
print(f"ogrenci_2 {2025- int(ogrenci_2[1])} yasindadir")
print(f"ogrenci_3 {2025- int(ogrenci_3[1])} yasindadir")

not_ortalama_1 = (ogrenci_1[2][0] + ogrenci_1[2][1] + ogrenci_1[2][2])/3
print(f"1. ogrencinin not ortalamasi: ", not_ortalama_1)

not_ortalama_2 = (ogrenci_2[2][0] + ogrenci_2[2][1] + ogrenci_3[2][2])/3
print(f"2. ogrencinin not ortalamasi: ", not_ortalama_2)

not_ortalama_3 = (ogrenci_3[2][0] + ogrenci_3[2][1] + ogrenci_3[2][2])/3
print(f"3. ogrencinin not ortalamasi: ", not_ortalama_3)





customers = ["sadikturan", "ahmetyilmaz", "cinarturan", "yigitbilgi"]
order_totals = [12000, 13000, 5000, 15000]

order_totals[0] += 5000
print("sadik turan kisisine 500tl yatirilmistir: ", order_totals)


for i in customers:
    print(f"{i} isimli müsterinin siparis toplami {order_totals[customers.index(i)]}")

order_totals.pop()
print("son siparis silinmistir: ", order_totals)

order_totals.sort()
order_totals.reverse()
print(f"siparis toplamlari siralanmis liste {order_totals}")

print(f"en dusuk siparis sayisi: ", min(order_totals))

print(f"sadik turan kisisinin siparis tutari: ", order_totals[customers.index("sadikturan")])

customers.remove("ahmetyilmaz")

customers.clear()
order_totals.clear()

kullaniciadi = input("kullanici adi giriniz: ")
siparistoplami = int(input("toplam siparis adedini giriniz: "))

customers.append(kullaniciadi)
order_totals.append(siparistoplami)

print("müsteri listesi: ", customers)
print("siparis adedleri: ", order_totals)