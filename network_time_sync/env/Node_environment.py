'''
Created on 24.07.2013

@author: Sascha Friedrich
'''
#Describes the environment for the nodes
from PySide.QtCore import *
from PySide.QtGui import *
from env.objects.Node_state import Node_state
from env.objects.Node import *
from gui.dialog_init import  *
from gui.Env_button import  *

#from simulation_ad_hoc_multi_hop_network import simulation_ad_hoc_multi_hop_network


class Node_environment(object):
    
    #static
    button_list=[]
    



    #Constructor
    def __init__(self,window, length, width):
        self.length=length
        self.width=width
        self.selected_item=None
        self.id=-1
        self.env_objects =   {}
        self.features_obj=None
        self.sync_algorithm=None
        self.history=[]
        self.window=window
         

      
      
    def set_sync_algorithm(self,sync_algorithm):
        self.sync_algorithm=sync_algorithm    
        
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
        
        
        

        
        if(self.selected_item!=None):
            if(self.selected_item.node_state.state_name==Node_state.STATE_CRASHED):
                self.selected_item.node_state.change_state(Node_state.STATE_ACTIVE)
                self.selected_item.gui_pushButton.setStyleSheet("\
                background: rgb(200, 200, 200);\
                border:2px solid rgb(255, 0, 0);")
            
            else:
                self.selected_item.node_state.change_state(Node_state.STATE_CRASHED)
                self.selected_item.gui_pushButton.setStyleSheet("\
                background: rgb(150, 0, 0);\
                border:2px solid rgb(255, 0, 0);")
            
            #TO DO in own method
            #new layer & gateway!
            self.selected_item.gateway=self.selected_item
            
            if(self.selected_item.is_beacon):
                self.selected_item.layer=0
            else:
                self.selected_item.layer=-1   
            
            

            
            
            
            
            #self.create_neighborhood_sorted_list_ALL()
        else:
            pass
        
        self.sync_algorithm.gateway_lost()
        self.features_obj.draw_trans_range()
        self.selected_item.view_parameter()
        self.selected_item.view_special_parameter()
        self.selected_item.set_items_to_neighborhood_sorted_list_view()
        
        
  
    
    def delete_node(self):

        
        #DELETE OR UNDELETE? -> ...
        if(self.selected_item!=None):
            
            
            
            #pop out node of env_objects and delete button
            
            #OLD:
#           self.env_objects.pop(self.selected_item.env_id).gui_pushButton.deleteLater())
    
            #NEW:
            node=self.env_objects.pop(self.selected_item.env_id)
            node.gui_pushButton.setVisible(False)
            
            #TO DO in own method
            #new layer & gateway!
            node.gateway=node
            if(self.selected_item.is_beacon):
                node.layer=0
            else:
                node.layer=-1
            
            
            self.history.append(node)
            
            
            self.create_neighborhood_sorted_list_ALL()
            #out of focus
            self.selected_item=None
            
            
            if(self.sync_algorithm.init_started):
            #EMIT!!
                self.sync_algorithm.gateway_lost()
                self.features_obj.draw_trans_range()
                
            
                
            else:
                pass
            
        else:
            pass
            
        
        
    
    def undelete_node(self):
        
        self.features_obj.draw_trans_range()
        
        if(len(self.history)!=0):
            old_id=self.history[-1].env_id
            self.env_objects[old_id]=self.history.pop()
            
            
            if(self.env_objects[old_id].node_state.state_name==Node_state.STATE_CRASHED):
                self.env_objects[old_id].gui_pushButton.setStyleSheet("background: rgb(150, 0, 0);")

            else:
                self.env_objects[old_id].gui_pushButton.setStyleSheet("")
                
                
            self.env_objects[old_id].view_parameter()
            self.env_objects[old_id].view_special_parameter()
            self.env_objects[old_id].gui_pushButton.setVisible(True)
            
            
            #self.create_neighborhood_sorted_list_ALL()
            
            if(self.sync_algorithm.init_started):
            #EMIT!!
                self.sync_algorithm.gateway_lost()
                self.features_obj.draw_trans_range()
                
            

            
        else:
            pass
        
    
    
    def create_neighborhood_sorted_list_ALL(self):
        for key in self.env_objects:
            self.env_objects[key].create_neighborhood_sorted_list()
            
            
    
    def input_node(self):
        MAX_TRANSMITTION_RANGE=150
        #id will autoimkremented!!
        id=self.id+1

        #OLD:
        #pushButton_robot = QtGui.QPushButton(self.window.widget_simulation_window)
        
        #NEW:
        pushButton_robot = Env_button(self.window.widget_simulation_window)
        
        pushButton_robot = QPushButton(self.window.widget_simulation_window)
        pushButton_robot.setGeometry(QRect(300, 300, 60, 41))
        pushButton_robot.setText(str(id))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/robot_passive.png"), QIcon.Normal, QIcon.Off)
        pushButton_robot.setIcon(icon)
        pushButton_robot.setIconSize(QSize(30, 30))
        pushButton_robot.setObjectName("pushButton_robot_"+str(id))
        pushButton_robot.setVisible(True)
        #INSERT WITH layer -> 10000
        node=Node(self.id,-1,False,MAX_TRANSMITTION_RANGE,(300,300),(0,0),pushButton_robot)
        node.set_env_ref(self)
        node.set_window_ref(self.window)
        self.set_env_object(node)     
        
        pushButton_robot.clicked.connect(node.view_parameter)
        pushButton_robot.clicked.connect(node.view_special_parameter)
        
        #register button:
        #simulation_ad_hoc_multi_hop_network.buttons.append(pushButton_robot)
        
           
        
        
        
        
        
    
    
        
        
        
        
        
          
        
    
        
        
        

        

        
        

           
        
           
        

        
       
        