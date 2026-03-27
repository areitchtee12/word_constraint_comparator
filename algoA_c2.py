import random
import time

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def satisfies_constraint(word):
    return "ee" in word   # <-- change this to any rule you want

def random_word_rejection(words):
    while True:
        word = random.choice(list(words))  # pick a random word
        if satisfies_constraint(word):     # check constraint
            return word                    # accept it

if __name__ == '__main__':
    start_time = time.time()
    english_words = load_words()
    print(random_word_rejection(english_words))
    end_time = time.time()
    print(end_time - start_time)