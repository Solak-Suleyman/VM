sozluk ={"Computer":"Bilgisayar",
         "Driver":"Sürücü",
         "Memory":"Hafıza",
         "Output":"Çıktı",
         "Software":"Yazılım",
         "Printer":"Yazıcı"}

print(sozluk) 
sozluk2= sozluk.copy()
print(sozluk2)

sozluk["Hardware"]= "Donanım"
print(sozluk)
print(sozluk2)

"""   ÇIKTI
{'Computer': 'Bilgisayar', 'Driver': 'Sürücü', 'Memory': 'Hafıza', 'Output': 'Çıktı', 'Software': 'Yazılım', 'Printer': 'Yazıcı'}
{'Computer': 'Bilgisayar', 'Driver': 'Sürücü', 'Memory': 'Hafıza', 'Output': 'Çıktı', 'Software': 'Yazılım', 'Printer': 'Yazıcı', 'Hardware': 'Donanım'}
{'Computer': 'Bilgisayar', 'Driver': 'Sürücü', 'Memory': 'Hafıza', 'Output': 'Çıktı', 'Software': 'Yazılım', 'Printer': 'Yazıcı'}

"""
