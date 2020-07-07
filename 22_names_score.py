'''
Find the total name score of the names in the file 22_names.txt.
Total name score: Sort the names in alphabetical order, multiply the names 
index in the list with the sum of the names letters index.
'''
import string 

tot_score = 0
name_pos = 0
f = open("22_names.txt", "r")

for line_str in f:
    line = sorted(line_str.replace('"', "").split(','))

    for i in range(0, len(line)):

        temp_name = line[i]
        name_pos += 1
        temp_score = 0

        for j in range(0, len(temp_name)):
            temp_score += string.ascii_uppercase.index(temp_name[j]) +1
        temp_score *= name_pos
        tot_score += temp_score
          
f.close()
print(tot_score)

