'''
Find how many paths there are in a 20x20 grid 
from the top left corner to the bottom right corner.
'''

import math 

cord1 = 20
cord2 = 20
nk = 1
n = 1
k = 1


temp = cord1 + cord2
while temp > 1:
    nk *= temp
    temp -= 1

temp = cord1
while temp > 1:
    k *= temp
    temp -= 1

temp = cord2
while temp > 1:
    n *= temp
    temp -= 1


paths = (nk /(k*n) )

print(paths)