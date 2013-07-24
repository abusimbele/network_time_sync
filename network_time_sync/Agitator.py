'''
Created on 24.07.2013

@author: Sascha Friedrich
'''
from Node_environment import Node_environment


class Agitator(object):
    
    
    
    
    
    def __init__(self, node_environment):
        self.node_environment=node_environment
        

    def random_distriution(self):
        print "Not implemented yet"
        
        
        
    def set_node_into_environment(self,node_id, coordinate):
        env=Node_environment
        env.set_grid_position_value(coordinate, node_id)
        
        
        
        
        
        
    


