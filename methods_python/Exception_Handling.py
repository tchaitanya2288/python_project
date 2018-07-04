#!/usr/bin/python

def exceptionhandling():
    try:
        a=10
        b=20
        c=0

        d=(a+b)/c
        print(d)
    except:
        print("In the except block")
        #raise Exception("This is an exception")
    else:
        print("The else block executed")
    finally:
        print("The final block executed")

exceptionhandling()