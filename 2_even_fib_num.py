'''
Calculate the sum of all even Fibonacci numbers under 4 million.
2 + 8 + 34 ... = 4613732
'''
import math 

old_num = 0 
num = 0
new_num = 1
sum = 0

while new_num < 4000000:
    old_num = new_num
    new_num = new_num + num
    num = old_num
    if new_num%2 == 0:
        sum = sum + new_num

print(sum)