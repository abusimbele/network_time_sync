'''
Created on 12.08.2013

@author: Sascha Friedrich
'''


from PySide.QtGui import *
from PySide.QtCore import *
from env.Node_environment import *
from gui.Draw_features import *
from own_math.Calculate import *








class Iteration_network_time_sync_thread(QThread):
    
    #static
    features_obj=None
    

    
    def __init__(self,window,dialog,env,features_obj):
        super(Iteration_network_time_sync_thread,self).__init__(None)
        self.window=window
        self.dialog=dialog
        self.env=env
        self.features_obj=features_obj
        
    def pause_sim(self):
        print("PAUSE")
         
        

    def run(self):
        while(True):
            self.env.move_all_nodes()
            self.sleep(1)
            self.env.create_neighborhood_sorted_list_ALL()
            self.env.sync_algorithm.gateway_lost()
            #self.env.selected_item.set_items_to_neighborhood_sorted_list_view()
            #self.env.selected_item.view_parameter()
            #self.env.selected_item.view_special_parameter()
            self.env.features_obj.draw_trans_range()
           
            
        
        
                   
                    
                    
            
                    
                    
                    
            

             
    

        
            
        
        
    
    
        
    



