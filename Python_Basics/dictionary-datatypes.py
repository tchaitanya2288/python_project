#!/usr/bin/python

cars = {'make' : 'Benz','model' : '550i','year' : 2016}
print(cars)
print('*#'*20)
print(cars['model'])
d = {}     #empty dictionary
d['one'] = 1  #we can add values to dict i.e mutable datatype
d['two'] = 2
d['three'] = 3
print(d)
sum_1 = d['two']+8
print(sum_1)
print(d)
print('*#'*20)
d['two'] = d['two']+8
print(d)