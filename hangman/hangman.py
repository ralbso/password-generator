# Hangman game

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

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed; 
      False otherwise
    '''
    letters_in_word = []
    for letter in lettersGuessed:
        if letter in secretWord:
            letters_in_word.append(letter)
            
    if sorted(set(letters_in_word)) == sorted(set(secretWord)):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed; 
      False otherwise
    '''
    guess = []
    hidden = ' _ '
    revealed = ''
    for letter in lettersGuessed:
        if letter in secretWord:
            guess.append(letter)
    
    if len(guess) == len(secretWord):
        revealed = secretWord
    else:
        for letter in secretWord:
            if letter not in guess:
                letter = hidden
                revealed += letter
            else:
                revealed += letter
    
    return revealed



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = string.ascii_lowercase
    
    for letter in lettersGuessed:
        if letter in alpha:
            alpha = alpha.replace(letter,'')
    return alpha
    

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')
    
    correct = False
    incorrect = False
    
    guess_count = 8
    guessed_letters = ''
    correct_letters = ''
    
    while not correct or not incorrect:
        
        if isWordGuessed(secretWord, correct_letters):
            correct = True
            print('Congratulations, you won!')
            break
        
        if guess_count <= 0:
            incorrect = True
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        
        print('You have', guess_count, 'guesses left.')
        print('Available Letters:', getAvailableLetters(guessed_letters))
        guess = str(input('Please guess a letter: ').lower())
        
            
        if guess in guessed_letters:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, correct_letters))
            print('-------------')
            continue
            
        if guess in secretWord:
            correct_letters += guess
            print('Good guess:', getGuessedWord(secretWord, correct_letters))
            guessed_letters = guessed_letters + str(guess)
            
        elif guess not in secretWord:
            guess_count -= 1
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, correct_letters))
            guessed_letters = guessed_letters + str(guess)
            
        print('-------------')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
