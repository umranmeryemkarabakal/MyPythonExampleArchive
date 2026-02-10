import os
import datetime

print("---")
print(os.name) # nt
print("---")
print(os.getcwd()) # C:\Users\umran\OneDrive\Masaüstü\Python_SadıkDuran

# os.mkdir("newDirectory")

# os.chdir('..')
# os.chdir('C:\\') 

os.makedirs("newDirectory/yeniKlasor")

print(os.listdir())
print(os.listdir("C:\\"))

for file in os.listdir():
    if file.endswith(".py"):
        print(file)

print(os.stat("demo-quiz-oop.py"))
print(os.stat("demo-quiz-oop.py").st_size/1024 , "kb")
print(datetime.datetime.fromtimestamp(os.stat("demo-quiz-oop.py").st_ctime)) # oluşturulma tarihi
print(datetime.datetime.fromtimestamp(os.stat("demo-quiz-oop.py").st_atime)) # son erişilme tarihi
print(datetime.datetime.fromtimestamp(os.stat("demo-quiz-oop.py").st_mtime)) # değiştirilme tarihi

# os.system("notepad.exe")
os.rename("newDirectory", "yeni_klasor")
os.removedirs("yeni_klasor/yeniKlasor")  # tüm dizinler boş olmalı
os.remove("yeni_klaor")

print(os.path.abspath("demo-quiz-oop.py"))
print(os.path.dirname(r"C:\Users\umran\OneDrive\Masaüstü\Python_SadıkDuran"))
print(os.path.dirname(os.path.abspath("demo-quiz-oop.py")))
print(os.path.exists(r"C:\Users\umran\OneDrive\Masaüstü\Python_SadıkDuran\demo-quiz-oop.py"))
print(os.path.exists(r"C:\Users\umran\OneDrive\Masaüstü\Python_SadıkDuran")) 
print(os.path.isdir(r"C:\Users\umran\OneDrive\Masaüstü\Python_SadıkDuran")) 
print(os.path.isfile(r"C:\Users\umran\OneDrive\Masaüstü\Python_SadıkDuran\demo-quiz-oop.py"))
print(os.path.join("C:\\","deneme","deneme1"))
print(os.path.split("C:\\deneme"))
result = os.path.splitext("demo-quiz-oop.py")
#result[0]
print(result[1])