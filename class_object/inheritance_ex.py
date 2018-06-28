#!/usr/bin/python

class Car(object):
    def __init__(self):
        print("You just created car Instance")
    def drive(self):
        print("Car just Started")
    def stop(self):
        print("car stopped....")

class Bmw(Car):                    #child class
    def __init__(self):
        Car.__init__(self)
        print("You just created Bmw car instance")
    def drive(self):
        super(Bmw,self)
        print("You are driving Bmw enjoy...........")
    def headsup_display(self):
        print("This is unique feature of Bmw")


c1 = Car()
c1.drive()
c1.stop()

b = Bmw()
b.drive()
b.headsup_display()
b.stop()