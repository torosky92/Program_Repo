from PyQt5 import QtWidgets
from bin.Main import Ui_MainWindow

class WantCodePR(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def find(self):
        # ----------------  If you check change label to say you want  ----------------#
        if self.VAP_2.isChecked():
            self.VAP_2.setText("Cod. De Barras")
            self.CB1_4.show()
            self.MAQ_2.close()
        # ----------------  If you don't check change label to say you don't want  ----------------#
        else:
            self.VAP_2.setText("Lista")
            self.CB1_4.close()
            self.MAQ_2.show()
            for x in range(len(self.CodeB)):
                self.MAQ_2.addItem(str(self.CodeB[x]))