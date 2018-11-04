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




def getAvailableLetters(lettersGuessed):

    # lettersGuessed: list of letters that have been guessed so far
    lettersGuessedClean = ",".join(lettersGuessed)
    print("Letters guessed: {}".format(lettersGuessedClean))

    lettersAvailable = string.ascii_lowercase
    lettersAvailableList = list(lettersAvailable)

    for letter in lettersGuessed:
      if lettersGuessed in lettersAvailableList:
        lettersAvailableList.remove(lettersGuessed)

    lettersAvailableListStr = "".join(lettersAvailableList)

    print("Letters available: {}".format(lettersAvailableListStr))

    return lettersAvailableListStr

    # return letters that has not been guessed (string)



def spaceman(secretWord):
    #
    makeSpace()
    makeSpace()


    print("Let's play Spaceman! 👨‍🚀🚀")
    for dot in "." * 10:
      print(dot)

    secretWord = loadWord()
    lenOfLetters = len(secretWord)
    print("The secret words containts {} letters!".format(lenOfLetters))

    lettersGuessed = []
    this = getGuessedWord(secretWord,lettersGuessed)
    secretWordList = list(secretWord)

    wrongLettersGuessed = []
    availLetters = getAvailableLetters(lettersGuessed)

    numOfGuessesLeft = 7

    while numOfGuessesLeft > 0:
        guessALetter = input("Guess a letter (a-z): ")
        makeSpace()

        if guessALetter in secretWordList:
          lettersGuessed.append(guessALetter)

          indexOfGuessedALetter = secretWordList.index(guessALetter)

          this[indexOfGuessedALetter] = guessALetter
          print("Correct! Guesses left: {}".format(this))
          makeSpace()
          print("Secret Word: {}".format(secretWordListClean))
          wrongLettersGuessedClean = "".join(wrongLettersGuessed)
          print("Letters guessed: {}".format(wrongLettersGuessedClean))

          print("Available letters: {}".format(availLetters))
        else:
          numOfGuessesLeft -= 1
          wrongLettersGuessed.append(guessALetter)
          print("Wrong! Guesses left: {}".format(numOfGuessesLeft))
          makeSpace()
          wrongLettersGuessedClean = "".join(wrongLettersGuessed)
          print("Secret Word: {}".format(secretWordListClean))
          wrongLettersGuessedClean = "".join(wrongLettersGuessed)

          print("Letters Guessed: {}".format(wrongLettersGuessedClean))
          print("Available letters: {}".format(availLetters))
          # if numOfGuessesLeft == 0:
          #    print("GAME OVER!")

    print("The word was {}!".format(secretWord))

    # missing the letters the user has not guessed so far // fix getAvailableLetters)()
    #


secretWord = loadWord()
spaceman(loadWord())
