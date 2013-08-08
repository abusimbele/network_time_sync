'''
Created on 24.07.2013

@author: Sascha Friedrich
'''
#Describes the environment for the nodes
from PySide.QtCore import *
from env.objects.Node_state import Node_state


class Node_environment(object):
    
    #static
    button_list=[]
    



    #Constructor
    def __init__(self, length, width):
        self.length=length
        self.width=width
        self.selected_item=None
        self.id=-1
        self.env_objects =   {}
        self.features_obj=None
         

        
        
    def set_env_object(self,environmental_object):  
        #self.env_objects.append(environmental_object)
        env_id=self.get_env_id()
        self.env_objects[env_id]=environmental_object
        #register env_id to env_object
        environmental_object.set_env_id(env_id)
        
        
        #add button to delete list!!
        Node_environment.button_list.append(environmental_object.gui_pushButton)
        
        
        
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
        
        
    def get_env_id(self):
        self.id=self.id+1
        return self.id
    
    def get_selected_item(self):
        return self.selected_item
    
    def set_selected_item(self,selected_item):
        self.selected_item=selected_item

        
    def set_features_obj(self,features_obj):
        self.features_obj=features_obj
        
        
    def crash_node(self):
        self.selected_item.node_state.change_state(Node_state.STATE_CRASHED)
        self.selected_item.gui_pushButton.setStyleSheet("background: rgb(150, 0, 0);")
        self.create_neighborhood_sorted_list_ALL()
        
        
    def create_neighborhood_sorted_list_ALL(self):
        for key in self.env_objects:
            self.env_objects[key].create_neighborhood_sorted_list()
            
        
        
        
        
        
    
    
        
        
        
        
        
          
        
    
        
        
        

        

        
        

           
        
           
        

        
       
        