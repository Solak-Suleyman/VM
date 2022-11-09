kelime=input("Bir kelime girin :")
sozluk ={"Computer":"Bilgisayar",
         "Driver":"Sürücü",
         "Memory":"Hafıza",
         "Output":"Çıktı",
         "Software":"Yazılım",
         "Printer":"Yazıcı"}
if kelime in sozluk:
    print(sozluk[kelime])
else:
    print("Aradığınız kelime Sözlükte bulunamadı")



print(sozluk.get(kelime,"Aradığınız kelime Sözlük içinde bulunmamaktadır"))
