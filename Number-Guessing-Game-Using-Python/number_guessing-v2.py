import random #Import Random Number

def number_guessing_game():
    # Generate a Random Number Between 1 To 100
    secret_number = random.randint(1, 100)
    # Initialize The Number of Attempts
    attempts = 0
    # The Maximum Number of Attempts
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Start The Game Loop 
    while attempts < max_attempts:
        # Input The Player Guess
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess the number between 1 to 100: "))
        # Increment Number of Attempts
        attempts += 1
        
        # Check The Guess is lower Than The Secret Number
        if guess < secret_number:
            print("The Guess Is Small ! Try again.")
        # Check The Guess is Higher Than The Secret Number
        elif guess > secret_number:
            print("The Guess Is High ! Try again.")
        # The Guess is Correct
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break #Break The Loop
    # If The Player Used All Attempts Not Guess Correct Number, Show The Secret Number
    else:
        print(f"Sorry, You've Used Your Max {max_attempts} Attempts. The Secret Number Was {secret_number}. Try again!")

# Start The Game
number_guessing_game()
