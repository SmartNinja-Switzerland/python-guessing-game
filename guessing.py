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

# get current highscore (as a number)
file = open("hiscore.txt", "r")
content = file.read()
hiscore = int(content)
file.close()

print(f"It took you {attempts} tries.")

# if better than highscore
if attempts < hiscore:
    # say "you are better than last time" if highscore improved
    print("Congratulations! You made a new highscore!")

    file = open("hiscore.txt", "w")
    text = str(attempts)
    file.write(text)
    file.close()
