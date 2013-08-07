'''
Created on 06.08.2013

@author: Work
'''
from PySide import QtCore, QtGui
from env.Node_environment import Node_environment




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
        
        qp=QtGui.QPainter()
        
        #INIT PEN_STYLE
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        
        
        
        
        qp.begin(self.window)
        
        #Draw Graph
        for key in self.env.env_objects:
            node=self.env.env_objects[key]        
            node_x  =   node.coordinates[0]
            node_y  =   node.coordinates[0]
            
            gateway =   node.gateway
            
            gateway_x   = gateway.coordinates[0]
            gateway_y   = gateway.coordinates[1]
            
            qp.drawLine(node_x, node_y, gateway_x, gateway_y)
            
            
        qp.end()
            
        
        
        
        
       
        
    
    
    
  
    

