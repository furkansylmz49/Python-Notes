"""
statistics_modul_rehberi.py

Bu dosya, Python statistics modülündeki fonksiyonların her birini tanıtır ve örneklerle açıklar.
"""

import statistics

def explain_mean():
    """mean(data): Verilen sayısal veri kümesinin aritmetik ortalamasını döndürür."""
    data = [10, 20, 30, 40, 50]
    result = statistics.mean(data)
    print("mean([10, 20, 30, 40, 50]) ->", result, "# 30")


def explain_median():
    """median(data): Verilen sayıların medyanını (ortanca) döndürür."""
    data_even = [1, 2, 3, 4]
    data_odd = [1, 2, 3]
    print("median([1,2,3,4]) ->", statistics.median(data_even), "# (2 + 3) / 2 = 2.5")
    print("median([1,2,3]) ->", statistics.median(data_odd), "# 2")


def explain_median_low():
    """median_low(data): Veri çift sayıda ise küçük ortancayı döndürür."""
    data = [1, 2, 3, 4]
    print("median_low([1,2,3,4]) ->", statistics.median_low(data), "# 2")


def explain_median_high():
    """median_high(data): Veri çift sayıda ise büyük ortancayı döndürür."""
    data = [1, 2, 3, 4]
    print("median_high([1,2,3,4]) ->", statistics.median_high(data), "# 3")


def explain_median_grouped():
    """median_grouped(data, interval): Grup içerisinden yaklaşık medyanı döndürür."""
    data = [1, 2, 2, 3, 4, 5, 5, 5]
    print("median_grouped([1,2,2,3,4,5,5,5]) ->",
          statistics.median_grouped(data), "# yaklaşık medyan")


def explain_mode():
    """mode(data): Tekil mod değerini döndürür; birden fazla mod varsa istatistik hatası."""
    data_single = [1, 2, 2, 3]
    print("mode([1,2,2,3]) ->", statistics.mode(data_single), "# 2")


def explain_multiple_modes():
    """multimode(data): Birden fazla mod varsa, hepsini liste olarak döndürür."""
    data_multi = [1, 2, 2, 3, 3]
    print("multimode([1,2,2,3,3]) ->", statistics.multimode(data_multi), "# [2, 3]")


def explain_variance():
    """variance(data): Örneklem varyansını (sample variance) döndürür."""
    data = [1, 2, 3, 4, 5]
    print("variance([1,2,3,4,5]) ->", statistics.variance(data), "# 2.5")


def explain_pvariance():
    """pvariance(data): Tümdistribisyon varyansı (population variance) döndürür."""
    data = [1, 2, 3, 4, 5]
    print("pvariance([1,2,3,4,5]) ->", statistics.pvariance(data), "# 2.0")


def explain_stdev():
    """stdev(data): Örneklem standart sapmasını (sample standard deviation) döndürür."""
    data = [1, 2, 3, 4, 5]
    print("stdev([1,2,3,4,5]) ->", statistics.stdev(data), "# ~1.5811")


def explain_pstdev():
    """pstdev(data): Tümdistribisyon standart sapmasını (population std dev) döndürür."""
    data = [1, 2, 3, 4, 5]
    print("pstdev([1,2,3,4,5]) ->", statistics.pstdev(data), "# ~1.4142")


def explain_harmonic_mean():
    """harmonic_mean(data): Harmonik ortalama hesaplar."""
    data = [1, 2, 4]
    print("harmonic_mean([1,2,4]) ->", statistics.harmonic_mean(data), "# ~1.7143")


def explain_geometric_mean():
    """geometric_mean(data): Geometrik ortalama hesaplar."""
    data = [1, 2, 4]
    print("geometric_mean([1,2,4]) ->", statistics.geometric_mean(data), "# ~2.0")


def explain_all():
    """Tüm fonksiyonları ve örneklerini çalıştırır."""
    explain_mean()
    explain_median()
    explain_median_low()
    explain_median_high()
    explain_median_grouped()
    explain_mode()
    explain_multiple_modes()
    explain_variance()
    explain_pvariance()
    explain_stdev()
    explain_pstdev()
    explain_harmonic_mean()
    explain_geometric_mean()


if __name__ == "__main__":
    explain_all()

        
        



