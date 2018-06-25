#!/usr/bin/python

car = {'make' :'bmw','model' : '550i','year' : 2016}
cars = {'Bmw':{'model':'550i','year':2016},'Audi' : {'model':'550a','year':2017}}
print(car.keys())

print(cars.keys())

print(car.values())
print(cars.values())
print(car.items())
print(cars.items())
a =car.copy()
print(a)
print(car.pop('model'))
print(car)
d={"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}
print(d["key1"][2])