from mymath_utils import input_data, calculate_basic_stats, calculate_z_scores

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


def main():
    print("Welcome to Data Analysis Application.\n")
    data = []

    while True:
        main_menu()

        if choice == "1":
            data = input_data()
            print("Operation completed. Returning to main menu.\n")

        elif choice == "2":
            if data == []:
                print("Please enter data first. Returning to main menu.\n")
            else:
                stats = calculate_basic_stats(data)
                for key, value in stats.items():
                    print(f"{key} -> {value}")
                print("Operation completed. Returning to main menu.\n")

        elif choice == "3":
            if data == []:
                print("Please enter data first. Returning to main menu.\n")
            else:
                stats = calculate_basic_stats(data)
                z_scores = calculate_z_scores(data, stats["mean"], stats["stdev"])

                print("Positive z-scores:")
                for i, z in enumerate(z_scores):
                    if z >= 0:
                        print(f"Index: {i}, Z-score: {z:.3f}")

                print("\nNegative z-scores:")
                for i, z in enumerate(z_scores):
                    if z < 0:
                        print(f"Index: {i}, Z-score: {z:.3f}")

                print("Operation completed. Returning to main menu.\n")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
