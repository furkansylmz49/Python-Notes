from datetime import datetime, timedelta, time, date

def datetime_modulu_ornekleri():
    print("=== datetime Modülü ===")

    simdi = datetime.now()
    print(f"Şu anki tarih ve zaman (datetime.now()): {simdi}")

    # ctime() — okunabilir string
    print(f"ctime() ile okunabilir format: {simdi.ctime()}")

    # Tarih ve saat oluşturma
    ozel_tarih = datetime(2025, 12, 25, 15, 30, 45, 123456)
    print(f"Özel datetime objesi: {ozel_tarih}")

    # strftime — string formatlama
    print("strftime ile formatlanmış:", simdi.strftime("%d-%m-%Y %H:%M:%S"))

    # strptime — string'den datetime
    dt_str = "21/08/2025 14:30:15"
    dt_obj = datetime.strptime(dt_str, "%d/%m/%Y %H:%M:%S")
    print(f"Str'den datetime objesi: {dt_obj}")

    # Haftanın günü
    print(f"Haftanın günü (0=pzt): {simdi.weekday()}")
    print(f"Haftanın günü (1=pzt): {simdi.isoweekday()}")

    # combine() — date ve time objelerini datetime'a çevirme
    d = date(2025, 10, 5)
    t = time(16, 45, 30)
    dt_birlestir = datetime.combine(d, t)
    print(f"date ve time combine ile datetime: {dt_birlestir}")

    # datetime'dan sadece tarih ve saat alma
    print(f"datetime objesinden sadece tarih: {simdi.date()}")
    print(f"datetime objesinden sadece saat: {simdi.time()}")

    # replace() ile tarih veya saatte değişiklik
    yenitarih = simdi.replace(year=2026, month=1, day=1)
    print(f"replace ile yeni tarih: {yenitarih}")

def timedelta_modulu_ornekleri():
    print("\n=== timedelta Modülü ===")

    fark = timedelta(days=2, hours=3, minutes=15, seconds=30, milliseconds=500, microseconds=200)
    print(f"Zaman farkı (timedelta): {fark}")

    simdi = datetime.now()
    gelecekte = simdi + fark
    gecmis = simdi - fark
    print(f"Şu an: {simdi}")
    print(f"2 gün 3 saat 15 dk 30.5 sn sonra: {gelecekte}")
    print(f"2 gün 3 saat 15 dk 30.5 sn önce: {gecmis}")

    # total_seconds()
    print(f"Toplam saniye: {fark.total_seconds()}")

def time_modulu_ornekleri():
    print("\n=== time Modülü ===")

    t = time(14, 30, 15, 123456)
    print(f"Saat objesi: {t}")
    print(f"Saat: {t.hour}, Dakika: {t.minute}, Saniye: {t.second}, Mikro saniye: {t.microsecond}")

    t1 = time(9, 0)
    t2 = time(17, 30)
    print(f"t1 < t2 mi? {t1 < t2}")

def date_modulu_ornekleri():
    print("\n=== date Modülü ===")

    bugun = date.today()
    print(f"Bugünün tarihi (date.today()): {bugun}")

    ozel_tarih = date(2025, 12, 31)
    print(f"Özel tarih objesi: {ozel_tarih}")

    # Tarihler karşılaştırma
    tarih1 = date(2025, 1, 1)
    tarih2 = date(2024, 12, 31)
    print(f"tarih1 > tarih2? {tarih1 > tarih2}")

    # Formatlama (strftime)
    print("Formatlı tarih:", ozel_tarih.strftime("%d-%m-%Y"))

def ekstra_ornekler():
    print("\n=== Ekstra datetime Örnekleri ===")

    now = datetime.now()
    # Tarih ve saat ayırma tekrar
    print(f"Şimdiki zaman: {now}")
    print(f"Sadece tarih: {now.date()}")
    print(f"Sadece zaman: {now.time()}")

    # ISO

