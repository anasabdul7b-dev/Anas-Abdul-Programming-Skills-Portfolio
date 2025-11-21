# EXERCISE 5 - Days of the Month (With BONUS)

months_days = { # Dictionary mapping month numbers to their names and number of days
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

# Loop until the user provides a valid month input
while True:
    month_input = input("\nEnter the month number (1-12): ") # Ask the user to enter a month number

    # Check if the input is a digit
    if month_input.isdigit():
        month = int(month_input) # Convert input to integer

        # Check if the month is within the valid range
        if 1 <= month <= 12:
            name, days = months_days[month] # Get month name and days

            # Special handling for February to check for leap year
            if month == 2:
                leap = input("Is it a leap year? (yes/no): ").strip().lower()
                if leap == "yes":
                    print(f'\n{name} has 29 days.\n') # February in a leap year
                    break
                elif leap == "no":
                    print(f'\n{name} has {days} days.\n') # February in a normal year
                    break
                else:
                    print("Invalid input. Please type ""yes"" or ""no"". ") # Executed if the leap year input is invalid
            else:
                print(f'\n{name} has {days} days.\n')
            break
        else:
            print("Invalid number. Please enter a number between 1 and 12.") # Executed if the month number is out of range
    else:
        print("Invalid input. Please enter a number.") # Executed if the input is not a number