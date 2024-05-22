import random

def guess_number_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
        
        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            print(f"It took you {attempts} attempts to win the game.")
            break

# Call the function to start the game
guess_number_game()
