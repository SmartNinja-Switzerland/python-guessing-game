min, max = 1, 50
secret = 42
guess = 0

while guess != secret:
    input_text = input(f"Guess the secret number (between {min} and {max}): ")
    guess = int(input_text)

    if guess < min or guess > max:
        print("This number is not in the valid range. Try again!")
    elif guess == secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
    else:
        print(f"Sorry, your guess is not correct... The secret number is not {guess}")
