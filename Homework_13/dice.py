# ● Dice Rolling Simulator:
# ○ Develop a simple dice rolling simulator. Generate random numbers between 1 and 6 to
# simulate the roll of a six-sided die using the random module.

import random

def dice():
    return f"Number is : {random.randint(1,6)}"

print(dice())