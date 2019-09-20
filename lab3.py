#Javier Diaz

# I pledge my honor that I have abided by the Stevens Honor System

def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == [] or amount < 0:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        return min(change(amount, coins[1:]),1 + change(amount - coins[0], coins))
