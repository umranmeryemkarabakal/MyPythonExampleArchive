name = "rose"
age = "19"
msj = "my name is {} i am {} years old".format(name,age)
print(msj)
msj = "my name is {0} i am {1} years old".format(name,age)
print(msj)
msj = "my name is {n} i am {a} years old".format(n = name,a = age)
print(msj)
msj = f"my name is {name} i am {age} years old"

mesaj = "btk akademi, python kursu" 

print("mesaj küçük harflerle mi ", mesaj.islower())
print("bas ve sondaki bosluk karakterlerini silinir ", mesaj.strip())
print("bosluk ile karakterleri ayirip listeler ", mesaj.split())
print(" ',' ile karakterleri ayirip listeler ", mesaj.split(','))
print("'akademi' kelimesi hangi indexten baslar ", mesaj.index('akademi'))
print("mesaj 's' ile mi bitiyor ", mesaj.endswith('s'))
print("mesaj icerisinde 'a' harfini 'e' ile degistir ", mesaj.replace('a', 'e'))

