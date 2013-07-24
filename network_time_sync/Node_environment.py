'''
Created on 24.07.2013

@author: Work
'''
#Describes the environment for the nodes
class Node_environment(object):

    #Geometric variables of the environment
    length  =   0
    width   =   0
    grid    =   []


    #Constructor
    def __init__(self, length, width):
        self.length=length
        self.width=width
         
        self.grid = [[[0] for x in range(length)] for y in range(width)]
         

        
    def show_grid_environment(self):
        for i in range(self.length):
            for j in range(self.width):
                print self.grid[i][j],
            print
            
    def set_grid_position_value(self,coordinate,field_value):
        self.grid[coordinate[0]][coordinate[1]]=[field_value]

           
        
           
        

        
       
        