'''
Created on 08.08.2013

@author: Work
'''

class Calculate(object):
    
    
    
    



    def __init__(self):
        pass
    
    
    @staticmethod
    def euclidean(base_node,node):
        sumSq=0.0
        x=[]
        y=[]
        x.append(base_node.coordinates[0])
        x.append(base_node.coordinates[1])
        y.append(node.coordinates[0])
        y.append(node.coordinates[1])
    
        #add up the squared differences
        for i in range(len(x)):
            sumSq+=(x[i]-y[i])**2
     
        #take the square root of the result
        return (sumSq**0.5)

        