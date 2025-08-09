"""
math_module_usage.py
-----------------------
Python 'math' modülündeki sık kullanılan fonksiyonlar:
- Açıklama
- Girdi türleri
- Örnek kullanım
"""

import math

# === Temel Fonksiyonlar ===
print("abs(-5) ->", abs(-5))  # Mutlak değer (int veya float alır)

print("pow(2, 3) ->", pow(2, 3))  # Üs alma, 2^3 = 8

# === Sabitler ===
print("math.e   ->", math.e)       # Euler sayısı (~2.71828)
print("math.pi  ->", math.pi)      # Pi sayısı (~3.14159)
print("math.inf ->", math.inf)     # Sonsuzluk değeri

# === Trigonometrik Fonksiyonlar ===
print("\n--- Trigonometric Functions ---")
print("math.sin(math.radians(30)) ->", math.sin(math.radians(30)))   # sin(30°)
print("math.cos(math.radians(60)) ->", math.cos(math.radians(60)))   # cos(60°)
print("math.tan(math.radians(45)) ->", math.tan(math.radians(45)))   # tan(45°)

# === Ters Trigonometrik Fonksiyonlar (Sonuç Radyan, Dereceye Çevrildi) ===
print("\n--- Inverse Trigonometric Functions ---")
print("math.degrees(math.asin(0.5)) ->", math.degrees(math.asin(0.5)))   # asin(0.5) in degrees
print("math.degrees(math.acos(0.5)) ->", math.degrees(math.acos(0.5)))   # acos(0.5) in degrees
print("math.degrees(math.atan(1))   ->", math.degrees(math.atan(1)))     # atan(1) in degrees

# === Açı Dönüşümleri ===
print("\n--- Angle Conversions ---")
print("math.degrees(math.pi) ->", math.degrees(math.pi))  # Radyanı dereceye çevirir
print("math.radians(180) ->", math.radians(180))          # Dereceyi radyana çevirir

# === Yuvarlama Fonksiyonları ===
print("\n--- Rounding ---")
print("math.ceil(4.2)  ->", math.ceil(4.2))   # Yukarı yuvarlar
print("math.floor(4.8) ->", math.floor(4.8))  # Aşağı yuvarlar

# === Karekök ===
print("\n--- Square Roots ---")
print("math.sqrt(16)  ->", math.sqrt(16))   # Karekök (float)
print("math.isqrt(13) ->", math.isqrt(13))  # Karekök (integer, tam sayı)

# === Ondalık Truncation ===
print("\n--- Truncation ---")
print("math.trunc(4.9) ->", math.trunc(4.9))  # Ondalık kısmı atar

# === Kombinasyon ve Mesafe ===
print("\n--- Combinatorics & Distance ---")
print("math.comb(5, 2) ->", math.comb(5, 2))  # Kombinasyon C(5, 2)
print("math.dist([0,0], [3,4]) ->", math.dist([0,0], [3,4]))  # İki nokta arası mesafe

# === Üstel Fonksiyonlar ===
print("\n--- Exponentials ---")
print("math.exp(2)  ->", math.exp(2))    # e^2
print("math.exp2(3) ->", math.exp2(3))   # 2^3

# === Mutlak Değer ===
print("\n--- Absolute Value ---")
print("math.fabs(-4.7) ->", math.fabs(-4.7))  # Mutlak değer (float döner)

# === Faktöriyel ===
print("\n--- Factorial ---")
print("math.factorial(5) ->", math.factorial(5))

# === Mod Alma ===
print("\n--- Modulo ---")
print("math.fmod(20, 3) ->", math.fmod(20, 3))  # Kalan (float döner)

# === Kesir Hatası Azaltılmış Toplama ===
print("\n--- Floating Sum ---")
print("math.fsum([0.1, 0.1, 0.1, 0.1]) ->", math.fsum([0.1, 0.1, 0.1, 0.1]))

# === Gamma Fonksiyonu ===
print("\n--- Gamma Function ---")
print("math.gamma(5) ->", math.gamma(5))  # (n-1)! ile ilişkili, sürekli fonksiyon

# === Çarpım ===
print("\n--- Product ---")
print("math.prod([1, 2, 3, 4]) ->", math.prod([1, 2, 3, 4]))

# === OBEB (GCD) ===
print("\n--- Greatest Common Divisor ---")
print("math.gcd(48, 18) ->", math.gcd(48, 18))

# === Hipotenüs ===
print("\n--- Hypotenuse ---")
print("math.hypot(3, 4) ->", math.hypot(3, 4))  # sqrt(3^2 + 4^2)

# === Yakınlık Kontrolü ===
print("\n--- isclose ---")
print("math.isclose(0.1+0.2, 0.3, abs_tol=1e-9) ->", math.isclose(0.1+0.2, 0.3, abs_tol=1e-9))

# === Sayı Kontrolleri ===
print("\n--- Number Checks ---")
print("math.isfinite(10) ->", math.isfinite(10))       # Sonsuz değilse True
print("math.isinf(math.inf) ->", math.isinf(math.inf)) # Sonsuz mu kontrolü

# === Logaritma ===
print("\n--- Logarithms ---")
print("math.log(8, 2)  ->", math.log(8, 2))    # log2(8)
print("math.log10(1000) ->", math.log10(1000)) # log10(1000)




