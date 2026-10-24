# 1) Number Guessing Game using While Loop

# 1.1) IMPORTING RANDOM MODULE
import random
# 1.2) GENERATING A RANDOM SECRET NUMBER
secret_number = random.randint(1, 10)
# 1.3) SETTING THE NUMBER OF ATTEMPTS
attempts = 3
# 1.4) WHILE LOOP
while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))
# 1.5) CHECKING IF THE GUESS IS OUT OF RANGE
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue
# 1.6) DECREASING THE NUMBER OF ATTEMPTS
    attempts -= 1
# 1.7) CHECKING IF THE GUESS IS CORRECT
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
# 1.8) CHECKING IF THE GUESS IS TOO LOW
    elif guess < secret_number:
        print("Too Low. Try again.")    

# 1.9) CHECKING IF THE GUESS IS TOO HIGH
    else:
        print("Too high. Try again.")
# 1.10) CHECKING IF THE USER HAS RUN OUT OF ATTEMPTS
else:
    print("Better luck next time!")
    print(f"The correct number was {secret_number}.")
