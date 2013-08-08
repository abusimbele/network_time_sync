'''
Created on 24.07.2013

@author: Sascha Friedrich
'''

from PySide import QtCore, QtGui
from env.Node_environment import Node_environment
from PySide.QtGui import *



class Draw_features(object):



    def __init__(self):
        self.env    =   None
        self.window =   None
        self.scene  =   None
    
    def set_window(self,window):
        self.window=window
        
    def set_env(self,env):
        self.env=env

        
        
    def draw_graph(self):
        
        
        #BAD, buttons behind view!!!
        #self.window.graphicsView_sim.raise_()
        self.scene=QGraphicsScene()
        self.window.graphicsView_sim.setScene(self.scene)  
        self.window.graphicsView_sim.setSceneRect(QtCore.QRect(0, 0, 575, 400))
        pen = QtGui.QPen(QtCore.Qt.gray, 2, QtCore.Qt.DotLine)

        

        #Draw Graph
        for key in self.env.env_objects:
            node=self.env.env_objects[key]        
            node_x  =   node.coordinates[0]
            node_y  =   node.coordinates[1]
             
            gateway =   node.gateway
             
            gateway_x   = gateway.coordinates[0]
            gateway_y   = gateway.coordinates[1]
            
            self.scene.addLine(gateway_x,gateway_y,node_x,node_y,pen)
            
    
        
             
            
        
        
        
        
       
        
    
    
    
  
    

