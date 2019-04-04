from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import glob
import moviepy.editor as mpy 
from main import *

########################## tao so do buoc di cua robot ########################
fig,ax = plt.subplots(height,width)
plt.subplots_adjust(wspace=0,hspace=0)
for i in range(height):
    for j in range(width):
        ax[i,j].axes.get_xaxis().set_visible(False)
        ax[i,j].axes.get_yaxis().set_visible(False)
robot = mpimg.imread(add+"\\robot_icon.png")
mine = mpimg.imread(add+"\mine_icon.png")
lightning = mpimg.imread(add+"\lightning_icon.png")
ax[0,0].imshow(robot)
ax[0,2].imshow(lightning)
ax[2,2].imshow(lightning)
ax[2,5].imshow(lightning)
ax[4,1].imshow(lightning)
ax[1,1].imshow(mine)
ax[1,4].imshow(mine)
ax[3,0].imshow(mine)
ax[3,3].imshow(mine)
plt.savefig(add+"\map\map_0.png")

########################### xay dung so do di cho robot ##########################
def position_score(height, width, number_locate,Q_table):
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
        value.append(Q_table[value[0],value[1]])
        value[0] = int(value[0])
        value[1] = int(value[1])
    position = np.asarray(position)
    return position

def evaluate(posible_position_with_score,Q_table):
        increase_score = sorted(posible_position_with_score,key=lambda x:x[2])
        locate_max_score = np.array([increase_score[len(increase_score)-1][0],increase_score[len(increase_score)-1][1]])
        a = int(locate_max_score[0])
        b = int(locate_max_score[1])
        Q_table[a,b] = -999999999
        return a,b

map_locate = []
map_locate.append(s0_locate)
fisrt_locate = s_0
locate = convert_int2locate(fisrt_locate,number_table)
target_locate = np.array([4,4])
while (np.array_equal(locate,target_locate) != True):
       posible_position_with_score = position_score(height,width,locate,Q_table) 
       a,b = evaluate(posible_position_with_score,Q_table)
       new_locate = np.array([a,b])
       map_locate.append(new_locate)
       locate = new_locate

############################# visualize robot move #############################
for i in range((len(map_locate)-1)):
        circle = plt.Circle((0,0.5),200,color='k')
        ax[map_locate[i][0],map_locate[i][1]].add_patch(circle)
        ax[map_locate[i+1][0],map_locate[i+1][1]].imshow(robot)
        plt.savefig(add+"\map\map_%d.png"%(i+1))

gif_name = 'map_move'
fps = 5
file_list = glob.glob(add+'\map\*.png') # Get all the pngs in the current directory
list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif(add+'\map\{}.gif'.format(gif_name), fps=fps)