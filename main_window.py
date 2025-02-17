from PyQt6 import QtCore,QtWidgets,QtGui
from graphic_array_widget import GraphicArrayWidget
from tool_widgets import *
from sorts import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setWindowTitle("Алгоритмы сортировки")
        self.resize(1100,500)
        self.graphArray=GraphicArrayWidget()
        self.setCentralWidget(self.graphArray)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.setIconSize(QtCore.QSize(32,32))
        self.statusBar().showMessage("")
        self.set_actions()
        self.add_menu()
        self.add_tool_bar()
        
    def set_actions(self):
        self.actShuffle=QtGui.QAction("Перемешать")
        ico=self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_BrowserReload)
        self.actShuffle.setIcon(ico)
        self.actShuffle.setShortcut("Ctrl+F")
        self.actShuffle.triggered.connect(self.on_shuffle)
        
        self.actStart=QtGui.QAction("Запуск")
        ico=self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaPlay)
        self.actStart.setIcon(ico)
        self.actStart.setShortcut("Ctrl+S")
        self.actStart.triggered.connect(self.on_start)
        
        self.actStop=QtGui.QAction("Остановить")
        ico=self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MediaStop)
        self.actStop.setIcon(ico)
        self.actStop.setShortcut("Ctrl+D")
        self.actStop.triggered.connect(self.on_stop)
        self.actStop.setEnabled(False)
        
        self.actAbout=QtGui.QAction("О программе")
        ico=self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation)
        self.actAbout.setIcon(ico)
        self.actAbout.triggered.connect(self.on_about)
        
        self.actQuit=QtGui.QAction("Выход")
        ico=self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton)
        self.actQuit.setIcon(ico)
        self.actQuit.setShortcut("Ctrl+Q")
        self.actQuit.triggered.connect(QtWidgets.QApplication.instance().quit)

    def add_menu(self):
        self.menu=QtWidgets.QMenu("Меню")
        self.menu.addAction(self.actShuffle)
        self.menu.addSeparator()
        self.menu.addAction(self.actStart)
        self.menu.addAction(self.actStop)
        self.menu.addSeparator()
        self.menu.addAction(self.actAbout)
        self.menu.addAction(self.actQuit)
        self.menuBar().addMenu(self.menu)

    def add_tool_bar(self):
        self.toolBar=QtWidgets.QToolBar("Инструменты")
        self.elemsWidget=ElementsWidget()
        self.elemsWidget.sbox.valueChanged.connect(self.on_elements_changed)
        self.toolBar.addWidget(self.elemsWidget)
        self.toolBar.addAction(self.actShuffle)
        self.toolBar.addSeparator()        
        self.sortsWidget=SortsWidget()
        self.toolBar.addWidget(self.sortsWidget)
        self.speedWidget=SpeedWidget()
        self.toolBar.addWidget(self.speedWidget)
        self.toolBar.addAction(self.actStart)
        self.toolBar.addAction(self.actStop)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea,self.toolBar)

    def on_elements_changed(self,v):
        print("Значение изменено",v)
        self.statusBar().showMessage("Количество элементов в массиве изменено")
        self.graphArray.set_array(v)
    
    def on_shuffle(self):
        self.statusBar().showMessage("Массив перемешан")
        self.graphArray.shuffle()
    
    def on_start(self):
        self.elemsWidget.setEnabled(False)
        self.actShuffle.setEnabled(False)
        self.sortsWidget.setEnabled(False)
        self.speedWidget.setEnabled(False)
        self.actStart.setEnabled(False)
        self.actStop.setEnabled(True)
        self.sort=SortAlgo(self,self.graphArray,self.speedWidget.cbox.currentData())
        self.sort.start()
    
    def on_stop(self):
        self.graphArray.selected1=-1
        self.graphArray.selected2=-1
        self.graphArray.selected3=-1
        self.graphArray.update()
        self.elemsWidget.setEnabled(True)
        self.actShuffle.setEnabled(True)
        self.sortsWidget.setEnabled(True)
        self.speedWidget.setEnabled(True)
        self.actStart.setEnabled(True)
        self.actStop.setEnabled(False)
        self.sort.terminate()
    
    def on_about(self):
        QtWidgets.QMessageBox.about(self,"О программе","<center>\"Алгоритмы сортировки\" v1.0.0<br><br>Программа визуализации аргоритмов сортировки<br><br>(c) FaaZMaaR, 2025")