'''
Find how many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
'''

seq = 0; 
powers = []

for i in range(2, 101): 
    for j in range(2, 101):
        pov = i**j
        if pov not in powers:
            powers.append(pov)
            seq += 1

print("Number of distinct powers:", seq)