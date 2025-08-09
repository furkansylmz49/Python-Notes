urunler = {
    "Laptop": {"fiyat": 15000, "puanlar": [5, 4, 4, 3]},
    "Mouse": {"fiyat": 500, "puanlar": [4, 4, 4, 5]},
    "Klavye": {"fiyat": 750, "puanlar": [3, 2, 4]},
    "Monitör": {"fiyat": 2000, "puanlar": [5, 5, 4, 5]},
    "Kulaklık": {"fiyat": 800, "puanlar": [2, 2, 3]}
}


UrunlerOrtalama = dict(map(lambda x: (x[0], sum(x[1]["puanlar"]) / len(x[1]["puanlar"])),urunler.items()))

Ortalama4Ustu = dict(filter(lambda x: x[1] >= 4,UrunlerOrtalama.items()))

İndirimli20Urunler = dict(map(lambda x:(x[0],x[1]["fiyat"]*0.8) ,urunler.items()))

for i, (urun_adi, bilgi) in enumerate(urunler.items(), start=1):
    ort_puan = sum(bilgi["puanlar"]) / len(bilgi["puanlar"])
    print(f"{i}. {urun_adi:<8} | Fiyat: {bilgi['fiyat']}₺ | Ortalama Puan: {round(ort_puan, 2)}")

Puan5OlanVarmı = any(y==5 for x,y in UrunlerOrtalama.items())
PuanHep2ÜstüMü = all(y>=2 for x,y in UrunlerOrtalama.items())


print()
print()
print()

print("Ürünlerin indirimli fiyatları:")
for x,y in İndirimli20Urunler.items():
    print(f"- {x}: {y}₺")

print()
print()
print()

print("En Sevilenler (4 ve üstü puan alanlar):")
for x,y in Ortalama4Ustu.items():
    print(f"- {x}")

print()
print()
print()

print("En Sevilen Ürün:")
for x,y in UrunlerOrtalama.items():
    if y == 4.0:
        print(f"- {x}")

print()
print()
print()

print(f"5 Puan Alan Ürün Varmı? -> {Puan5OlanVarmı}")

print()
print()
print()

print(f"2'nin altında puan alan Varmı? -> {not(PuanHep2ÜstüMü)}")


Urunİsim = list()
UrunFiyat = list()
UrunPuan = list()
for x,y in urunler.items():
    Urunİsim.append(x)
    UrunFiyat.append(y["fiyat"])
    UrunPuan.append(sum(y["puanlar"])/len(y["puanlar"]))

ZipUrunler = zip(Urunİsim,UrunFiyat,UrunPuan)

for t,(x,y,z) in enumerate(ZipUrunler):
    print(f"{t}. {x} | Fiyat: {y} | Ortalama Puan: {round(z,2)}")