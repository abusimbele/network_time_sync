'''
Created on 24.07.2013

@author: Work
'''
#Describes the environment for the nodes






class Node_environment(object):

    #Geometric variables of the environment
    length      =   0
    width       =   0
    grid        =   []
    env_objects =   []


    #Constructor
    def __init__(self, length, width):
        self.length=length
        self.width=width
         
       

        
        
    def set_env_object(self,environmental_object):  
        self.env_objects.append(environmental_object)  
        
    #def show_environment(self):
        
        
        

        

        
        

           
        
           
        

        
       
        