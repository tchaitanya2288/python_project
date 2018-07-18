#!/usr/bin/python

def cal_simple_intrest(principal,intrest,duration):
    total_intrest = intrest*0.01*duration*principal
    total_amount  = principal + total_intrest
    return total_amount

print(cal_simple_intrest(10000,5,5))