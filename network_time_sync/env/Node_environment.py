'''
Created on 24.07.2013

@author: Work
'''
#Describes the environment for the nodes
from PySide.QtCore import *


class Node_environment(object):
    
    selected_item=None
    
    id=-1
    #Geometric variables of the environment
    length      =   0
    width       =   0
    grid        =   []
    env_objects =   {}


    #Constructor
    def __init__(self, length, width):
        self.length=length
        self.width=width
         

        
        
    def set_env_object(self,environmental_object):  
        #self.env_objects.append(environmental_object)
        env_id=self.get_env_id()
        self.env_objects[env_id]=environmental_object
        #register env_id to env_object
        environmental_object.set_env_id(env_id)
        
        
        

        
        
    def get_env_id(self):
        self.id=self.id+1
        return self.id
    
    def get_selected_item(self):
        return self.selected_item
    
    def set_selected_item(self,selected_item):
        self.selected_item=selected_item
        
    
        
        
        
        
        
          
        
    
        
        
        

        

        
        

           
        
           
        

        
       
        