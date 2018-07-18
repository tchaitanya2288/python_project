#!/usr/bin/python

def sample1_method(no_of_times):
    for i in range(1,no_of_times+1):
        print("Hello World")

sample1_method(5)

print("#################")

def numbers_sample(n):
    for i in range(1,n+1):
        print(i)

numbers_sample(10)

print("%%%%%%%%%%%%%%%%%%%")

def squre_num(n):
    for i in range(1,n+1):
        print(i*i)

squre_num(10)

print('$$$$$$$$$$$$$$$$$')

def sample2_method(str,n):
    for i in range(1,n+1):
        print(str)

sample2_method("Hello World",5)
print("&&&&&&&&&&&&&&&&&&&&&")

#By giving Default value in method
def sample3_method(str="Welcome to Python",n=5):
    for i in range(1,n+1):
        print(str)

sample3_method()
#sample3_method("Hey hi i am chaithnay",3)

