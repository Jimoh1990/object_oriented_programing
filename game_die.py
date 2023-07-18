from random import randint

class Die:
    """initialising a class for die"""
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

#create a 6 sided die
rolled_6 = Die()
print("Rolling a 6 sided die 10 times:")
for i in range(10):
    rolled_6.roll_die()

# create a 10 sided die
rolled_10 = Die(10)
print("Rolling a 10 sised die 10 times:")
for i in range(10):
    rolled_10.roll_die()

# create a 20 sided die
rolled_20 = Die(20)
print("Rolling a 20 sided die 10 times")
for i in range(10):
    rolled_20.roll_die()
