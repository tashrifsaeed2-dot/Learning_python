import random

secret = random.randint(1, 50)

attempts = 0
max_attempts = 5
has_won = False

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50. You have 5 attempts.\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        has_won = True
        break
    else:
        difference = secret - guess
        if difference < 0:
            difference = difference * -1  

        if difference <= 3:
            print("🔥 hot")
        elif difference <= 10:
            print("🌡️ warm")
        elif difference <= 20:
            print("🥶 cold")
        else:
            print("🧊 ice cold")

        remaining_lives = max_attempts - attempts - 1
        print("Remaining hearts: ", end="")
        for i in range(remaining_lives):
            print("❤️", end="")
        print("\n")

    attempts = attempts + 1

print("\n----------------------------------------")
if has_won:
    print("You won! You guessed the secret number.")
else:
    print("Game Over! You ran out of attempts.")
    print("The secret number was:", secret)
print("----------------------------------------")