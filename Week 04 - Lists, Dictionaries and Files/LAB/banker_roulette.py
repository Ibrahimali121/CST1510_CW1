import random

friends = ["Jim","Faisal","Tayyab","Robert"]

payer = random.choice(friends)

print(payer, "Will be the indvidual that will be playing the bill today")

# version 2

import random
num_friends = len(friends)

index = random.randint(0, num_friends -1)

payer = friends [index]

print(payer, "will be paying the food bill today")
           