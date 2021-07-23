# Hangman game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
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
    wordlist (list): list of words (strings) Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, letters_Guessed):
    '''
    secretWord: string, the word the user is guessing lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed; False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count=0
    for i,c in enumerate(secretWord):
        if c in letters_Guessed:
            count+=1
    if count==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, letters_Guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count=0
    blank=['_']*len(secretWord)
    for i,c in enumerate(secretWord):
        if c in letters_Guessed:
            count+=1
            blank.insert(count-1,c)
            blank.pop(count)
            if count==len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count+=1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count==len(secretWord):
                return ''.join(str(e) for e in blank)



def getAvailableLetters(lettersGuessed):
    '''
-----------------------------------------------------------------------------------
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE..
#------------------------------------------------------------------------------------------ .

    letter=string.ascii_lowercase
    alphabet=list(letter)
    alphabet=alphabet[:]
    def removeDupsBetter(L1,L2):
        L1start=l1[:]
        for e in L1:
            if e in L1start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)
    return removeDupsBetter(lettersGuessed,alphabet)
    

def hangman(secretWord):
    '''
-----------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------
    intro=str(len(secretWord))
    letterGuessed=[]
    guess=str
    WordGuessed=False
    mistakmode=8
    if WordGuessed==True:
        return 'Congratulations,you won!'
    elif mistakmode==0:
        print('Sorry,you ran out of guesses.the word was') + secretWord

    print('I am thinking a word that is ') + intro + 'letters long'
    print("-----------------")
    while mistakmode>0 and mistakmode <= 8:
        while WordGuessed is False:
            if secretWord== getGuessedWord(secretWord,letterGuessed):
                WordGuessed==True
                break
            print('You have') + str(mistakmode) + 'guess left.'
            guess=raw_input('')




chooseWord(wordlist)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
