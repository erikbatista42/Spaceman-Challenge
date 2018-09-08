import random

secretWordBank = ["blue", "yellow", "orange", "red", "purple", "white", "black", "green"]

secureRandom = random.SystemRandom()

pickedColor = secureRandom.choice(secretWordBank)
print(pickedColor)

letters = []
# guessALetter = input("Guess a letter from A-Z")
# letters.append(guessALetter)
# guessAnotherLetter = input("Guess another letter from A-Z")
# letters.append(guessAnotherLetter)
# print(letters)
# print(len(letters))

while len(letters) < 7:
    if len(letters) == 7:
        print("Game Over")
    else:
        if len(letters) < 7:
            guessALetter = input("Guess a letter from A-Z")
            letters.append(guessALetter)
            print(letters)
        else:
            print("Game Over")
