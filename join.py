"""Penggabungan Series dan DataFrame
[1] Menggunakan append()
[2] Menggunakan concat()
[3] Menggunakan merge()
[4] Menggunakan join()"""

import pandas as pd

"""--------------------APPEND--------------------------"""
# [1] append() = menambah row saja pada series atau dataframe, ekuivalen with union in SQL
print("[1] MENGGUNAKAN APPEND()")
# Buat series of int(s1) dan series string (s2)
s1 = pd.Series([1, 2, 3, 4, 5, 6])
s2 = pd.Series(["a", "b", "c", "d", "e", "f"])
# Apply method append() on series
s1_append_s2 = s1.append(s2)
print("Series - append()\n", s1_append_s2)

# Buat dataframe df1 dan df2
df1 = pd.DataFrame({'a': [1, 2],
                    'b': [3, 4]})
df2 = pd.DataFrame({'a': [5, 6],
                    'b': [7, 8]})

# Apply method append() on series
df1_append_d2 = df1.append(df2)
print("\nDataFrame - append\n", df1_append_d2)

"""--------------------CONCAT--------------------------"""
# [2] concat = pengabungan dataframe baik row-wise atau column-wise
print("\n[2] MENGGUNAKAN CONCAT()")
# Apply method concat row-wise
row_wise_concat = pd.concat([df1, df2])
print("row-wise concat\n", row_wise_concat)

# Apply method concat column-wise
col_wise_concat = pd.concat([df1, df2], axis=1)
print("column-wise concat\n", col_wise_concat)

# Penambahan identifier -> membentuk hasil penggabungan multiindex
multiindex_concat = pd.concat([df1, df2], axis=0, keys=['df1', 'df2'])
print("Multi index concat\n", multiindex_concat)

"""--------------------MERGE--------------------------"""
# [3] merge() = Menggabungkan series dan dataframe, ekuivalen with join in SQL
# Merge single index
# Buat dataframe df1 dan df2
df1_mer = pd.DataFrame({
    'key': ['k1', 'k2', 'k3', 'k4', 'k5'],
    'val1': [200, 500, 0, 500, 100],
    'val2': [30, 50, 100, 20, 10]
})
df2_mer = pd.DataFrame({
    'key': ['k1', 'k3', 'k5', 'k7', 'k10'],
    'val3': [1, 2, 3, 4, 5],
    'val4': [6, 7, 8, 8, 10]
})
print("\n[3] MENGGUNAKAN MERGE()")

# Merge left join (key yang terdapat di DataFrame left)
merge_left = pd.merge(left=df2_mer, right=df1_mer, how='left', left_on='key', right_on='key')
print("Merge - Left :\n", merge_left)

# Merge right join (key yang terdapat di DataFrame right)
merge_right = pd.merge(left=df2_mer, right=df1_mer, how='right', left_on='key', right_on='key')
print("Merge - Right :\n", merge_right)

# Merge inner join, (tampilkan key yang terdapat di kedua DataFrame)
merge_inner = pd.merge(df1_mer, df2_mer, how='inner', left_on='key', right_on='key')
print("Merge - Inner :\n", merge_inner)

# Merge outer join, (tampilkan key pada semua DataFrame)
merge_outer = pd.merge(left=df1_mer, right=df2_mer, how='outer', left_on='key', right_on='key')
print("Merge - Outer :\n", merge_outer)

# Merge multi index
# Buat dataframe df1 dan df2
df1_merge = pd.DataFrame({
    'key': ['k1', 'k2', 'k3', 'k4', 'k5'],
    'val1': [200, 500, 0, 500, 100],
    'val2': [30, 50, 100, 20, 10]
}).set_index(['key', 'val2'])
df2_merge = pd.DataFrame({
    'key': ['k1', 'k3', 'k5', 'k7', 'k10'],
    'val3': [1, 2, 3, 4, 5],
    'val4': [6, 7, 8, 8, 10]
}).set_index(['key', 'val3'])

# Merge dataframe multi index
merge_multiindex = pd.merge(df1_merge.reset_index(), df2_merge.reset_index())
print("\nMerge - Multi Index :\n", merge_multiindex)

"""--------------------JOIN--------------------------"""
# Penerapan join menggunakan set_index default 'key'
print("\n[4] MENGGUNAKAN JOIN()")
# Secara default hasilnya seperti merge left join, right join jika df2_merge disimpan diawal deklarasi
print(df1_mer.set_index('key').join(df2_mer.set_index('key')))

# Penerapan join dengan menggunakan set_index dan keyword how
join_df = df1_mer.set_index('key').join(df2_mer.set_index('key'), how='inner')
print("JOIN - Inner\n", join_df)
