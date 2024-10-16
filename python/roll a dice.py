def roll_a_dice():
    # roll a dice
    return random.randint(1,6)


def order_dice(d1, d2):
    # change the order of the dice to highest value first and join the values together
    if d1>= d2:
        return int(d1+ d2)
    else:
        return int(d2 + d1)


def output_throw():
    #output the results of the two dice thrown
    dice1 = 0
    dice2 = 0
    while dice1 == dice2:
        dice1 = str(roll_a_dice())
        dice2 = str(roll_a_dice())
        print("Dice 1:",dice1)
        print("Dice 2:",dice2)
        roll = order_dice(dice1,dice2)
        return roll



#main program
#this tool outputs the vlue of two dice

import random
print(output_throw())
