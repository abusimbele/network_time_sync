'''
Created on 10.08.2013

@author: Sascha Friedrich
'''

from PySide import QtCore, QtGui

class Widget_simulation_window(QtGui.QWidget):

    def __init__(self,parent):
        super(Widget_simulation_window,self).__init__(parent)
        
        self.env=None
        
        self.setAcceptDrops(True)
        self.show()
        
        
        print(parent)


    def set_env(self,env):
        self.env=env
       
           
        
#     def dropEvent(self,e):
#         print("FOO")
#         position = e.pos()
#     #         btn=self..env.get_selected_item.gui_pushButton
#         btn=super.pushButton_pause_simulation
#         btn.move(e.pos())
#         e.setDropAction(QtCore.Qt.MoveAction)
#         e.accept()
        
    def mouseReleaseEvent(self,e):
        position = e.pos()
    #         btn=self..env.get_selected_item.gui_pushButton
        node=self.env.get_selected_item()
        btn=node.gui_pushButton
        btn.move(e.pos())
        
        node.coordinates=((e.pos().x(),e.pos().y()))
        
        
        node.view_special_parameter()
        node.view_parameter()
        
        e.accept()
        
        
        