# Imporing Modules
from random import randint

def roll_dice():
    print("Rolling the Dice...")
    dice_result = randint(1, 6)
    return f"{dice_result}"

while True:
    a = input("Press Enter to Roll the Dice: ")
    if a == "":
        result = roll_dice()
        print(result)
    if a != "":
        break
