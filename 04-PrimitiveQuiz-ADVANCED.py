5# EXERCISE 4 - Primitive Quiz (With BONUS)

quiz = { # Dictionary containing countries and their capitals
    "Belgium": "Brussels",
    "Denmark": "Copenhagen",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Netherlands": "Amsterdam",
    "Norway": "Oslo",
    "Portugal": "Lisbon",
    "Spain": "Madrid",
    "Sweden": "Stockholm"
}

# Welcome message for the quiz
print("\nWelcome to the Euro Capitals Quiz! Enter your name to start.")
name = input("Enter name: ")

print(f'\nHello {name}! Let''s start with the quiz.')
score = 0 # Initialize the score counter

# Loop through each country-capital pair in the quiz dictionary
for country, capital in quiz.items():
    answer = input(f'\nWhat is the capital of {country}? ') # Ask the user for the capital of the current country

    # Check if the user's answer is correct (case-insensitive)
    if answer.lower() == capital.lower(): # 
        print(f'Correct! The capital of {country} is {capital}')
        score += 1 #Increase score by 1 for correct answer
        
    else: # Executed if the user's answer is wrong
        print(f'Wrong. The capital of {country} is {capital}')

# Show the final score after the quiz ends
print(f'\nQuiz finished! You got {score}/{len(quiz)} correct.')