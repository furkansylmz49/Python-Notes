import statistics 

def input_data():

  while(True):
    
    data_str = input("Lütfen verileri aralarında birer boşluk bırakarak giriniz.").split()
  
    try:
      data_int = list(map(int,data_str))
      
      if len(data_int) == 0:
        print("Empty list is not allowed. Try again.")
      else:
        return data_int
      
    except ValueError:
      print("Invalid input! Please enter integers only.")



def calculate_basic_stats(data):
  statistic = dict()
  
  statistic["mean"] = statistics.mean(data)
  statistic["median"] = statistics.median(data)
  statistic["variance"] = statistics.variance(data)
  statistic["stdev"] = statistics.stdev(data)
  
  try:
    statistic["mode"] = statistics.mode(data)
  except statistics.StatisticsError:
    statistic["mode"] = "No unique mode"


  return statistic



def calculate_z_scores(data, mean, stdev):
  if stdev == 0:
      print("Standard deviation is zero, z-score cannot be calculated.")
      return []

  z_score = list()
  
  for i in range(len(data)):
      z_score.append((data[i] - mean) / stdev)

  return z_score



def main_menu():
  while True:
      print("\n--- Main Menu ---")
      print("1. Enter data")
      print("2. Calculate basic statistics")
      print("3. Calculate z-scores")
      print("0. Exit")
    
      global choice
      choice = input("Choose an option: ")

      if choice == "1":
          print("Data entry selected.\n")
          break

      elif choice == "2":
          print("Basic statistics selected.\n")
          break

      elif choice == "3":
          print("Z-scores selected.\n")
          break

      elif choice == "0":
          print("Exiting program. Goodbye!\n")
          break
      else:
          print("Invalid choice, please try again.\n")



print("Veri Analizi Uygulamasına Hoşgeldiniz.\n")
data = []

while(True):
  main_menu()

  if choice == "1":
    data = input_data()
    print("İşlem tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")

  
  elif choice == "2":
    if data == []:
      print("Lütfen veri girişi yapınız. Ana menüye yönlendiriliyorsunuz.\n")
      
    else:
      statistic = calculate_basic_stats(data)
      
      for x,y in statistic.items():
        print(f"{x} -> {y}")

      print("İşlem tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")


  elif choice == "3":
    if data == []:
      print("Lütfen veri girişi yapınız. Ana menüye yönlendiriliyorsunuz.\n")

    else:
      stats = calculate_basic_stats(data)
      z_score = calculate_z_scores(data, stats["mean"], stats["stdev"])


      print("Positive z-scores:")
      for i, x in enumerate(z_score):
          if x >= 0:
              print(f"Index: {i} , Z-score: {x:.3f}")

      print("\nNegative z-scores:")
      for i, x in enumerate(z_score):
          if x < 0:
              print(f"Index: {i} , Z-score: {x:.3f}")
            
      print("İşlem tamamlanmıştır ana menüye yönlendiriliyorsunuz.\n")


  elif choice == "0":
    break
        
        



