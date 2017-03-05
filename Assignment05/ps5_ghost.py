# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()
print
# TO DO: your code begins here!

def charInput(fragment, player):
    while True:
        msg = 'Player '+str(player)+' says letter: '
        char = raw_input(msg)
        if char == '.': break
        fragment += char.lower()
        print
        print "Current word fragment: '"+fragment+"'"
        if fragment in wordlist and len(fragment) > 3:
            print 'Player '+str(player)+" loses because '"+fragment+"' is a word!"
            print 'Player '+str(player % 2 + 1)+' wins!'
            break

        test = False
        for word in wordlist:
            if fragment in word:
                test = True
                break
        if not test:
            print 'Player '+str(player)+" loses because no word begins with '"+fragment+"'!"
            print 'Player ' + str(player % 2 + 1) + ' wins!'
            break

        # if player == 1:
        #     player = 2
        # else: player = 1
        player = player % 2 + 1
        print 'Player '+str(player)+"'s turn."
    # msg = 'Player ' + str(player) + ' says letter: '
    # char = raw_input(msg)
    return None

# charInput('', 1)

def ghost():
    print 'Welcome to Ghost!'
    print 'Player 1 goes first.'
    print "Current word fragment: ''"
    fragment = ''
    player = 1
    charInput(fragment, player)
    return None

ghost()
