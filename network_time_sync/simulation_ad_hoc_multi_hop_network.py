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
from gui.Env_button import  *

import sys
import random

from gui import dialog_init
from gui.Draw_features import *
from algorithms.Network_time_sync import Network_time_sync
#from tkinter.dialog import DIALOG_ICON
import PySide
from PySide import QtGui




MAX_TRANSMITTION_RANGE=150.0









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
    app=None
    
    @staticmethod
    def delete_buttons():
        
        
        
#         for i in simulation_ad_hoc_multi_hop_network.buttons:
#             i.deleteLater()
#             simulation_ad_hoc_multi_hop_network.buttons=[]

        for key in simulation_ad_hoc_multi_hop_network.env.env_objects:
            simulation_ad_hoc_multi_hop_network.env.env_objects[key].gui_pushButton.deleteLater()
        
    
    

    

class MyApplication(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)
        
class MyDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)        


app = QtGui.QApplication(sys.argv)
simulation_ad_hoc_multi_hop_network.app= app

simulation_ad_hoc_multi_hop_network.window =  MyApplication()
window = simulation_ad_hoc_multi_hop_network.window

simulation_ad_hoc_multi_hop_network.dialog_init = MyDialog()
dialog_init =simulation_ad_hoc_multi_hop_network.dialog_init

#env=Node_environment(0,0)




#print("env:",env)








 




     
    




#Action_methods:
#INIT the environment trough the dialog choices
def init_env():
    
    #set seed
    random.seed(simulation_ad_hoc_multi_hop_network.dialog_init.doubleSpinBox_seed.value())
    
    
    #clear scene:
    simulation_ad_hoc_multi_hop_network.window.graphicsView_sim.setScene(PySide.QtGui.QGraphicsScene())
    #ANTIALISING ON
    simulation_ad_hoc_multi_hop_network.window.graphicsView_sim.setRenderHint(QtGui.QPainter.Antialiasing)
        
    
    if (len(simulation_ad_hoc_multi_hop_network.buttons)>0):
        simulation_ad_hoc_multi_hop_network.delete_buttons()
        
        #DISCONNECT old trigger and register at the end the new trigger with the new ENV-OBJECT!!!
        window.pushButton_crash_node.clicked.disconnect(simulation_ad_hoc_multi_hop_network.env.crash_node)
        window.pushButton_delete_node.clicked.disconnect(simulation_ad_hoc_multi_hop_network.env.delete_node)
        window.pushButton_undelete_node.clicked.disconnect(simulation_ad_hoc_multi_hop_network.env.undelete_node)
        window.pushButton_input_node.clicked.disconnect(simulation_ad_hoc_multi_hop_network.env.input_node)
        window.pushButton_pause_simulation.clicked.disconnect(simulation_ad_hoc_multi_hop_network.sync_algorithm.timerScreen.stop)
        window.pushButton_start_simulation.clicked.disconnect(simulation_ad_hoc_multi_hop_network.sync_algorithm.start_iteration)
        
        window.actionINIT.triggered.disconnect(simulation_ad_hoc_multi_hop_network.sync_algorithm.timerScreen.stop)
        window.actionINIT.triggered.disconnect(simulation_ad_hoc_multi_hop_network.sync_algorithm.initial_layer_creation)
        
        
         
        
    
        
    env_length=dialog_init.spinBox_env_length.value()
    env_width=dialog_init.spinBox_env_width.value()
    simulation_ad_hoc_multi_hop_network.env = Node_environment(simulation_ad_hoc_multi_hop_network.window,env_length,env_width)
    #Store for all classes
    env=simulation_ad_hoc_multi_hop_network.env
    
    
    #Init features object
    simulation_ad_hoc_multi_hop_network.features_obj=Draw_features()
    simulation_ad_hoc_multi_hop_network.features_obj.set_window(window)
    simulation_ad_hoc_multi_hop_network.features_obj.set_env(simulation_ad_hoc_multi_hop_network.env)
    features_obj=simulation_ad_hoc_multi_hop_network.features_obj
     
    simulation_ad_hoc_multi_hop_network.sync_algorithm=Network_time_sync(window,dialog_init,simulation_ad_hoc_multi_hop_network.env,features_obj)
    simulation_ad_hoc_multi_hop_network.sync_algorithm.set_app(simulation_ad_hoc_multi_hop_network.app)
    
    #print("1: ",simulation_ad_hoc_multi_hop_network.sync_algorithm)
    
    #register syc-algorithm
    env.set_sync_algorithm(simulation_ad_hoc_multi_hop_network.sync_algorithm)
    
    

    
    
    
    
    
