renkListesi = ["sarı","kırmızı", "siyah", "beyaz", "bordo", "mavi"]
print(renkListesi[0]) #sarı
print(renkListesi[5]) #mavi
print(renkListesi[-1]) #mavi
print(renkListesi[-3]) #beyaz

#liste dilimleme yöntemi
print(renkListesi[::]) #['sarı', 'kırmızı', 'siyah', 'beyaz', 'bordo', 'mavi']
print(renkListesi[1::1]) #['kırmızı', 'siyah', 'beyaz', 'bordo', 'mavi']
print(renkListesi[1::2]) #['kırmızı', 'beyaz', 'mavi']
print(renkListesi[:4]) #['sarı', 'kırmızı', 'siyah', 'beyaz']
print(renkListesi[::-1]) #['mavi', 'bordo', 'beyaz', 'siyah', 'kırmızı', 'sarı']
print(renkListesi[:2:-1]) #['mavi', 'bordo', 'beyaz']


renkListesi[0:2] = ['sarı', 'lacivert'] 
print(renkListesi) #['sarı', 'lacivert', 'siyah', 'beyaz', 'bordo', 'mavi']

renkListesi.append('yeşil')
print(renkListesi) #['sarı', 'lacivert', 'siyah', 'beyaz', 'bordo', 'mavi', 'yeşil']

renkListesi.remove('siyah')
print(renkListesi) #['sarı', 'lacivert', 'beyaz', 'bordo', 'mavi', 'yeşil']

renkListesi = renkListesi + ['turuncu']
print(renkListesi) #['sarı', 'lacivert', 'beyaz', 'bordo', 'mavi', 'yeşil', 'turuncu']



#liste metotları
renkListesi.reverse()
print(renkListesi) #['turuncu', 'yeşil', 'mavi', 'bordo', 'beyaz', 'lacivert', 'sarı']

renkListesi.sort()
print(renkListesi) #['beyaz', 'bordo', 'lacivert', 'mavi', 'sarı', 'turuncu', 'yeşil']
