from datetime import timedelta,datetime,time,date

def main_menu():
  while(True):
    print("======ANA MENÜ======")
    print("-> 1) Etkinlik ekle ")
    print("-> 2) Tüm etkinlikleri listele")
    print("-> 3) Yaklaşan etkinlikleri göster")
    print("-> 4) Geçmiş etkinlikleri göster")
    print("-> 5) Çıkış\n")
    
    try: 
      choice = int(input("Lütfen Seçiminizi Giriniz: "))
  
      if choice == 1:
        print("Etkinlik ekle seçildi.\n")
        return choice
      elif choice == 2:
        print("Tüm etkinlikleri listele seçildi.\n")
        return choice
      elif choice == 3:
        print("Yaklaşan etkinlikleri göster seçildi.\n")
        return choice
      elif choice == 4:
        print("Geçmiş etkinlikleri göster seçildi.\n")
        return choice
      elif choice == 5:
        print("Çıkış seçildi.\n")
        return choice
      else:
        print("Yanlış tuşlama yaptınız tekrar deneyiniz.\n")
        
    except ValueError:
        print("Yanlış tuşlama yaptınız tekrar deneyiniz.\n")

    return choice
  

print(f"Akıllı Etkinlik Planlayıcıya Hoşgeldiniz. Bugünün tarihi -> {datetime.now().ctime()}\n")

kayıt_defteri = list()

while(True):
  choice = main_menu()
  

  if choice == 1:
    Etkinlik_Ismi = input("Lütfen etkinlik ismini giriniz: ")   

    tarihi = input("Lütfen tarihini giriniz (gg/aa/yyyy): ")
    tarihi = datetime.strptime(tarihi, "%d/%m/%Y")

    bas_saati = input("Lütfen etkinlik başlangıç saatini giriniz (ss.dd): ")
    bas_saati = datetime.strptime(bas_saati, "%H.%M")

    süre = int(input("Lütfen etkinliğin süresini dakika cinsinden giriniz: "))

    baslangıc_tarihi = datetime.combine(tarihi.date(),bas_saati.time())
    bitis_tarihi = baslangıc_tarihi + timedelta(minutes = süre)
    
    kayıt_defteri.append({"Etkinlik Ismi":Etkinlik_Ismi,"Başlangıç Tarihi":baslangıc_tarihi,"Bitiş Tarihi":bitis_tarihi})
    
    print("\nİşleminiz tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")
    
  elif choice == 2:
    print("Tüm etkinlikler:")

    for i in range(len(kayıt_defteri)):
      print(f"Etkinlik ismi: {kayıt_defteri[i]["Etkinlik Ismi"]}, Başlangış-Bitiş saati: {kayıt_defteri[i]["Başlangıç Tarihi"].time()}-{kayıt_defteri[i]["Bitiş Tarihi"].time()}")

    print("\nİşleminiz tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")

  elif choice == 3:
    print("Önümüzdeki 10 gün içerisinde olacak etkinlikler:")

    for i in range(len(kayıt_defteri)):
      kalan = kayıt_defteri[i]["Başlangıç Tarihi"] - datetime.now()
      
      if timedelta(days=0) <= kalan <= timedelta(days=10):
        print(f"Etkinlik ismi: {kayıt_defteri[i]["Etkinlik Ismi"]}, Başlangış-Bitiş saati: {kayıt_defteri[i]["Başlangıç Tarihi"].time()}-{kayıt_defteri[i]["Bitiş Tarihi"].time()}")

    print("\nİşleminiz tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")

  elif choice == 4:
    print("Geçmiş etkinlikler:")

    for i in range(len(kayıt_defteri)):
      kalan = kayıt_defteri[i]["Başlangıç Tarihi"] - datetime.now()
      
      if timedelta(days=0) > kalan:
        print(f"Etkinlik ismi: {kayıt_defteri[i]["Etkinlik Ismi"]}, Başlangış-Bitiş saati: {kayıt_defteri[i]["Başlangıç Tarihi"].time()}-{kayıt_defteri[i]["Bitiş Tarihi"].time()}")

    print("\nİşleminiz tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")

  elif choice == 5:
    print("Bizi tercih ettiğiniz için teşekkür ederiz. yine bekleriz :)")
    break





