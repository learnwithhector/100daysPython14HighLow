from data import data
from art import logo, vs
import random
import os

print(logo)
print()
score = 0
valid_choices = ['a', 'b']

a = random.choice(data)
b = random.choice(data)

while True:
    # print(a)
    # print(b)  # TODO Delete after debugging

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print()
    print(vs)
    print()
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    print()

    answer = 'c'
    while answer not in valid_choices:
        answer = input("Who has more followers? Type 'a' or 'b': ").casefold()

    if ((answer == 'a' and a['follower_count'] >= b['follower_count']) or
        (answer == 'b' and b['follower_count'] >= a['follower_count'])):
        os.system('cls')
        print(f"{a['name']} has {a['follower_count']} million followers, compared to {b['name']} who has "
              f"{b['follower_count']} million. Correct!")
        score += 1
        print()
        print(f"Current score {score}")
        print()
        a = b
        b = random.choice(data)
    else:
        print()
        print(f"{a['name']} has {a['follower_count']} million followers, compared to {b['name']} who has "
              f"{b['follower_count']} million. Wrong!")
        break

print()
print(f"Your final score was {score} point{'' if score == 1 else 's'}")
