# pandas

import pandas as pd

# Örnek veri
s = pd.Series([1, 2, 3, 4, 5])

# Her değeri karesiyle değiştirelim
squared = s.apply(lambda x: x**2)
print(squared)


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Her hücreye 2 ekleyelim
df_new = df.apply(lambda x: x + 2)
print(df_new)


df["Toplam"] = df.apply(lambda row: row["A"] + row["B"], axis=1)
print(df)
