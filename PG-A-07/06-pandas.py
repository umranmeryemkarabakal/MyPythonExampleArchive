import pandas as pd

df = pd.DataFrame({"A": [1, 2, 2, 3, 3, 3, 4, 4]})
# tekrarsız,Benzersiz değerleri döndürür sadece series nesnesinde çalışır
print(df["A"].unique())



df = pd.DataFrame({"A": [1, 2, 2, 3, 3, 3, 4, 4, None]})
# Benzersiz değer sayısını döndürür, NaN değerleri saymaz
print(df["A"].nunique())  # Çıktı: 4
print(df["A"].nunique(dropna=False))  # Çıktı: 5 (NaN dahil edildi)



# her değerin kaç kez tekrarlandığını gösterir, asceding=False varsayılan olarak azalan
df = pd.DataFrame({"A": [1, 2, 2, 3, 3, 3, 4, 4, None]})
print(df["A"].value_counts()) # NaN değerleri saymaz
print(df["A"].value_counts(dropna=False)) # NaN değerleri de sayılır



df = pd.DataFrame({"A": [1, 2, None, 4]})
print(df["A"].isnull())  # NaN olan yer True döner
print(df["A"].notnull()) # NaN olmayan yer True döner



# pivot table
df = pd.DataFrame({
    "Category": ["A", "A", "B", "B"],
    "Subcategory": ["X", "Y", "X", "Y"],
    "Sales": [100, 200, 150, 250]
})
pivot = df.pivot_table(values="Sales", index="Category", columns="Subcategory", aggfunc="sum")
print(pivot)



# loc etiketle - label ile seçim yapar, iloc sayısal index ile 
df = pd.DataFrame({"A": [10, 20, 30], "B": [40, 50, 60]}, index=["a", "b", "c"])
print(df.loc["a"])   # Etiketle seçim
print(df.iloc[0])    # İlk satırı getir
print(df.iloc[:, 1]) # Tüm satırlardan 2. sütunu getir



# multiIndex
arrays = [["A", "A", "B", "B"], ["X", "Y", "X", "Y"]]
index = pd.MultiIndex.from_arrays(arrays, names=["Category", "Subcategory"])
df = pd.DataFrame({"Sales": [100, 200, 150, 250]}, index=index)
print(df)
print(df.loc["A"])



# veriyi belirli bir sütuna göre gruplar
df = pd.DataFrame({
    "Category": ["A", "A", "B", "B"],
    "Sales": [100, 200, 150, 250]
})
grouped = df.groupby("Category").sum()
print(grouped)



# dataframe özetini döndürür
df = pd.DataFrame({"A": [10, 20, 30, 40, 50]})
print(df.describe())



# concatenation
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
df_concat = pd.concat([df1, df2])
print(df_concat)
df_concat.reset_index(drop=True) # indeksi sıfırlar
df_concat = pd.concat([df1, df2], axis=1) # yan yana birleştirir


