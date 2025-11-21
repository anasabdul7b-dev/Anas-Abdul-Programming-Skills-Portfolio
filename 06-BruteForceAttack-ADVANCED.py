# EXERCISE 6 - Brute Force Attack (With BONUS)

password = "12345" # Predefined correct password
max_attempts = 5 # Maximum number of allowed attempts
attempts_left = max_attempts # Tracks how many attempts are remaining

name = input("\nEnter your name: ")

# Display welcome and security message
print(f'\nHello, {name}. Access is restricted to authorized personnel only.')
print(f'You are allowed {max_attempts} attempts to enter the correct password.')

# Loop until the user runs out of attempts or enters the correct password
while attempts_left > 0:
    attempt = input("\nEnter password: ") # Ask user to enter a password attempt

    # Check if the attempt matches the correct password
    if attempt == password:
        print(f'\nAccess granted. Welcome {name}!\n') # Successful login message
        break
    else:
        attempts_left -= 1 # Wrong password case
        if attempts_left > 0: # Check if attempts remain
            print(f'\nIncorrect password. You have {attempts_left} attempt/s left.') # Warning message
        else:
            print("\nMaximum attempts reached. Authorities have been alerted!!!\n") # Executed when all attempts are used up