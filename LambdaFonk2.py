#lamba fonksiyon içeren fonksiyon tanımları
def fnc3(n):
  return lambda x : x ** n

fnc_kare_al = fnc3(2) #Dinamik kare alma fonksiyonu oluşturuluyor
fnc_kup_al = fnc3(3)  #Dinamik küp alma fonksiyonu oluşturuluyor

print(fnc_kare_al(3))
print(fnc_kup_al(3))


