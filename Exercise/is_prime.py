#!/usr/bin/python

def is_prime(number):
    for i in range(2,number):
#check if number is divisible by 2 and number-1
        if number % i == 0:
            return False

    return True

print(is_prime(11))

print("%"*20)

#Sum upto n numbers

def sum_upto_n(number):

    sum = 0
    for i in range(1,number+1):
        sum = sum + i

    return sum

print(sum_upto_n(6))
print(sum_upto_n(10))

print('&'*20)
#To print a number triangle

def print_a_no_triangle(number):
    for j in range(1,number+1):
        for i in range(1,j+1):
            print(i,end=' ')
        print()

print_a_no_triangle(5)
