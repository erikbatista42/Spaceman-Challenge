import random
import string
import os

def makeSpace():
    print("")

def loadWord():
   f = open('spaceman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord


def isWordGuessed(secretWord, lettersGuessed):
    lettersGussedString = "".join(lettersGuessed)

    if lettersGussedString == secretWord:
      return True
    else:
      return False


def getGuessedWord(secretWord, lettersGuessed):
    guessingWord = []

    secretWordCopy = secretWord[:]
    secretWordCopy = "_" * len(secretWord)
    secretWordCopyList = list(secretWordCopy)

    return secretWordCopyList


def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def getAvailableLetters(lettersGuessed):
    alphabet = string.ascii_lowercase
    alphabetList = list(alphabet)
    for letter in lettersGuessed:
        if letter in alphabetList:
            alphabetList.remove(letter)
    remainingLetters = "".join(alphabetList)
    return remainingLetters


def spaceman(secretWord):
    makeSpace()
    makeSpace()

    print("Let's play Spaceman! 👨‍🚀🚀")
    for dot in "." * 10:
      print(dot)

    secretWord = loadWord()
    lenOfLetters = len(secretWord)
    print("The secret words containts {} letters!".format(lenOfLetters))

    lettersGuessedList = []

    secretWordWithUnderscores = getGuessedWord(secretWord,lettersGuessedList)
    secretWordList = list(secretWord)

    numOfGuessesLeft = 7

    while numOfGuessesLeft > 0:
      print(secretWord)
      if "_" not in secretWordList:
        guessALetter = input("Guess a letter (a-z): ").lower()
        makeSpace()

        lettersGuessedList.append(guessALetter)
        # availLetters = getAvailableLetters(lettersGuessedList)
        print("ayyy: ", getAvailableLetters(lettersGuessedList))
        if guessALetter in secretWordList:

          # lettersGuessedList.append(guessALetter)

          indexOfGuessedALetter = secretWordList.index(guessALetter)

          secretWordWithUnderscores[indexOfGuessedALetter] = guessALetter

          dups = duplicates(secretWordList, guessALetter)
          for indexNum in dups:
              secretWordWithUnderscores[indexNum] = guessALetter

          print("------------------------------------------")
          print("Correct! Guesses left: {}".format(numOfGuessesLeft))
          makeSpace()
          secretWordListClean = " ".join(secretWordWithUnderscores)
          print("Secret Word: {}".format(secretWordListClean))
          lettersGuessedClean = "".join(lettersGuessedList)
          print("Letters guessed: {}".format(lettersGuessedClean))

          print("Available letters: {}".format(getAvailableLetters(lettersGuessedList)))
        else:
          numOfGuessesLeft -= 1
          # lettersGuessedList.append(guessALetter)
          # availLetters = getAvailableLetters(lettersGuessedList)
          print("------------------------------------------")
          print("Wrong! Guesses left: {}".format(numOfGuessesLeft))
          makeSpace()
          lettersGuessedClean = "".join(lettersGuessedList)
          secretWordListClean = " ".join(secretWordWithUnderscores)
          print("Secret Word: {}".format(secretWordListClean))

          print("Letters Guessed: {}".format(lettersGuessedClean))
          print("Available letters: {}".format(getAvailableLetters(lettersGuessedList)))
          # if numOfGuessesLeft == 0:
          #    print("GAME OVER!")
      else:
        print("you did it. You won.")
    print("The word was {}!".format(secretWord))

    # missing the letters the user has not guessed so far // fix getAvailableLetters)()


secretWord = loadWord()
spaceman(loadWord())
