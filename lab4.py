# Javier Diaz
# CS 115
# KnapSack Lab 9/27/2018

# I pledge my honor that I have abided by the Stevens Honor System

def knapsack(capacity,itemList):
    if capacity <= 0 or itemList == []:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity,itemList[1:])
    else:
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        useoutput = [use[0] + itemList[0][1], [itemList[0]] + use[1]]
        loseoutput = [lose[0], lose[1]]
        if use[0] <= lose[0]:
            return max(useoutput,loseoutput)
    
