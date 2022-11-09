tr_harfler = "ŞşÇçĞğÖöÜüİı"
parola = input("Parolanız: ")
for karakter in parola:
 if karakter in tr_harfler:
     print("Parolada Türkçe karakter kullanılamaz")
