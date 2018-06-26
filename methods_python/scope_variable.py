a = 10

# def test_method(a):
#     print("The value of a is:", str(a))
#     a=2
#     print("The value of local variable a is:",str(a))
#
# print("The value of global variable is :",str(a))
# test_method(a)
# print("did the value global variable changed??", str(a))

def test_method():
    global a
    print("The value of 'a' is:", str(a))
    a=2
    print("The value of local variable 'a' is:",str(a))

print("The value of global a variable is :",str(a))
test_method()
print("did the value global a changed??", str(a))