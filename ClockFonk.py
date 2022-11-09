import time

baslangicZamani = (time.time())
print(baslangicZamani)

ad=input("İsminizi Giriniz: ")

bitisZamani = (time.time())
print(bitisZamani)

zaman = bitisZamani-baslangicZamani
print(zaman)

print("İsminizi tam %.2f" % zaman, "saniyede girdiniz")
