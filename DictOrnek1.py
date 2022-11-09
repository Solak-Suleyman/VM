"""İngilizce Sözlük uygulaması"""
kelime = input("İngilizce Kelime girin :")

sozluk ={"Computer":"Bilgisayar","Driver":"Sürücü","Memory":"Hafıza",
"Output":"Çıktı","Software":"Yazılım","Printer":"Yazıcı","Mouse":"Fare"}

for sozcuk in sozluk:
    if sozcuk == kelime :
        print(sozluk[sozcuk])
