#live game
import numpy as np
import copy
import os
import matplotlib.pyplot as plt
from random import randint
def near_num(array,point):
    num=-array[point[0]][point[1]]
    around=[-1,1,0]
    for i in around:
        for j in around:
            if array[point[0]+i][point[1]+j]==1:
                num+=1
    return num
def refresh(game_map):
    copy_map=copy.copy(game_map)
    for x in range(copy_map.shape[0]-1):
        for y in range(copy_map.shape[1]-1):
            num=near_num(copy_map,[x,y])
            if num>3:
                game_map[x][y]=0
            elif num==3:
                game_map[x][y]=1
            elif num==0 or num==1:
                game_map[x][y]=0
    return game_map
def output(game_map):
    for line in game_map:
        out_line=""
        for point in line:
            if point==1:
                out_line+="M"
            else :
                out_line+=" "
            out_line+=" "
        print(out_line)
    return "done"


# start with random cells
size=160
start_num=16000
mid=int(size/2)
game_map=np.zeros([size,size+150])
start_point_x=np.random.randint(0,size,size=start_num)
start_point_y=np.random.randint(0,size+150,size=start_num)
for i in range(len(start_point_x)):
        game_map[start_point_x[i]][start_point_y[i]]=1
    
while True:
    #plt.colorbar(game_map,shrink=0.8,autoscale_None=None)
    alive=0
    os.system("cls")
    output(game_map)
    for line in game_map:
        for point in line:
            if point==1:
                alive+=1
    print(alive)
    game_map=refresh(game_map)