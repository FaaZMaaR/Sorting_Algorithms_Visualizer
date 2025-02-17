from PyQt6 import QtWidgets,QtCore,QtGui
import random

class GraphicArrayWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.array=[]
        self.set_array(100)
        self.selected1=-1
        self.selected2=-1
        self.selected3=-1
        
    def paintEvent(self,e):
        painter=QtGui.QPainter(self)
        black=QtCore.Qt.GlobalColor.black
        white=QtCore.Qt.GlobalColor.white
        red=QtCore.Qt.GlobalColor.red
        blue=QtCore.Qt.GlobalColor.blue
        green=QtCore.Qt.GlobalColor.green
        cyan=QtCore.Qt.GlobalColor.cyan
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3,3,self.width()-6,self.height()-6)
        
        painter.setPen(QtGui.QPen(red,3,style=QtCore.Qt.PenStyle.SolidLine))
        for i in range(len(self.array)):
            painter.drawLine(QtCore.QLine(20+i*7,350,20+i*7,350-(self.array[i]+1)*2))
            
        if self.selected1!=-1:
            painter.setPen(QtGui.QPen(blue,3,style=QtCore.Qt.PenStyle.SolidLine))
            painter.drawLine(QtCore.QLine(20+self.selected1*7,350,20+self.selected1*7,350-(self.array[self.selected1]+1)*2))
        if self.selected2!=-1:
            painter.setPen(QtGui.QPen(green,3,style=QtCore.Qt.PenStyle.SolidLine))
            painter.drawLine(QtCore.QLine(20+self.selected2*7,350,20+self.selected2*7,350-(self.array[self.selected2]+1)*2))
        if self.selected3!=-1:
            painter.setPen(QtGui.QPen(cyan,3,style=QtCore.Qt.PenStyle.SolidLine))
            painter.drawLine(QtCore.QLine(20+self.selected3*7,350,20+self.selected3*7,350-(self.array[self.selected3]+1)*2))
        
    def set_array(self,count):
        self.array=[i for i in range(count)]
        self.update()
        
    def shuffle(self):
        random.shuffle(self.array)
        self.update()