#lambda fonksiyon 1
fnc1 = lambda x : x + 1
print(fnc1(1))          #Çıktı: 2
print(fnc1(fnc1(1)))    #Çıktı: 3

#lambda fonksiyon 2
fnc2 = lambda x, y : x + y
print(fnc2(4,7))         #Çıktı: 11
print(fnc2(4,fnc1(1)))   #Çıktı: 6
"""
def fnc1(x):
    return (x+1)

def fnc2(x,y):
    return (x+y)
"""
