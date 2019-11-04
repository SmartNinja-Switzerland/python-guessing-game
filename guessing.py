"""
Guessing game developed for smart female and male ninjas.
"""
import random

minimum, maximum = 0, 3
secret = random.randint(minimum, maximum)
guess = None
attempts = 0

while guess != secret:
    input_text = input(f"Guess the secret number (between {minimum} and {maximum}): ")
    guess = int(input_text)
    attempts += 1

    if guess < minimum or guess > maximum:
        print("This number is not in the valid range. Try again!")
    elif guess == secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
    else:
        print(f"Sorry, your guess is not correct... The secret number is not {guess}")

# TODO: read file "hiscore.txt", get current highscore

# TODO: say "you are better than last time" if highscore improved
print(f"It took you {attempts} tries.")

# TODO: save current number of attempts to file "hiscore.txt" if better than highscore
hiscore = open("hiscore.txt", "w")
hiscore.write(f"{attempts}")
hiscore.close()
