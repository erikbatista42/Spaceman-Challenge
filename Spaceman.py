import random
import sys

def load_word():
   f = open('spaceman_words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def get_available_letters(letters_guessed):
    # outputs remaining letters after each guess 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    myAlphabet = list(alphabet)
    for char in alphabet:
        if char in letters_guessed:
            myAlphabet.remove(char)
    remainingLetters = ''.join(myAlphabet)
    return remainingLetters
    
def get_guessed_word(secret_word, letters_guessed):
    secretWordList = list(secret_word)
    for char in secretWordList:
        if char not in letters_guessed:
            charPosition = secretWordList.index(char)
            secretWordList.remove(char)
            secretWordList.insert(charPosition, ' _ ')
    strSoFar = ''.join(secretWordList)
    return strSoFar

def is_word_guessed(secret_word, letters_guessed):
    secretWordList = list(secret_word)
    if set(secretWordList).intersection(set(letters_guessed)) == set(secretWordList):
        return True
    else:
        return False

def spaceman(secret_word):
    totalGuesses = 0
    letters_guessed = []
    secretWordLen = len(secret_word)
    print("The secret word is {0} letters long".format(secretWordLen))
    print("You have 7 total guesses \n")
    
    while (totalGuesses < 7):
        guessLetter = input("Guess a letter: ").lower()
        letters_guessed.append(guessLetter)
        totalGuesses += 1
        guessesLeft = 7 - totalGuesses
        
        print("The secret word is ", get_guessed_word(secret_word, letters_guessed))
        print("You have {0} guesses left".format(guessesLeft))
        print("The remaining letters are", get_available_letters(letters_guessed))

        
        gameStatus = is_word_guessed(secret_word, letters_guessed)
        # print("Game Status: {0} \n".format(gameStatus))
        if (gameStatus == True) and (guessesLeft > 0):
            sys.exit("Yay! You won")
        elif (gameStatus == False) and (guessesLeft <= 0):
            sys.exit("Game Over")

        

secret_word = load_word()
spaceman(load_word())
