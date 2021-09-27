# Imporing Modules
from random import randint

# Roll Dice Function
def roll_dice():
    '''
    Rolls the Dice, and returns a random number between 1 and 6
    '''
    print("Rolling the Dice...")
    dice_result = randint(1, 6)
    return f"{dice_result}"

# Mail Loop
while True:
    a = input("Press Enter to Roll the Dice: ")
    if a == "":
        result = roll_dice()
        print(result)
    if a != "":
        break
