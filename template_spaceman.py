import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def get_guessed_word(secret_word, letters_guessed):
    # turn the secret_word into a list of chars, since you cannot iterate over a string
    secretWordList = list(secret_word)
    for char in secretWordList:
        if char not in letters_guessed:
            charPosition = secretWordList.index(char)
            secretWordList.remove(char)
            secretWordList.insert(charPosition, '_ ')
    strSoFar = ''.join(secretWordList)
    print(strSoFar)
            
            
secret_word = "batastab"
letters_guessed = ['b', 'a']
get_guessed_word(secret_word, letters_guessed)
    


def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''




def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Spaceman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...


#
# secret_word = load_word()
# spaceman(load_word())
