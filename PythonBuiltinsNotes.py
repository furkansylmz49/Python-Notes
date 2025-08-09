# 📘 Python Yerleşik Fonksiyonlar ve Listeler Üzerine Notlar

## 📑 İçindekiler
1. enumerate()
2. any() ve all()
3. zip()
4. String to list comprehension
5. *args ve **kwargs
6. map()
7. lambda
8. filter()
9. random modülü
10. Liste Metodları (list methods)
11. Sözlük (dict) Metodları
12. Küme (set) Metodları
13. Diğer Kullanışlı Fonksiyonlar: sorted(), reversed(), len(), type(), isinstance()

---

## 1. enumerate()
Bir listedeki elemanların **indeksleriyle birlikte** alınmasını sağlar. Döngülerde çok kullanılır. Genellikle `tuple` olarak (index, değer) şeklinde eleman verir.

```python
liste = ["furkan", "ali", "mehmet", "sadık", "berk", "katip"]
x = list(enumerate(liste, start=1))
print(x)

for (i, isim) in x:
    print(f"Sırası: {i} Kendisi: {isim}")
```

## 2. any() ve all()
- `any(iterable)` → iterable içindeki **en az bir** eleman `True` ise `True` döner.
- `all(iterable)` → iterable içindeki **tüm elemanlar** `True` ise `True` döner.

```python
print(any(x % 2 == 0 for x in range(10)))  # True
print(all(x > 0 for x in [1, 2, 3]))       # True
```

## 3. zip()
Birden fazla listeyi **indeks bazlı eşleştirerek** `tuple` şeklinde gruplayan fonksiyondur.

```python
liste1 = [1, 2, 3, 4, 5]
liste2 = [1.1, 2.2, 3.3, 4.4, 5.5]
z = list(zip(liste1, liste2))
print(z)  # [(1, 1.1), (2, 2.2), ...]
```

## 4. String to list comprehension:
```python
s = "furkan"
string_listesi = [karakter for karakter in s]
print(string_listesi)  # ['f', 'u', 'r', 'k', 'a', 'n']
```

## 5. *args ve **kwargs
- `*args` → fonksiyona **istediğin kadar pozisyonel argüman** gönder.
- `**kwargs` → fonksiyona **istediğin kadar anahtar=değer çifti** gönder.

```python
def deneme(*notlar):
    toplam = sum(notlar)
    print(f"{notlar} toplamı: {toplam}")

deneme(90, 10, 20)


def selam(**kişiler):
    for isim, yaş in kişiler.items():
        print(f"{isim} {yaş} yaşında")

selam(ali=25, ayşe=22)
```

## 6. map()
Belirli bir fonksiyonu bir listedeki **her elemana** uygular.

```python
sayılar = [2, 4, 6, 8, 9]
kareler = list(map(lambda x: x * x, sayılar))
print(kareler)
```

## 7. lambda fonksiyonu
**Tek satırlık fonksiyon** oluşturmak için kullanılır.
```python
kare = lambda x: x * x
print(kare(5))
```

## 8. filter()
Bir fonksiyona göre **True dönen elemanları** listeler.

```python
sayılar = [32, 43, 546, 65, 76, 68, 78]
çiftler = list(filter(lambda x: x % 2 == 0, sayılar))
print(çiftler)
```

## 9. random modülü:
```python
from random import shuffle, choice, randint

liste = [1, 2, 3, 4, 5]
shuffle(liste)         # Listeyi karıştırır
print(choice(liste))   # Listeden rastgele bir eleman seçer
print(randint(0, 5))   # 0 ile 5 arasında rastgele sayı üretir
```

## 10. Liste İşlemleri (List Methods)
```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print(liste1 + liste2)      # Listeleri birleştirir
print(liste1 * 2)           # Listeyi tekrarlar

liste1.append(10)           # Sona ekler
liste1.insert(1, 99)        # Belirtilen indexe ekler

liste_kopya = liste1.copy()  # Listeyi kopyalar

liste1.remove(2)            # Belirtilen elemanı siler
del liste1[0]               # Belirtilen indexteki elemanı siler

print(3 in liste1)          # 3 elemanı var mı?

print(liste1.index(10))     # 10 elemanının indexi

print(min(liste1))          # Minimum
print(max(liste1))          # Maksimum
print(sum(liste1))          # Toplam

liste1.sort()               # Küçükten büyüğe sıralar
liste1.sort(reverse=True)   # Büyükten küçüğe sıralar

liste1.pop()                # Sondaki elemanı siler
print(liste1.count(99))     # 99 kaç defa var?

liste1.clear()              # Tüm elemanları siler
```

## 11. Sözlük (dict) Metodları
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())      # dict_keys(['a', 'b', 'c'])
print(d.values())    # dict_values([1, 2, 3])
print(d.items())     # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(d.get("b"))    # 2

print("a" in d)       # True
print(len(d))        # 3

kopya = d.copy()
d.pop("b")
print(d)
d.update({"z": 99})
```

## 12. Küme (set) Metodları
```python
kume = {1, 2, 3}
kume.add(4)
kume.remove(2)
kume.discard(10)  # Eleman yoksa hata vermez
kume2 = {3, 4, 5}

print(kume.union(kume2))        # Birleşim
print(kume.intersection(kume2)) # Kesişim
print(kume.difference(kume2))   # Fark
```

## 13. Diğer Kullanışlı Fonksiyonlar
```python
liste = [5, 2, 9, 1]
sıralı = sorted(liste)        # Listeyi sıralar ama orijinalini bozmaz
ters = list(reversed(liste)) # Listeyi ters çevirir
print(len(liste))            # Eleman sayısı
print(type(liste))           # Tipini verir
print(isinstance(liste, list))  # liste mi?
```

---
