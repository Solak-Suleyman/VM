import pandas as pd
import numpy as np

sozluk = {'İsim':pd.Series(['Ada','Cem','Sibel','Ahmet','Mehmet','Ali','Veli',
          'Ayşe','Hüseyin','Necmi','Nalan','Namık']),
          'Meslek':pd.Series(['işçi','işçi','memur','serbest','serbest',None,None,
          'sigortacı','işsiz',None,None,'memur']),
          'Tarih':pd.Series(['11.11.2010','11.11.2010','11.11.2010','18.11.2011','18.11.2011',None,None,
          None,'11.11.2010',None,'18.11.2011','18.11.2011']),
          'Yaş':pd.Series([21, 24, 25, 44, 31, 27, 35, 33, 42, 29, 41, 43]),
          'ÇocukSayısı':pd.Series([None, None, None, None, None, 1, 2, 0, None, None, None, None]),
          'Puan':pd.Series([89, 87, 77, 55, 70, 79, 73, 79, 54, 92, 61, 69])}
df = pd.DataFrame(sozluk)
print(df)

print("\n İLK 5 SATIR")
print(df.head())   # İlk 5 satırı görüntüleme

print("\n SON 5 SATIR")
print(df.tail())    # Son 5 satırı görüntüleme

print("\n RASTGELE 5 SATIR")
print(df.sample(5))    # Rastgele 5 satırı görüntüleme

print("\n SATIR ve SÜTUN (ÖZNİTELİK)) SAYISINI GÖRÜNTÜLEME")
print(df.shape)    # Satır ve sütun (öznitelik) sayısını görüntüleme

print("\n INFO GÖRÜNTÜLEME")
print(df.info())  # Özniteliklerin veri türleri, içerdikleri kayıt sayıları ve bellek kullanımı hakkında bilgi edinme

print("\n ÖZNİTELİK SEÇEREK KAYITLARI GÖSTERME")
print(df['Meslek'])  # Öznitelik seçerek kayıtları gösterme (projection)

print("\n ÖZNİTELİK SEÇEREK İLK 5 KAYDI GÖSTERME")
print(df['Meslek'][:5])  # Öznitelik seçerek ilk 5 kaydı gösterme (top)

print("\n BİRDEN FAZLA ÖZNİTELİK SEÇME")
print(df[['Meslek', 'Yaş']])  # Birden fazla öznitelik seçme

print("\n MANTIKSAL FİLTRELEME (Yaşı 30'dan büyük ve (and) Puanı 50'den büyük kayıtlar) ")      # Yaşı 30'dan büyük ve (and) Puanı 50'den büyük kayıtları getir.
print(df[(df['Yaş']>30) & (df['Puan']>50)])   # Kayıtlar üzerinde mantıksal koşul uygulayarak (and, or) filtreleme

print("\n MANTIKSAL FİLTRELEME (Mesleği ‘işçi’ olan veya (or) Puanı 90'dan büyük olan kayıtlar) ")      # Mesleği ‘işçi’ olan veya (or) Puanı 90'dan büyük olan kayıtları getir.
print(df[(df['Meslek']=='işçi') | (df['Puan']>90)])   # Kayıtlar üzerinde mantıksal koşul uygulayarak (and, or) filtreleme

# query() fonksiyonu ile filtreleme
print("\n QUERY FONKSİYONU İLE FİLTRELEME ")
df_filtered = df.query('Yaş>20 & Puan>70')
print(df_filtered)

# Sıralama (sorting)
print("\n SIRALAMA (SORTING) ")
print(df.sort_values('Puan', axis = 0, ascending = False))   # Puan bilgisine göre azalan şekilde sırala (büyükten → küçüğe).
# “axis = 0” → satırların sıralanacağı anlamına gelir.
# “ascending = false” → azalan şekilde sıralama yapılmasını sağlar.

# Koşul ve sıralamayı birlikte kullanma
# Yaşı 30'dan ve Puanı 50'den büyük olan kayıtları, puan bilgisine göre azalan şekilde sırala.
print("\n KOŞUL ve SIRALAMA ")
print(df[(df['Yaş']>30) & (df['Puan']>65)].sort_values('Puan', axis=0, ascending=False))

# Gruplama: Meslek bazında kayıt sayısı görüntüleme (groupby)
print("\n GRUPLAMA  ")
print(df.groupby('Meslek').size())

print("\n GRUPLAMA  (BOŞ KAYITLARI DA DAHİL EDEREK)  ")
df['Meslek'] = df['Meslek'].astype(str)     # astype(str) ile tip dönüşümü
print(df.groupby('Meslek').size())

# Gruplama: Meslek bazında alınan puanların ortalamasını görüntüleme (groupby)
# lambda ve apply() fonksiyonunu birlikte kullanıyoruz.
print("\n LAMBDA ve APPLY() fonksiyonunu  ")
print(df.groupby('Meslek')['Puan'].apply(lambda x: np.mean(x)))
