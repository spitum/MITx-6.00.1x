import string

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    if set(list(secretWord)).issubset(lettersGuessed):
        return True
    else:
        return False

# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','a','l']
# print(isWordGuessed(secretWord, lettersGuessed))




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    new_string = ''
    for s in secretWord:
        if s in lettersGuessed:
            #print(s)
            new_string += s
        else:
            new_string += '_ '
    return new_string

# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    return ''.join([x for x in map(chr, range(ord('a'), ord('z') + 1)) if x not in lettersGuessed])

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))
# #abcdefghijklmnopqrstuvwxyz

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    numGuesses = 8
    LettersGuessed = []

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.\n-----------'.format(len(secretWord)))

    while numGuesses > 0:
        print('You have {} guesses left.'.format(numGuesses))
        print('Available letters: {}'.format(getAvailableLetters(LettersGuessed)))
        guess = input('Please guess a letter: ').lower()
        if guess in LettersGuessed:
            print('Oops! You\'ve already guessed that letter: {}\n-----------'.format(getGuessedWord(secretWord, LettersGuessed)))
            continue
        else:
            LettersGuessed.append(guess)
            if isWordGuessed(secretWord, LettersGuessed):
                print('Good guess: {}\n-----------'.format(getGuessedWord(secretWord, LettersGuessed)))
                print('Congratulations, you won!')
                break

            elif guess in getGuessedWord(secretWord, LettersGuessed):
                print('Good guess: {}\n-----------'.format(getGuessedWord(secretWord, LettersGuessed)))
                continue
            elif guess not in getGuessedWord(secretWord, LettersGuessed):
                print('Oops! That letter is not in my word: {}\n-----------'.format(getGuessedWord(secretWord, LettersGuessed)))
                numGuesses -= 1
                if numGuesses == 0:
                  print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
                  break
                continue

        numGuesses -= 1
                
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(loadWords()).lower()
#secretWord = 'apple' 
hangman(secretWord)
