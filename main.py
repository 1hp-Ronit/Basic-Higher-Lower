from art import arts
from Data import celebrities
import random

play = True
celeb1 = ''
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


def Start():
    global play
    to_play = input("Type 'yes' to play a game of higher or lower, Type 'no' other wise\n").lower()
    if to_play == 'yes':
        print(arts[0])
        points = 0
        while play:
            choose_celeb()
            print(f"Compare A: {celeb1["name"]}, a {celeb1["profession"]}, from {celeb1["residence"]}")
            print(arts[1])
            print(f"Against B: {celeb2["name"]}, a {celeb2["profession"]}, from {celeb2["residence"]}")
            choice = input("Who has more followers in M? Type 'A' or 'B':\n").lower()
            match choice:
                case 'a':
                    if celeb1["instagram_followers"] > celeb2["instagram_followers"]:
                        points += 1
                        print(f"Ayo you on fire, Your points {points}")
                    elif celeb1["instagram_followers"] < celeb2["instagram_followers"]:
                        print(f"You lost with {points = }")
                        play = False
                        break
                case 'b':
                    if celeb1["instagram_followers"] < celeb2["instagram_followers"]:
                        points += 1
                        print(f"Ayo you on fire, Your points {points}")
                    elif celeb1["instagram_followers"] > celeb2["instagram_followers"]:
                        print(f"You lost with {points = }")
                        play = False
                        break
    else:
        print('Bye')
Start()