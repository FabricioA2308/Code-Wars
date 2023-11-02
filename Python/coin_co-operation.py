# https://www.codewars.com/kata/64fc00392b610b1901ff0f17/python 

def get_coin_balances(lst1, lst2):
    person1, person2 = 3, 3

    shares1, shares2 = lst1.count("share"), lst2.count("share")

    person1 += 3 * shares2 - 1 * shares1
    person2 += 3 * shares1 - 1 * shares2

    return person1, person2

# Expected result: (3, 11)    
print( get_coin_balances(['share', 'share', 'share'], ['steal', 'share', 'steal']) )