# ==============================
# DECORATOR ANLATIM DOSYASI
# ==============================

from time import time

# ANSI renk kodları (konsolda renkli çıktı için)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ------------------------------
# 1. Decorator Nedir?
# ------------------------------
# Bir fonksiyonu alıp, onu başka bir fonksiyonla sarmalayarak
# ek özellikler kazandırmamızı sağlar.
# @ işareti ile fonksiyonun üstüne yazılır.

# ------------------------------
# Logger Decorator
# ------------------------------
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{CYAN}[LOGGER] {func.__name__} başladı...{RESET}")
        result = func(*args, **kwargs)
        print(f"{CYAN}[LOGGER] {func.__name__} bitti.{RESET}")
        return result
    return wrapper

# ------------------------------
# Veri Kontrolü Decorator
# ------------------------------
def check_data(func):
    def wrapper(data, *args, **kwargs):
        if not data:
            print(f"{RED}[CHECK_DATA] Hata: Veri boş!{RESET}")
            return
        print(f"{GREEN}[CHECK_DATA] Veri dolu, işleme devam...{RESET}")
        return func(data, *args, **kwargs)
    return wrapper

# ------------------------------
# Zaman Ölçer Decorator
# ------------------------------
def timer(func):
    def wrapper(*args, **kwargs):
        print(f"{YELLOW}[TIMER] Zaman ölçümü başlıyor...{RESET}")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{YELLOW}[TIMER] {func.__name__} süresi: {end - start:.6f} saniye{RESET}")
        return result
    return wrapper

# ------------------------------
# Decorator Zincirleme
# ------------------------------
# Burada @logger en dışta → ilk ve son o çalışacak.
# @check_data ortada → veri kontrolünü yapacak.
# @timer en içte → asıl fonksiyonun süresini ölçecek.
@logger
@check_data
@timer
def process_data(data):
    print(f"{GREEN}[PROCESS_DATA] Veriler işleniyor...{RESET}")
    squares = [x**2 for x in data]
    print(f"{GREEN}[PROCESS_DATA] Kareler: {squares}{RESET}")
    return squares

# ------------------------------
# Çalışma Mantığı (Soğan Modeli)
# ------------------------------
# 1. En dıştaki decorator (logger) → başladı
# 2. Ortadaki decorator (check_data) → veri kontrolü
# 3. En içteki decorator (timer) → zaman ölçümü
# 4. Asıl fonksiyon → process_data
# 5. İçten dışa çıkış → timer biter → check_data biter → logger biter

# ------------------------------
# Testler
# ------------------------------
print(f"{CYAN}=== Test 1: Dolu veri ==={RESET}")
process_data([1, 2, 3, 4])

print()
print(f"{CYAN}=== Test 2: Boş veri ==={RESET}")
process_data([])
