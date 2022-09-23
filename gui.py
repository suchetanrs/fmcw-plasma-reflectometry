import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
import matplotlib
matplotlib.use('TkAgg')
from PyEMD import EMD, Visualisation, EEMD
import math
from random import random

import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout


class SignalProcessing():

    def __init__(self):
        self.signal=0
        self.time=0
        self.signal_generation()
        pass

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
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QtCore.QRect(110, 60, 16, 23))
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QtCore.QRect(110, 100, 16, 23))
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QtCore.QRect(110, 140, 16, 23))
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QtCore.QRect(630, 110, 16, 23))
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QtCore.QRect(630, 150, 16, 23))
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QtCore.QRect(630, 190, 16, 23))
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QtCore.QRect(630, 230, 16, 23))

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
        self.pushButton.clicked.connect(self.show_plot)
        self.pushButton_2.clicked.connect(self.emd)
        self.pushButton_3.clicked.connect(self.eemd)
        self.pushButton_5.clicked.connect(self.stft)
    # retranslateUi


    def signal_generation(self):
        # Generating the self.signal
        self.time=np.arange(0,10,0.1)
        amplitude_sin1 = np.sin(self.time)
        amplitude_sin05 = np.sin(0.5*self.time)
        amplitude_cos2 = np.cos(2*self.time)
        amplitude_cos3 = np.cos(3*self.time)
        # noise = self.time*random()*1
        # print(self.time,noise)
        self.signal=amplitude_sin1*amplitude_cos3
        # +amplitude_sin05+amplitude_cos2+amplitude_cos3


    def emd(self):
        # EMD generation
        emd =EMD()
        emd.emd(self.signal)
        imfs, residue = emd.get_imfs_and_residue()
        no_of_imf=len(imfs)


        self.fig2 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=no_of_imf+2, figure=self.fig2)
        for i in range(0,no_of_imf):
            print(i)
            x = self.fig2.add_subplot(spec2[i,0])
            x.plot(self.time,imfs[i],'r')
        x = self.fig2.add_subplot(spec2[no_of_imf,0])
        x.plot(self.time,residue,'b')
        x = self.fig2.add_subplot(spec2[no_of_imf+1,0])
        x.plot(self.time,self.signal,'g')
    

    def eemd(self):
        eemd=EEMD()
        eemd.eemd(self.signal)
        imfs, residue = eemd.get_imfs_and_residue()
        no_of_imf=len(imfs)

        self.fig3 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=no_of_imf+2, figure=self.fig3)
        for i in range(0,no_of_imf):
            print(i)
            x = self.fig3.add_subplot(spec2[i,0])
            x.plot(self.time,imfs[i],'r')
        x = self.fig3.add_subplot(spec2[no_of_imf,0])
        x.plot(self.time,residue,'b')
        x = self.fig3.add_subplot(spec2[no_of_imf+1,0])
        x.plot(self.time,self.signal,'g')


    def stft(self):
        self.fig4 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=1, figure=self.fig4)
        x = self.fig4.add_subplot(spec2[0,0])
        x.specgram(self.signal,Fs=10)


    def show_plot(self):
        plt.show()
        # vis = Visualisation()
        # vis.plot_imfs(imfs=imfs, residue=residue, t=self.time, include_residue=True)
        # vis.plot_instant_freq(self.time, imfs=imfs)
        # vis.show()
    

    def main(self):
        self.signal_generation()
        self.emd()
        self.show_plot()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SignalProcessing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())