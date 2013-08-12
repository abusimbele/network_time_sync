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
    myOwnSignal=Signal()

    
    def __init__(self,window,dialog,env,features_obj):
        super(Iteration_network_time_sync_thread,self).__init__(None)
        self.window=window
        self.dialog=dialog
        self.env=env
        self.app=None
        self.features_obj=features_obj
        self.myOwnSignal.connect(self.env.slot_render)
        
    def pause_sim(self):
        print("PAUSE")
         
    
    def set_app(self,app):
        self.app=app    
        print("Thread: ",self.app)
        

    
    def fire_signal_to_render(self):
        self.myOwnSignal.emit()
        
    
    
    def run(self):

        while(True):
            #DIRECT method call for synchronization! mega brain :)
            self.sleep(1)
            self.fire_signal_to_render()
            
           
            
        
        
                   
                    
                    
            
                    
                    
                    
            

             
    

        
            
        
        
    
    
        
    



