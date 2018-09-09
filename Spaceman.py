import random

# secretWordBank = ["BLUE", "YELLOW", "ORANGE", "RED", "PURPLE", "WHITE", "BLACK", "GREEN"]
secretWordBank = ["BLUE"]


secureRandom = random.SystemRandom()

pickedColor = secureRandom.choice(secretWordBank)

# print(pickedColor)
guessedLetters = []

# guessALetter = input("Guess a letter from a-z")

if pickedColor == "BLUE":
    # pickedColor = "_ _ _ _"
    myColor = list(pickedColor)
    print(myColor)
    guessALetter = input("Guess a letter from a-z")
    guessedLetters.append(guessALetter)

    if guessALetter == "B":
        print("the letter " + guessALetter + " is in there!")
        pickedColor = "B _ _ _"
        print(pickedColor)
    else:
        print("the letter " + guessALetter + " is not there!")
    
print(guessedLetters)


# elif pickedColor == "YELLOW":
#     pickedColor == "_ _ _ _ _ _"
#     print(pickedColor)
# elif pickedColor == "ORANGE":
#         pickedColor == "_ _ _ _ _ _"
#         print(pickedColor)
# elif pickedColor == "RED":
#         pickedColor = "_ _ _"
#         print(pickedColor)
# elif pickedColor == "PURPLE":
#         pickedColor = "_ _ _ _ _ _"
#         print(pickedColor)
# elif pickedColor == "WHITE":
#         pickedColor = "_ _ _ _ _"
#         print(pickedColor)
# elif pickedColor == "BLACK":
#         pickedColor = "_ _ _ _ _"
#         print(pickedColor)
# elif pickedColor == "GREEN":
#     pickedColor = "_ _ _ _ _"
#     print(pickedColor)

# guessedLetters = []

# guessALetter = input("Guess a letter from a-z")

# guessedLetters.append(guessALetter)
# if guessALetter in pickedColor:
#     print("the letter " + guessALetter + " is in there!")
# else:
#      print("the letter " + guessALetter + " is not there!")

# print(guessedLetters)

# while len(letters) < 7:
#     if len(letters) == 7:
#         print("Game Over")
#     else:
#         if len(letters) < 7:
#             guessALetter = input("Guess a letter from A-Z")
#             letters.append(guessALetter)
#             print(letters)
# print("Game Over")
            
