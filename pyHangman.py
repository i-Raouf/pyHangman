import string

def hangman(word):
    word = word.upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

if __name__ == '__main__':
    hangman("hello")