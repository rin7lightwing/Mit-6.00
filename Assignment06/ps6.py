# Problem Set 5: 6.00 Word Game
# Name: Lin Jiang
# Collaborators: 
# Time: 07:20 -
#

import random
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
points_dict = {}

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
        # print letter, score
    if len(word) == n:
        score += 50
    return score
    # DONE


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,  # print all on the same line
    print  # print an empty line


#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

word_list = load_words()
hand = deal_hand(HAND_SIZE)
# print hand


def build_subStr(string):
    subset = []
    if len(string) == 1:
        subset.append(string)
    else:
        for substring in build_subStr(string[:-1]):
            subset.append(substring)
            substring += string[-1]
            subset.append(substring)
        subset.append(string[-1])
        subset = list(set(subset))     # set: Build an unordered collection of unique elements.
        subset.sort()
    return subset



def get_word_rearrangements(word_list):
    rearrange_dict = {}
    for word in word_list:
        rearrange_dict[''.join(sorted(word))] = word
    return rearrange_dict

rearrange_dict = get_word_rearrangements(word_list)



def pick_best_word_faster(hand, rearrange_dict):
    hand_string = ''
    for key in hand:
        if hand[key] > 0:
            hand_string += key * hand[key]
    # print hand_string

    str_set = build_subStr(hand_string)
    # print str_set
    best_word = ''
    best_score = 0
    for string in str_set:
        rearrange_str = ''.join(sorted(string))
        # print string
        # print rearrange_str
        if rearrange_str in rearrange_dict:
            str_score = get_word_score(rearrange_str, HAND_SIZE)
            # print rearrange_str, str_score
            if str_score > best_score:
                best_word = rearrange_dict[rearrange_str]
                best_score = str_score
                # print best_word, best_score
    if best_score > 0:
        return best_word
    else: return '.'


# print pick_best_word_faster(hand, rearrange_dict)


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    for i in word:
        hand[i] = hand.get(i, 0) - 1
    return hand
    # Done



def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    global points_dict
    for word in word_list:
        points_dict[word] = get_word_score(word, HAND_SIZE)
    return points_dict


# points_dict = get_words_to_points(word_list)


def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return word in points_dict

    # Done

def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the given hand.
    Return '.' if no words can be made with the given hand.
    """
    bestWord = ''
    bestWord_Value = 0
    for word in points_dict.keys():
        if is_valid_word(word, hand, points_dict):
            word_Value = points_dict[word]
            if word_Value > bestWord_Value:
                bestWord = word
                bestWord_Value = word_Value
    if bestWord_Value > 0:
        return bestWord
    return '.'

# print pick_best_word(hand, points_dict)

def get_time_limit(points_dict, k):
    """
     Return the time limit for the computer player as a function of the
    multiplier k.
     points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

# print get_time_limit(points_dict, 7)






def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    print 'Current hand:',
    display_hand(hand)
    totalScore = 0
    score = 0
    while True:
        start_time = time.time()
        word = raw_input('Enter word, or a . to indicate that you are finished: ')
        end_time = time.time()
        total_time = end_time - start_time
        if total_time == 0:
            total_time = 1
        if word == '.':
            print 'Game ended.'
            break
        if not is_valid_word(word, hand, word_list):
            print 'Invalid word. Please choose another word.'
        else:
            # hand = update_hand(hand, word)
            print 'It took %0.2f seconds to provide an answer.' % total_time
            score = get_word_score(word, HAND_SIZE) / total_time
            totalScore += score
            print '%s earned %0.2f points.' % (word, score), 'Total: %0.2f points.' % totalScore
            # word, 'earned', score, 'points.', 'Total: ', totalScore, 'points.'
            print 'Current hand:',
            display_hand(hand)
            # print hand

            sum = 0
            for value in hand.values():
                sum += value
            if sum == 0:
                print 'Hand finished.'
                break
    print 'Total points: %0.2f' % totalScore
    # Done
