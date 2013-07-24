from Environment_object import Environment_object

class Node(Environment_object):

    #Classvariables    
    layer               =   0
    mac_id              =   0
    layer_id            =   0
    is_beacon           =   False
    position            =   (0,0)
    velocity_vector     =   (0,0)
    STRING_CODE_TYPE    =   "X"   
    
    
    
    
    def __init__(self, mac_id,layer):
        Environment_object.__init__(self,self.STRING_CODE_TYPE)
        print("")
        
        
        