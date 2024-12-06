import random #Use For Import Random Number From Python Library

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    # Initialize the number of attempts made by the player
    attempts = 0
    # Set the maximum number of attempts
    max_attempts = 5
    
    # Print the welcome message and game instructions
    print("Welcome to the Number Guessing Game!!!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Start 
    while attempts < max_attempts:
        try:
            # Prompt the Player to Make a Guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess the number between 1 to 100: "))
            # Increment the Attempts
            attempts += 1
            
            # Check if Guess is lower Than  Secret Number
            if guess < secret_number:
                print("THE Nnumber Is Lower Than Your Guess! Try Again.")
            # Check if Guess is Higher Than Secret number
            elif guess > secret_number:
                print("Too Number Is Higher Than Your Guess! Try Again.")
            # If the guess is correct
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break #Break The Loop
        except ValueError:
            # User Invalid Input
            print("Invalid Input. Please Enter a Valid Number Between 1 to 100.")
    # The Player Used All Attempts 
    else:
        print(f"Sorry, you've Used All {max_attempts} Attempts. The Secret Number Was {secret_number}. Try Again!")

# Start The GAME
number_guessing_game()
