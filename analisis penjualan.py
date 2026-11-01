import pandas as pd

# membaca file
df= pd.read_excel('Data_Dummy_Penjualan_Wilayah_181.xlsx',sheet_name=1)
df.head()

# menentukan tipe data
print(f"tipe data:\n", df.dtypes)

# melihat jumlah data kosong
print(f"\njumlah data kosong: ", df.isnull().sum())

# menggabungkan data berdasarkan wilayah dan total penjualan
gabung = df.groupby('Wilayah')['Penjualan (Juta Rp)'].agg(
    Total_Penjualan = 'sum', # ini string krna ada .agg() jadi np.sum dst
    Rata_Penjualan = 'mean',
    jumlah_terjual = 'count'
).round(3)

# mengurutkan wilayah penjualan dari terbanyak
sorted_df = gabung.sort_values(by='jumlah_terjual', ascending=False)
print(f"\n", sorted_df)
# mengambil 5 wilayah penjualan terbanyak
top_5 = sorted_df.head(5)

# memvisualisasikan wilayah penjualan terbanyak dengan grafik batang
import matplotlib.pyplot as plt
plt.bar(top_5.index, top_5['jumlah_terjual'], color='blue', edgecolor='black')
plt.xlabel('Wilayah')
plt.ylabel('Jumlah terjual')
plt.title('Wilayah Penjualan Terbanyak')
plt.show()

# menghitung banyaknya kategori yang terjual menggunakan persentase
jum_kategori = df['Kategori'].value_counts()
print(f"\n", jum_kategori)
# memvisualisasikan banyak barang yang terjual per kategori menggunakan diagram lingkaran
plt.pie(
    jum_kategori,
    labels=jum_kategori.index,
    autopct=lambda p: f'{p:.1f}%\n({p * jum_kategori.sum() / 100:.0f} barang)',
    startangle=90,
)
plt.title('Jumlah Kategori Barang Terjual')
plt.show()