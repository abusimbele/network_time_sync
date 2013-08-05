'''
Created on 24.07.2013

@author: Work
'''

class Environment_object(object):
    
    string_code_type=""
    coordinates         =   (0,0)
    velocity_vector     =   (0,0)


    def __init__(self,string_code_type,coordinates,velocity_vector):
#         print "Not yet implemented"
        self.string_code_type=string_code_type
        self.coordinates=coordinates
        self.velocity_vector=velocity_vector
        
        
    def string_code_for_type(self):
        return self.string_code_type 
        
        
    
