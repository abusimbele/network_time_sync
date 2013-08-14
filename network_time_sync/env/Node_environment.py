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
import random
import math


#from simulation_ad_hoc_multi_hop_network import simulation_ad_hoc_multi_hop_network


class Node_environment(QObject):
    
    #static
    button_list=[]
    



    #Constructor
    def __init__(self,window, length, width):
        super(Node_environment,self).__init__(None)
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
        
        #print("COLL: ",self.look_for_collision(self.selected_item))
        #print("Field: ",self.look_for_field_boundary(self.selected_item))
       

        
        
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
                #self.selected_item.layer=0
                pass
            else:
                self.selected_item.layer=-1   

        else:
            pass
        self.create_neighborhood_sorted_list_ALL()
        self.sync_algorithm.gateway_lost()
        if(self.selected_item!=None):
            self.selected_item.view_parameter()
            self.selected_item.view_special_parameter()
            self.selected_item.set_items_to_neighborhood_sorted_list_view()
        self.features_obj.draw_trans_range()
        
        
  
    
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
                self.sync_algorithm.gateway_lost()
                self.features_obj.draw_trans_range()
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
        
        self.sync_algorithm.gateway_lost()
        self.selected_item.view_parameter()
        self.selected_item.view_special_parameter()
        self.selected_item.set_items_to_neighborhood_sorted_list_view()
        self.features_obj.draw_trans_range()
        
    
    
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
        
        security_cap=0
        while(True):
            
            x=random.randint(0,self.width-60)
            y=random.randint(0,self.length-40)
            
            if(not self.look_for_collision_xy(x,y)):
                break
            security_cap= security_cap+1
            if(security_cap>100000):
                x=0
                y=0
                break
        
        
        
        pushButton_robot = Env_button(self.window.widget_simulation_window)
        
        pushButton_robot = QPushButton(self.window.widget_simulation_window)
        pushButton_robot.setGeometry(QRect(x, y, 60, 41))
        pushButton_robot.setText(str(id))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/robot_passive.png"), QIcon.Normal, QIcon.Off)
        pushButton_robot.setIcon(icon)
        pushButton_robot.setIconSize(QSize(30, 30))
        pushButton_robot.setObjectName("pushButton_robot_"+str(id))
        pushButton_robot.setVisible(True)
        #INSERT WITH layer -> 10000
        node=Node(id,-1,False,MAX_TRANSMITTION_RANGE,(x,y),(0,0),0,pushButton_robot)
        node.set_env_ref(self)
        node.set_window_ref(self.window)
        self.set_env_object(node)     
        
        pushButton_robot.clicked.connect(node.view_parameter)
        pushButton_robot.clicked.connect(node.view_special_parameter)
        
        #register button:
        #simulation_ad_hoc_multi_hop_network.buttons.append(pushButton_robot)
        
        
    #move the node and it`s button to the new coordinates for a given time-interval     
    def move_node(self,node,time):
        
        x_old   =   node.coordinates[0]
        y_old   =   node.coordinates[1]
        
        x   =   node.coordinates[0]
        y   =   node.coordinates[1]
        v_x =   node.velocity_vector[0]
        v_y =   node.velocity_vector[1]
        
        node.coordinates=(x+v_x*time,y+v_y*time)
        
        if(self.look_for_field_boundary(node) or self.look_for_collision(node)):
            node.coordinates=(x_old,y_old)
            self.set_node_random_velocity(node)
            #node.velocity_vector=(-node.velocity_vector[0],-node.velocity_vector[1])
            
            
        
        
        
        self.move_node_button(node)
        
        
    def move_node_button(self,node):
        node.gui_pushButton.move(node.coordinates[0],node.coordinates[1])
        
    
    def move_all_nodes(self):
        for key in self.env_objects:
            self.move_node(self.env_objects[key], 1)
        
        
        
    def set_node_random_velocity(self,node,rnd=False):
        length=node.velocity_vector_length
        alpha=random.random()*0.5*math.pi
        
        v_x =   math.cos(alpha)*length *(-1)**(random.randint(0,1))   
        v_y =   math.sin(alpha)*length *(-1)**(random.randint(0,1)) 

        node.velocity_vector=(v_x,v_y)
        
        
    def look_for_collision_xy(self,node_x,node_y,node=None):
        
        
        
        for key in self.env_objects:
            if(self.env_objects[key]!=node):
                if(abs(self.env_objects[key].coordinates[0]-node_x)<60 and abs(self.env_objects[key].coordinates[1]-node_y)<41):
                    #print(self.env_objects[key].mac_id,self.env_objects[key].coordinates[0],self.env_objects[key].coordinates[1])
                    return True
                    
                else: 
                    pass
            
        return False
    
    
    def look_for_collision(self,node):
        return self.look_for_collision_xy(node.coordinates[0],node.coordinates[1],node)
        
        
            
        return False
    
    
    def look_for_field_boundary(self,node):
        
        if((node.coordinates[0])>=self.width-8 or node.coordinates[0]<=0 or (node.coordinates[1])>=self.length or  node.coordinates[1]<=0):
            return True
        else:
            return False
        
        
    def slot_render(self):
    
        self.move_all_nodes()
        self.create_neighborhood_sorted_list_ALL()
        self.sync_algorithm.gateway_lost()
        if(self.selected_item!=None):
            self.selected_item.set_items_to_neighborhood_sorted_list_view()
            self.selected_item.view_parameter()
            self.selected_item.view_special_parameter()
        self.features_obj.draw_trans_range()
        
    
    def change_selected_node_type(self):
        self.get_selected_item().change_node_type()
        
        self.sync_algorithm.gateway_lost()
        self.selected_item.view_parameter()
        self.selected_item.view_special_parameter()
        self.selected_item.set_items_to_neighborhood_sorted_list_view()
        self.features_obj.draw_trans_range()  
        
        
    def set_velocity_for_node(self):
        node=self.selected_item
        v_x=self.window.doubleSpinBox_input_vx.value()
        v_y=self.window.doubleSpinBox_input_vy.value()
        
         
        self.selected_item.velocity_vector=(v_x,v_y)

        self.selected_item.velocity_vector_length=(v_x**2+v_y**2)**0.5
        
        self.selected_item.view_parameter()
        self.selected_item.view_special_parameter()
        
        
            
        
    def connection_to_beacon(self,start_node):
        
        reached_nodes=[start_node]
        node=start_node
        
        while(not node.is_beacon):
            
            node=node.gateway
            
            
            if(reached_nodes.count(node)>0):
                return False
            else:
                reached_nodes.append(node)
        return True
        
        
        
    
        
       
    
    
        
        
        
        
        
        
        
           
        
        
        
        
        
    
    
        
        
        
        
        
          
        
    
        
        
        

        

        
        

           
        
           
        

        
       
        