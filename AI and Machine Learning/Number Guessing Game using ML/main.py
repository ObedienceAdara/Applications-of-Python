import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)  # Secret number to guess
        self.guesses = []  # List to store user guesses
    
    def guess_number(self):
        if not self.guesses:
            return random.randint(1, 100)  # Initial random guess if no history
        
        # In a real ML-based game, you'd use a model to predict the next guess based on self.guesses
        # For simplicity, let's use a random guess here
        return random.randint(1, 100)
    
    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("Try to guess the secret number between 1 and 100.")
        
        while True:
            guess = self.guess_number()
            print(f"Is it {guess}?")
            
            feedback = input("Enter 'high', 'low', or 'correct': ").strip().lower()
            
            if feedback == 'correct':
                print("Congratulations! You've guessed the secret number.")
                break
            elif feedback == 'high':
                print("Go lower!")
            elif feedback == 'low':
                print("Go higher!")
            else:
                print("Invalid input. Please enter 'high', 'low', or 'correct'.")
                continue
            
            self.guesses.append((guess, feedback))  # Store the guess and feedback for future predictions

# Example usage:
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
