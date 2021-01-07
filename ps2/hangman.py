# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for i in letters_guessed:
        if i in secret_word:
            count += 1
    if len(letters_guessed) >= count:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = list()
    
    for i in list(secret_word):
        if i in letters_guessed:
            guessed.append(i)
        else:
            guessed.append("_ ")
            
    return "".join(guessed)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabets = list(string.ascii_lowercase)
    for i in alphabets:
        if i in letters_guessed:
            alphabets.remove(i)
    return "".join(alphabets)

def welcome(length,warnings):
    print("Welcome to the Hangman")
    print("I am thinking of a {} chracters long word".format(length))
    print("You have {} warnings left".format(warnings))
    print("=="*10)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length = len(secret_word)
    num_guesses = length + 3
    warnings = 3
    vowels = "aeiou"
    letters_guessed = list()
    welcome(length,warnings)
    
    
    while num_guesses > 0:
        print("-"*20)
        
        print("You have {} guesses left".format(num_guesses))
        print("Available Letters: {}".format(get_available_letters(letters_guessed)))
        
        letter = input("Guess a Word: ")
        # check if letter already guessed
            
        
        # check if character is valid
        if (not str.isalpha(letter)) or (len(letter) > 1) or (letter in letters_guessed):
            warnings -= 1
            if letter in letters_guessed:
                print("Oops! you have already guessed that letter. You have {} warnings left".format(warnings))
            else:
                print("Please enter valid character. You have {} warnings left".format(warnings))
        else:
            letters_guessed.append(letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            
            if letter in secret_word:
                print("Good Guess: {}".format(guessed_word))
            else:
                print("Oops that was wrong guess: {}".format(guessed_word))
                if letter in vowels:
                    num_guesses -= 2
                else:
                    num_guesses -= 1
        
        if warnings == 0:
            print("*** Warnings Exceeded. You lose 1 guess ***")
            num_guesses -= 1
            
        if "_ " in letters_guessed:
            score = num_guesses*len(set(letters_guessed)) - 2
        else:
            score = num_guesses*len(set(letters_guessed))
        
        if is_word_guessed(secret_word, letters_guessed) and ("_ " not in guessed_word) :
            print("Congratulations... You Won")
            print("*** Score: {} ***".format(score))
            break
        
    if "_ " in guessed_word:
        print("You Lost!")
        print("*** Score: {} ***".format(score))
        
        
    
        
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ","")
    if len(my_word) != len(other_word):
        return False
    
    t = 0
    for i,j in zip(my_word,other_word):
        #print(i,j)
        if i == j or i == "_":
            t += 1
            
    if t == len(my_word) : return True
    else: return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    cond = False
    for i in wordlist:
        if match_with_gaps(my_word, i):
            cond = True
            print(i)
    if not cond: print("No Matches Found!")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    length = len(secret_word)
    num_guesses = length + 3
    warnings = 3
    vowels = "aeiou"
    letters_guessed = list()
    welcome(length,warnings)
    
    
    while num_guesses > 0:
        print("-"*20)
        
        print("You have {} guesses left".format(num_guesses))
        print("Available Letters: {}".format(get_available_letters(letters_guessed)))
        
        letter = input("Guess a Word: ")
        # check if letter already guessed
            
        
        # check if character is valid
        
        if letter == "*":
            show_possible_matches(guessed_word)
            
        elif (not str.isalpha(letter)) or (len(letter) > 1) or (letter in letters_guessed):
            warnings -= 1
            if letter in letters_guessed:
                print("Oops! you have already guessed that letter. You have {} warnings left".format(warnings))
            else:
                print("Please enter valid character. You have {} warnings left".format(warnings))
            
        else:
            letters_guessed.append(letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            
            if letter in secret_word:
                print("Good Guess: {}".format(guessed_word))
            else:
                print("Oops that was wrong guess: {}".format(guessed_word))
                if letter in vowels:
                    num_guesses -= 2
                else:
                    num_guesses -= 1
        
        if warnings == 0:
            print("*** Warnings Exceeded. You lose 1 guess ***")
            num_guesses -= 1
            
        if "_ " in letters_guessed:
            score = num_guesses*len(set(letters_guessed)) - 2
        else:
            score = num_guesses*len(set(letters_guessed))
        
        if is_word_guessed(secret_word, letters_guessed) and ("_ " not in guessed_word) :
            print("Congratulations... You Won")
            print("*** Score: {} ***".format(score))
            break
        
    if "_ " in guessed_word:
        print("You Lost!")
        print("*** Score: {} ***".format(score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
