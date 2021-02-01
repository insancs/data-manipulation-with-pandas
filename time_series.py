import pandas as pd
import matplotlib.pyplot as plt

# Pada load dataset bisa menggunakan parse_dates=True, index_col='timestamp' untuk menjadikan kolom 'timestamp' menjadi
# type data datetime dan menjadi index
gaq = pd.read_csv("E:/DQLab/Dataset/global_air_quality_4000rows.csv")

"""
Keyword argument 'parse_dates', yang jika di set True dan set index untuk kolom waktu tersebut maka kolom datetime 
tersebut akan transform as datetime Pandas dan menjadi index
"""
print(gaq.head())
print(gaq.info())

# [1] Convert to datetime
print("\n[1] CONVERT TO DATETIME")
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')
print("Sesudah di convert", gaq.dtypes)
print("\nDataFrame :\n", gaq.head())

# [2] Resampling Time Series :
# Downsampling = Mengurangi baris datetime menjadi frekuensi yang lebih lambat, bisa dibilang juga mengurangi rows dataset menjadi lebih sedikit
# Upsampling = menambah baris datetime menjadi frekuensi yang lebih cepat, menambah rows dataset dengan membuat kolom datetime menjadi lebih detail

print("\n[2] DOWNSAMPLING")
# Downsampling Daily to Monthly dan hitung rata-rata untuk sebulan
gaq_month = gaq.resample('M').mean()
print("Downsapling daily to monthly :\n", gaq_month.head())

# Downsampling Daily to Monthly dan hitung totalnya untuk setahun
gaq_years = gaq.resample('A').sum()
print("\nDownsapling daily to yearly :\n", gaq_years.head())

# Upsampling Data
print("\n[3] UPSAMPLING")
# Upsampling Daily to Hourly
gaq_hourly = gaq.resample('H').sum()
print("\nUpsampling Daily to Hourly:\n", gaq_hourly.head())

# [3] Resampling by Frequency
# Downsampling Frequency Daily to 2 Weekly, jika ada nilai NaN isi dengan method fillna = 'ffill'
gaq_2weekly = gaq.resample('2W').mean().fillna(method='ffill')
print("\nDownsampling Frequency Daily to 2 Weekly :\n", gaq_2weekly.head())

# Upscaling Frequency Daily to 8 hourly, jika ada nilai NaN isi dengan method fillna = 'bfill'
gaq_8hourly = gaq.resample('8H').mean().fillna(method='bfill')
print("\nUpsampling Frequency Daily to 8 hourly :\n", gaq_8hourly.head())

# [4] Visualisasi
print("\n[4] Visualisasi")
# Membuat pivot table yang menunjukkan waktu di baris nya dan masing-masing value dari pollutant nya dalam kolom
gaq_viz = gaq[['pollutant', 'value']].reset_index().set_index(['timestamp', 'pollutant'])
gaq_viz = gaq_viz.pivot_table(index='timestamp', columns='pollutant', aggfunc='mean').fillna(0)
gaq_viz.columns = gaq_viz.columns.droplevel(0)
print("Data Visualisasi :\n", gaq_viz.head())


# Membuat fungsi yang memberikan default value 0 ketika value nya di bawah 0 dan
# apply ke setiap elemen dari dataset tersebut, kemudian menampilkannya sebagai chart
def default_val(val):
    if val < 0:
        return 0
    else:
        return val


line1 = gaq_viz.resample('M').mean().ffill().applymap(lambda x: default_val(x)).apply(lambda x: x / x.max())
print("\n", line1.head())
# default value if value < 0 then 0, kemudian menghasilkan % value = value/max(value)
line1.plot(
    title='average value of each pollutant over months',
    figsize=(10, 10),  # ukuran canvas 10px x 10px
    subplots=True  # memecah plot menjadi beberapa bagian sesuai dengan jumlah kolom
)
plt.ylabel('avg pollutant (%)')
plt.xlabel('month')
plt.show()
