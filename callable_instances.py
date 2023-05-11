import random

file_path = "DATA/words.txt"

class RandomWordA:
    def __init__(self) -> None:
        self._load_words()

    def _load_words(self):
        self.words = open(file_path).read().splitlines()

    def get_random_word(self):
        return random.choice(self.words)

ra = RandomWordA()
for _ in range(10):
    print(ra.get_random_word())
print('-' * 60)

class RandomWord:
    def __init__(self) -> None:
        self.words = open(file_path).read().splitlines()

    def __call__(self):
        return random.choice(self.words)

word = RandomWord()
for _ in range(10):
    print(word())



