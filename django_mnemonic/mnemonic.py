from wordlist import WORDS
import random

def random_word():
    return WORDS[random.randint(0,len(WORDS))].title()
