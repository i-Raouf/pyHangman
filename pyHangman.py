from os import system
import string
import random

def printHangmanArt(lives): # Prints the ASCII art for the hangman
    frames = ['', '', '', '', '', '', '', '']
    frames[0] = ' /------+\n/\t|\n|\t|\n|      (_)\n|      /|\\\n|\t|\n|      / \\\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[1] = ' /------+\n/\t|\n|\t|\n|      (_)\n|      /|\\\n|\t|\n|      /\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[2] = ' /------+\n/\t|\n|\t|\n|      (_)\n|      /|\\\n|\t|\n|\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[3] = ' /------+\n/\t|\n|\t|\n|      (_)\n|      /|\\\n|\n|\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[4] = ' /------+\n/\t|\n|\t|\n|      (_)\n|      /|\n|\n|\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[5] = ' /------+\n/\t|\n|\t|\n|      (_)\n|       |\n|\n|\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[6] = ' /------+\n/\t|\n|\t|\n|      (_)\n|\n|\n|\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    frames[7] = ' /------+\n/\t|\n|\t|\n|\n|\n|\n|\n|_____________\n|\t      |_\n|\t\t|_\n|_________________|\n'
    print('\n'+frames[lives])

def get_word():
    system('clear')
    print('    __  __\n   / / / /___ _____  ____ _____ ___  ____ _____ \n  / /_/ / __ `/ __ \\/ __ `/ __ `__ \\/ __ `/ __ \\\n / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /\n/_/ /_/\\__,_/_/ /_/\\__, /_/ /_/ /_/\\__,_/_/ /_/ \n                  /____/                        ')
    wordLists = ['Places.txt', 'Animals.txt', 'Technology.txt']
    workListInput = ''
    while workListInput.strip() not in ['1', '2', '3']:
        workListInput = input('[1] Places \n[2] Animals \n[3] Technology \n\n Please input the number of the wordlist you would like to use: ')
    wordList = wordLists[int(workListInput)-1]
    file = open(wordList, 'r')
    words = file.readlines()
    system('clear')
    return str(random.choice(words)).strip().upper() # remove "\n" from word

def hangman():
    word = get_word()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        printHangmanArt(lives)
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').strip().upper() # Removes whitespace
        system('clear')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    system('clear')
    printHangmanArt(lives)
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()
