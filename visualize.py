from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from main import *

########################## tao so do buoc di cua robot ########################
fig,ax = plt.subplots(height,width)
plt.subplots_adjust(wspace=0,hspace=0)
for i in range(height):
    for j in range(width):
        ax[i,j].axes.get_xaxis().set_visible(False)
        ax[i,j].axes.get_yaxis().set_visible(False)
robot = mpimg.imread("E:\\robot_icon_64px.png")
mine = mpimg.imread("E:\\mine_icon.png")
lightning = mpimg.imread("E:\\lightning_icon.png")
ax[0,0].imshow(robot)
ax[0,2].imshow(lightning)
ax[2,2].imshow(lightning)
ax[2,5].imshow(lightning)
ax[4,1].imshow(lightning)
ax[1,1].imshow(mine)
ax[1,4].imshow(mine)
ax[3,0].imshow(mine)
ax[3,3].imshow(mine)
print("sojog")
