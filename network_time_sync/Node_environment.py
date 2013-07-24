'''
Created on 24.07.2013

@author: Work
'''
#Describes the environment for the nodes

from Space import Space

class Node_environment(object):

    #Geometric variables of the environment
    length  =   0
    width   =   0
    grid    =   []


    #Constructor
    def __init__(self, length, width):
        self.length=length
        self.width=width
         
        space_fields=[]
        for i in range(length*width):
            space_fields.append(Space())
             
         
        self.grid = [[space_fields[x*length+y] for x in range(length)] for y in range(width)]
         

        
    def show_grid_environment(self):
        for i in range(self.length):
            for j in range(self.width):
                print self.grid[i][j].string_code_for_type(),
            print
            
    def set_grid_position_value(self,coordinate,environmental_object):
        self.grid[coordinate[0]][coordinate[1]]=environmental_object

           
        
           
        

        
       
        