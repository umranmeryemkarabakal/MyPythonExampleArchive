import re

#lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

with open(r"C:\Users\umran\OneDrive\Masaüstü\lorem_ipsum.txt","r") as loremtxt:
    lorem = loremtxt.read()

print(lorem)
search = re.findall("elit", lorem)
print(search)
print(len(search))

loremList = re.split("\n", lorem)
print(loremList)
print(len(loremList))


lorem_change = re.sub(" ","-",lorem)
print(lorem_change)
print("-----")
searchObject = re.search("elit", lorem)
print(searchObject) # <re.Match object; span=(51, 55), match='elit'>
result = searchObject.span() # (51,55)
print(result)
result = searchObject.start()
print(result)
result = searchObject.end()
print(result)
result = searchObject.group() # elit
print(result)
result = searchObject.string
print(result) # lorem metni


"""
[a-e]  => [abcde]
[1-5]  => [12345]
[0-39] => [01239]   

[^abc] => abc dışındaki karakterler.
[^0-9] => rakam olmayan karakterler.
"""

# result = re.findall("[abc]", lorem)
# 'a', 'b', veya 'c' karakterlerinden herhangi birini içeren eşleşmeleri bulur.

# result = re.findall("[sat]", lorem)
# 's', 'a', veya 't' karakterlerinden herhangi birini içeren eşleşmeleri bulur.

# result = re.findall("[a-e]", lorem)
# 'a' ile 'e' arasındaki karakterlerden herhangi birini içeren eşleşmeleri bulur (küçük harf).

# result = re.findall("[a-z]", lorem)
# Tüm küçük harf karakterlerinden herhangi birini içeren eşleşmeleri bulur.

# result = re.findall("[0-5]", lorem)
# '0' ile '5' arasındaki rakamlardan herhangi birini içeren eşleşmeleri bulur.

# result = re.findall("[^abc]", lorem)
# 'a', 'b', veya 'c' karakterleri dışındaki karakterleri eşleştirir.

# result = re.findall("[^0-9]", lorem)
# Rakamlar dışındaki karakterleri eşleştirir.

# result = re.findall("...", lorem)
# Üç karakterden oluşan tüm grupları eşleştirir (boşluklar dahil).

# result = re.findall("e.it", lorem)
# 'e' ile başlayıp, herhangi bir karakter ('.') ile devam eden ve ardından 'it' ile biten eşleşmeleri bulur.

# result = re.findall("^M", lorem)
# Metin '^' ile başlıyorsa ve 'M' harfi ile başlıyorsa eşleştirme yapar.

# result = re.findall("^L", lorem)
# Metin '^' ile başlıyorsa ve 'L' harfi ile başlıyorsa eşleştirme yapar.

# result = re.findall("adipiscing elit.$", lorem)
# 'adipiscing elit.' ile biten metni eşleştirir (nokta dahil).

# result = re.findall("abc.$", lorem)
# 'abc' ile başlayan ve herhangi bir karakter ('.') ile biten eşleşmeleri bulur.

# result = re.findall("...$", lorem)
# Metindeki son üç karakteri eşleştirir.

# result = re.findall("el*t", lorem)
# 'e' ile başlayıp, ardından sıfır veya daha fazla 'l' karakteri ve 't' ile biten eşleşmeleri bulur.

# result = re.findall("ab*t", lorem)
# 'a' ile başlayıp, ardından sıfır veya daha fazla 'b' karakteri ve 't' ile biten eşleşmeleri bulur.

# result = re.findall("ab*j", lorem)
# 'a' ile başlayıp, ardından sıfır veya daha fazla 'b' karakteri ve 'j' ile biten eşleşmeleri bulur.

# result = re.findall("sa+t", lorem)
# 's' ile başlayıp, ardından bir veya daha fazla 'a' karakteri ve 't' ile biten eşleşmeleri bulur.

# result = re.findall("e+t", lorem)
# 'e' ile başlayıp, ardından bir veya daha fazla 'e' karakteri ve 't' ile biten eşleşmeleri bulur.

# result = re.findall("sa?t", lorem)
# 's' ile başlayıp, ardından sıfır veya bir 'a' karakteri ve 't' ile biten eşleşmeleri bulur.

# result = re.findall("a{2}", lorem)
# Yan yana iki 'a' karakterini eşleştirir.

# result = re.findall("[0-9]{2}", str)
# İki ardışık rakamı eşleştirir.

# result = re.findall("\ALorem", lorem)
# Metnin başında 'Lorem' varsa eşleştirir.

result = re.findall("elit.\Z", lorem)
# Metnin sonunda 'elit' ile başlayan ve ardından herhangi bir karakter ('.') ile biten eşleşmeleri bulur.

print(result)