###################################
#TO CHANGE ERROR_PRONE CODE ->BEGIN
###################################
    
    
    
    
#############################################################
#set nodes to the envornment
    
    
    #get actual seed
    
    #set beacons
    i=0
    security_cap= security_cap=0
    for nb in range(dialog_init.spinBox_nb_beacons.value()):
        node_id=nb
        
        while(True):
            x=random.randint(0,env_width-60)
            y=random.randint(0,env_length-40)
            
            if(not env.look_for_collision_xy(x,y)):
                break
            security_cap= security_cap+1
            if(security_cap>100000):
                x=0
                y=0
                break
            
            
        

        #OLD:
        #pushButton_robot = QtGui.QPushButton(window.widget_simulation_window)
        
        #NEW:
        pushButton_robot = Env_button(window.widget_simulation_window)
        
        
      
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
        
        
        

        
        node = Node(node_id,0,True,MAX_TRANSMITTION_RANGE,(x,y),(dialog_init.doubleSpinBox_vx.value(),dialog_init.doubleSpinBox_vy.value()),dialog_init.doubleSpinBox_v_length.value(),pushButton_robot)
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
        
        
        
        #first beacon for focus
        if(i==0):
            first_beacon=node
       
       
        env.set_node_random_velocity(node)
    
        i=i+1
    
    
    #set other nodes
    
    for nb in range(dialog_init.spinBox_nb_nodes.value()):
        node_id=nb+dialog_init.spinBox_nb_beacons.value()
        
        
        security_cap=0
        while(True):
            x=random.randint(0,env_width-60)
            y=random.randint(0,env_length-40)
            
            if(not env.look_for_collision_xy(x,y)):
                break
            security_cap= security_cap+1
            if(security_cap>100000):
                x=0
                y=0
                break
            
        
        
        
        #OLD:
        #pushButton_robot = QtGui.QPushButton(window.widget_simulation_window)
        
        #NEW:
        pushButton_robot = Env_button(window.widget_simulation_window)
        
        
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
        
        node = Node(node_id,-1,False,MAX_TRANSMITTION_RANGE,(x,y),(dialog_init.doubleSpinBox_vx.value(),dialog_init.doubleSpinBox_vy.value()),dialog_init.doubleSpinBox_v_length.value(),pushButton_robot)
        env.set_env_object(node)
        
        #after env-placement, to get the wright ENV_ID
        pushButton_robot.setObjectName(str(node.env_id))
        
        #register window-ref
        node.set_window_ref(window)
        node.set_env_ref(env)
        
        
        
        pushButton_robot.clicked.connect(node.view_parameter)
        pushButton_robot.clicked.connect(node.view_special_parameter)
        
        env.set_node_random_velocity(node)
        
        i=i+1
        
        

    window.pushButton_start_simulation.clicked.connect(simulation_ad_hoc_multi_hop_network.sync_algorithm.start_iteration)
        
    
    #input node CONNECT
    window.pushButton_input_node.clicked.connect(simulation_ad_hoc_multi_hop_network.env.input_node)
        
    #crash a node CONNECT
    window.pushButton_crash_node.clicked.connect(simulation_ad_hoc_multi_hop_network.env.crash_node)
    
    #delete & undelete SIGNAL SLOT
    window.pushButton_delete_node.clicked.connect(simulation_ad_hoc_multi_hop_network.env.delete_node)
    window.pushButton_undelete_node.clicked.connect(simulation_ad_hoc_multi_hop_network.env.undelete_node)
    
    #INIT first neighborhood-tables
    env.create_neighborhood_sorted_list_ALL()
    
    env.set_features_obj(features_obj)
    
    #set focus to beacon 0:
    env.set_selected_item(first_beacon)
    first_beacon.gui_pushButton.click()
    
    #register env to widget:
    simulation_ad_hoc_multi_hop_network.window.widget_simulation_window.set_env(simulation_ad_hoc_multi_hop_network.env)

    window.pushButton_pause_simulation.clicked.connect(simulation_ad_hoc_multi_hop_network.sync_algorithm.timerScreen.stop)   
    
    window.actionINIT.triggered.connect(simulation_ad_hoc_multi_hop_network.sync_algorithm.timerScreen.stop)  
    
    window.actionINIT.triggered.connect(simulation_ad_hoc_multi_hop_network.sync_algorithm.initial_layer_creation)
        
    #simulation_ad_hoc_multi_hop_network.sync_algorithm.myOwnSignal.connect(simulation_ad_hoc_multi_hop_network.env.slot_render)    

         
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
window.actionNewSim.triggered.connect(dialog_init.show)



#INIT-Dialog:
dialog_init.buttonBox_dialog_init.accepted.connect(init_env)










#######################################################################


#BAD, buttons behind view!!!
# window.graphicsView_sim.setStyleSheet("background:transparent;");
# window.graphicsView_sim.setAttribute(Qt.WA_TranslucentBackground);
# window.graphicsView_sim.setWindowFlags(Qt.FramelessWindowHint);
# window.graphicsView_sim.raise_()


print(app)

#print(window)
window.show()
#QCoreApplication.exit(0)
sys.exit(app.exec_())
#close Thread
simulation_ad_hoc_multi_hop_network.sync_algorithm.timerScreen.destroy()



