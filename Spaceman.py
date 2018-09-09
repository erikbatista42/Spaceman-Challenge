import random

secretWordBank = ["blue", "yellow", "orange", "red", "purple", "white", "black", "green"]

secureRandom = random.SystemRandom()

pickedColor = secureRandom.choice(secretWordBank)

print(pickedColor.upper())

letters = []
incorrectLetters = []
guessALetter = input("Guess a letter from A-Z")
letters.append(guessALetter)
if guessALetter in pickedColor:
    print("the letter " + guessALetter + " is in there!")
else:
     print("the letter " + guessALetter + " is not there!")

print(letters)

# while len(letters) < 7:
#     if len(letters) == 7:
#         print("Game Over")
#     else:
#         if len(letters) < 7:
#             guessALetter = input("Guess a letter from A-Z")
#             letters.append(guessALetter)
#             print(letters)
# print("Game Over")
            
