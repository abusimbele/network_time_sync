'''
Created on 24.07.2013

@author: Work
'''
from .Environment_object import *

class Obsticle(Environment_object):
    STRING_CODE_TYPE    =   "$" 
    
    def __init__(self,coordinates,velocity_vector):
        Environment_object.__init__(self,self.STRING_CODE_TYPE,coordinates,velocity_vector)

        