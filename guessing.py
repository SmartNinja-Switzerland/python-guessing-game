"""
Guessing game developed for smart female and male ninjas.
"""
import random

minimum, maximum = 0, 3
secret = random.randint(minimum, maximum)
guess = None
attempts = 0

player = input("What is your nickname? ")
player = player.replace(' ', '-')

while guess != secret:
    input_text = input(f"Guess the secret number (between {minimum} and {maximum}): ")
    try:
        guess = int(input_text)
    except ValueError:
        print("Please, enter a number.")
        continue
    attempts += 1

    if guess < minimum or guess > maximum:
        print("This number is not in the valid range. Try again!")
    elif guess == secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
    else:
        print(f"Sorry, your guess is not correct... The secret number is not {guess}")

try:
    file = open("hiscore.txt", "r")
    content = file.read()
    champion, score = content.split()
    hiscore = int(score)
    file.close()
except FileNotFoundError:
    champion, hiscore = None, 999_999_999
except ValueError:
    print("Highscore file is corrupt.")
    champion, hiscore = None, 999_999_999

print(f"It took you {attempts} tries.")

if attempts < hiscore:
    print(f"Congratulations! You defeated {champion} with a new highscore!")

    try:
        file = open("hiscore.txt", "w")
        text = str(attempts)
        file.write(f"{player} {attempts}")
        file.close()
    except IOError as error:
        print(f"Error writing file: {error}")
