sozluk ={"Computer":"Bilgisayar",
         "Driver":"Sürücü",
         "Memory":"Hafıza",
         "Output":"Çıktı",
         "Software":"Yazılım",
         "Printer":"Yazıcı"}
 
sozluk2= sozluk.copy()
print(sozluk2)

"""{'Output': 'Çıktı',
    'Driver': 'Sürücü',
    'Software': 'Yazılım',
    'Computer': 'Bilgisayar',
    'Memory': 'Hafıza',
    'Printer': 'Yazıcı'}
"""


sozluk["Hardware"]= "Donanım"
print(sozluk2)

"""
    {'Memory': 'Hafıza',
    'Printer': 'Yazıcı',
    'Output': 'Çıktı',
    'Software': 'Yazılım',
    'Computer': 'Bilgisayar',
    'Hardware': 'Donanım',
    'Driver': 'Sürücü'}
"""
ozluk2= sozluk.copy()
sozluk["Hardware"]= "Donanım"
print(sozluk2)

""" {'Software': 'Yazılım',
     'Output': 'Çıktı',
     'Printer': 'Yazıcı',
     'Computer': 'Bilgisayar',
     'Memory': 'Hafıza',
     'Driver': 'Sürücü'}


"""
