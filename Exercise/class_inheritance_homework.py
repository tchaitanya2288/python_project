#!/usr/bin/python

class Fruit(object):
    def __init__(self):
        print("The fruit is very good for health")
    def nutrition(self):
        print("If we eat this fruit we get good nutritions")
    def fruit_shape(self):
        print("The fruit is in round shape")
class Banana(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("You just created banana fruit class")
    def nutrition(self):
        print("The fruit has more vitamins")
    def color(self):
        print("The banana is in yellow color")

f = Fruit()
f.nutrition()
f.fruit_shape()

b = Banana()
b.nutrition()
b.fruit_shape()
b.color()