import pandas as pd

df_cov = pd.read_csv("E:/DQLab/Dataset/missval_public_data_covid19.csv")
print(df_cov)
print(df_cov.info())
# Cetak jumlah missing value tiap kolom
print("\nJumlah missing value :\n", df_cov.isna().sum())

# [1] Treatment Missing Value : Hapus kolom
print("\n[1] Hapus Kolom")

# Cetak ukuran awal dataframe
print("Awal : %d baris dan %d kolom" % df_cov.shape)

# Hapus kolom yang seluruh missing value dan cetak ukurannya
df_cov = df_cov.dropna(axis=1, how="all")
print("\nUkuran df setelah dibuang kolom dengan seluruh missing value : %d baris dan %d kolom" % df_cov.shape)

# Hapus baris jika ada satu saja data yang missing value dan cetak ukurannya
df_cov = df_cov.dropna(axis=0, how="any")
print("Ukuran df setelah dibuang baris missing value : %d baris dan %d kolom" % df_cov.shape)

# [2] Treatment Missing Value : Mengisi missing value dengan nilai statistik
df_cov1 = pd.read_csv("E:/DQLab/Dataset/missval_public_data_covid19.csv")
print("\n[2] Mengisi Missing Value dengan string")

# Cetak unique value pada kolom province_state
print("Unique value awal :", df_cov1["province_state"].unique())

# Isi missing value pada kolom province_state dengan string "unknown_province_state"
df_cov1["province_state"] = df_cov1["province_state"].fillna("unknown_province_state")
print("Unique value setelah fillna", df_cov1["province_state"].unique())

print("\n[3] Mengisi Missing Value dengan mean dan median")
# Cek missing value di kolom active
print("Jumlah missing value : ", df_cov1["active"].isna().sum())
# Cetak nilai mean dan median awal
print("Awal : mean %f, median %f" % (df_cov1["active"].mean(), df_cov1["active"].median()))

# Isi missing value kolom active dengan median
df_median = df_cov1["active"].fillna(df_cov1["active"].median())
# Cetak nilai mean dan median setelah diisi dengan median
print("Mean : %f, Median : %f" % (df_median.mean(), df_median.median()))

# Isi missing value kolom active dengan median
df_mean = df_cov1["active"].fillna(df_cov1["active"].mean())
# Cetak nilai mean dan median setelah diisi mean
print("Mean : %f, Median : %f" % (df_mean.mean(), df_mean.median()))

# [3] Treatment Missing Value : Mengisi missing value dengan interpolasi
import numpy as np
print("\n[4] Mengisi Missing Value dengan interpolasi pada time series")
#example
# Data
ts = pd.Series({
    "2020-01-01": 9,
    "2020-01-02": np.nan,
    "2020-01-05": np.nan,
    "2020-01-07": 24,
    "2020-01-10": np.nan,
    "2020-01-12": np.nan,
    "2020-01-15": 33,
    "2020-01-17": np.nan,
    "2020-01-16": 40,
    "2020-01-20": 45,
    "2020-01-22": 52,
    "2020-01-25": 75,
    "2020-01-28": np.nan,
    "2020-01-30": np.nan
})
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi
print("Setelah interpolasi\n", ts)
