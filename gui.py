import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
import matplotlib
matplotlib.use('TkAgg')
from PyEMD import EMD, Visualisation
import math
from random import random
import tftb

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
    
    def wvd(self):
        # Wigner Ville Distribution
        fs = 10
        dt = 1/fs
        ts = self.time
        ts = ts*dt

        wvd = tftb.processing.WignerVilleDistribution(self.signal, timestamps=ts)
        tfr_wvd, t_wvd, f_wvd = wvd.run()

        f_wvd = np.fft.fftshift(np.fft.fftfreq(tfr_wvd.shape[0], d=2 * dt))
        df_wvd = f_wvd[1]-f_wvd[0] 

        x = self.fig2.add_subplot()
        x.plot(self.time, np.fft.fftshift(tfr_wvd, axes=0))
        # set xlabel, ylabel 

    def HilbertHuangTransform(self):
        ''' 
        EMD -> Hilbert transform to calculate IFs -> Time-frequency distribution
        '''
        emd =EMD()
        emd.emd(self.signal)
        imfs, _ = emd.get_imfs_and_residue()

        # IP - instantaneous phase, IF - frequency, IA - amplitude
        IP, IF, IA = emd.spectra.frequency_transform(imfs, 256, 'nht')

        freq_edges, freq_centres = emd.spectra.define_hist_bins(0, 100, 128, 'linear')   # need to change range from 0-100 to signal range

        # Amplitude weighted HHT per IMF
        f, spec_weighted = emd.spectra.hilberthuang(IF, IA, freq_edges, sum_imfs=False)

        plt.plot(freq_centres, spec_weighted)
        plt.xticks(np.arange(10)*10)
        plt.xlim(0, 100)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.title('IA-weighted\nHilbert-Huang Transform')
        plt.legend(['IMF-1', 'IMF-2', 'IMF-3', 'IMF-4', 'IMF-5'], frameon=False)


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


# f2_ax1 = self.fig2.add_subplot(spec2[0, 0])
# f2_ax2 = self.fig2.add_subplot(spec2[0, 1])
# f2_ax3 = self.fig2.add_subplot(spec2[1, 0])
# f2_ax4 = self.fig2.add_subplot(spec2[1, 1])

# f2_ax1.plot(self.time,self.signal)
# f2_ax2.plot(self.time,imfs[0])
# f2_ax3.plot(self.time,imfs[1])
# f2_ax4.plot(self.time,residue)

# plt.show()
# print(np.size(imfs[1]))
# plt.plot(self.time,imfs[1])
# plt.show()
# plt.subplot(1,4,4)
# plt.plot(self.time,self.signal)

# plt.subplot(1,4,1)
# plt.plot(self.time,imfs[0])

# plt.subplot(1,4,2)
# plt.plot(self.time,imfs[1])

# plt.subplot(1,4,3)
# plt.plot(self.time,residue)

# plt.show()


