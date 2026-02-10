"""
### **Lazy Iterator (Tembel Yüklenen Yineleyici) Nedir?**
**Lazy iterator**, verileri **gerektiği zaman hesaplayan** ve **tüm veriyi belleğe yüklemeyen** bir veri yapısıdır.  

---

## **🔹 Lazy ve Eager Evaluation (Tembel vs Hızlı Değerlendirme)**
📌 **Lazy Evaluation (Tembel Yükleme)**  
- Veriler **ihtiyaç duyuldukça hesaplanır**.
- Bellek kullanımı **daha azdır**.
- **`zip()`, `map()`, `filter()` gibi fonksiyonlar** lazy evaluation kullanır.

📌 **Eager Evaluation (Hızlı Yükleme)**  
- **Tüm veri** hemen hesaplanır ve belleğe yüklenir.
- Bellekte **fazla yer kaplar**, ancak erişim **daha hızlıdır**.
- **List comprehension** eager evaluation kullanır.

---
"""
## **🔹 `zip()` Lazy Iterator Örneği**

a = [1, 2, 3]
b = ["a", "b", "c"]

result = zip(a, b)  # Lazy iterator döner
print(result)  # <zip object at 0x...>

# Listeye çevrildiğinde verileri görebiliriz:
print(list(result))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# ✅ **`zip()` iterator döndürdüğü için `list(result)` demeden içeriği göremiyoruz.**



## **🔹 `map()` Lazy Iterator Örneği**

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)  # Lazy iterator
print(result)  # <map object at 0x...>

# Listeye çevirdiğimizde işlem yapılır
print(list(result))  # [2, 4, 6, 8, 10]

## **🔹 `filter()` Lazy Iterator Örneği**

numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, numbers)  # Lazy iterator
print(result)  # <filter object at 0x...>

# Listeye çevirdiğimizde işlem yapılır
print(list(result))  # [2, 4]

"""
## **🔹 Lazy Iteration Avantajları**
✅ **Bellek dostudur**: Büyük veri kümeleriyle çalışırken, verinin tamamını belleğe yüklemez.  
✅ **Performanslıdır**: Yalnızca ihtiyaç duyulan verileri işler.  
"""
