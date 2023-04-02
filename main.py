import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSlot

from ui_Interface import Ui_mainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

##############################################################################################################
    #DEFINIMOS SLOTS O CONEXIONES ENTRE OBEJTOS Y ACCIONES
        self.ui.buttonConnect.clicked.connect(slot=self.copyANDpasteText)
        
##############################################################################################################        
    #DEFINIMOS ACCIONES    
    @pyqtSlot()
    def copyANDpasteText(self):
        self.ui.outputLine.setText((self.ui.inputLine).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())