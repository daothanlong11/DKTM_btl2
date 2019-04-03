from __future__ import print_function
import numpy as np
import csv
import random

def position(height, width, number_locate,number_table):
    position_table = np.zeros((height+2, width+2), dtype=int)
    a_position_row = number_locate[0]+1
    a_position_col = number_locate[1]+1
    for i in range(height):
        if (i > 0 & i < (height)):
            for j in range(width):
                if (j > 0 & j < (width)):
                    position_table[i, j] = 0
    all_move = np.array(position_table[(a_position_row-1):(a_position_row+2),
                                       (a_position_col-1):(a_position_col+2)])
    position_filter = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    position_table[(a_position_row-1):(a_position_row+2),
                   (a_position_col-1):(a_position_col+2)] = all_move + position_filter
    p = np.where(position_table == 1)
    position = []
    list_position = []
    for i in range((np.shape(p))[1]):
        if (((p[0][i]) > 0) & ((p[0][i]) < 6) & ((p[1][i]) > 0) & ((p[1][i]) < 7)):
            position.append([(p[0][i]-1), (p[1][i]-1)])
    for value in position:
        value.append(number_table[value[0],value[1]])
        list_position.append(number_table[value[0],value[1]])
    position = np.asarray(position)
    return position,list_position

def convert_int2locate(int_number,number_table):
    l_int = np.where(number_table==int_number)
    int_locate = np.array([l_int[0][0],l_int[1][0]])
    return int_locate

#def q_function(s, a, posible_move_position):



    # khoi tao ma tran R-table tu du kien bai toan
width = 6
height = 5
R_talbe = np.array([[0, -1, +1, -1, -1, -1], [-1, -100, -1, -1, -100, -1],
                    [-1, -1, +1, -1, -1, +1], [-100, -1, -1, -100, -1, -1], [-1, +1, -1, -1, +100, -1]])
"""
with open("D:\Code_software\VScode\python\DKTM_btl2\R_talbe.csv",'w') as csvfile:
    write = csv.writer(csvfile,delimiter=',')
    for i in range(height):
        write.writerow(R_talbe[i,:])

"""
# khoi tao ma tran 0 cua Q learning
Q_table = np.zeros((height, width), dtype=float)

# khoi tao stt cua tung buoc di trong table
number_table = np.zeros((height,width),dtype=int)
number = 0
for i in range(height):
    for j in range(width):
        number_table[i,j] = number
        number+=1


# tao bien state ban dau
s_0 = int(input("nhap stt cua vi tri state ban dau: "))
s_locate = convert_int2locate(s_0,number_table)
posible_move_position,list_posible_move = position(height, width, s_locate,number_table)



print("something")
