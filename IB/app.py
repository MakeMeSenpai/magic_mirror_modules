from random import random, choice

class fish:
    def __init__(self, size, color):
        self.size = size #int
        self.color = color #str
        self.speed = "" #int
        self.X = "" #int
        self.Y = "" #int
        self.Z
    
    def start_location(self):
        #should determine whether or not fished will be placed in the z-index -4 or -3
        # and should randomly plot fish all over the screen in the begging of the codes runtime
        self.X = random.int(0, 1000) #max number should be canvous size
        self.Y = random.int(0, 1000) 
        self.Z = random.int(3, 4)

    def swimming(self):
        #swims in a certain derection until timmer runs out in which they must change their
        # direction, or if they run into an obsticle
        pass

#runs all of our program
def run():
    one = fish(25, "red")
    two = fish(35, "blue")
    three = fish(15, "green")
    one.start_location()
    two.start_location()
    three.start_location()

run()