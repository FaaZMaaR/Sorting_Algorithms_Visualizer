from PyQt6 import QtWidgets,QtGui
import sys
from main_window import MainWindow

app=QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(r"sort.png"))
window=MainWindow()
window.show()
sys.exit(app.exec())