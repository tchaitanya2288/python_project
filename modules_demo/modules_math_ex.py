import math
from math import sqrt
#import modulesexternal.car as car
#from modulesexternal import car
from modulesexternal.car import info

class modules_demo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(64))
    def car_description(self):
        make = "Audi"
        model= "55ai"
        info(make,model)


m = modules_demo()
#m.builtin_modules()
m.car_description()