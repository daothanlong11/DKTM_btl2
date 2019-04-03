from __future__ import print_function
import numpy as np
# import pandas as pd
import csv


def position(height, width, a):
    position_table = np.zeros((height+2, width+2), dtype=int)
    a_position_row = a[0]+1
    a_position_col = a[1]+1
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
    for i in range((np.shape(p))[1]):
        if (((p[0][i]) > 0) & ((p[0][i]) < 6) & ((p[1][i]) > 0) & ((p[1][i]) < 7)):
            position.append([(p[0][i]-1), (p[1][i]-1)])
    position = np.asarray(position)
    return position


def q_function(s, a, posible_move_position):


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

# tao hai bien state ban dau va action
s = np.array([1, 1])
a = np.array([4, 5])
posible_move_position = position(height, width, a)


print("something")
