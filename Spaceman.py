import random

#loads the word from a text randomly

def load_word():
   f = open('spaceman_words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

#this is really nice and succinct! :D
def get_available_letters(letters_guessed):
    # outputs remaining letters after each guess 
    alphabet = "abcdefghijklmnopqrstuvwxy"
    myAlphabet = list(alphabet) # turns the alphabet string into characters
    for char in alphabet: # loops over the alphabet string 
        if char in letters_guessed:  # if characters in letters guessed exist, removed that character that exists
            myAlphabet.remove(char)
    remainingLetters = "".join(myAlphabet) # 
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
            secretWordList.insert(charPosition, " _ ") 
    strSoFar = ''.join(secretWordList) # turns the characters back into a word 
    return strSoFar

def is_word_guessed(secret_word, letters_guessed):
    # remove the duplicates from the secret word list
    # sort the secret word list and the guessed letters list
    # if the two lists are equal, the secret word has been guessed
    secretWordList = list(secret_word)
    noDuplicatesList = []
    for char in secretWordList: # loop characters inside the word list
        if char not in noDuplicatesList: # if the character is not in the list, add the character to the list
            noDuplicatesList.append(char) 
    if sorted(noDuplicatesList) == sorted(letters_guessed):#
        return True
    else:
        return False

# def spaceman(secret_word):
#     letters_guessed = []
#     secretWordLen = len(secret_word)
#     print('The secret word is {0} letters long'.format(secretWordLen)) 
# test = 0
# countDown = 7
#     while len(letters_guessed) < 7: 
#         print("You have 6 guesses left")
#         guessLetter = input("Guess a letter: ").lower()
#         letters_guessed.append(guessLetter)
#         print("The secret word is ", get_guessed_word(secret_word, letters_guessed))
#         print("The remaining letters are ", get_available_letters(letters_guessed))

# secret_word = load_word()
# spaceman(load_word())
def spaceman(secret_word):
	totalGuesses = 7
	letters_guessed = []
	secretWordLen = len(secret_word)
	print("The secret word is {0} letters long".format(secretWordLen)) 

	while (is_word_guessed(secret_word, letters_guessed) is False):
		guessLetter = input("Guess a letter: ").lower()
		letters_guessed.append(guessLetter)
		totalGuesses -= 1
		print("The secret word is ", get_guessed_word(secret_word, letters_guessed))
		print("You have {0} guesses left".format(totalGuesses))
		print("The remaining letters are ", get_available_letters(letters_guessed))

secret_word = load_word()
spaceman(load_word())

print("Game Over")


