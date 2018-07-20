#!/usr/bin/python

i = 0
while i < 5:

    print(i)
    i = i+1

# i = 0
# while i < 5:
#     print(i,end=" ")
#     i = i + 1

print('#'*20)

def print_square_number(limit):
    i=1
    while i*i < limit:
        print(i*i)
        i=i+1

print_square_number(30)

print('&'*20)
def print_cube_number(limit):
    i=1
    while i*i*i < limit:
        print(i*i*i)
        i=i+1

print_cube_number(30)