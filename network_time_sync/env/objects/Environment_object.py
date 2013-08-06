'''
Created on 24.07.2013

@author: Work
'''

class Environment_object(object):
    
    string_code_type=""
    coordinates         =   (0,0)
    velocity_vector     =   (0,0)
    env_id              =   -1
    window_ref          =   None
    env_ref             =   None



    def __init__(self,string_code_type,coordinates,velocity_vector):
#         print "Not yet implemented"
        self.string_code_type=string_code_type
        self.coordinates=coordinates
        self.velocity_vector=velocity_vector
    
        
        
    def string_code_for_type(self):
        return self.string_code_type 
    
    def set_env_id(self,env_id):
        self.env_id=env_id
        
    def set_window_ref(self, window_ref):
        self.window_ref=window_ref
        
    def set_env_ref(self, env_ref):
        self.env_ref=env_ref
        
    
    def view_parameter(self):
    #Look in dictionary
        
        node=self.env_ref.env_objects[self.env_id]
        self.window_ref.label_x.setText(str(node.coordinates[0]))
        self.window_ref.label_y.setText(str(node.coordinates[1]))
        self.window_ref.label_layer.setText(str(node.layer))
        self.window_ref.label_v_x.setText(str(node.velocity_vector[0]))
        self.window_ref.label_v_y.setText(str(node.velocity_vector[1]))
        
  
        
        
    
