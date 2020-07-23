'''
Find the millionth lexicographic permutation 
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
from itertools import permutations 

#Create a list with the numbers 
numbers = []
for i in range(0, 10):
    numbers.append(i)

perm = permutations(numbers)

print(list(perm)[999999])