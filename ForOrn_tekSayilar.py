for n in range(1,100,2): 
 print(n, end=" ")





"""

range(10)        → 0, 1,2,3,4,5,6,7,8,9 ^# başlangıç ve artış değeri yok. Sadece bitiş değeri var.
range(1, 10)     → 1,2,3,4,5,6,7,8,9 #  artış değeri yok. Sadece başlangıç ve bitiş değeri var.
range(1, 10, 2)  → 1,3,5,7,9 #  başlangıç, bitiş ve artış değeri var. 
range(10, 0, -1) → 10,9,8,7,6,5,4,3,2,1 #  buradaki artış değeri eksiye doğru gitmektedir. 
range(10, 0, -2) → 10,8,6,4,2
range(2, 11, 2)  → 2,4,6,8,10
range(-5, 5)     → −5,−4,−3,−2,−1,0,1,2,3,4
range(1, 2)      → 1
range(1, -1, -1) → 1,0
range(0)         → ()


"""

