import numpy as np

# 1️⃣ arange: Belirtilen aralıktaki sayıları oluşturur.
arr1 = np.arange(0, 10, 2)  # 0'dan 10'a kadar 2 artarak gider
print("arange:", arr1)  # [ 0  2  4  6  8]

# 2️⃣ linspace: Belirtilen aralıkta eşit bölünmüş sayılar üretir.
arr2 = np.linspace(0, 5, 5)  # 0 ile 5 arasında 5 eşit parça
print("linspace:", arr2)  # [0.   1.25 2.5  3.75 5.  ]

# 3️⃣ zeros: Sıfırlardan oluşan matris
arr3 = np.zeros((2, 3))  # 2 satır, 3 sütun
print("zeros:\n", arr3)

# 4️⃣ ones: Birlerden oluşan matris
arr4 = np.ones((3, 2))  # 3 satır, 2 sütun
print("ones:\n", arr4)

# 5️⃣ eye: Birim matris oluşturur (NxN)
arr5 = np.eye(3)  # 3x3 birim matrisi
print("eye:\n", arr5)

# 6️⃣ random.randn: Normal dağılımlı rastgele sayılar üretir
arr6 = np.random.randn(3, 3)  # 3x3 boyutunda rastgele sayılar
print("random.randn:\n", arr6)

# 7️⃣ random.randint: Belirtilen aralıkta rastgele tam sayılar üretir
arr7 = np.random.randint(1, 100, (3, 3))  # 1 ile 100 arasında 3x3 matris
print("random.randint:\n", arr7)

# 8️⃣ reshape: Dizinin şeklini değiştirir
arr8 = np.arange(1, 10).reshape(3, 3)  # 1-9 arası sayıları 3x3 matrise dönüştürüyor
print("reshape:\n", arr8)

# 9️⃣ argmax: En büyük değerin indeksini döndürür
index_max = np.argmax(arr8)  # Maksimum değerin indeksi
print("argmax:", index_max)

# 🔟 argmin: En küçük değerin indeksini döndürür
index_min = np.argmin(arr8)  # Minimum değerin indeksi
print("argmin:", index_min)
