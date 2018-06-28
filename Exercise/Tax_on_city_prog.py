#!/usr/bin/python
'''
create a method that takes state and gross income as arguments and that returns net income
after deducting tax based on state
Assume Federal Tax 10%
Assume state Tax As your wish.
'''

def calculate_netincome(gross,state):

    state_tax = {'Mississauga': 12,
                 'Brampton' : 13,
                 'Kitchner' : 11,
                 'Toronto' : 13}
    #calculate net_income after Federal tax
    net = gross-(gross*.10)
    if state in state_tax:
        net = net-(gross*state_tax[state]/100)
        print("The income after all the heavy deduction is:",str(net))
        return net
    else:
        print("The state is not in the list")
        return None
calculate_netincome(70000,'Brampton')