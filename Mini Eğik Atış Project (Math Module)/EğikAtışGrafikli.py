import math

while True:
    choice = int(input("Welcome to the Projectile Motion Calculator! Press 1 to continue or 0 to exit: "))
    print()

    if choice != 1 and choice != 0:
        print("Invalid input! Please enter a valid choice (0 or 1).")
    else:
        break

while True:
    if choice == 1:
        initial_velocity = float(input("Please enter the initial velocity (m/s): "))
        launch_angle_deg = float(input("Please enter the launch angle (degrees): "))
        launch_angle_rad = math.radians(launch_angle_deg)

        print()

        gravity = 9.81

        vertical_velocity = initial_velocity * math.sin(launch_angle_rad)
        horizontal_velocity = initial_velocity * math.cos(launch_angle_rad)

        flight_time = (2 * vertical_velocity) / gravity
        horizontal_range = horizontal_velocity * flight_time
        max_height = math.pow(vertical_velocity, 2) / (2 * gravity)

        print(f"Flight Time -> {round(flight_time, 2)} seconds")
        print(f"Horizontal Range (x-axis) -> {round(horizontal_range, 2)} meters")
        print(f"Maximum Height (y-axis) -> {round(max_height, 2)} meters\n")

        while True:
            choice = int(input("Calculation complete. Press 1 to try again or 0 to exit: "))
            if choice != 1 and choice != 0:
                print("Invalid input! Please enter a valid choice (0 or 1).")
            else:
                break

        if choice == 0:
            break

    elif choice == 0:
        break

print("Thank you for using our service! See you again :)")