# play_hand(hand, word_list)



# Problem #2: Time Limit
def play_hand2(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    print 'Current hand:',
    display_hand(hand)
    totalScore = 0
    total_time = 0
    while True:
        start_time = time.time()
        word = raw_input('Enter word, or a . to indicate that you are finished: ')
        end_time = time.time()
        total_time += end_time - start_time
        if total_time == 0:
            total_time = 0.01

        if word == '.':
            print 'Game ended.'
            break
        if not is_valid_word(word, hand, word_list):
            print 'Invalid word. Please choose another word.'
        else:
            # hand = update_hand(hand, word)
            print 'It took %0.2f seconds to provide an answer.' % total_time
            if total_time > timeLimit:
                print 'Total time exceeds %d seconds. You scored %0.2f points.' % (timeLimit, totalScore)
                return totalScore
            else:
                print 'You have %0.2f seconds remaining.' % (timeLimit - total_time)
            score = get_word_score(word, HAND_SIZE) / total_time
            totalScore += score
            print '%s earned %0.2f points.' % (word, score), 'Total: %0.2f points.' % totalScore
            print 'Current hand:',
            display_hand(hand)
            # print hand

            sum = 0
            for value in hand.values():
                sum += value
            if sum == 0:
                print 'Hand finished.'
                break
    print 'Total points: %0.2f' % totalScore
    return totalScore

# play_hand2(hand, word_list)

timeLimit = get_time_limit(points_dict, 3)



# Problem #3: Computer Player
def play_hand3(hand, word_list, timeLimit):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    print 'Current hand:',
    display_hand(hand)
    totalScore = 0
    total_time = 0
    while True:
        start_time = time.time()
        word = pick_best_word(hand, points_dict)
        print 'Computer gave an answer:', word
        print
        end_time = time.time()
        total_time += end_time - start_time
        # if total_time == 0:
        #     total_time = 0.01
        if word == '.':
            print 'Game ended.'
            break

        print 'It took %0.2f seconds to provide an answer.' % total_time
        if total_time > timeLimit:
            print 'Total time exceeds %d seconds. You scored %0.2f points.' % (timeLimit, totalScore)
            return totalScore
        else:
            print 'You have %0.2f seconds remaining.' % (timeLimit - total_time)
        score = get_word_score(word, HAND_SIZE)
        totalScore += score
        print '%s earned %d points.' % (word, score), 'Total: %d points.' % totalScore
        print
        print 'Current hand:',
        hand = update_hand(hand, word)
        display_hand(hand)

        sum = 0
        for value in hand.values():
            sum += value
        if sum == 0:
            print 'Hand finished.'
            break
    print 'Total points: %d' % totalScore
    return totalScore

# play_hand3(hand, word_list, timeLimit)



# Problem #4: Even Faster Computer Player
def play_hand4(hand, rearrange_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    print 'Current hand:',
    display_hand(hand)
    totalScore = 0
    total_time = 0
    while True:
        word = pick_best_word_faster(hand, rearrange_dict)
        print 'Computer gave an answer:', word
        print
        if word == '.':
            print 'Game ended.'
            break

        score = get_word_score(word, HAND_SIZE)
        totalScore += score
        print '%s earned %d points.' % (word, score), 'Total: %d points.' % totalScore
        print
        print 'Current hand:',
        hand = update_hand(hand, word)
        display_hand(hand)

        sum = 0
        for value in hand.values():
            sum += value
        if sum == 0:
            print 'Hand finished.'
            break
    print 'Total points: %d' % totalScore
    return totalScore

play_hand4(hand, rearrange_dict)



# Problem #5: Playing a game
# O(N) for pick_best_word
# O(logN) for pick_best_word_faster





def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...

    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE)
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

# Build data structures used for entire session and play game
#
# if __name__ == '__main__':
#     word_list = load_words()
#     play_game(word_list)
