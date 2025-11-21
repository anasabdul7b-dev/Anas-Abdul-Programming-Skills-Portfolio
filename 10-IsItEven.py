# EXERCISE 10 - Is it even?

def check_even_odd(number): # Function to check if a number is even or odd
    if number % 2 == 0: # If the number is divisible by 2, it is even
        return (f'{number} is even.\n')
    else: # Otherwise, it is odd
        return (f'{number} is odd.\n')

# Main function to run the program
def main():
    num = int(input("\nEnter a number: ")) # Ask the user to input a number
    result = check_even_odd(num) # Call the function to check even/odd and store the result
    print(result) # Display the result

# Execute the main function
main()