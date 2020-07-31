'''
Find the value of d < 1000 for which 1/d 
contains the longest recurring cycle in its decimal fraction part.
'''
from decimal import *

max_len = 1
max_denominator = 0

for i in range(2,1000):
    temp_len = 0
    temp_cy = ""
    getcontext().prec = i*10
    temp_dec = str(Decimal(1)/Decimal(i))

    for j in range(2, len(temp_dec)):

        temp_cy += temp_dec[j]

        if j + len(temp_cy) <= len(temp_dec):

            comp_cy = temp_dec[ j+1 : j+len(temp_cy)+1]

            if temp_cy == comp_cy:
                if len(temp_cy) > max_len:
                    max_len = len(temp_cy)
                    max_denominator = i
                break
                
        else: 
            break

    for j in range(3, len(temp_dec)):

        temp_cy += temp_dec[j]

        if j + len(temp_cy) <= len(temp_dec):

            comp_cy = temp_dec[ j+1 : j+len(temp_cy)+1]

            if temp_cy == comp_cy:
                if len(temp_cy) > max_len:
                    max_len = len(temp_cy)
                    max_denominator = i
                break
                
        else: 
            break


print(max_denominator, ":", max_len)