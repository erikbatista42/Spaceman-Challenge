import random

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
    # turn the secret_word into a list of chars, since you cannot iterate over a string
    # compare the chars in the secret word list to the chars in the guessed letters list
    # if a secret word letter has not been guessed yet, replace it with an _
    secretWordList = list(secret_word)
    for char in secretWordList:
        if char not in letters_guessed:
            charPosition = secretWordList.index(char)
            secretWordList.remove(char)
            secretWordList.insert(charPosition, ' _ ')
    strSoFar = ''.join(secretWordList)
    return strSoFar

def is_word_guessed(secret_word, letters_guessed):
    # remove the duplicates from the secret word list
    # sort the secret word list and the guessed letters list
    # if the two lists are equal, the secret word has been guessed
    secretWordList = list(secret_word)
    noDuplicatesList = []
    for char in secretWordList:
        if char not in noDuplicatesList:
            noDuplicatesList.append(char)
    if sorted(noDuplicatesList) == sorted(letters_guessed):
        return True
    else:
        return False

def spaceman(secret_word):
    letters_guessed = []
    secretWordLen = len(secret_word)
    print("The secret word is {0} letters long".format(secretWordLen)) 

    while (is_word_guessed(secret_word, letters_guessed) is False):
        guessLetter = input("Guess a letter: ").lower()
        letters_guessed.append(guessLetter)
        print("The secret word is ", get_guessed_word(secret_word, letters_guessed))
        print("The remaining letters are ", get_available_letters(letters_guessed))

secret_word = load_word()
spaceman(load_word())