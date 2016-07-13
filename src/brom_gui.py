# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

#!/usr/bin/env python

# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
from matplotlib.backends import qt_compat
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from PyQt4.QtGui import (QApplication, QComboBox, QDialog, 
        QDoubleSpinBox, QGridLayout, QLabel,QSpinBox,QPushButton,
        QDialogButtonBox)
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSignal as Signal
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from readfile import *   # import all variables from readfile
from limits import *

progname = os.path.basename(sys.argv[0])
progversion = "0.1"

numday = 100 #to change

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(24,15), dpi=dpi)
        
        gs = gridspec.GridSpec(3, 6) 
        gs.update(left=0.06, right=0.93,top = 0.86,bottom = 0.20,wspace= 0.6,hspace= 0.05)
        self.ax1 = fig.add_subplot(gs[0])
        self.ax2 = fig.add_subplot(gs[1]) 
        self.ax3 = fig.add_subplot(gs[2])
        self.ax4 = fig.add_subplot(gs[3])  
        self.ax5 = fig.add_subplot(gs[4])
        self.ax6 = fig.add_subplot(gs[5]) 
        self.ax7 = fig.add_subplot(gs[6])
        self.ax8 = fig.add_subplot(gs[7])
        self.ax9 = fig.add_subplot(gs[8])
        self.ax10= fig.add_subplot(gs[9]) 
        self.ax11= fig.add_subplot(gs[10])
        self.ax12= fig.add_subplot(gs[11])  
        self.ax13= fig.add_subplot(gs[12])
        self.ax14= fig.add_subplot(gs[13]) 
        self.ax15= fig.add_subplot(gs[14])
        self.ax16= fig.add_subplot(gs[15])
        self.ax17= fig.add_subplot(gs[16])
        self.ax18= fig.add_subplot(gs[17])       
   
          
        # We want the axes cleared every time plot() is called
        self.ax1.hold(False)
        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
         
    def compute_initial_figure(self):
        pass

class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
#        self.ax2.plot(temp[numday], depth,'r')
        self.ax2.set_ylabel('Depth (m)')
        self.ax2.set_ylim([y2min, 0])
        plt.setp(self.ax1.get_xticklabels(), visible=False)
        self.ax2.set_xlim([kzmin,kzmax])
        self.ax2.set_xticks(np.arange(kzmin,2*kzmax ,(kzmax)))
#        fig.text(0, 1.5,numday , fontweight='bold', #Write number of day to Figure
#                 bbox={'facecolor': 'white', 'alpha':0.5, 'pad':10}, fontsize=14,
#            transform=self.ax1.transAxes)
#        self.ax2 = self.ax1.twiny()
#        for spinename, spine in ax11.spines.iteritems():
#            if spinename != 'top':
#                spine.set_visible(False)
#        self.ax11.spines['top'].set_position('outward') #, axis1))
        self.ax2.spines['top'].set_color('g')
        self.ax2.plot(sal[numday],depth,'g-')
#        plt.grid(True)
#        self.ax11.set_xticks(np.arange(kzmin,kzmax +(kzmax- kzmin)/2. ,(kzmax- kzmin)/2.))
#ax11.xaxis.set_major_locator(ticker.LogLocator(base = 1.e-10)) # can make xaxis logarithmic
        self.ax2.set_xlim(salmin, salmax)
#ax11.set_xticks(np.arange(1.e-6,(1.e-0)+ ((1.e-0 - 1.e-6)/2.),((1.e-0 - 1.e-6)/2.)))
        self.ax2.set_ylim([y1max, 0])
#        self.ax11.annotate(r'$\rm Kz $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
#            xycoords='axes fraction',  fontsize = xlabel_fontsize,color='g')
#        self.draw()


    def update_figure(self):
        print "called update figure"
        getvalue = ApplicationWindow()

        numday = getvalue.updateUi() #SpinBox.value()
#        numday = int(numday)
#       numday = getvalue.numday()
        print numday
#        numday = 160 #getvalue.numday()
#        numday = getvalue.self.numday
        print numday
#        n = numday 
#        self.ax1.plot(sal[n],depth,'b-')
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
#        l = self.numday
#        self.ax1.plot([0, 1, 2, 3],l,'r')
        self.draw()


class ApplicationWindow(QtGui.QMainWindow):
#    MyDynamicMplCanvas.update_figure() 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
#        self.create_connections(self)
       
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.file_menu.addAction('Change day', self.numday)
#        penButton.clicked.connect(self.setPenProperties)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)      
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
#        self.menuBar().addMenu(self.change_menu)
        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QVBoxLayout(self.main_widget)
#        currentnumdayLabel = QLabel('Current numday: ')
#        self.numdaySpinBox = QSpinBox()
#        applyButton = QPushButton('Apply')  
        self.currentnumdayResultLabel1 = QLabel() 


      

        l.addWidget(self.currentnumdayResultLabel1) 
#        l.addWidget(self.numdaySpinBox) 
#        l.addWidget(applyButton)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(dc)       
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

#        self.statusBar().showMessage("All hail matplotlib!", 2000)
#        self.numday()
#        self.updateUi()  
    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self, "About", 
                                '''embedding_in_qt4.py example                            
Copyright 
Needs to be filled 
It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.''')

    def numday(self):
        dialog = QtGui.QDialog()
        self.text = QLabel("Choose day to plot")
        self.numdayLabel = QLabel("day:")
        self.numdaySpinBox = QSpinBox()
        self.numdaySpinBox.setRange(1, 365)
        self.numdaySpinBox.setValue(100)
        self.ok = QtGui.QPushButton('OK', dialog)

        self.ok.setDefault(True)
        self.applyButton = QPushButton('Apply')
        self.cancelButton = QPushButton('Cancel')
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Apply|
                         QDialogButtonBox.Close)        
        self.currentnumdayLabel = QLabel('Current numday: ')
        self.currentnumdayResultLabel = QLabel()
        dialog.layout = QtGui.QGridLayout(dialog)     
        dialog.layout.addWidget(self.text,0,0)
        dialog.layout.addWidget(self.numdayLabel, 1, 0)
        dialog.layout.addWidget(self.numdaySpinBox, 1, 1)  
        dialog.layout.addWidget(self.buttonBox,2, 0, 2, 2)   
        dialog.layout.addWidget(self.currentnumdayLabel,4,0)
        dialog.layout.addWidget(self.currentnumdayResultLabel,4,1)  
        dialog.layout.addWidget(self.ok, 5, 5) 
             
        numday = self.numdaySpinBox.value()
        printnumday = str(numday)
        self.currentnumdayResultLabel.setText(printnumday)
        self.numdaySpinBox.valueChanged.connect(self.updateUi)  #create_connections
        
        dialog.exec_()  
           
    def updateUi(self):
        """Takes the new value of numday """
        numday2 = self.numdaySpinBox.value()
        print type(numday2)
        printnumday = str(numday2)
        print "numday: "+printnumday
        self.currentnumdayResultLabel.setText(printnumday)
        self.currentnumdayResultLabel1.setText('Current day:'+printnumday)  
        toconnect = MyDynamicMplCanvas()
        self.ok.clicked.connect(toconnect.update_figure)
         
        return printnumday     
#        self.dialog.exec_()           

qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()