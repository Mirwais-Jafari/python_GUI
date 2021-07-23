
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("""
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    
""")
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

    return random.choice(wordlist)
# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for c in secretWord:
    	if c in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False


def getGuessedWord(secretWord, lettersGuessed):

    count = 0
    blank = ['_'] * len(secretWord)

    for c in secretWord:
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)

def getAvailableLetters(lettersGuessed):
    alphabet=list(string.ascii_lowercase)

    def removeDupsBetter(L1, L2):
        L1Start = L1[:]

        for e in L1:
            if e in L1Start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)

    return removeDupsBetter(lettersGuessed, alphabet)

def hangman(secretWord):
    print(secretWord)
    lenght_word= str(len(secretWord))
    lettersGuessed = []
    guess = str
    chance= 8
    wordGuessed = False

    print('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + lenght_word + ' letters long.')
    print ('------------')

    while chance > 0 and chance <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ' + str(chance) + ' guesses left.')
        print ('Available letters: '+ getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess.isalpha() and len(guess)==1:
            if guess in secretWord:
                if guess in lettersGuessed:
                    print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                    print ('------------')
                else:
                    lettersGuessed.append(guess)
                    print ('Good guess: '+ getGuessedWord(secretWord, lettersGuessed))
                    print ('------------')
            else:
                if guess in lettersGuessed:
                    print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                    print ('------------')
                else:
                    lettersGuessed.append(guess)
                    chance -= 1
                    print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                    print ('------------')
        else:
            if len(guess)>1:
                print('pleas enter one letter.')
            else:
                print('Oh no! only letter not number.')
                chance-=1

    if wordGuessed ==True:
        print( 'Congratulations, you won!')
        print("You have guessed all the letters in the word")
        print("""

        db   d8b   db d888888b d8b   db 
        88   I8I   88   `88'   888o  88 
        88   I8I   88    88    88V8o 88 
        Y8   I8I   88    88    88 V8o88 
        `8b d8'8b d8'   .88.   88  V888 
         `8b8' `8d8'  Y888888P VP   V8P 
          """)
    elif chance == 0:
        print ('Sorry, you ran out of guesses. The word was ' + secretWord)
        print("""
         _______   _______   _______   _______ 
        ( ____ \  (  ___  ) (       ) (  ____ 
        |
        (      \/ | (   ) | | () () | | (    \/
        | |       | (___) | | || || | | (__    
        | | ____  |  ___  | | |(_)| | |  __)   
        | | \_  ) | (   ) | | |   | | | (      
        | (___) | | )   ( | | )   ( | | (____/
        

         _______           _______  _______ 
        (  ___  )|\     /|(  ____ \(  ____ )
        | (   ) || )   ( || (    \/| (    )|
        | |   | || |   | || (__    | (____)|
        | |   | |( (   ) )|  __)   |     __)
        | |   | | \ \_/ / | (      | (\ (   
        | (___) |  \   /  | (____/\| ) \ \__
        (_______)   \_/   (_______/|/   \__/""")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)