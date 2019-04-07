from __future__ import print_function
import numpy as np
import csv
import random
import os

add = os.path.dirname(os.path.realpath(__file__))
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
        if (((p[0][i]) > 0) & ((p[0][i]) < (height+1)) & ((p[1][i]) > 0) & ((p[1][i]) < (width+1))):
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

def Max_score(R_talbe,number_table,a_locate,height,width):
    list_locate,_ = position(height,width,a_locate,number_table)
    list_score = []
    for i in range(len(list_locate)):
        list_score.append(R_talbe[list_locate[i][0],list_locate[i][1]])
    max_score = max(list_score)
    return max_score

def q_function(a_locate,lr,gamma, posible_move_position,Q_table,R_talbe,number_table,height,width):
    Q_table[a_locate[0],a_locate[1]] = ( Q_table[a_locate[0],a_locate[1]] + lr*( R_talbe[a_locate[0],a_locate[1]] + gamma*(Max_score(R_talbe,number_table,a_locate,height,width)) ) )
    


    # khoi tao ma tran R-table tu du kien bai toan

################################ khoi tao R table ###################################
R_talbe = np.array([[0, -1, +1, -1, -1, -1], [-1, -100, -1, -1, -100, -1],
                    [-1, -1, +1, -1, -1, +1], [-100, -1, -1, -100, -1, -1], [-1, +1, -1, -1, +100, -1]])
height = np.shape(R_talbe)[0]
width = np.shape(R_talbe)[1]

############################### khoi tao ma tran 0 cua Q learning #########################
Q_table = np.zeros((height, width), dtype=float)

######################### khoi tao stt cua tung buoc di trong table #######################
number_table = np.zeros((height,width),dtype=int)
number = 0
for i in range(height):
    for j in range(width):
        number_table[i,j] = number
        number+=1

###################################### phan code chay chinh#####################################
s_0 = int(input("nhap stt cua vi tri state ban dau: "))
s0_locate = convert_int2locate(s_0,number_table)
posible_move_position,list_posible_move = position(height, width, s0_locate,number_table)
episode = int(input("nhap so episode muon huan luyen: "))
lr = float(input("nhap learning rate cho model: "))
gamma = float(input("nhap discount rate cho model: "))
for i in range(episode):
    a = random.choice(list_posible_move)
    a_locate = convert_int2locate(a,number_table)
    q_function(a_locate,lr,gamma,posible_move_position,Q_table,R_talbe,number_table,height,width)
    s_locate = a_locate
    posible_move_position,list_posible_move = position(height,width,s_locate,number_table)

############################### ghi ket qua ra file excel de theo doi ####################################
with open(add+"\R_Q_table.csv",'w') as csvfile:
    write = csv.writer(csvfile,delimiter=',')
    for i in range(height):
        write.writerow(R_talbe[i,:])
    write.writerow("\n")
    write.writerow("\n")
    for i in range(height):
        write.writerow(Q_table[i,:])
    csvfile.close()

