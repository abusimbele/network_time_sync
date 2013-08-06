from .Environment_object import *
from PySide.QtCore import *
class Node(Environment_object):

    #variables    
    mac_id              =   0
    layer               =   0
    is_beacon           =   False
    STRING_CODE_TYPE    =   "X" 
    gateway=-1  
    gui_pushButton      =   None
    
    #const
    MAX_TRANSMITTION_RANGE  =   0
    
    
    
    
    def __init__(self, mac_id,layer,is_beacon,MAX_TRANSMITTION_RANGE,coordinates,velocity_vector,gui_pushButton):
        Environment_object.__init__(self,self.STRING_CODE_TYPE,coordinates,velocity_vector)
        
        self.mac_id=mac_id
        self.layer=layer
        self.is_beacon=is_beacon
        self.MAX_TRANSMITTION_RANGE=MAX_TRANSMITTION_RANGE
        
        
        
    def view_special_parameter(self):
    #Look in dictionary
        node=self.env_ref.env_objects[self.env_id]
        
        self.window_ref.label_gateway.setText(str(self.gateway))
        self.window_ref.label_node.setText(str(self.mac_id))
        if(node.is_beacon):
            self.window_ref.checkBox_beacon.setCheckState(Qt.Checked)
        else:
           self. window_ref.checkBox_beacon.setCheckState(Qt.Unchecked)
        
        
        