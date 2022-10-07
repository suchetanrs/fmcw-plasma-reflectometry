import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
import matplotlib

import math
import sys
import os

from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout

from random import random
from PyEMD import EMD, Visualisation, EEMD
import tftb
import pywt

from scipy import signal
matplotlib.use('TkAgg')

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
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QtCore.QRect(20, 180, 99, 25))
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QtCore.QRect(20, 250, 99, 25))
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QtCore.QRect(20, 280, 99, 25))
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
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QtCore.QRect(121, 183, 16, 23))
        # self.checkBox_9 = QtWidgets.QCheckBox(Dialog)
        # self.checkBox_9.setObjectName(u"checkBox_9")
        # self.checkBox_9.setGeometry(QtCore.QRect(121, 183, 16, 23))
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
        self.pushButton_5.setText(QtCore.QCoreApplication.translate("Dialog", u"Spectrogram", None))
        self.pushButton_6.setText(QtCore.QCoreApplication.translate("Dialog", u"Wigner Ville", None))
        self.pushButton_7.setText(QtCore.QCoreApplication.translate("Dialog", u"P Wigner Ville", None))
        self.pushButton_8.setText(QtCore.QCoreApplication.translate("Dialog", u"STFT", None))
        self.pushButton_9.setText(QtCore.QCoreApplication.translate("Dialog", u"WaveletPacket", None))
        self.pushButton_10.setText(QtCore.QCoreApplication.translate("Dialog", u"InverseWaveletPacket", None))
        self.pushButton_11.setText(QtCore.QCoreApplication.translate("Dialog", u"RAW SIGNAL", None))
        self.pushButton.clicked.connect(self.show_plot)
        self.pushButton_2.clicked.connect(self.emd)
        self.pushButton_3.clicked.connect(self.eemd)
        self.pushButton_5.clicked.connect(self.spectro_gram)
        self.pushButton_6.clicked.connect(self.wvd)
        # self.pushButton_7
        self.pushButton_8.clicked.connect(self.short_time_ft)
        self.pushButton_9.clicked.connect(self.waveletTransform)
        self.pushButton_10.clicked.connect(self.InverseWaveletTransform)
        self.pushButton_11.clicked.connect(self.plot_signal)
    # retranslateUi


    def signal_generation(self):

        ###### CUSTOM SIGNAL
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



        ##### PLASMA WALL DATA #######

        # home=os.getenv('HOME')
        # wall_data_path=os.path.join(home,'SOP_3_2/Wall_data_files/shtt601')
        # print(wall_data_path)

        # curr_file=os.path.join(wall_data_path,'tIQ_t601_1.dat')
        # print(curr_file)

        # t, I, Q = np.loadtxt(curr_file)

        # self.time=t
        # I_square=np.multiply(I,I)
        # Q_square=np.multiply(Q,Q)
        # self.signal=np.sqrt(I_square+Q_square)

        # self.signal=I+1j*Q

    def plot_signal(self):
        self.fig0=plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=1, figure=self.fig0)
        x = self.fig0.add_subplot(spec2[0,0])
        x.plot(self.time,self.signal)

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


    def spectro_gram(self):
        self.fig4 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=1, figure=self.fig4)
        x = self.fig4.add_subplot(spec2[0,0])
        x.specgram(self.signal,Fs=200000000,noverlap=92,pad_to=10240,mode='magnitude',scale='linear',sides='onesided')

    def short_time_ft(self):
        fs=200000000
        self.fig6 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=1, figure=self.fig6)
        x = self.fig6.add_subplot(spec2[0,0])

        f, t, Zxx = signal.stft(self.signal, fs,noverlap=92,return_onesided=True,nfft=102,padded=True,nperseg=100)
        x.pcolormesh(t, f, np.abs(Zxx), shading='auto')
        # x.title('STFT Magnitude')
        # x.ylabel('Frequency [Hz]')
        # x.xlabel('Time [sec]')
        print('stft generated')
        # print(np.shape(Zxx))

    def wvd(self):
        # Wigner Ville Distribution
        fs = 1000000000
        dt = 1/fs
        ts = self.time
        ts = ts*dt

        wvd = tftb.processing.WignerVilleDistribution(self.signal, timestamps=ts)
        tfr_wvd, t_wvd, f_wvd = wvd.run()

        f_wvd = np.fft.fftshift(np.fft.fftfreq(tfr_wvd.shape[0], d=2 * dt))
        df_wvd = f_wvd[1]-f_wvd[0]
        self.fig5 = plt.figure(constrained_layout=True)
        x = self.fig5.add_subplot()

        im = x.imshow(np.fft.fftshift(tfr_wvd, axes=0), aspect='auto', origin='lower',
            extent=(ts[0] - dt/2, ts[-1] + dt/2,
                    f_wvd[0]-df_wvd/2, f_wvd[-1]+df_wvd/2))

        # x.plot(self.time, np.fft.fftshift(tfr_wvd, axes=0))
        # set xlabel, ylabel 
        print("Wigner Ville completed")
    
    def waveletTransform(self):
        self.coeffs = pywt.wavedec(self.signal,wavelet='db1')
        no_of_dec=len(self.coeffs)
        print(type(self.coeffs[0]))
        print(self.coeffs)
        self.fig7 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=no_of_dec+2, figure=self.fig7)
        for i in range(0,no_of_dec):
            print(i)
            x = self.fig7.add_subplot(spec2[i,0])
            x.plot(self.coeffs[no_of_dec-i-1],'r')
            x.set_title("Decomposition {}".format(i+1))
        x = self.fig7.add_subplot(spec2[no_of_dec,0])
        x.plot(self.time,self.signal,'g')
        print(len(self.coeffs))

    def InverseWaveletTransform(self):
        rec_signal = pywt.waverec(self.coeffs,wavelet='db1')
        self.fig8 = plt.figure(constrained_layout=True)
        spec2 = gridspec.GridSpec(ncols=1, nrows=1, figure=self.fig8)
        # for i in range(0,no_of_dec):
        #     print(i)
        #     x = self.fig7.add_subplot(spec2[i,0])
        #     x.plot(self.coeffs[no_of_dec-i-1],'r')
        #     x.set_title("Decomposition {}".format(i+1))
        x = self.fig8.add_subplot(spec2[0,0])
        x.plot(self.time,rec_signal,'g')
        print(len(self.coeffs))

    def show_plot(self):
        plt.show()
        # vis = Visualisation()
        # vis.plot_imfs(imfs=imfs, residue=residue, t=self.time, include_residue=True)
        # vis.plot_instant_freq(self.time, imfs=imfs)
        # vis.show()
    

    def main(self):
        self.signal_generation()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SignalProcessing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())