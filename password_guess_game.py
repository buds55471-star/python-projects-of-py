import random

easy_words = ["apple","train", "tiger", "India"]
medium_words = ["python","Neha kakkar","bottle","planet","laptop"]
hard_words = ["elephant","diamond","umbrella", "computer","mountain"]

print("Welcome to the password guessing game")
print("Chose a difficulty level:easy, medium, or hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts +=1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint+=guess[i]
        else:
            hint+="_"

        
    print("Hint: ",hint)
print("Game Over")