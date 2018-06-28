"""
object oriented programmimg
_init_ -->  is a function or method used to intialize all the objects that we go to create with the class
"""

class Car(object):

    wheels = 4 #member variable

    def __init__(self,make,model):
        self.make = make
        self.model= model

    def info(self):
        print("make of the car:",self.make)
        print("model of the car:",self.model)

c1 = Car('Bmw','550i')
c1.info()
c2 = Car("Audi","330A")
c2.info()

print(Car.wheels)





