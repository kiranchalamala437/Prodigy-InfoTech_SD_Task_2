import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize attempts counter
    attempts = 0
    
    while True:
        # Prompt user for a guess
        user_guess = int(input("Guess the number: "))
        
        # Increment attempts
        attempts += 1
        
        # Compare user's guess with the secret number
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
guess_the_number()