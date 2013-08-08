'''
Created on 24.07.2013

@author: Sascha Friedrich
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

from gui import dialog_init
from gui.Draw_features import *
from algorithms.Network_time_sync import Network_time_sync
from tkinter.dialog import DIALOG_ICON
import PySide
from PySide import QtGui



MAX_TRANSMITTION_RANGE=150.0




#SET SEED
random.seed(1)





#!/usr/bin/python

# -*- coding: utf-8 -*-

##########
#INIT GUI#
##########

class simulation_ad_hoc_multi_hop_network(object):
    def __init__(self):
        pass
    
    env=None
    sync_algorithm=None
    window=None
    dialog_init=None
    buttons=[]
    features_obj=None
    
    @staticmethod
    def delete_buttons():
        for i in simulation_ad_hoc_multi_hop_network.buttons:
            i.deleteLater()
            simulation_ad_hoc_multi_hop_network.buttons=[]
        
    
    

    

class MyApplication(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)
        
class MyDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)        


app = QtGui.QApplication(sys.argv)
simulation_ad_hoc_multi_hop_network.window =  MyApplication()
window = simulation_ad_hoc_multi_hop_network.window

simulation_ad_hoc_multi_hop_network.dialog_init = MyDialog()
dialog_init =simulation_ad_hoc_multi_hop_network.dialog_init

#env=Node_environment(0,0)




#print("env:",env)








 




     
    




#Action_methods:
#INIT the environment trough the dialog choices
def init_env():
    
    #clear scene:
    simulation_ad_hoc_multi_hop_network.window.graphicsView_sim.setScene(PySide.QtGui.QGraphicsScene())
        
    
    if (len(simulation_ad_hoc_multi_hop_network.buttons)>0):
        simulation_ad_hoc_multi_hop_network.delete_buttons()
        #DISCONNECT old trigger and register at the end the new trigger with the new ENV-OBJECT!!!
        window.pushButton_crash_node.clicked.disconnect(simulation_ad_hoc_multi_hop_network.env.crash_node)
        
         
        
        
    env_length=dialog_init.spinBox_env_length.value()
    env_width=dialog_init.spinBox_env_width.value()
    simulation_ad_hoc_multi_hop_network.env = Node_environment(env_length,env_width)
    #Store for all classes
    env=simulation_ad_hoc_multi_hop_network.env
    
    

    
    
    
    
    
###################################
#TO CHANGE ERROR_PRONE CODE ->BEGIN
###################################
    
    
    
    
#############################################################
#set nodes to the envornment
    
    #set beacons
    i=0
    for nb in range(dialog_init.spinBox_nb_beacons.value()):
        node_id=nb
        x=random.randint(0,env_width)
        y=random.randint(0,env_length)
        
        
        pushButton_robot = QtGui.QPushButton(window.widget_simulation_window)
        pushButton_robot.setGeometry(QtCore.QRect(x, y, 60, 41))
        pushButton_robot.setText(str(node_id))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/robot_beacon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_robot.setIcon(icon)
        pushButton_robot.setIconSize(QtCore.QSize(30, 30))
        pushButton_robot.setVisible(True)
        #register for deletion
        simulation_ad_hoc_multi_hop_network.buttons.append(pushButton_robot)
        
#         pushButton_robot.setCheckable(True)        
#         pushButton_robot.setStyleSheet("QPushButton{\
#         color: rgb(255, 255, 255);\
#         text-align: left;\
#         font-size: 12pt;\
#         border: none;\
#     }\
#         QPushButton:checked {\
#         background: rgb(105, 105, 105);}")
        
        
        

        
        node = Node(node_id,0,True,MAX_TRANSMITTION_RANGE,(x,y),(dialog_init.doubleSpinBox_vx.value(),dialog_init.doubleSpinBox_vy.value()),pushButton_robot)
        env.set_env_object(node)
        
        #after env-placement, to get the wright ENV_ID
        pushButton_robot.setObjectName(str(node.env_id))
        
        #register window-ref
        node.set_window_ref(window)
        node.set_env_ref(env)


        ################################
        # SIGNAL_SLOTS AFTER ENV INIT: #
        ################################
        
        #show parameter at the right side of the main-window
        pushButton_robot.clicked.connect(node.view_parameter)
        pushButton_robot.clicked.connect(node.view_special_parameter)
        
        
       
        i=i+1
    
    
    #set other nodes
    
    for nb in range(dialog_init.spinBox_nb_nodes.value()):
        node_id=nb+dialog_init.spinBox_nb_beacons.value()
        
        x=random.randint(0,env_width)
        y=random.randint(0,env_length)
        
        pushButton_robot = QtGui.QPushButton(window.widget_simulation_window)
        pushButton_robot.setGeometry(QtCore.QRect(x, y, 60, 41))
        pushButton_robot.setText(str(node_id))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/robot_passive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton_robot.setIcon(icon)
        pushButton_robot.setIconSize(QtCore.QSize(30, 30))
        pushButton_robot.setObjectName("pushButton_robot_"+str(i))
        pushButton_robot.setVisible(True)
        
        #register for deletion
        simulation_ad_hoc_multi_hop_network.buttons.append(pushButton_robot)
        
#         pushButton_robot.setCheckable(True)
#         pushButton_robot.setStyleSheet("QPushButton{\
#         color: rgb(255, 255, 255);\
#         text-align: left;\
#         font-size: 12pt;\
#         border: none;\
#         }\
#         QPushButton:checked {\
#         background: rgb(105, 105, 105);}")
        
        node = Node(node_id,-1,False,MAX_TRANSMITTION_RANGE,(x,y),(dialog_init.doubleSpinBox_vx.value(),dialog_init.doubleSpinBox_vy.value()),pushButton_robot)
        env.set_env_object(node)
        
        #after env-placement, to get the wright ENV_ID
        pushButton_robot.setObjectName(str(node.env_id))
        
        #register window-ref
        node.set_window_ref(window)
        node.set_env_ref(env)
        
        
        
        pushButton_robot.clicked.connect(node.view_parameter)
        pushButton_robot.clicked.connect(node.view_special_parameter)
        
        i=i+1
        
        
        #Init features object
        simulation_ad_hoc_multi_hop_network.features_obj=Draw_features()
        simulation_ad_hoc_multi_hop_network.features_obj.set_window(window)
        simulation_ad_hoc_multi_hop_network.features_obj.set_env(simulation_ad_hoc_multi_hop_network.env)
        features_obj=simulation_ad_hoc_multi_hop_network.features_obj
        
        simulation_ad_hoc_multi_hop_network.sync_algorithm=Network_time_sync(window,dialog_init,simulation_ad_hoc_multi_hop_network.env,features_obj)
        window.pushButton_start_simulation.clicked.connect(simulation_ad_hoc_multi_hop_network.sync_algorithm.initial_layer_creation)
        
        
    #crash a node CONNECT
    window.pushButton_crash_node.clicked.connect(simulation_ad_hoc_multi_hop_network.env.crash_node)
    
    #INIT first neighborhood-tables
    env.create_neighborhood_sorted_list_ALL()

        
        
        

         
 ######################################
 #ERROR_PRONE CODE -> END
 ######################################
    
    
        
        
#################################################################


    
    #Debugging
#     for id in env.env_objects:
#         print(env.env_objects[id],env.env_objects[id].mac_id,env.env_objects[id].layer,env.env_objects[id].coordinates,env.env_objects[id].is_beacon,env.env_objects[id].env_id)
      
  
    
      
    



    
    
    
    
    
    #Debugging
    #print(sync_algorithm.env.env_objects)
    
    
       
  


                    
def poo():
    print("POO")





#######################################################################
#ACTIONS

#Main-Window:
window.actionINIT.triggered.connect(dialog_init.show)


#INIT-Dialog:
dialog_init.buttonBox_dialog_init.accepted.connect(init_env)










#######################################################################


#BAD, buttons behind view!!!
# window.graphicsView_sim.setStyleSheet("background:transparent;");
# window.graphicsView_sim.setAttribute(Qt.WA_TranslucentBackground);
# window.graphicsView_sim.setWindowFlags(Qt.FramelessWindowHint);
# window.graphicsView_sim.raise_()


window.show()
sys.exit(app.exec_())



