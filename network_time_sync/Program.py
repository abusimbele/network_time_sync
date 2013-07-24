'''
Created on 24.07.2013

@author: Work
'''
from Node_environment import Node_environment


env = Node_environment(20,20)
env.show_grid_environment()
print 
print
env.set_grid_position_value((0,0), 1)
env.show_grid_environment()


