'''
Created on 06.08.2013

@author: Work
'''
from PySide import QtCore, QtGui
from env.Node_environment import Node_environment
from PySide.QtGui import *



class Draw_features(object):
    
    env=None
    window=None

    def __init__(self):
        pass
    
    def set_window(self,window):
        self.window=window
        
    def set_env(self,env):
        self.env=env

        
        
    def draw_graph(self):
        scene=QGraphicsScene()
        self.window.graphicsView_sim.setScene(scene)  
        self.window.graphicsView_sim.fitInView(QtCore.QRect(0,0,300,300))      
        scene.addLine(300,300,0,0) 
        
        OFFSET_X=0
        OFFSET_Y=0
        #Draw Graph
        for key in self.env.env_objects:
            node=self.env.env_objects[key]        
            node_x  =   node.coordinates[0]-OFFSET_X
            node_y  =   node.coordinates[1]-OFFSET_Y
             
            gateway =   node.gateway
             
            gateway_x   = gateway.coordinates[0]-OFFSET_X
            gateway_y   = gateway.coordinates[1]-OFFSET_Y
            
            print
            print(gateway_x,gateway_y,node_x,node_y)
            scene.addLine(gateway_x,gateway_y,node_x,node_y)
        
             
            
        
        
        
        
       
        
    
    
    
  
    

