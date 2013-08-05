from .Environment_object import *

class Node(Environment_object):

    #variables    
    mac_id              =   0
    layer               =   0
    is_beacon           =   False
    STRING_CODE_TYPE    =   "X" 
    gateway=-1  
    
    #const
    MAX_TRANSMITTION_RANGE  =   0
    
    
    
    
    def __init__(self, mac_id,layer,is_beacon,MAX_TRANSMITTION_RANGE,coordinates,velocity_vector):
        Environment_object.__init__(self,self.STRING_CODE_TYPE,coordinates,velocity_vector)
        
        self.mac_id=mac_id
        self.layer=layer
        self.is_beacon=is_beacon
        self.MAX_TRANSMITTION_RANGE=MAX_TRANSMITTION_RANGE
        
        
        