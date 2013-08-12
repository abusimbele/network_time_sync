'''
Created on 24.07.2013

@author: Sascha Friedrich
'''

class Environment_object(object):
    

    def __init__(self,string_code_type,coordinates,velocity_vector,velocity_vector_length):
        
        self.env_id              =   -1
        self.window_ref          =   None
        self.env_ref             =   None
        self.string_code_type=string_code_type
        self.coordinates=coordinates
        self.velocity_vector=velocity_vector
        self.velocity_vector_length=velocity_vector_length

    
        
        
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
        
  
        
        
    
