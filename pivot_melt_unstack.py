import pandas as pd

# Dataframe
data = pd.DataFrame({
    'kelas': 6 * ['A'] + 6 * ['B'],
    'murid': 2 * ['A1'] + 2 * ['A2'] + 2 * ['A3'] + 2 * ['B1'] + 2 * ['B2'] + 2 * ['B3'],
    'pelajaran': 6 * ['math', 'english'],
    'nilai': [90, 60, 70, 85, 50, 60, 100, 40, 95, 80, 60, 45]
}, columns=['kelas', 'murid', 'pelajaran', 'nilai'])
print(data)

"""-----------------------PIVOT""-----------------------"""
# Carilah unique records/value pada keempat kolom dataframe 'data'
for column in data.columns:
    print("Unique value %s: %s " % (column, data[column].unique()))

# [1] Pivot
# Pivoting dengan single column measurement
print("\n[1] PIVOTING")
pivot1 = data.pivot(index='murid', columns='pelajaran', values='nilai')
print("Pivoting single column\n", pivot1)

# Pivoting dengan multiple column measurement
pivot2 = data.pivot(index='murid', columns='pelajaran')
print("Pivoting multiple column\n", pivot2)

# pivot_table = melakukan pivot tapi juga melakukan groupby dan aggregation pada level rows
# sehingga dipastikan tidak ada dupicate index di rows
print("\n[2] MENGGUNAKAN pivot_table")
# Creating pivot and assign pivot_tab dengan menggunakan keyword aggfunc='mean'
pivot_tab_mean = data.pivot_table(index='kelas', columns='pelajaran', values='nilai', aggfunc='mean')
print("Creating pivot table -- aggfunc mean:\n", pivot_tab_mean)

"""---------------------------MELT----------------------------"""
# [2] melt() = mengembalikan kondisi data yg sudah di pivot (default data)
# Pivoting dataframe
pivot_data = data.pivot_table(index='kelas', columns='pelajaran', values='nilai', aggfunc='mean').reset_index()
print("\n[2] MELT DATA")
# Melting dataframe pivot_data
data_melt = pd.melt(pivot_data)
print(data_melt)

# Melting dataframe pivot_data dengan id_vars
data_melt1 = pd.melt(pivot_data, id_vars='kelas')
print("\nMELT data dengan id_vars\n", data_melt1)

# melt() dengan spesifikasikan value_vars untuk menampilkan variasi value apa saja yang ditampilkan
data_melt2a = pd.melt(pivot_data, value_vars=['math'])
print("\nMELT data dengan value_vars\n", data_melt2a)

# Melting data dengan id_vars dan value_vars
data_melt2b = pd.melt(pivot_data, id_vars='kelas', value_vars=['math'])
print("\nMELT data dengan id_vars dan value_vars\n", data_melt2b)

# Melting data dengan id_vars dan value_vars, var_name dan value_name
data_melt2c = pd.melt(pivot_data, id_vars='kelas', value_vars=['english', 'math'], var_name='mapel',
                      value_name='nilai')
print("\nMELT data dengan id_vars, value_vars, var_name dan value_name\n", data_melt2c)

"""----------------------STACK------------------------"""
"""Konsep stack/unstack sama dengan melt dan pivot secara berurutan, 
hanya saja tidak memasukkan index sebagai parameter di stack/unstack tapi harus set index terlebih dahulu, 
baru bisa melakukan stacking/unstacking dengan level yang bisa ditentukan sendiri"""

print("\n[3] UNSTACK DATA")
# Set index untuk kolom kelas, murid, dan pelajaran
data2 = data.set_index(['kelas', 'murid', 'pelajaran'])
print("Data multi index\n", data2)

# Penerapan unstack pada multi index data2
data_unstack1 = data2.unstack()
print("\nUnstack data2 :\n", data_unstack1)

# Unstacking dengan specify level name
data_unstack2 = data2.unstack(level='murid')
print("\nUnstacking dengan level name :\n", data_unstack2)

# Unstacking dengan specify level position (index position column dari set_index)
data_unstack3 = data2.unstack(level=1)  # level 1= murid
print("\nUnstack dengan level position :\n", data_unstack3)

# Stacking Data
print("\n[4] STACK DATA")
data_stack = data_unstack3.stack()
print("Stacking DataFrame :\n", data_stack)

# Tukar posisi index setelah stacking
data_swap = data_stack.swaplevel(1, 2)
print("\nSwapped Data :\n", data_swap)

# Melakukan sort_index pada stacking
data_sort = data_swap.sort_index()
print("\nSort index :\n", data_sort)
