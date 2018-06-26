# some built in functions
# max()-->It takes any number of arguments and retuns largest one
# min()-->It takes any number of arguments and retuns smallest one
# type()-->It returns type of data it receives as an argument
# abs() --> It returns the absolute value of the number,that number's distance from 0
#It always returns positive value and it only takes single value

def largest_num(*args):
    print(max(args))
    return
largest_num(10,20,34,56,100)

def smallest_num(*args):
    print(min(args))
    return
smallest_num(12,45,67,89,-12)