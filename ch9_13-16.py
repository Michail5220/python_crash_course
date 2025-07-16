from random import randint

class Dice:
    """A Dice class that utilises random function"""

    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        print(f"Throwing a {self.sides} side Dice: {randint(1,self.sides)}")


a_die = Dice(6)

i=0
while i<10:
    a_die.roll_die()
    i+=1

b_die = Dice(10)

i=0
while i<10:
    b_die.roll_die()
    i+=1