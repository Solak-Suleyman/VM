import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Puan özniteliğinin modu
print("\nMOD değeri")
print(df['Puan'].mode())

# Puan özniteliğinin medyanı
print("\nMEDIAN değeri")
print(df['Puan'].median())

# Puan özniteliğinin aritemtik ortalaması
print("\nAritmetik Ortalaması")
print(df['Puan'].mean())

# Sayısal tüm özniteliklerin ortalamaları
print("\nSayısal tüm Özniteliklerin Ortalaması")
print(df.mean(axis=0, numeric_only=True, skipna=False))

# Puan özniteliğinin standart sapması
print("\nStandart Sapma")
print(df['Puan'].std())

# Kovaryans matrisi hesapla
print("\nKovaryans ")
print(df.cov())

# Korelasyon hesapla
print("\nKorelasyon ")
print(df.corr())

# Korelasyon Grafiksel Gosterim
print("\nKorelasyon Grafiksel Gosterim")
print(df.plot(x='Yaş', y='Puan', style='*'))
plt.savefig('grafik.png', dpi=300, bbox_inches='tight')
#plt.show()

# HEATMAP Haritası
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.savefig('heatmap1.png', dpi=300, bbox_inches='tight')
#plt.show()

plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(corr, vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);
# save heatmap as .png file
# dpi - sets the resolution of the saved image in dots/inches
# bbox_inches - when set to 'tight' - does not allow the labels to be cropped
plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
#plt.show()