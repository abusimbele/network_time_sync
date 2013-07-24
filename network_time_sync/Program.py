'''
Created on 24.07.2013

@author: Work
'''
from Node_environment import Node_environment
from Node import Node
from Space import Space
from Obsticle import Obsticle

from pylab import *
import time



env = Node_environment(20,20)
# env.show_grid_environment()
# print 
# print
# env.set_grid_position_value((0,0),Node(1,1))
# env.set_grid_position_value((1,1),Node(2,1))
# env.set_grid_position_value((2,2),Node(3,1))
# env.set_grid_position_value((3,3),Node(4,1))
# env.set_grid_position_value((4,4),Node(5,1))
# env.set_grid_position_value((4,5),Obsticle())
# env.set_grid_position_value((1,3),Obsticle())
# env.set_grid_position_value((4,8),Obsticle())
# 
# env.show_grid_environment()
# print 
# print
# 
# env.set_grid_position_value((4,4),Space())
# env.show_grid_environment()

env.set_env_object((0,0), Node(1,1))
env.set_env_object((1,1), Node(2,1))
env.set_env_object((2,2), Node(3,1))
env.set_env_object((3,3), Node(4,1))
env.show_environment()



# ion()
# 
# tstart = time.time()               # for profiling
# x = arange(0,2*pi,0.01)            # x-array
# line, = plot(x,sin(x))
# for i in arange(1,200):
#     line.set_ydata(sin(x+i/10.0))  # update the data
#     draw()                         # redraw the canvas
# 
# print 'FPS:' , 200/(time.time()-tstart)



