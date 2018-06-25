#!/usr/bin/python

d = {'k1':{'nest1':'nestvalue1','nest2':'nestvalue2'}}
a = d['k1']['nest1']
cars ={'Benz':{'model':'550i','year':2016},'Audi':{'model':'550a','year':2017}}
benz_year = cars['Benz']['year']
print(benz_year)
print(cars)
print(d)
print(a)