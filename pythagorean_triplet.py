'''
Find the product of the pythagorean triplet abc where a+b+c = 1000.
200 x 375 x 425 = 31875000
'''

import math 

found = False  

for a in range(1, 1001):
    for b in range(1, 1001):

        c = math.sqrt((a**2) + (b **2))

        if c.is_integer(): 
            if a + b +c == 1000:
                found = True
                break
    if found:
        break
    
print(a,'x',b,'x',c,'=', (a*b*c))



