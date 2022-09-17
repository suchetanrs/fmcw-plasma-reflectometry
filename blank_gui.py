
import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(888, 544)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(720, 40, 89, 25))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 17))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 89, 25))
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(20, 100, 89, 25))
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QtCore.QRect(20, 140, 89, 25))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(720, 80, 111, 17))
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QtCore.QRect(648, 110, 221, 25))
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QtCore.QRect(648, 150, 221, 25))
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QtCore.QRect(650, 190, 221, 25))
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QtCore.QRect(650, 230, 221, 25))

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtCore.QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QtCore.QCoreApplication.translate("Dialog", u"Plot", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"Decompositions", None))
        self.pushButton_2.setText(QtCore.QCoreApplication.translate("Dialog", u"EMD", None))
        self.pushButton_3.setText(QtCore.QCoreApplication.translate("Dialog", u"EEMD", None))
        self.pushButton_4.setText(QtCore.QCoreApplication.translate("Dialog", u"VMD", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("Dialog", u"Distributions", None))
        self.pushButton_5.setText(QtCore.QCoreApplication.translate("Dialog", u"STFT", None))
        self.pushButton_6.setText(QtCore.QCoreApplication.translate("Dialog", u"Wigner Ville", None))
        self.pushButton_7.setText(QtCore.QCoreApplication.translate("Dialog", u"P Wigner Ville", None))
        self.pushButton_8.setText(QtCore.QCoreApplication.translate("Dialog", u"Smoothed Pseudo Wigner Ville", None))
    # retranslateUi

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())