from PyQt5 import QtWidgets
from bin.Main import Ui_MainWindow

class WantVapPR(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def Select(self):
        # ----------------  If you check change label to say you want  ----------------#
        if self.VAP.isChecked():
            self.VAP.setText("VAPORIZAR")
        # ----------------  If you don't check change label to say you don't want  ----------------#
        else:
            self.VAP.setText("NO VAPORIZAR")