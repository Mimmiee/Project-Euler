'''
Find the maximum total from top to bottom of the given triangle.
'''

import math 

triangle =             [[75],
                        [95, 64],
                        [17, 47, 82],
                        [18, 35, 87, 10],
                        [20, 4, 82, 47, 65],
                        [19, 1, 23, 75, 3, 34],
                        [88, 2, 77, 73, 7, 63, 67],
                        [99, 65, 4, 28, 6, 16, 70, 92],
                        [41, 41, 26, 56, 83, 40, 80, 70, 33],
                        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

                    #     [[3],
                    #    [7, 4],
                    #   [2, 4, 6],
                    #  [8, 5, 9, 3]]        
                   

max_sum = 0 

from copy import copy, deepcopy
check_tri = deepcopy(triangle)

for i in range(0, len(check_tri)):
    temp_line = check_tri[i]
    for j in range(0, len(temp_line)):
        check_tri[i][j] = False



def check_next(i, j):
    if j < len(triangle[i]) and not check_tri[i][j] == True:
        return int(triangle[i][j])
    else:
        return 0

def new_sequence():
    i = 0
    j = 0
    temp_sum = 0

    while i < len(triangle) -1:

        left = check_tri[i+1][j]
        right = check_tri[i+1][j+1]

        if not left:
            temp_sum += check_next(i,j)
            j = j
            i += 1
        elif not right:
            temp_sum += check_next(i,j)
            j +=1 
            i += 1
        else:
            check_tri[i+1][j] = False
            check_tri[i+1][j+1] = False
            break


    temp_sum += check_next(i,j)
    check_tri[i][j] = True 

    # if check_tri[0][0] == True:
    #     end = True

    return temp_sum 
 

while check_tri[0][0] == False: 
    temp = new_sequence()
    # print(temp)
    # print(check_tri)
    if temp > max_sum:
        max_sum = temp

print("Max sum =", max_sum)










