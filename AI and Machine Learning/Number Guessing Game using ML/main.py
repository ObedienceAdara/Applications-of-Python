import random

class NumberGuessingGame:

    def __init__(self):
        self.secret_number = random.randint(1, 100)  # Secret number to guess
        self.guesses = []  # List to store user guesses
        self.low_max = 0
        self.high_min = 100

    def guess_number(self):
        if not self.guesses:
            return random.randint(1, 100)  # Initial random guess if no history

        # Use the updated low_max and high_min to make a better guess
        return random.randint(self.low_max + 1, self.high_min - 1)

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("Try to guess the secret number between 1 and 100.")
        low_guesses = [0]
        high_guesses = [100]
        
        while True:
            guess = self.guess_number()
            print(f"Is it {guess}?")

            feedback = input("Enter 'high', 'low', or 'correct': ").strip().lower()

            if feedback == 'correct':
                print("Congratulations! You've guessed the secret number.")
                break
            elif feedback == 'high':
                high_guesses.append(guess)
                print("Go lower!")
            elif feedback == 'low':
                low_guesses.append(guess)
                print("Go higher!")
            else:
                print("Invalid input. Please enter 'high', 'low', or 'correct'.")
                continue

            self.guesses.append((guess, feedback))  # Store the guess and feedback for future predictions

            # Calculate the new max of low guesses and min of high guesses
            if low_guesses:
                self.low_max = max(low_guesses)
            
            if high_guesses:
                self.high_min = min(high_guesses)
            
            print(f"Lowest high guess: {self.high_min}, Highest low guess: {self.low_max}")

# Example usage:
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()