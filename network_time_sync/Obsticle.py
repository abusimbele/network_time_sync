'''
Created on 24.07.2013

@author: Work
'''
from Environment_object import Environment_object

class Obsticle(Environment_object):
    STRING_CODE_TYPE    =   "$" 
    
    def __init__(self):
        Environment_object.__init__(self,self.STRING_CODE_TYPE)

        