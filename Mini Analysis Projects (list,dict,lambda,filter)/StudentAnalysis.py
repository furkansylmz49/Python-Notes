OgrenciSayısı = int(input("Lütfen kaç tane öğrenci olduğunu giriniz: "))
print()

OgrenciBilgileri = dict()

for i in range(OgrenciSayısı):
    print(f"{i+1}. öğrencinin ismini giriniz:")
    isim = input("İsim: ")
    print(f"{i+1}. öğrencinin notlarını aralarında boşluk bırakarak giriniz:")
    notlar = input("Notlar: ").split()
    notlar = list(map(int, notlar))  # stringleri int'e çeviriyoruz
    OgrenciBilgileri[isim] = notlar
    print()

# Ortalamaları hesapla
Ortalamalar = dict(map(lambda x: (x[0], sum(x[1])/len(x[1])), OgrenciBilgileri.items()))

# Geçen ve kalan öğrencileri ayır
DersiGeçenler = dict(filter(lambda x: x[1] >= 50, Ortalamalar.items()))
DerstenKalanlar = dict(filter(lambda x: x[1] < 50, Ortalamalar.items()))

# En yüksek ve en düşük ortalamaya sahip öğrenciyi bul
maxOrtalama = max(Ortalamalar.items(), key=lambda x: x[1])
minOrtalama = min(Ortalamalar.items(), key=lambda x: x[1])

# Sayılar
KalanOgrenciSay = len(DerstenKalanlar)
GecenOgrenciSay = len(DersiGeçenler)

# Sıralı ortalamaları yazdır
print("Düşükten yükseğe öğrencilerin not ortalamaları:")
for isim, ort in sorted(Ortalamalar.items(), key=lambda x: x[1]):
    print(f"{isim} isimli öğrencinin ortalaması: {ort:.2f}")
print()

# En yüksek / en düşük ortalama sahip öğrenciler
print(f"En yüksek ortalamaya sahip öğrenci: {maxOrtalama[0]} → {maxOrtalama[1]:.2f}")
print(f"En düşük ortalamaya sahip öğrenci: {minOrtalama[0]} → {minOrtalama[1]:.2f}")
print()

# Geçen / kalan sayısı
print(f"Geçen öğrenci sayısı: {GecenOgrenciSay}")
print(f"Kalan öğrenci sayısı: {KalanOgrenciSay}")
