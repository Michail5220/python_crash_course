from random import randint

class Dice:
    """A Dice class that utilises random function"""

    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        print(f"Throwing a {self.sides} side Dice: {randint(1,self.sides)}")


a_die = Dice(6)

# i=0
# while i<10:
#     a_die.roll_die()
#     i+=1

# b_die = Dice(10)

# i=0
# while i<10:
#     b_die.roll_die()
#     i+=1


def get_combination(a_list, combo_length):
    
    winning_string = ''

    for value in range (1,combo_length+1):
        tuple_index = randint(0,len(a_list)-1)
        winning_string = winning_string + str(a_list[tuple_index])

    return winning_string


# my_tuple = ('a', 'b','c','d', 0,1,2,3,4,5,6,7,8,9)
my_list = ['a', 'b','c','d', 0,1,2,3,4,5,6,7,8,9]
winning_combo=get_combination(my_list, 4)

print(f"We are trying to match this combination: {winning_combo}.\n" 
      f"Let's see how many iterations to 'win' by finding a match.")

flag=True
i=0

while flag:
    i+=1
    try_combo = get_combination(my_list, 4)
    if try_combo == winning_combo:
        flag=False

print(f"It was necessary to play the game {i} times to get a match! {try_combo}")

# Go to python module of the week: https://pymotw.com