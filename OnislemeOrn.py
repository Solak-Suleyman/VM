import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sozluk = {'İsim': pd.Series(['Ada', 'Cem', 'Sibel', 'Ahmet', 'Mehmet', 'Ali', 'Veli',
                             'Ayşe', 'Hüseyin', 'Necmi', 'Nalan', 'Namık']),
          'Meslek': pd.Series(['işçi', 'işçi', 'memur', 'serbest', 'serbest', None, None,
                               'sigortacı', 'işsiz', None, None, 'memur']),
          'Tarih': pd.Series(['11.11.2010', '11.11.2010', '11.11.2010', '18.11.2011', '18.11.2011', None, None,
                              None, '11.11.2010', None, '18.11.2011', '18.11.2011']),
          'Yaş': pd.Series([21, 24, 25, 44, 31, 27, 35, 33, 42, 29, 41, 43]),
          'ÇocukSayısı': pd.Series([None, None, None, None, None, 1, 2, 0, None, None, None, None]),
          'Puan': pd.Series([89, 87, 77, 150, 70, 79, 73, 79, 40, 92, 65, 69])}
df = pd.DataFrame(sozluk)

print("\n", df)
print("\n",df.info())

bosAlanSayisi = df.isnull().sum().sum()
print("\nBoş Alan Sayısı = ", bosAlanSayisi)  # Kaç boş alan var kontrolü

print("\nÖzniteliklerin değer almadığı satır sayısı\n------------------------------------------\n")
print(df.isnull().sum())  # Özniteliklerin değer almadığı satır sayısı


# Eksik değer tablosu
def eksik_deger_tablosu(df):
    eksik_deger = df.isnull().sum()
    eksik_deger_yuzde = 100 * df.isnull().sum() / len(df)
    eksik_deger_tablo = pd.concat([eksik_deger, eksik_deger_yuzde], axis=1)
    eksik_deger_tablo_son = eksik_deger_tablo.rename(
        columns={0: 'Eksik Değerler', 1: '% Değeri'})
    return eksik_deger_tablo_son


print("\n", eksik_deger_tablosu(df))

# %70 üzerinde null değer içeren sütunları silme işlemi

tr = len(df) * .3
df.dropna(thresh=tr, axis=1, inplace=True)
print("\n\n\t\tSİLME İŞLEMİNDEN SONRA\n-----------------------------------------------\n", df)

# DOLDURMA İŞLEMİ
# Meslek özniteliğindeki Null değerleri 'Diğer' değeri ile doldur
df['Meslek'] = df['Meslek'].fillna('Diğer')

# Tarih özniteliğindeki Null değerleri Tarih benzersiz değerlerden ilki ile doldur
print(df['Tarih'].unique()[0])
df['Tarih'] = df['Tarih'].fillna(df['Tarih'].unique()[0])

print("\n\n\t\tDOLDURMA İŞLEMİNDEN SONRA\n-----------------------------------------------\n", df)


# Apply fonksiyonu kullanarak sınav başarı durumunu yeni öznitelik olarak ekle
def basari_durumu(puan):
    return (puan >= 70)

df['Geçti'] = df['Puan'].apply(basari_durumu)
print("\n\n\t\tYENİ ÖZNİTELİK EKLENDİKTEN SONRA\n----------------------------------------------------\n", df)


#Tarih özniteliğindeki yıl bilgisini kullanarak 'Yıl' isimli yeni bir öznitelik oluşturuyoruz
trh = pd.to_datetime(df['Tarih'], format='%d.%m.%Y')
df['Yıl'] = trh.dt.year
print(df.info())

print("\n\n\t\tTARİH ÖZNİTELİĞİNİN AYRIŞTIRILMASINDAN SONRA\n-----------------------------------------------------------\n",df)

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['Geçti_Encoded']= label_encoder.fit_transform(df['Geçti'])
df['Meslek_Encoded']= label_encoder.fit_transform(df['Meslek'])
print("\n\n\t\t LABEL ENCODER İŞLEMİNDEN SONRA\n-----------------------------------------------------------\n",df)

# onehotencoder = preprocessing.OneHotEncoder()
df['Meslek'] = pd.Categorical(df['Meslek'])
dfDummies = pd.get_dummies(df['Meslek'], prefix = 'Kat')
print("\n\n\t\t onehotencoder ENCODER İŞLEMİNDEN SONRA\n-----------------------------------------------------------\n",dfDummies)

df_new = pd.concat([df, dfDummies], axis=1)
print("\n\n\t\t İKİ DATAFRAME BİRLEŞİMİNDEN SONRA\n-----------------------------------------------------------\n",df_new)

#Puan özniteliğini ölçeklendirmek istiyoruz
x = df[['Puan']].values.astype(float)

#Ölçeklendirme için MinMaxScaler fonksiyonunu kullanıyoruz.
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df['Puan2'] = pd.DataFrame(x_scaled)

print("\n\n\t\t MinMaxScaler FONKSİYONU\n-----------------------------------------------------------\n",df)

# Quartile (Kartiller) ve IQR ile Aykırı Değer Tespiti
fig, ax = plt.subplots()
sns.boxplot(x=df['Puan'],data=df, ax=ax)
plt.savefig('BoxPlot.png', dpi=300, bbox_inches='tight')
plt.show()
Q1 = df.Puan.quantile(0.25)
Q2 = df.Puan.quantile(0.5)
Q3 = df.Puan.quantile(0.75)
Q4 = df.Puan.quantile(1)
IQR = Q3 - Q1

print("Q1-->", Q1)
print("Q2-->", Q2)
print("Q3-->", Q3)
print("Q4-->", Q4)
print("IQR-->", IQR)
print("Alt sınır: Q1 - 1.5 * IQR--->", Q1 - 1.5 * IQR)
print("Üst sınır: Q3 + 1.5 * IQR--->", Q3 + 1.5 * IQR)

# AYKIRI DEĞERLERİ BAŞKA BİR DATAFRAME'E AKTARMA
outliers_df = df[(df.Puan < (Q1-1.5*IQR))|(df.Puan > (Q3+1.5*IQR))]
print("\n\n\t\t OUTLIERS \n-------------------------------------------------------------------------------------\n",outliers_df)

