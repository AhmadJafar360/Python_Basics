# Generating Random Values

import random

# for i in range(3):
#     print(random.randint(10, 20))

members = ['Ahmad','Jafar','Ali']
leader = random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first = random.randint(2, 3)
        second = random.randint(2, 3)
        return first, second
dice = Dice()
print(dice.roll())