

from PySide.QtGui import *
from PySide.QtCore import *
from env.Node_environment import *



class Network_time_sync(object):
    
    active_node_list=[]
    passive_node_list=[]
    
    def __init__(self,window,dialog,env):
        self.window=window
        self.dialog=dialog
        self.env=env
    
    
    def euclidean(self,base_node,node):
        sumSq=0.0
        x=[]
        y=[]
        x.append(base_node.coordinates[0])
        x.append(node.coordinates[0])
        
        y.append(base_node.coordinates[1])
        y.append(node.coordinates[1])

        
        
     
        #add up the squared differences
        for i in range(len(x)):
            sumSq+=(x[i]-y[i])**2
     
        #take the square root of the result
        return (sumSq**0.5)
    
    
    
    
    def initial_layer_creation(self):

    
    
        #initial node for start of the algorithm
        for node in self.env.env_objects:
            if node.is_beacon:
                self.active_node_list.append((0,node))
            else:
                self.passive_node_list.append(node)
                
        nb_iter=0
        
        while(len(self.active_node_list)>0):
            nb_iter=nb_iter+1
            while(len(self.active_node_list)>0):
                
                base_node = self.active_node_list.pop()[1]
                print("**************")
                print("active_node: ",base_node.mac_id)
                    
                for node in self.passive_node_list:                
                    #euclidean distance    
                    print("node: ",node.mac_id )
                    distance = self.euclidean(base_node,node)
                    
                    print("distance",distance)
                    if distance <= base_node.MAX_TRANSMITTION_RANGE:
                        
                        node.layer=base_node.layer+1
                        node.gateway=base_node.mac_id
                        self.active_node_list.append((distance,node))
                        self.passive_node_list.remove(node)
                        
                self.active_node_list.sort(key=lambda tup: tup[0],reverse=True)
                
                #Degugging
        for i in self.env.env_objects:
            print(i,i.mac_id,i.layer,i.coordinates,i.is_beacon,i.gateway)
                
                        
                
                
           

        
                   
                    
                    
            
                    
                    
                    
            

             
    

        
            
        
        
    
    
        
    



