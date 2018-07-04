#!/usr/bin/python


def exceptionhandling():
    try:
        car = {'make':'bmw','model':'330i','year':2015}
        print(car["color"])
    except:
        print("The exception block")
    finally:
        print("The final block")
exceptionhandling()
