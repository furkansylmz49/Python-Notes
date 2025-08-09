SeçimSayıları = dict()
SeçimSayıları.update({"Python": 0,"C++":0})

OyVerenSayısı = int(input("Lütfen Kaç Kişinin Oy Kullancağını Giriniz: "))

for i in range(OyVerenSayısı):
  KullanıcıSeçimi = input("Sizce Hangisi Daha Kullanışlı: Python? or C++? -> ").lower()
  if KullanıcıSeçimi == "python":
    SeçimSayıları["Python"] += 1
  elif KullanıcıSeçimi == "c++":
    SeçimSayıları["C++"] += 1
  print()

EnCokOy = max(SeçimSayıları.items(), key=lambda x: x[1])
YüzdelikSeçimSayıları = dict(map(lambda x: (x[0],(x[1]*100)/OyVerenSayısı),SeçimSayıları.items()))

print(f"Kazanan Seçim {EnCokOy[1]} oy ile {EnCokOy[0]}")

print()

print("Yüzdelik Dilimler Şu Şekildedir: ")
for isim,yüzdelik in YüzdelikSeçimSayıları.items():
  print(f"{isim}-> {yüzdelik}%")