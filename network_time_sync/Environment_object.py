'''
Created on 24.07.2013

@author: Work
'''

class Environment_object(object):
    
    string_code_type=""


    def __init__(self,string_code_type):
#         print "Not yet implemented"
        self.string_code_type=string_code_type
        
        
    def string_code_for_type(self):
        return self.string_code_type 
        
        
    
