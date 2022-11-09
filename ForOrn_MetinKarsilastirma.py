ilk_metin = "Bilgisayar"
ikinci_metin = "Bilişim"
for s in ilk_metin:        # ilk_metin’deki her öğeye s diyoruz
 if not s in ikinci_metin: # eğer bu öğeler ikinci_metinde yoksa
     print(s, end=" ")     # bu olmayan s’leri yazdırıyoruz
