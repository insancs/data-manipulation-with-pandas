import pandas as pd

'''Part 1 Attribute '''
# Series
number_list = pd.Series([1, 2, 2, 3, 4, 4, 5, 6, 6])
print(number_list)

# DataFrame
matrix = [[1, 2, 3],
          ['a', 'b', 'c'],
          [3, 4, 5],
          ['d', 4, 6]]

matrix_list = pd.DataFrame(matrix)
print(matrix_list)

# attribute info(), hanya bisa pada DataFrame
# [1] attribute .info()
print("[1] attribute .info()")
print("Attribute info()", matrix_list.info())

# attribute shape, untuk mengetahui jumlah baris dan kolom, bisa Series dan DataFrame
# [2] attribute .shape
print("\n[2] attribute .shape")
print("Attribute shape number_list :", number_list.shape)
print("Attribute shape matrix_list :", matrix_list.shape)

# attribute dtypes, untuk mengetahui type data, bisa Series dan DataFrame
# [3] attribute .dtypes
print("\n[3] attribute .dtypes")
print("Type data number_list :", number_list.dtypes)
print("Type data matrix_list :\n", matrix_list.dtypes)

# attribute astype(), untuk merubah type data
# [4] attribute .astype()
print("\n[4] attribute .astype()")
conv_str = number_list.astype("string")
print("Hasil convert type data number_list :\n", conv_str.dtypes)

# [5] attribute .copy()
print("\n[5] attribute .copy()")
num_list = number_list.copy()
print("Hasil copy() ke num_list :\n", num_list)
mat_list = matrix_list.copy()
print("Hasil copy ke mat_list :\n", mat_list)

# [5] attribute .to_list()
# Merubah Series menjadi list, tidak bisa untuk DataFrame
print("\n[6] attribute .to_list()")
print(number_list.to_list())

# [7] attribute .unique()
# Menghasilkan nilai unik dari suatu kolom, hanya pada Series
print("\n[7] attribute .unique()")
print(number_list.unique())

# [8] attribute .index
# Digunakan untuk mencari index/key dari Series dan DataFrame
print("\n[8] attribute .index")
print("Index number_list :", number_list.index)
print("Index matrix_list :", matrix_list.index)

# [9] attribute .columns
# Digunakan untuk mengetahui kolom yang terdapat di DataFrame
print("\n[9] attribute .columns")
print(matrix_list.columns)

# [10] attribute .loc
# Digunakan untuk slice DataFrame atau Series berdasarkan nama kolom dan\atau nama index
print("\n[10] attribute .loc[]")
print(".loc[0:1] pada number_list :\n", number_list.loc[0:1])
print(".loc[0:1] pada martix_list :\n", matrix_list.loc[0:1])

# [11] attribute .iloc
# Digunakan untuk slice DataFrame atau Series berdasarkan nama kolom dan\atau nama index
print("\n[11] attribute .iloc")
print(".iloc[0:1] pada number_list :\n", number_list.iloc[0:1])
print(".iloc[0:1] pada martix_list :\n", matrix_list.iloc[0:1])

'''Part 2 Creating Series dan DataFrame'''
# Creating series from list
ex_list = ['a', 1, 3, 5, 'c', 'd']
ex_series = pd.Series(ex_list)
print(ex_series)
# Creating dataframe from list of list
ex_list_of_list = [[1, 'a', 'b', 'c'],
                   [2.5, 'd', 'e', 'f'],
                   [5, 'g', 'h', 'i'],
                   [7.5, 'j', 10.5, 'l']]
index = ['dq', 'lab', 'kar', 'lan']
cols = ['float', 'char', 'obj', 'char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print("\n", ex_df)

# Creating series from dictionary
dict_series = {'1': 'a',
               '2': 'b',
               '3': 'c'}
ex_series = pd.Series(dict_series)
print("\nSeries from dict\n", ex_series)
# Creating dataframe from dictionary
df_series = {'1': ['a', 'b', 'c'],
             '2': ['b', 'c', 'd'],
             '4': [2, 3, 'z']}
ex_df = pd.DataFrame(df_series)
print("\nDataFrame from dict\n", ex_df)
