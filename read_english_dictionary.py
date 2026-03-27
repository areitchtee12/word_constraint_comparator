import time
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()

    start_time = time.time()
    end_time = time.time()
    print(end_time - start_time)