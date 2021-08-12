'''
find the sum of all the numbers that can be written as the sum of fith powers 
of their digits. 
'''

sum = 0

roof= 1000000

for i in range (10, roof):
    tempsum = 0
    for j in  str(i):
        tempsum += int(j)**5
        if tempsum > i:
            break

    if i == tempsum:
        sum += i
        print(i)

print(sum)

