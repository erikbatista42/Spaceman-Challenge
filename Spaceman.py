import random
import string

def loadWord():
   f = open('spaceman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord


def isWordGuessed(secretWord, lettersGuessed):
    secretWord = loadWord()
    lettersGussedString = "".join(lettersGuessed)

    if lettersGussedString == secretWord:
      return True
    else:
      return False


def getGuessedWord(secretWord, lettersGuessed):
    secretWord = loadWord()
    print(secretWord)
    guessingWord = []

    secretWordList = list(secretWord)

    secretWordCopy = secretWord[:]
    secretWordCopy = "_" * len(secretWord)
    secretWordCopyList = list(secretWordCopy)

    if "_" in secretWordCopyList:
      for letters in range(0, 2):
          guessALetter = input("Guess a letter (a-z): ")

          if guessALetter in secretWordList:
            lettersGuessed.append("letters guessed: ".format(guessALetter))

            indexOfGuessedALetter = secretWordList.index(guessALetter)

            secretWordCopyList[indexOfGuessedALetter] = guessALetter
            print("Correct! You have #12 tries left!")
            print("secret word copy list: {}".format(secretWordCopyList))
          else:
            print("Nope! The letter doesn't exist. You have #12 tries left!")
    else:
        print("The _ character is not in there")


def getAvailableLetters(lettersGuessed):

    # lettersGuessed: list of letters that have been guessed so far
    print("Letters guessed: {}".format(lettersGuessed))

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

    # print("Lets play Spaceman! :) ")
    # for dot in "." * 10:
    #   print(dot)

    # 1. The secret word contains # of letters -> len(secretWord)
    secretWord = loadWord()
    lenOfLetters = len(secretWord)
    print("The secret words containts {} letters!".format(lenOfLetters))

    # 2. Ask to guess a letter
    # input("Guess one letter per round: ")
    lettersGuessed = []
    getGuessedWord(secretWord,lettersGuessed)

    # 3.Feedback on the letter they input
    #  If letter is in word:
    #       print("Good! You guess the right word")
    # else:
    #       print("Wrong! You have # of tries left.")



    # * After each round, you should also display to the user the
    #   partially guessed word so far, as well as letters that the
    #   user has not yet guessed.
    getAvailableLetters(lettersGuessed)

    print("The word was {}!".format(secretWord))



secretWord = loadWord()
spaceman(loadWord())
