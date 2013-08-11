'''
Created on 10.08.2013

@author: Sascha Friedrich
'''
from PySide import  QtGui
from PySide import  QtCore


class Env_button(QtGui.QPushButton):
    def __init__(self,parent):
        super(Env_button,self).__init__(parent)
        
        
#    def mouseMoveEvent(self, e):
#         if(e.buttons()!= QtCore.Qt.LeftButton):
#             return
#         
#         mimeData =QtCore.QMimeData()
#         
#         drag=QtGui.QDrag(self)
#         drag.setMimeData(mimeData)
#         drag.setHotSpot(e.pos()-self.rect().topLeft())
#         
#         dropAction=drag.start(QtCore.Qt.MoveAction)
        
#        print("FOO-EMITT")
        
    
    
    
    