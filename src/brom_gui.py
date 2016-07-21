import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QSpinBox

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#import matplotlib.rcParams as rc
from readfile import *
from limits import * 
import matplotlib.gridspec as gridspec
from matplotlib import style
#import matplotlib as mpl

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure(figsize = (24,15))

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        self.numdaySpinBox = QSpinBox()
        self.numdaySpinBox.setRange(1, 366)
        self.numdaySpinBox.setValue(100)
        self.button.clicked.connect(self.plot)       
        
        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.numdaySpinBox)       
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        plt.clf() #clear figure before updating 
        numday = self.numdaySpinBox.value() #take the input value of numday
        wspace=0.40
        hspace = 0.05
        gs = gridspec.GridSpec(2, 6) 
        gs.update(left=0.06, right=0.93,top = 0.86,bottom = 0.4, wspace=wspace,hspace=hspace)
        gs1 = gridspec.GridSpec(1, 6)
        gs1.update(left=0.06, right=0.93, top = 0.26, bottom = 0.02, wspace=wspace,hspace=hspace)        
        
        style.use('ggplot')
#        mpl.rc('xtick', direction = 'out')
#        mpl.rc('xtick.major',pad = 0 )      
  
        # create an axis
        ax00 = self.figure.add_subplot(gs[0])
        ax10 = self.figure.add_subplot(gs[1])
        ax20 = self.figure.add_subplot(gs[2])
        ax30 = self.figure.add_subplot(gs[3])        
        ax40 = self.figure.add_subplot(gs[4])
        ax50 = self.figure.add_subplot(gs[5]) 
        
        ax01 = self.figure.add_subplot(gs[6])
        ax11 = self.figure.add_subplot(gs[7])
        ax21 = self.figure.add_subplot(gs[8])
        ax31 = self.figure.add_subplot(gs[9])        
        ax41 = self.figure.add_subplot(gs[10])
        ax51 = self.figure.add_subplot(gs[11])  

        ax02 = self.figure.add_subplot(gs1[0])
        ax12 = self.figure.add_subplot(gs1[1])
        ax22 = self.figure.add_subplot(gs1[2])
        ax32 = self.figure.add_subplot(gs1[3])        
        ax42 = self.figure.add_subplot(gs1[4])
        ax52 = self.figure.add_subplot(gs1[5])
        
                      

 
        def y_lim(axis):
            if axis in (ax00,ax10,ax20,ax30,ax40,ax50):
                axis.set_ylim([y2min, 0])
            elif axis in (ax01,ax11,ax21,ax31,ax41,ax51):
                axis.set_ylim([y2max, y2min]) 
            elif axis in (ax02,ax12,ax22,ax32,ax42,ax52):
                axis.set_ylim([y3max, y3min])      
                
                
                           
        ax00.set_ylabel('Depth (m)')
        ax01.set_ylabel('Depth (m)')   
        ax02.set_ylabel('Depth (cm)') 
                     
        ax00_1 = ax00.twiny() 
        ax00_2 = ax00.twiny()  
  
        ax10_1 = ax10.twiny() 
        ax10_2 = ax10.twiny() 
        

        
        def spines(axis):        
            for spinename, spine in axis.spines.iteritems():
                if spinename != 'top':
                    spine.set_visible(False)
            if axis in (ax00_1,ax10_1):
                axis.spines['top'].set_position(('outward', axis1))
                axis.spines['top'].set_color('b')                 
            elif axis in (ax00_2,ax10_2):    
                axis.spines['top'].set_position(('outward', axis2))
                axis.spines['top'].set_color('r')   
                
                
        spines(ax00_1)
        spines(ax00_2)                  
        spines(ax10_1) 
        spines(ax10_2)             
        # discards the old graph
#        ax.hold(False)
#        ax1.hold(False)
        #define limits for all axis
        
        #water subplots
        y_lim(ax00) 
        y_lim(ax10) 
        y_lim(ax20) 
        y_lim(ax30)         
        y_lim(ax40) 
        y_lim(ax50) 
        #bbl subplots                
        y_lim(ax01) 
        y_lim(ax11)         
        y_lim(ax21) 
        y_lim(ax31)         
        y_lim(ax41) 
        y_lim(ax51)       
        #sediment subplots        
        y_lim(ax02) 
        y_lim(ax12)         
        y_lim(ax22) 
        y_lim(ax32)         
        y_lim(ax42) 
        y_lim(ax52)  
        
          
        ax00_1.set_xlim([tempmin,tempmax])      
        ax00_2.set_xlim([salmin,salmax])  
        
        # plot data
        ax00_1.plot(temp[numday],depth,'b-') 
        ax00_2.plot(sal[numday],depth,'r-')       
        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())























'''# -*- coding: utf-8 -*-

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

        self.ax1.plot(sal[numday],depth,'g-')

    def update_figure(self):
        print "called update figure"

        getvalue = ApplicationWindow()
        numday = getvalue.updateUi() #SpinBox.value()

        intnumday = int(numday)
        print numday
        self.ax1.plot(sal[intnumday],depth,'g-')      
#        numday = int(numday)
#       numday = getvalue.numday()

#        numday = 160 #getvalue.numday()
#        numday = getvalue.self.numday

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
        self.currentnumdayResultLabel = QLabel('Current day: ')
        self.numdaySpinBox = QSpinBox()
        self.applyButton = QPushButton('Apply')  
        self.currentnumdayResultLabel1 = QLabel() 
        l.addWidget(self.currentnumdayResultLabel) 
        l.addWidget(self.numdaySpinBox) 
        l.addWidget(self.applyButton)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(dc)       
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.numdaySpinBox.valueChanged.connect(self.updateUi)
        toconnect = MyDynamicMplCanvas()
#        self.applyButton.clicked.connect(toconnect.update_figure)
#        toconnect = MyDynamicMplCanvas()
#        self.ok.clicked.connect(toconnect.update_figure)
        self.applyButton.clicked.connect(toconnect.update_figure)         
        numday2 = self.numdaySpinBox.value()
        self.statusBar().showMessage("Wait", 2000)
        return numday2 
#        self.numday()
        self.updateUi()  
    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self, "About", 
                                '''#embedding_in_qt4.py example                            
#Copyright 
#Needs to be filled 
#It may be used and modified with no restriction; raw copies as well as
#modified versions may be distributed without limitation.''')

'''    def numday(self):
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
#        print type(numday2)
        printnumday = str(numday2)
#        print "numday: "+printnumday
        self.currentnumdayResultLabel.setText(printnumday)
        self.currentnumdayResultLabel.setText('Current day:'+printnumday)  
    
#        self.dialog.exec_()           

qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()'''