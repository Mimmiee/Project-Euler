'''
Find the sum of the diagonals in a 1001 by 1001 spiral? 
'''

sum = 1

num = 1
jump = 2

while num < 1001**2:

    i = 0
    while i < 4:
        num += jump
        sum += num
        i += 1

    jump += 2

print(sum)