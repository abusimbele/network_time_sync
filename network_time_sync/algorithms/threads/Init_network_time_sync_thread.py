'''
Created on 24.07.2013

@author: Sascha Friedrich
'''

from PySide.QtGui import *
from PySide.QtCore import *
from env.Node_environment import *
from gui.Draw_features import *
from own_math.Calculate import *







class Init_network_time_sync_thread(QThread):
    
    #static
    features_obj=None
    

    
    def __init__(self,window,dialog,env,features_obj):
        super(Init_network_time_sync_thread,self).__init__(None)
        self.window=window
        self.dialog=dialog
        self.env=env
        self.features_obj=features_obj
        
        

    def run(self):
        new_passive_node_list=[]
        active_node_list=[]
        passive_node_list=[]

    
    
        #initial node for start of the algorithm
        for id in self.env.env_objects:
            node=self.env.env_objects[id]
            if node.is_beacon:
                active_node_list.append((0,node))
            else:
                passive_node_list.append(node)
                
        
        
        while(len(active_node_list)>0):
            new_passive_node_list=[]
            base_node = active_node_list.pop(0)[1] 
            for node in passive_node_list:                
                distance = Calculate.euclidean(base_node,node)

                if distance <= base_node.MAX_TRANSMITTION_RANGE:
                    node.layer=base_node.layer+1
                    node.set_gateway(base_node)
                    active_node_list.append((distance,node))
                else:
                    new_passive_node_list.append(node)
                    
            
            passive_node_list=new_passive_node_list[:]
            
            #####################################################
            # reverse=True/False is essential for the algorithm #
            # order matters!                                    #
            #####################################################
            active_node_list.sort(key=lambda tup: tup[0],reverse=False)
        self.terminate()
            
         
         
         
        #Degugging
#         for id in self.env.env_objects:
#             print(self.env.env_objects[id],self.env.env_objects[id].mac_id,self.env.env_objects[id].layer,self.env.env_objects[id].coordinates,self.env.env_objects[id].is_beacon,self.env.env_objects[id].gateway.mac_id)
                
                           
                   
                
           

        
                   
                    
                    
            
                    
                    
                    
            

             
    

        
            
        
        
    
    
        
    



