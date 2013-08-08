'''
Created on 24.07.2013

@author: Sascha Friedrich
'''

from .Environment_object import *
from PySide.QtCore import *
from PySide.QtGui import *
from env.objects.Node_state import *
from own_math.Calculate import *
from gui import Draw_features




class Node(Environment_object):

    
    
    
    
    def __init__(self, mac_id,layer,is_beacon,MAX_TRANSMITTION_RANGE,coordinates,velocity_vector,gui_pushButton):
        
        STRING_CODE_TYPE    =   "X" 
        
        Environment_object.__init__(self,STRING_CODE_TYPE,coordinates,velocity_vector)
        
        self.node_state=Node_state()
        self.mac_id=mac_id
        self.layer=layer
        self.is_beacon=is_beacon
        self.MAX_TRANSMITTION_RANGE=MAX_TRANSMITTION_RANGE
        self.gui_pushButton=gui_pushButton
        self.gateway=self
        self.neighborhood_sorted_list=[]
        
        
        
        
        
    def view_special_parameter(self):
        
        
       
        
        
        #Show neighborhood
        self.set_items_to_neighborhood_sorted_list_view()
        
        
    #Look in dictionary
        if(self.env_ref.get_selected_item()!=None):
            
            
            #DELETE OLD MARKER AT OLD SELECTED ITEM
            if(self.env_ref.get_selected_item().node_state.state_name==Node_state.STATE_CRASHED):
                self.env_ref.get_selected_item().gui_pushButton.setStyleSheet("background: rgb(150, 0, 0);")

            else:
                self.env_ref.get_selected_item().gui_pushButton.setStyleSheet("")
            
            
        self.env_ref.set_selected_item(self)
        
        #Set to the first layer
        self.gui_pushButton.raise_()
        
        #mark as focused
        
        if(self.node_state.state_name==Node_state.STATE_CRASHED):
            self.gui_pushButton.setStyleSheet("\
            background: rgb(150, 0, 0);\
            border:2px solid rgb(255, 0, 0);")
        else:
            self.gui_pushButton.setStyleSheet("\
            background: rgb(200, 200, 200);\
            border:2px solid rgb(255, 0, 0);")
        
        node=self.env_ref.env_objects[self.env_id]
        
        self.window_ref.label_gateway.setText(str(self.gateway.mac_id))
        self.window_ref.label_node.setText(str(self.mac_id))
        if(node.is_beacon):
            self.window_ref.checkBox_beacon.setCheckState(Qt.Checked)
        else:
           self. window_ref.checkBox_beacon.setCheckState(Qt.Unchecked)
           
           
        #show max-trans-circle
        self.env_ref.features_obj.draw_trans_range()
           
           
           

    def set_gateway(self,gateway):
        self.gateway=gateway
        
        
        

        
        
        
    def create_neighborhood_sorted_list(self):
        self.neighborhood_sorted_list=[]
        for key in self.env_ref.env_objects:
            node=self.env_ref.env_objects[key]
            if(node !=self and node.node_state.state_name==Node_state.STATE_ACTIVE):
                distance = Calculate.euclidean(self,node)
                if distance <= node.MAX_TRANSMITTION_RANGE:
                    self.neighborhood_sorted_list.append((distance,node))
        self.neighborhood_sorted_list.sort(key=lambda tup: tup[0],reverse=False)
        #print(self.neighborhood_sorted_list)
        
        
    def set_items_to_neighborhood_sorted_list_view(self):
        list=self.window_ref.listView_neighbours
        model = QStandardItemModel(list)
        for neighb in self.neighborhood_sorted_list:
            item    =   QStandardItem('node: '+str(neighb[1].mac_id)+'   dist.: '+ str(round(neighb[0],2))+'m')
            model.appendRow(item)
        
            
        list.setModel(model)
        list.show()
          
            
        
 
    
        
        
        