'''
Created on 24.07.2013

@author: Sascha Friedrich
'''

from PySide.QtGui import *
from PySide.QtCore import *
from env.Node_environment import *
from gui.Draw_features import *
from algorithms.threads.Init_network_time_sync_thread import *
from env.objects.Node import *
import random







class Network_time_sync(object):
    
    #static
    features_obj=None
    

    
    def __init__(self,window,dialog,env,features_obj):
        self.window=window
        self.dialog=dialog
        self.env=env
        self.features_obj=features_obj
        self.init_started=False
    


    def initial_layer_creation(self):

        
        self.init_ts_thread=Init_network_time_sync_thread(self.window,self.dialog,self.env,self.features_obj)
        
       
        try:
             self.init_ts_thread.start()
        except:
            pass
        
        
        
        #View with circle at focus-node
        #self.features_obj.draw_graph() 
        
        #View without circle at focus-node
        self.features_obj.draw_trans_range()
        
        
         
        self.init_started=True
        
           

        
                  
    def gateway_lost(self):
       
        #RANDOM FACTOR!!
        randomized_queue=list(self.env.env_objects.keys())
        #print(randomized_queue)
        random.shuffle(randomized_queue)
        #print(randomized_queue)
    
        for key in randomized_queue:
            
            
            
#             print("gateway: ",self.env.env_objects[key].gateway.mac_id)
#             print("mac: ",self.env.env_objects[key].mac_id)
            
            
            #new layer?! BEACONS DON'T GET NEW LAYER!
            if(self.env.env_objects[key].is_beacon or self.env.env_objects[key].node_state.state_name==Node_state.STATE_CRASHED):
                pass
            
            else:
                #new gateway
                
                #NO neighbors available -> own gateway, but with a high layer!
                if(len(self.env.env_objects[key].neighborhood_sorted_list)==0):
                    self.env.env_objects[key].gateway=self.env.env_objects[key]
                    #TO DO infinity implemenetation!
                    self.env.env_objects[key].layer= -1
                    
                    
                else:
                    
                    for i in self.env.env_objects[key].neighborhood_sorted_list:
                         
                        if(i[2].layer!=-1):
                    
                            self.env.env_objects[key].gateway=i[2]
                            self.env.env_objects[key].layer= self.env.env_objects[key].gateway.layer+1
                            break
            
                        
            
                    
                    
                    
            

             
    

        
            
        
        
    
    
        
    



