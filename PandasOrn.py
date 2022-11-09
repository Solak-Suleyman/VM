import pandas as pd

# Pandas Series tanımalama
from pandas import DataFrame

s = pd.Series([11, -3, -1, 2], index=['a', 'b', 'c', 'd'])
veri = [['Türkiye', 'Ankara', 500], ['İngiltere', 'Londra', 800], ['USA', 'NewYork', 900],
        ['Türkiye', 'İstanbul', 1500]]


# 2 boyutlu veriyi Pandas DataFrame yapısına çevirme
# columns parametresi ile dataframe veri yapısında sütun isimleri tanımlanır.
veriTablo = pd.DataFrame(veri, columns=['Ulke', 'Sehir', 'Nufus'])

# Tablo hakkında basit bilgiler edinme
print("\nINFO\n--------------------------\n")
print(veriTablo.info())  # tablonun satır, sütun sayısı, veri tipi, eksik veri sayısı gibi bilgileri verir


print("\nDESCRIBE\n--------------------------\n")
print(veriTablo.describe())  # tablonun genel tanımlayıcı istatistik değerlerini verir


print("\nMIN\n--------------------------\n")
print(veriTablo.min())  # her sütun için en küçük veriyi bulur

print("\nMAXIMUM\n--------------------------\n")
print(veriTablo.max())  # her sütun için en küçük veriyi bulur

print("\nMEAN\n--------------------------\n")  # her sütun için ortalama değer hesaplar
print(veriTablo.mean(numeric_only=True))

print("\nSHAPE\n--------------------------\n")
print(veriTablo.shape)  # tabloda bulunan satır ve sütun sayısını verir

# Tablodaki konumuna göre veri seçme
print("\nILOC\n--------------------------\n")
print(veriTablo.iloc[:2])

# Başlığa göre veri seçme
print("\nLOC\n--------------------------\n")
print(veriTablo.loc[:, 'Nufus'] > 750)

print("\n\nTABLODAKİ VERİLER\n--------------------------\n")
print(veriTablo)

# Veri silme
print("\nDROP\n--------------------------\n")
veriTablo.drop(veriTablo.columns[0], axis=1, inplace=True)
print(veriTablo)

# Csv dosyasından veri okuma
print("\nCVS DOSYADAN ÇEKİLEN VERİLER\n--------------------------\n")
data = pd.read_csv('HavaDurumu.csv', nrows=10, sep=';')
print(data, "\n\n")

veriCSVTablo = pd.DataFrame(data, columns=['day', 'outlook', 'temp','humidity','windy','play'])
print(veriCSVTablo.loc[:,'play'] == 'Yes')