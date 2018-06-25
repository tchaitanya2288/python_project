"""
and
###########
true and true --> true
true and false --> false
false and false --> false
###########
or
%%%%%%%%%%
true or true --> true
true or false --> true
false or false --> false
%%%%%%%%%%
not true --> false
not false --> true

"""

and_output1 = (10 == 10)and(10>=9)
and_output2 = (10 == 10)and(10<=9)
and_output3 = (10 != 10)and(10>=12)
print(and_output1)
print(and_output2)
print(and_output3)
or_output1 = (10 == 10)or(10<=9)
or_output2 = (10 == 10)or(10>=9)
or_output3 = (10 != 10)or(10>=12)
print(or_output1)
print(or_output2)
print(or_output3)
not_true = not(10==10)
not_false = not(12>18)
print(not_true)
print(not_false)