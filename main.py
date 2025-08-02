from art import arts
from Data import celebrities
import random

play = True
celeb1 = 'yo'
celeb2 = ''


def choose_celeb():
    global celeb1, celeb2
    celeb1 = random.choice(celebrities)
    celeb2 = None

    diff_celeb = False
    while not diff_celeb:
        temp_celeb = random.choice(celebrities)
        if celeb1['name'] != temp_celeb['name']:
            celeb2 = temp_celeb
            diff_celeb = True
choose_celeb()


