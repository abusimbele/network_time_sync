'''
Created on 08.08.2013

@author: Sascha Friedrich
'''

class Node_state(object):
    
    #Possible states
    
    STATE_ACTIVE    =   0
    STATE_PASSIVE   =   1
    STATE_CRASHED   =   2
    
    #First state
    FIRST_STATE     =   STATE_ACTIVE   



    def __init__(self):
        
        self.state_name=Node_state.FIRST_STATE

            
            
    def change_state(self,state):
        self.state_name = state  
        
                

        