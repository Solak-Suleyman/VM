import random 
for i in range(6):
    print("\t{}.Rastgele tam sayı = {}".format(i+1,random.randint(1,50)))

print("\n\tRastgele tam sayı = ", random.randrange(1,100))
print("\n\tRastgele virgüllü sayı = %.4f" % random.triangular(40,120))


liste = ["Kuzey", "Alp", "Sevgi", "Sevim", "Selin", "Zeynep", "Kaan"]
print("\n\tSeçilen isimler : ",random.sample(liste, 2))

