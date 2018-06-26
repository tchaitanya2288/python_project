#!/usr/bin/python
'''
A group of code statements which can perform some specific task
methods are reusable and can be called when needed in the code
'''

def sum_numbs(n1,n2,n3):
    print(n1 + n2 + n3)

sum_numbs(30,50,20)
print('##########')
print('*************')

def isMetro(city):
    l=['Hyd','Vizag','Thirupathi','Delhi']
    if city in l:
        return True
    else:
        return False
x=isMetro('medak')
print(x)