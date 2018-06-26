#!/usr/bin/python
#string for loop

my_str = "abcabc"
for m in my_str:
    print(m,end='')
print()

value = "dcbabc"
for c in value:
    print(c)
print('#'*20)

str1 = 'ddbbccaa'
for i in str1:
    if i == "b":
        print('B',end='')
    else:
        print(i,end='')
print()

#list for loop
cars = ['bmw','benz','honda','audi']
for car in cars:
    print(car)
print()

num = [1,2,3]
for n in num:
    print(n*10,end=' ')
print()
#Dict for loop
d = {'one':1,'two':2,'three':3}
for k in d:
    print(k +" " + str(d[k]))
    #print(k)
print('#'*20)
for k,v in d.items():
    print(k)
    print('************')
    print(v)
    print('************')