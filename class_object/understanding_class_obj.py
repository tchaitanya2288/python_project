"""
object oriented programmimg
_init_ -->  is a function or method used to intialize all the objects that we go to create with the class
"""

class Car(object):

    def __init__(self,make,model):
        self.make = make
        self.model= model
c1 = Car('bmw','550i')
print(c1.make)
print(c1.model)







