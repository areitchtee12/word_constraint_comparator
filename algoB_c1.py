import random
import time

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def satisfies_constraint(word):
    return len(word) == 5

def preprocess_valid_words(words):
    return [w for w in words if satisfies_constraint(w)]

def random_word_preprocessed(valid_words):
    return random.choice(valid_words)

if __name__ == '__main__':
    start_time = time.time()
    english_words = load_words()

    # Preprocess once
    filtered_words = preprocess_valid_words(english_words)

    print(random_word_preprocessed(filtered_words))
    end_time = time.time()
    print(end_time - start_time)
