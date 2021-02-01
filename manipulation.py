import pandas as pd
import numpy as np

df = pd.read_csv("E:/DQLab/Dataset/sample_csv.csv")
df1 = pd.read_csv("E:/DQLab/Dataset/sample_csv.csv", nrows=10)
df2 = pd.read_csv("E:/DQLab/Dataset/sample_csv.csv", index_col=["order_date", "order_id"])
print(df)

"""-----------------Indexing----------------------"""
# Indexing Part 1
# index dari df
print("\n[1] Indexing Part 1")
print(df.index)
# columns dari df
print(df.columns)

# Indexing Part 2
# Set multi index menggunakan set_index([])
print("\n[2] Indexing Part 2")
df_index = df.set_index(["order_id", "customer_id", "product_id", "order_date"])
print(df_index)
# Melihat multi index yang telah diset
print("Index df_index :", df_index.index)
# Print nama dan levels dari multi index
print("Name and Levels")
for name, level in zip(df_index.index.names, df_index.index.levels):
    print(name, ":", level)

# Indexing Part 3
# Example
print("\n[3] Indexing Part 3")
df_week = pd.DataFrame({
    "day_number": [1, 2, 3, 4, 5, 6, 7],
    "week_type": ["weekday" for i in range(5)] + ["weekend" for i in range(2)]
})
df_week.index = ["Monday", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(df_week)

# DataFrame awal
print("DataFrame awal :\n", df1)
# Set index baru
df1.index = ["Pesanan ke-" + str(i) for i in range(1, 11)]
# print dataframe baru
print("DataFrame dengan index baru", df1)

# Indexing Part 4
print("\n[4] Indexing Part 4")
# Indexing langsung pada read_csv,lihat df2
print("Indexing pada read_csv", df2.head())

"""-------Slicing : Filter berdasarkan kriteria tertentu----------"""

print("\n[5] Slicing menggunakan loc[]")
# Menggunakan iloc[] bedasarkan nilai index, dan loc[] berdasarkan nama kolom
# Mengambil tgl 1 Januari 2019 dari kolom order_date dan product_id(P2154 dan pP2556)
# Slice langusng berdasarkan kolom
# Slice langusng berdasarkan kolom
df_slice_loc = df.loc[(df["order_date"] == "2019-01-01") & (df["product_id"].isin(["P2154", "P2556"]))]
print("Hasil slicing berdasarkan order_date dan product_id\n", df_slice_loc)

print("\n[6] Slicing menggunakan loc[]")
# set index dari df berdasarkan order_date, order_id dan product_id
df = df.set_index(["order_date", "order_id", "product_id"])
# Gunakan loc[]
df_slice_iloc = df.loc[("2019-01-01", 1612339, ["P2154", "P2159"]), :]
print("Hasil slicing berdasarkan order_date, order_id, dan product_id\n", df_slice_iloc)

"""----------------------Transformating------------------"""
df_trans = pd.read_csv("E:/DQLab/Dataset/sample_csv.csv")
# Langkah-langkah transformationg
# [1] Lihat type data yang digunakan
# Tampilkan type data
print("\n[7] Type data menggunakan dtypes")
# Tampilkan tipe data
print("Type data sebelum transformation\n", df_trans.dtypes)
# Ubah kolom order_date menjadi datetime
df_trans["order_date"] = pd.to_datetime(df_trans["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nType data setelah transformation\n", df_trans.dtypes)

# [2] Rubah type data jika diperlukan
# Merubah type data menjadi int dan category
print("\n[8] Type data menggunakan dtypes")
df_trans["quantity"] = pd.to_numeric(df_trans["quantity"])
df_trans["city"] = df_trans["city"].astype("category")
print(df_trans.dtypes)

# [3] Gunakan apply() dan map()
print("\n[9] Method apply() dan map()")
# apply() = menerapkan suatu fungsi pada dataframe atau series atau hanya pada kolom tertentu
# Tampilkan baris teratas
print(df_trans["brand"].head())
# Ubah kolom brand menjadi lower case
df_trans["brand"] = df_trans["brand"].apply(lambda x: x.lower())
# Tampilkan data setelah apply()
print("Kolom brand setelah apply\n", df_trans["brand"].head())

# map() = digunakan untuk mensubstitusikan suatu nilai ke dalam tiap baris datanya.
# map() hanya untuk series atau dataframe yang diakses satu kolom saja
# Ambil karakter terakhir dari kolom brand, x[-1] merupakan pengambilan index dari belakang
df_trans["brand"] = df_trans["brand"].map(lambda x: x[-1])
print("Kolom brand setelah di map()\n", df_trans["brand"].head())

# Method applymap() dapat digunakan untuk dataframe
# number generator, set angka seed menjadi suatu angka, bisa semua angka, supaya hasil random nya selalu
# sama ketika kita run
print("\n[10] Method applymap()")
np.random.seed(100)
# create dataframe 3 baris dan 4 kolom dengan angka random
df_tr = pd.DataFrame(np.random.rand(3, 4))
print("\nDataFrame\n", df_tr)

# Cara 1 : tanpa define function awal,  langsung dengan anonymous lambda x
df_tr1 = df_tr.applymap(lambda x: x ** 2 + 3 * x + 2)
print("\nDataFrame cara-1:\n", df_tr1)


# Cara 2 : dengan defina function
def quadratic_fun(x):
    return x ** 2 + 3 * x + 2


df_tr2 = df_tr.applymap(quadratic_fun)
print("\nDataFrame cara-2:\n", df_tr2)
