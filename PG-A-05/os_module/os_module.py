import os

# os.mkdir("C:\\Users\\umran\\python_try\\os_try")
# os_try klasörünü oluşturdu

# os.makedirs("hm.try\\bosh")
# hm.try klasörü ve altındaki bosh klasöürünü oluşturdu
print(os.getcwd())
os.chdir("C:\\Users\\umran\\python_try\\os_try")
print(os.getcwd())

print(os.path.isfile("bosh"))
# şu anki içerisinde bulunduğu dizinde yani os_try klasörü içinde 
# bosh dosyasını arıyor bulamadığı için False dönüyor
print(os.listdir()) # klasör boş dönüyor yani içinde bir dosya yok

# Boş bir dosya oluşturmak için
newfile = "bosh"
with open(newfile, "w") as file:
    pass

print(os.listdir()) # ['bosh'] klasörün içi doldu

print(os.path.isfile("bosh")) # artık True dönüyor

"""
ssdeki verdiği hatanın sebebi hm.try klasörü hm_try olarak yazılmış
klasörü bulamadığı için hata veriyor 
False döndürmesinin sebebi klasör için bash dosyasını arıyor ama 
bizim bash klasörümüz hem burada değil hemde dosya değil klasör
"""

os.chdir("C:\\Users\\umran\\python_try\\hm.try") # bash klasöürün bulunduğu dizine gidersek
print(os.path.isfile("bosh")) # False döner çünkü bash klasör , dosya olarak gözükmüyor


