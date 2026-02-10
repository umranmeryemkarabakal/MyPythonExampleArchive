kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

str_arr = ' Btk Akademi '
print("bas ve sondaki bosluk harfleri silinmis ", str_arr.split())

print("tum karakterler kucuk harfe cevirme ",kursAdi.lower())

print("icerisinde kac tane '-' sembolu var ", kursAdi.count('-'))

print("'https' ile mi basliyor ", website.startswith('https'))

print("'tr' ile mi bitiyor ", website.endswith('tr'))

print(" tum karakterler harflerden mi olusuyor ", kursAdi.isalpha())

print("tum bosluklar '-' ile degistirilir ", kursAdi.replace(' ','-'))

print("'python' kelimesinin 'ReactJs' ile degistirildi ", kursAdi.replace('Python', 'ReactJs'))

print("'www' iceriyor mu ", website.find('www'))
# index = find(value,start,end)

print("listeye cevirme", website.split())
