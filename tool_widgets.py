from PyQt6 import QtWidgets,QtCore

class ElementsWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.label=QtWidgets.QLabel("Количество элементов")
        self.sbox=QtWidgets.QSpinBox()
        self.sbox.setRange(0, 150)
        self.sbox.setValue(100)
        self.sbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        vbox=QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.sbox)
        self.setLayout(vbox)

class SortsWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.label=QtWidgets.QLabel("Сортировка")
        self.cbox=QtWidgets.QComboBox()
        sorts=["Пузырьком","Выбором","Быстрая","Слиянием"]
        self.cbox.addItems(sorts)
        self.cbox.setEditable(False)
        self.cbox.textActivated.connect(self.on_activated)
        vbox=QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.cbox)
        self.setLayout(vbox)
        
    def on_activated(self,s):
        print("Выбран пункт",s)
        
class SpeedWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.label=QtWidgets.QLabel("Скорость")
        self.cbox=QtWidgets.QComboBox()
        self.cbox.addItem("x0.5",0.5)
        self.cbox.addItem("x1",1)
        self.cbox.addItem("x2",2)
        self.cbox.addItem("x4",4)
        self.cbox.setEditable(False)
        self.cbox.setCurrentIndex(1)
        self.cbox.textActivated.connect(self.on_activated)
        vbox=QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.cbox)
        self.setLayout(vbox)
        
    def on_activated(self,s):
        print("Выбран пункт",s)  