#!/usr/bin/python

class Car(object):
    def __init__(self):
        print("You just created car Instance")
    def drive(self):
        print("Car just Started")
    def stop(self):
        print("car stopped....")

c1 = Car()
c1.drive()
c1.stop()