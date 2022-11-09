#Demet oluşturma:
demet = (1,2,3,4,5,6,7,8,9)
print(demet)

#Çıktı: (1, 2, 3, 4, 5, 6, 7, 8, 9)


#Tek elemanlı bir demet tanımlama:
demet = (1)
print(type(demet))
print(demet)

#Çıktı:
# <class 'int'>
# 1

demet = (1,)
print(type(demet))
print(demet)

#Çıktı:
# <class 'tuple'>
# (1,)

demetStr = "Elma"
print(type(demetStr))
print(demetStr)

#Çıktı:
# <class 'str'>
# Elma


demetStr1 = "Elma",
print(type(demetStr1))
print(demetStr1)

# Çıktı:
# <class 'tuple'>
# ('Elma',)


#0. indekse ulaşma:
demet = (1,2,3,4,5,6,7,8,9)
print(demet[0])

#Çıktı: 1


#Elemanların indexini yani kaçıncı sırada olduğunu bulma:
demet = (1,2,3,"python","kodlama","Ali")
print(demet.index("python"))

#Çıktı: 3



#Elemanların demette kaç defa geçtiğini bulma:
demet = (1,23,34,34,2,1,4,5,1,1,34)
print(demet.count(34))

#Çıktı: 3



#Demetler değiştirilemez:
demet = ("Elma","Armut","Muz")
demet[0] = "Kiraz"

#Çıktı: Hata



#Demetler değiştirilemez:
demet = ("Elma","Armut","Muz")
demet.remove = "Kiraz" #Kiraz değerini silmeye çalıştık hata aldık

#Çıktı: Hata





