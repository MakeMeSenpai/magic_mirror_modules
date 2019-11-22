from random import random, choice
#installation porblems with processing 5, good luck
from p5 import *

class fish:
    def __init__(self, size, color):
        self.size = size #int
        self.color = color #str
        self.speed = "" #int
        self.X = "" #int
        self.Y = "" #int
        self.Z = "" #int
    
    def start_location(self):
        #should determine whether or not fished will be placed in the z-index -4 or -3
        # and should randomly plot fish all over the screen in the begging of the codes runtime
        self.X = random.randint(0, 1000) #max number should be canvous size
        self.Y = random.randint(0, 1000) 
        self.Z = random.randint(3, 4)
        self.size = self.size * self.Z

    def swimming(self):
        #swims in a certain derection until timmer runs out in which they must change their
        # direction, or if they run into an obsticle
        pass

#runs our code
size = random.randint(11, 39)
print(size)
#chooses a random size at birth
size = random.randint(11, 39)
#chooses a random color at birth
colors = ["red", "orange", "yellow", "green", "blue", "indago", "violet"]
color = random.choice(colors)
#creating our fish
one = fish(size, color)
two = fish(size, color)
three = fish(size, color)
one.start_location()
two.start_location()
three.start_location()
#gives us test results
num = 0
fish_bowl = [one, two, three]
for fish in fish_bowl:
    print(num + ": " + fish)
    num += 1