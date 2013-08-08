'''
Created on 24.07.2013

@author: Sascha Friedrich
'''

from PySide.QtGui import *
from PySide.QtCore import *
from env.Node_environment import *
from gui.Draw_features import *
from algorithms.threads.Init_network_time_sync_thread import *






class Network_time_sync(object):
    
    #static
    features_obj=None
    

    
    def __init__(self,window,dialog,env,features_obj):
        self.window=window
        self.dialog=dialog
        self.env=env
        self.features_obj=features_obj
    


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
           

        
                   
                    
                    
            
                    
                    
                    
            

             
    

        
            
        
        
    
    
        
    



