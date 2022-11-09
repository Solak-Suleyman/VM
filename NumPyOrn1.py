import numpy as np

#Dizi oluşturma
d1 = np.array([5.5,9,10])
d2 = np.array([(3.5,8,11), (4,7,9), (2,2,1.1)], dtype=float)

#Fark alma 1. Yöntem
d3 = d2 - d1
print("Fark 1 / d3 --> ")
print(d3)

#Fark alma 2. Yöntem
d3 = np.subtract(d1, d2) 
print("\nFark 2 / d3 --> ")
print(d3)

#d1 ve d2'yi toplayıp d1 üzerine yazma
d1 = d1 + d2
print("\nToplam d1 --> ")
print(d1)

#Değeri 3'ten büyük elemanların indislerini bul
sonuc = d1 > 3

#Bulunan indisleri kullanarak, elemanları ekranra yazdır
print("\n3'ten büyük elemanlar -->")
print(d1[sonuc])

#İki matrisin çarpımı
d4 = np.dot(d1, d2)
print("\nÇarpım d4:")
print(d4)

#Matristen 1.sütunu çıkartma
d4 = np.delete(d4,0,1)
print("\nÇıkartma d4:")
print(d4)


#Dizideki en küçük eleman bulma
print("\nd4 min:", np.min(d4))

#Dizideki en büyük eleman bulma
print("\nd4 max:", np.max(d4))

#Dizinin ortalamasını alma
print("\nd4 ortalama:", d4.mean())

#Dizinin toplamını bulma
print("\nd4 toplam:", d4.sum())

#Karekök alma
print("\nd4 karekök-->", np.sqrt(d4))

#Dizinin logaritmasını hesaplama
print("\nd4 logaritma-->", np.log(d4))

#Transpoz alma
print("\nd4 transpoz:", np.transpose(d4))