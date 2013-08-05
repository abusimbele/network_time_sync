'''
Created on 24.07.2013

@author: Work
'''

from PySide.QtGui import *
from PySide.QtCore import *

from env.Node_environment import *
from env.objects.Node import *
from env.objects.Space import *
from env.objects.Obsticle import *


from gui.window_main import *
from gui.dialog_init import  *

import sys
import random

from Agitator import Agitator
from gui import dialog_init
from tkinter.dialog import DIALOG_ICON




#SET SEED
random.seed(1)



#!/usr/bin/python

# -*- coding: utf-8 -*-

##########
#INIT GUI#
##########

class MyApplication(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)
        
class MyDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)        


app = QtGui.QApplication(sys.argv)
window = MyApplication()
window.show()

dialog_init = MyDialog()


#Action_methods:
#INIT the environment trough the dialog choices
def init_env():
    env_length=dialog_init.spinBox_env_length.value()
    env_width=dialog_init.spinBox_env_width.value()
    env = Node_environment(env_length,env_width)
    
    
#############################################################
#set nodes to the envornment
    
    #set beacons
    for nb in range(dialog_init.spinBox_nb_beacons.value()):
        node = Node(nb,-1,True,(random.randint(0,env_width),random.randint(0,env_length)),(dialog_init.doubleSpinBox_vx,dialog_init.doubleSpinBox_vy))
        env.set_env_object(node)
    
    
    #set other nodes
    for nb in range(dialog_init.spinBox_nb_nodes.value()):
        node = Node(nb+dialog_init.spinBox_nb_beacons.value(),-1,False,(random.randint(0,env_width),random.randint(0,env_length)),(dialog_init.doubleSpinBox_vx,dialog_init.doubleSpinBox_vy))
        env.set_env_object(node)
        
        
#################################################################


    #Debugging
    for i in env.env_objects:
        print(i,i.mac_id,i.layer,i.coordinates,i.is_beacon)
        
    
    


#######################################################################
#ACTIONS

#Main-Window:
window.actionINIT.triggered.connect(dialog_init.show)


#INIT-Dialog:
dialog_init.buttonBox_dialog_init.accepted.connect(init_env)


#######################################################################




sys.exit(app.exec_())



