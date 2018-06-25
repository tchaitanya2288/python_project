"""
break --> to Break out the closest enclosing loop
continue --> go to the start of closest enclosing loop
"""
x = 0
while x<10:
    print("The value of x is:",x)
    x += 1
    if x == 8:
        continue
    print("The example is awesome")
    print('*'*20)
print("come out of the loop")