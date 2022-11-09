"""İlk sayının ikinci sayıya tam bölünüp bölünmediğini hesaplayan ve 
sonuca göre kullanıcıyı bilgilendiren program:
"""
bölünen = int(input("Bir sayı girin: "))
bölen = int(input("Bir sayı daha girin: "))
şablon = "{} sayısı {} sayısına tam".format(bölünen, bölen)
if bölünen % bölen == 0:
 print(şablon, "bölünüyor!")
else:
 print(şablon, "bölünmüyor!")
