import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QSpinBox,QLabel

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
#import numpy as np
from readfile import *
from limits import * 
import matplotlib.gridspec as gridspec
from matplotlib import style
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import ScalarFormatter
#import matplotlib as mpl

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("BROM Pictures")
        self.setWindowIcon(QtGui.QIcon('like.png'))
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.figure = plt.figure(figsize = (30,10))

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot Figure 1')
        self.button2 = QtGui.QPushButton('Plot Figure 2')        
        self.button.clicked.connect(self.plot1)
        self.button2.clicked.connect(self.plot2)
        self.numdaySpinBox = QSpinBox()
        self.Daylabel = QLabel('Choose day to plot:')
        self.numdaySpinBox.setRange(1, 366)
        self.numdaySpinBox.setValue(100)
        self.button.clicked.connect(self.plot1)       

        # set the layout
        layout = QtGui.QGridLayout()
        layout.addWidget(self.toolbar,0,2,1,2)
        layout.addWidget(self.canvas,1,2,1,2)
        layout.addWidget(self.numdaySpinBox,4,2,1,1) 
        layout.addWidget(self.button,3,3,1,2)
        layout.addWidget(self.button2,4,3,1,2)        
#        layout.addWidget(self.Daylabel,3,2,1,2)        
        self.setLayout(layout)


    def plot1(self): #main function to define figure
        ''' plot some random stuff '''
        plt.clf() #clear figure before updating 

        numday = self.numdaySpinBox.value() #take the input value of numday
        style.use('ggplot')    #use predefined style        
        wspace=0.40 #define values for grid
        hspace = 0.05
        gs = gridspec.GridSpec(2, 6) 
        gs.update(left=0.06, right=0.93,top = 0.84,bottom = 0.4, wspace=wspace,hspace=hspace)
        gs1 = gridspec.GridSpec(1, 6)
        gs1.update(left=0.06, right=0.93, top = 0.26, bottom = 0.02, wspace=wspace,hspace=hspace)     
           
                #create subplots
        ax00 = self.figure.add_subplot(gs[0]) # water
        ax10 = self.figure.add_subplot(gs[1])
        ax20 = self.figure.add_subplot(gs[2])
        ax30 = self.figure.add_subplot(gs[3])        
        ax40 = self.figure.add_subplot(gs[4])
        ax50 = self.figure.add_subplot(gs[5]) 
        
        ax01 = self.figure.add_subplot(gs[6]) #BBL
        ax11 = self.figure.add_subplot(gs[7])
        ax21 = self.figure.add_subplot(gs[8])
        ax31 = self.figure.add_subplot(gs[9])        
        ax41 = self.figure.add_subplot(gs[10])
        ax51 = self.figure.add_subplot(gs[11])  

        ax02 = self.figure.add_subplot(gs1[0]) #sediment
        ax12 = self.figure.add_subplot(gs1[1])
        ax22 = self.figure.add_subplot(gs1[2])
        ax32 = self.figure.add_subplot(gs1[3])        
        ax42 = self.figure.add_subplot(gs1[4])
        ax52 = self.figure.add_subplot(gs1[5])
        
        plt.text(1.1, 0.5,'Water ', fontweight='bold', #Write number of day to Figure
        bbox={'facecolor': wat_color, 'alpha':0.5, 'pad':10}, fontsize=14, rotation=90, 
        transform=ax50.transAxes) 
            
        def y_lim(axis): #function to define y limits 
#            y_formatter = 
            majorLocator = MultipleLocator(2.)
            majorFormatter = ScalarFormatter(useOffset=False)   #format y scales to be scalar 
            minorLocator = MultipleLocator(1.)

            if axis in (ax00,ax10,ax20,ax30,ax40,ax50): #water
                axis.set_ylim([y2min, 0])
                axis.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat)
            elif axis in (ax01,ax11,ax21,ax31,ax41,ax51): #BBL
                axis.set_ylim([y2max, y2min])
                axis.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
                axis.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
            elif axis in (ax02,ax12,ax22,ax32,ax42,ax52): #sediment 
                axis.set_ylim([y3max, y3min])      
                axis.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)  
                axis.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)    
                axis.yaxis.set_major_locator(majorLocator)
                axis.yaxis.set_major_formatter(majorFormatter)
                axis.yaxis.set_minor_locator(minorLocator)
                axis.yaxis.grid(True,'minor')
                axis.yaxis.grid(True,'major')
                plt.setp(axis.get_xticklabels(), visible=False) 
                 
                 
                 
                                              
        ax00.set_ylabel('Depth (m)')
        ax01.set_ylabel('Depth (m)')   
        ax02.set_ylabel('Depth (cm)')                

        plt.text(0, 1.61,'{}{}'.format('day', numday) , fontweight='bold', #Write number of day to Figure
        bbox={'facecolor': wat_color, 'alpha':0.5, 'pad':10}, fontsize=14,
        transform=ax00.transAxes)
        
 
        #Create axes sharing y              
        ax00_1 = ax00.twiny()  #water
        ax00_2 = ax00.twiny()  
        ax00_3 = ax00.twiny()
        
        ax01_1 = ax01.twiny() #bbl
        ax01_2 = ax01.twiny()
        ax01_3 = ax01.twiny()


        ax02_1 = ax02.twiny() #sediment
        ax02_2 = ax02.twiny()
        ax02_3 = ax02.twiny()
#        ax02_4 = ax02.twiny()
                 
        ax10_1 = ax10.twiny() #water
        ax10_2 = ax10.twiny() 
        ax10_3 = ax10.twiny()        
        ax10_4 = ax10.twiny()
#        ax10_5 = ax10.twiny()
        
        ax11_1 = ax11.twiny() #bbl
        ax11_2 = ax11.twiny()
        ax11_3 = ax11.twiny()
        ax11_4 = ax11.twiny()  

        ax12_1 = ax12.twiny() #sediment
        ax12_2 = ax12.twiny()
        ax12_3 = ax12.twiny()
        ax12_4 = ax12.twiny() 
                 
        ax20_1 = ax20.twiny() 
        ax20_2 = ax20.twiny() 
        ax20_3 = ax20.twiny()        
#        ax20_4 = ax20.twiny() 
        
        ax21_1 = ax21.twiny() 
        ax21_2 = ax21.twiny() 
        ax21_3 = ax21.twiny()        
#        ax21_4 = ax21.twiny() 

        ax22_1 = ax22.twiny() 
        ax22_2 = ax22.twiny() 
        ax22_3 = ax22.twiny() 
                       
        ax30_1 = ax30.twiny() 
        ax30_2 = ax30.twiny() 
        ax30_3 = ax30.twiny()        
        ax30_4 = ax30.twiny()            
        ax30_5 = ax30.twiny()
        
        ax31_1 = ax31.twiny() 
        ax31_2 = ax31.twiny() 
        ax31_3 = ax31.twiny()        
        ax31_4 = ax31.twiny()            
        ax31_5 = ax31.twiny()        
 
        ax32_1 = ax32.twiny() 
        ax32_2 = ax32.twiny() 
        ax32_3 = ax32.twiny()        
        ax32_4 = ax32.twiny()            
        ax32_5 = ax32.twiny()  
       
        ax40_1 = ax40.twiny() 
        ax40_2 = ax40.twiny() 
        ax40_3 = ax40.twiny()        
        ax40_4 = ax40.twiny()            
 
        ax41_1 = ax41.twiny() 
        ax41_2 = ax41.twiny() 
        ax41_3 = ax41.twiny()        
        ax41_4 = ax41.twiny() 

        ax42_1 = ax42.twiny() 
        ax42_2 = ax42.twiny() 
        ax42_3 = ax42.twiny()        
        ax42_4 = ax42.twiny() 
       
        ax50_1 = ax50.twiny() #water
        ax50_2 = ax50.twiny() 
        ax50_3 = ax50.twiny()        
        ax50_4 = ax50.twiny() 
               
        ax51_1 = ax51.twiny() #bbl
        ax51_2 = ax51.twiny() 
        ax51_3 = ax51.twiny()        
        ax51_4 = ax51.twiny()       

        ax52_1 = ax52.twiny() #bbl
        ax52_2 = ax52.twiny() 
        ax52_3 = ax52.twiny()        
        ax52_4 = ax52.twiny()
               
        def spines(axis):        
            for spinename, spine in axis.spines.iteritems():
                if spinename != 'top':
                    spine.set_visible(False)
            if axis in (ax00_1,ax02_1,ax10_1,ax12_1,ax20_1,ax22_1,ax30_1,ax32_1,ax40_1,ax42_1,ax50_1,ax52_1):
                axis.spines['top'].set_position(('outward', axis1))
                axis.spines['top'].set_color('g')                   
            elif axis in (ax00_2,ax02_2,ax10_2,ax12_2,ax20_2,ax22_2,ax30_2,ax32_2,ax40_2,ax42_2,ax50_2,ax52_2):    
                axis.spines['top'].set_position(('outward', axis2))
                axis.spines['top'].set_color('r')   
            elif axis in (ax00_3,ax02_3,ax10_3,ax12_3,ax20_3,ax22_3,ax30_3,ax32_3,ax40_3,ax42_3,ax50_3,ax52_3):    
                axis.spines['top'].set_position(('outward', axis3))
                axis.spines['top'].set_color('b') 
            elif axis in (ax10_4,ax12_4,ax30_4,ax32_4,ax40_4,ax42_4,ax50_4,ax52_4):    #ax20_4,
                axis.spines['top'].set_position(('outward', axis4))
                axis.spines['top'].set_color('m')     
            elif axis in (ax30_5, ax32_5) :    
                axis.spines['top'].set_position(('outward', axis5))
                axis.spines['top'].set_color('c')    
            elif axis in (ax00,ax01,ax02,ax01_1,ax01_2,ax01_3,ax10,#ax01_4,
                          ax11,ax11_1,ax11_2,ax11_3,ax11_4,ax12,ax20,
                          ax21,ax21_1,ax21_2,ax21_3,ax22,ax30,#ax21_4,
                          ax31,ax31_1,ax31_2,ax31_3,ax31_4,ax31_5,ax32,ax40,
                          ax41,ax41_1,ax41_2,ax41_3,ax41_4,ax42,ax50,ax51,
                          ax51_1,ax51_2,ax51_3,ax51_4,ax52):  
                plt.setp(axis.get_xticklabels(), visible=False)   
                 
        #call function to place spines                         
        spines(ax00)               
        spines(ax00_1) 
        spines(ax00_2)      
        spines(ax00_3)

        spines(ax01)         
        spines(ax01_1)
        spines(ax01_2)
        spines(ax01_3)
#        spines(ax01_4)

        spines(ax02)         
        spines(ax02_1)
        spines(ax02_2)
        spines(ax02_3)
#        spines(ax02_4)

        spines(ax10)                            
        spines(ax10_1) 
        spines(ax10_2)
        spines(ax10_3)      
        spines(ax10_4)        
   
        spines(ax11)                            
        spines(ax11_1) 
        spines(ax11_2)
        spines(ax11_3)      
        spines(ax11_4)        

        spines(ax12)                            
        spines(ax12_1) 
        spines(ax12_2)
        spines(ax12_3)      
        spines(ax12_4)
           
        spines(ax20)                
        spines(ax20_1) 
        spines(ax20_2)
        spines(ax20_3)      
#        spines(ax20_4)
        
        spines(ax21)                
        spines(ax21_1) 
        spines(ax21_2)
        spines(ax21_3)      
#        spines(ax21_4)
        spines(ax22)                
        spines(ax22_1) 
        spines(ax22_2)
        spines(ax22_3)
        
        spines(ax30)               
        spines(ax30_1) 
        spines(ax30_2)
        spines(ax30_3)      
        spines(ax30_4)                
        spines(ax30_5)

        spines(ax31)               
        spines(ax31_1) 
        spines(ax31_2)
        spines(ax31_3)      
        spines(ax31_4)                
        spines(ax31_5)

        spines(ax32)               
        spines(ax32_1) 
        spines(ax32_2)
        spines(ax32_3)      
        spines(ax32_4)                
        spines(ax32_5)
          
        spines(ax40)         
        spines(ax40_1) 
        spines(ax40_2)
        spines(ax40_3)      
        spines(ax40_4) 

        spines(ax41)         
        spines(ax41_1) 
        spines(ax41_2)
        spines(ax41_3)      
        spines(ax41_4) 

        spines(ax42)         
        spines(ax42_1) 
        spines(ax42_2)
        spines(ax42_3)      
        spines(ax42_4)
         
        spines(ax50)                      
        spines(ax50_1) 
        spines(ax50_2)
        spines(ax50_3)      
        spines(ax50_4)

        spines(ax51)                      
        spines(ax51_1) 
        spines(ax51_2)
        spines(ax51_3)      
        spines(ax51_4)
        
        spines(ax52)                      
        spines(ax52_1) 
        spines(ax52_2)
        spines(ax52_3)      
        spines(ax52_4)                            
        # discards the old graph
#        ax.hold(False)
#        ax1.hold(False)

        #call function to define limits for all axis        
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
                

     
        
        def minmax(axis): #define xlimits and ticks positions 
            if axis in ( ax00, ax00_1,  ax01_1):   
                axis.set_xlim([tempmin,tempmax])
                axis.set_xticks(np.arange(tempmin,tempmax+((tempmax - tempmin)/2.),
                                ((tempmax - tempmin)/2.))) 
            elif axis ==  ax02_1:  
                axis.set_xlim([sed_tempmin,sed_tempmax])
                axis.set_xticks(np.arange(sed_tempmin,sed_tempmax+
                                ((sed_tempmax -sed_tempmin)/2.),((sed_tempmax - sed_tempmin)/2.)))                  
                
#                mpl.rc('xtick', direction = 'out')
                #        mpl.rc('xtick.major',pad = 0 ) 
            elif axis in ( ax00_2, ax01_2):  
                axis.set_xlim([salmin,salmax])
                axis.set_xticks(np.arange(salmin,salmax+((salmax -salmin)/2.),((salmax -salmin)/2.))) 

            elif axis in ( ax02, ax02_2):  
                axis.set_xlim([sed_salmin,sed_salmax])
                axis.set_xticks(np.arange(sed_salmin,sed_salmax+((sed_salmax -sed_salmin)/2.),((sed_salmax -sed_salmin)/2.)))  
                axis.annotate(r'$\rm S $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize, color='r')                   
            elif axis in ( ax10, ax10_1,  ax11_1, ax11):  
                axis.set_xlim([o2min,o2max])
                axis.set_xticks(np.arange(o2min,o2max+((o2max - o2min)/2.),((o2max - o2min)/2.)))   
            elif axis in ( ax12, ax12_1):  
                axis.set_xlim([sed_o2min,sed_o2max])
                axis.set_xticks(np.arange(sed_o2min,sed_o2max+
                                ((sed_o2max - sed_o2min)/2.),((sed_o2max - sed_o2min)/2.)))  
                axis.annotate(r'$\rm O _2 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='g')                
            elif axis in ( ax10_2,  ax11_2):  
                axis.set_xlim([0,nh4max])
                axis.set_xticks(np.arange(0,nh4max+(nh4max /2.),(nh4max/2.)))   
            elif axis ==  ax12_2:   
                axis.set_xlim([0,sed_nh4max])
                axis.set_xticks(np.arange(0,sed_nh4max+(sed_nh4max /2.),(sed_nh4max/2.)))   
                axis.annotate(r'$\rm NH _4 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize, color='r')                          
            elif axis in ( ax10_3,  ax11_3):  
                axis.set_xlim([0,no2max])
                axis.set_xticks(np.arange(0,no2max+(no2max /2.),(no2max/2.))) 
            elif axis ==  ax12_3:
                axis.set_xlim([0,sed_no2max])
                axis.set_xticks(np.arange(0,sed_no2max+(sed_no2max /2.),(sed_no2max/2.))) 
                axis.annotate(r'$\rm NO _2 $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='b')                                  
            elif axis in ( ax10_4,  ax11_4):  
                axis.set_xlim([0,no3max])
                axis.set_xticks(np.arange(0,no3max+(no3max /2.),(no3max/2.)))  
            elif axis ==  ax12_4: 
                axis.set_xlim([0,sed_no3max])
                axis.set_xticks(np.arange(0,sed_no3max+(sed_no3max /2.),(sed_no3max/2.)))                             
            elif axis in ( ax20, ax20_1,  ax21_1, ax21):  
                axis.set_xlim([0,po4max])
                axis.set_xticks(np.arange(0,po4max+(po4max /2.),(po4max /2.)))   
            elif axis in ( ax22,  ax22_1):
                axis.set_xlim([0,sed_po4max])
                axis.set_xticks(np.arange(0,sed_po4max+(sed_po4max /2.),(sed_po4max /2.)))  
                axis.annotate(r'$\rm PO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='g')                  
            elif axis in ( ax20_2,  ax21_2):  
                axis.set_xlim([0,ponmax])
                axis.set_xticks(np.arange(0,ponmax+(ponmax /2.),(ponmax/2.))) 
            elif axis ==  ax22_2:  
                axis.set_xlim([0,sed_ponmax])
                axis.set_xticks(np.arange(0,sed_ponmax+(sed_ponmax /2.),(sed_ponmax/2.))) 
                axis.annotate(r'$\rm PON $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='r')                 
            elif axis in ( ax20_3,  ax21_3):  
                axis.set_xlim([0,donmax])
                axis.set_xticks(np.arange(0,donmax+(donmax /2.),(donmax/2.)))                
            elif axis ==  ax22_3:
                axis.set_xlim([0,sed_donmax])
                axis.set_xticks(np.arange(0,sed_donmax+(sed_donmax /2.),(sed_donmax/2.)))    
                axis.annotate(r'$\rm DON $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='b')                                                                                                                                                 
            elif axis in ( ax30, ax30_1,  ax31_1, ax31):  
                axis.set_xlim([0,mn2max])
                axis.set_xticks(np.arange(0,mn2max+(mn2max/2.),(mn2max/2.)))    
            elif axis in ( ax32,  ax32_1):  
                axis.set_xlim([0,sed_mn2max])
                axis.set_xticks(np.arange(0,sed_mn2max+(sed_mn2max/2.),(sed_mn2max/2.)))                              
            elif axis in ( ax30_2,  ax31_2):  
                axis.set_xlim([0,mn3max])
                axis.set_xticks(np.arange(0,mn3max+(mn3max /2.),(mn3max/2.))) 
            elif axis ==  ax32_2: 
                axis.set_xlim([0,sed_mn3max])
                axis.set_xticks(np.arange(0,sed_mn3max+(sed_mn3max /2.),(sed_mn3max/2.)))                                   
            elif axis in ( ax30_3,  ax31_3):  
                axis.set_xlim([0,mn4max])
                axis.set_xticks(np.arange(0,mn4max+(mn4max /2.),(mn4max/2.)))    
            elif axis ==  ax32_3: 
                axis.set_xlim([0,sed_mn4max])
                axis.set_xticks(np.arange(0,sed_mn4max+(sed_mn4max /2.),(sed_mn4max/2.)))                                
            elif axis in ( ax30_4,  ax31_4):  
                axis.set_xlim([0,mnsmax])
                axis.set_xticks(np.arange(0,mnsmax+(mnsmax /2.),(mnsmax/2.)))   
            elif axis ==  ax32_4:   
                axis.set_xlim([0,sed_mnsmax])
                axis.set_xticks(np.arange(0,sed_mnsmax+(sed_mnsmax /2.),(sed_mnsmax/2.)))                                   
            elif axis in ( ax30_5, ax31_5):  
                axis.set_xlim([0,mnco3max])
                axis.set_xticks(np.arange(0,mnco3max+(mnco3max /2.),(mnco3max/2.)))    
            elif axis == ax32_5: 
                axis.set_xlim([0,sed_mnco3max])
                axis.set_xticks(np.arange(0,sed_mnco3max+(sed_mnco3max /2.),(sed_mnco3max/2.)))                 
            elif axis in (ax40,ax40_1, ax41_1,ax41):  
                axis.set_xlim([0,fe2max])
                axis.set_xticks(np.arange(0,fe2max+(fe2max/2.),(fe2max/2.))) 
            elif axis in (ax42, ax42_1):     
                axis.set_xlim([0,sed_fe2max])
                axis.set_xticks(np.arange(0,sed_fe2max+(sed_fe2max/2.),(sed_fe2max/2.)))                                
            elif axis in (ax40_2, ax41_2):  
                axis.set_xlim([0,fe3max])
                axis.set_xticks(np.arange(0,fe3max+(fe3max /2.),(fe3max/2.))) 
            elif axis == ax42_2:   
                axis.set_xlim([0,sed_fe3max])
                axis.set_xticks(np.arange(0,sed_fe3max+(sed_fe3max /2.),(sed_fe3max/2.)))                                 
            elif axis in (ax40_3, ax41_3):  
                axis.set_xlim([0,fesmax])
                axis.set_xticks(np.arange(0,fesmax+(fesmax /2.),(fesmax/2.))) 
            elif axis == ax42_3: 
                axis.set_xlim([0,sed_fesmax])
                axis.set_xticks(np.arange(0,sed_fesmax+(sed_fesmax /2.),(sed_fesmax/2.)))                                    
            elif axis in (ax40_4, ax41_4):  
                axis.set_xlim([0,fes2max])
                axis.set_xticks(np.arange(0,fes2max+(fes2max /2.),(fes2max/2.)))  
            elif axis == ax42_4: 
                axis.set_xlim([0,sed_fes2max])
                axis.set_xticks(np.arange(0,sed_fes2max+(sed_fes2max /2.),(sed_fes2max/2.)))                 
            elif axis in (ax50,ax50_1, ax51_1,ax51):  
                axis.set_xlim([0,so4max])
                axis.set_xticks(np.arange(0,so4max+(so4max/2.),(so4max/2.)))  
            elif axis in (ax52, ax52_1):
                axis.set_xlim([0,sed_so4max])
                axis.set_xticks(np.arange(0,sed_so4max+(sed_so4max/2.),(sed_so4max/2.)))                                    
            elif axis in (ax50_2, ax51_2):  
                axis.set_xlim([0,s0max])
                axis.set_xticks(np.arange(0,s0max+(s0max /2.),(s0max/2.)))
            elif axis == ax52_2:
                axis.set_xlim([0,sed_s0max])
                axis.set_xticks(np.arange(0,sed_s0max+(sed_s0max /2.),(sed_s0max/2.)))                       
            elif axis in (ax50_3, ax51_3):  
                axis.set_xlim([0,h2smax])
                axis.set_xticks(np.arange(0,h2smax+(h2smax /2.),(h2smax/2.))) 
            elif axis == ax52_3:
                axis.set_xlim([0,sed_h2smax])
                axis.set_xticks(np.arange(0,sed_h2smax+(sed_h2smax /2.),(sed_h2smax/2.)))                        
            elif axis in (ax50_4, ax51_4):  
                axis.set_xlim([0,s2o3max])
                axis.set_xticks(np.arange(0,s2o3max+(s2o3max /2.),(s2o3max/2.)))
            elif axis == ax52_4:
                axis.set_xlim([0,sed_s2o3max])
                axis.set_xticks(np.arange(0,sed_s2o3max+(sed_s2o3max /2.),(sed_s2o3max/2.)))                


                     
        # plot data
        ax00_1.plot(temp[numday],depth,'g-') 
        ax01_1.plot(temp[numday],depth,'g-')  
        ax02_1.plot(temp[numday],depth_sed,'g-')                       
        ax00_2.plot(sal[numday],depth,'r-')   
        ax01_2.plot(sal[numday],depth,'r-')   
        ax02_2.plot(sal[numday],depth_sed,'r-')  
                    
        ax10_1.plot(o2[numday], depth, 'g-')
        ax11_1.plot(o2[numday], depth, 'g-')
        ax12_1.plot(o2[numday], depth_sed, 'g-')                 
        ax10_2.plot(nh4[numday], depth, 'r-')
        ax11_2.plot(nh4[numday], depth, 'r-') 
        ax12_2.plot(nh4[numday], depth_sed, 'r-')                
        ax10_3.plot(no2[numday], depth, 'b-')
        ax11_3.plot(no2[numday], depth, 'b-') 
        ax12_3.plot(no2[numday], depth_sed, 'b-')                 
        ax10_4.plot(no3[numday], depth, 'm-')        
        ax11_4.plot(no3[numday], depth, 'm-')  
        ax12_4.plot(no3[numday], depth_sed, 'm-') 
                       
        ax20_1.plot(po4[numday], depth, 'g-') 
        ax21_1.plot(po4[numday], depth, 'g-') 
        ax22_1.plot(po4[numday], depth, 'g-')                
        ax20_2.plot(pon[numday], depth_sed, 'r-')
        ax21_2.plot(pon[numday], depth, 'r-')
        ax22_2.plot(pon[numday], depth_sed, 'r-')                
        ax20_3.plot(don[numday], depth, 'b-') 
        ax21_3.plot(don[numday], depth, 'b-')  
        ax22_3.plot(don[numday], depth_sed, 'b-')                
               
        ax30_1.plot(mn2[numday], depth, 'g-') 
        ax31_1.plot(mn2[numday], depth, 'g-') 
        ax32_1.plot(mn2[numday], depth_sed, 'g-')               
        ax30_2.plot(mn3[numday], depth, 'r-')
        ax31_2.plot(mn3[numday], depth, 'r-') 
        ax32_2.plot(mn3[numday], depth_sed, 'r-')                
        ax30_3.plot(mn4[numday], depth, 'b-') 
        ax31_3.plot(mn4[numday], depth, 'b-') 
        ax32_3.plot(mn4[numday], depth_sed, 'b-')                
        ax30_4.plot(mns[numday], depth, 'm-')  
        ax31_4.plot(mns[numday], depth, 'm-') 
        ax32_4.plot(mns[numday], depth_sed, 'm-')                     
        ax30_5.plot(mnco3[numday], depth, 'c-')   
        ax31_5.plot(mnco3[numday], depth, 'c-')  
        ax32_5.plot(mnco3[numday], depth_sed, 'c-')                       

        ax40_1.plot(fe2[numday], depth, 'g-') 
        ax41_1.plot(fe2[numday], depth, 'g-')  
        ax42_1.plot(fe2[numday], depth_sed, 'g-')               
        ax40_2.plot(fe3[numday], depth, 'r-')
        ax41_2.plot(fe3[numday], depth, 'r-') 
        ax42_2.plot(fe3[numday], depth_sed, 'r-')                
        ax40_3.plot(fes[numday], depth, 'b-') 
        ax41_3.plot(fes[numday], depth, 'b-')  
        ax42_3.plot(fes[numday], depth_sed, 'b-')              
        ax40_4.plot(fes2[numday], depth, 'm-')  
        ax41_4.plot(fes2[numday], depth, 'm-')
        ax42_4.plot(fes2[numday], depth_sed, 'm-')
        ax50_1.plot(so4[numday], depth, 'g-') 
        ax51_1.plot(so4[numday], depth, 'g-') 
        ax52_1.plot(so4[numday], depth_sed, 'g-')                
        ax50_2.plot(s0[numday], depth, 'r-')
        ax51_2.plot(s0[numday], depth, 'r-') 
        ax52_2.plot(s0[numday], depth_sed, 'r-')                
        ax50_3.plot(h2s[numday], depth, 'b-') 
        ax51_3.plot(h2s[numday], depth, 'b-')  
        ax52_3.plot(h2s[numday], depth_sed, 'b-')              
        ax50_4.plot(s2o3[numday], depth, 'm-')  
        ax51_4.plot(s2o3[numday], depth, 'm-')
        ax52_4.plot(s2o3[numday], depth_sed, 'm-')

        minmax(ax00)        
        minmax(ax00_1)                
        minmax(ax00_2) 
        minmax(ax01_1)        
        minmax(ax01_2)        
        minmax(ax01_3) 
        minmax(ax02)       
        minmax(ax02_1)        
        minmax(ax02_2)                        
        minmax(ax10)
        minmax(ax10_1) 
        minmax(ax10_2)    
        minmax(ax10_3)  
        minmax(ax10_4)
        minmax(ax11)                                                           
        minmax(ax11_1)        
        minmax(ax11_2)        
        minmax(ax11_3)        
        minmax(ax11_4)       
        minmax(ax12)                                                           
        minmax(ax12_1)        
        minmax(ax12_2)        
        minmax(ax12_3)        
        minmax(ax12_4)  
              
        minmax(ax20)
        minmax(ax20_1) 
        minmax(ax20_2)    
        minmax(ax20_3) 
        minmax(ax21)                                                          
        minmax(ax21_1)        
        minmax(ax21_2)        
        minmax(ax21_3)
        minmax(ax22)                                                          
        minmax(ax22_1)        
        minmax(ax22_2)        
        minmax(ax22_3)                
        minmax(ax30)
        minmax(ax30_1) 
        minmax(ax30_2)    
        minmax(ax30_3)
        minmax(ax30_4)
        minmax(ax30_5)
        minmax(ax31)                                                                           
        minmax(ax31_1)        
        minmax(ax31_2)        
        minmax(ax31_3)      
        minmax(ax31_4)        
        minmax(ax31_5) 
        minmax(ax32)                                                                           
        minmax(ax32_1)        
        minmax(ax32_2)        
        minmax(ax32_3)      
        minmax(ax32_4)        
        minmax(ax32_5)  
        
        minmax(ax40)
        minmax(ax40_1) 
        minmax(ax40_2)    
        minmax(ax40_3)  
        minmax(ax40_4)
        minmax(ax41)                                                           
        minmax(ax41_1)        
        minmax(ax41_2)        
        minmax(ax41_3)        
        minmax(ax41_4)        
        minmax(ax42)                                                           
        minmax(ax42_1)        
        minmax(ax42_2)        
        minmax(ax42_3)        
        minmax(ax42_4) 
        
        minmax(ax50)
        minmax(ax50_1) 
        minmax(ax50_2)    
        minmax(ax50_3)  
        minmax(ax50_4)
        minmax(ax51)                                                           
        minmax(ax51_1)        
        minmax(ax51_2)        
        minmax(ax51_3)        
        minmax(ax51_4) 
        minmax(ax52)                                                           
        minmax(ax52_1)        
        minmax(ax52_2)        
        minmax(ax52_3)        
        minmax(ax52_4) 
            
#        QDesktopWidget * QApplication::desktop ()        
#        figManager = plt.get_current_fig_manager()
#        figManager.window.showMaximized()
                                      
        # refresh canvas
        self.canvas.draw()


    def plot2(self): #main function to define figure
        ''' plot some random stuff '''
        plt.clf() #clear figure before updating 

        numday = self.numdaySpinBox.value() #take the input value of numday
        style.use('ggplot')    #use predefined style        
        wspace=0.40 #define values for grid
        hspace = 0.05
        gs = gridspec.GridSpec(2, 6) 
        gs.update(left=0.06, right=0.93,top = 0.84,bottom = 0.4, wspace=wspace,hspace=hspace)
        gs1 = gridspec.GridSpec(1, 6)
        gs1.update(left=0.06, right=0.93, top = 0.26, bottom = 0.02, wspace=wspace,hspace=hspace)     
           
                #create subplots
        ax00 = self.figure.add_subplot(gs[0]) # water
        ax10 = self.figure.add_subplot(gs[1])
        ax20 = self.figure.add_subplot(gs[2])
        ax30 = self.figure.add_subplot(gs[3])        
        ax40 = self.figure.add_subplot(gs[4])
        ax50 = self.figure.add_subplot(gs[5]) 
        
        ax01 = self.figure.add_subplot(gs[6]) #BBL
        ax11 = self.figure.add_subplot(gs[7])
        ax21 = self.figure.add_subplot(gs[8])
        ax31 = self.figure.add_subplot(gs[9])        
        ax41 = self.figure.add_subplot(gs[10])
        ax51 = self.figure.add_subplot(gs[11])  

        ax02 = self.figure.add_subplot(gs1[0]) #sediment
        ax12 = self.figure.add_subplot(gs1[1])
        ax22 = self.figure.add_subplot(gs1[2])
        ax32 = self.figure.add_subplot(gs1[3])        
        ax42 = self.figure.add_subplot(gs1[4])
        ax52 = self.figure.add_subplot(gs1[5])
        
        plt.text(1.1, 0.5,'Water ', fontweight='bold', #Write number of day to Figure
        bbox={'facecolor': wat_color, 'alpha':0.5, 'pad':10}, fontsize=14, rotation=90, 
        transform=ax50.transAxes) 
        
        plt.text(1.1, 0.7,'BBL ', fontweight='bold', # draw legend to BBL
        bbox={'facecolor': bbl_color, 'alpha':0.5, 'pad':10}, fontsize=14, rotation=90,
        transform=ax51.transAxes)
        plt.text(1.1, 0.3,'Sediment ', fontweight='bold', #draw legend to Sediment
        bbox={'facecolor': sed_color , 'alpha':0.6, 'pad':10}, fontsize=14, rotation=90,
        transform=ax52.transAxes)        
        
            
        def y_lim(axis): #function to define y limits 
#            y_formatter = 
            majorLocator = MultipleLocator(2.)
            majorFormatter = ScalarFormatter(useOffset=False)   #format y scales to be scalar 
            minorLocator = MultipleLocator(1.)

            if axis in (ax00,ax10,ax20,ax30,ax40,ax50): #water
                axis.set_ylim([y2min, 0])
                axis.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat)
            elif axis in (ax01,ax11,ax21,ax31,ax41,ax51): #BBL
                axis.set_ylim([y2max, y2min])
                axis.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
                axis.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)

            elif axis in (ax02,ax12,ax22,ax32,ax42,ax52): #sediment 
                axis.set_ylim([y3max, y3min])      
                axis.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)  
                axis.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)    
                axis.yaxis.set_major_locator(majorLocator)
                axis.yaxis.set_major_formatter(majorFormatter)
                axis.yaxis.set_minor_locator(minorLocator)
                axis.yaxis.grid(True,'minor')
                axis.yaxis.grid(True,'major')
                plt.setp(axis.get_xticklabels(), visible=False) 
                 
                 
                 
                                              
        ax00.set_ylabel('Depth (m)')
        ax01.set_ylabel('Depth (m)')   
        ax02.set_ylabel('Depth (cm)')                


        
 
        #Create axes sharing y              
        ax00_1 = ax00.twiny()  #water
        ax00_2 = ax00.twiny()  
        ax00_3 = ax00.twiny()
        
        ax01_1 = ax01.twiny() #bbl
        ax01_2 = ax01.twiny()
        ax01_3 = ax01.twiny()


        ax02_1 = ax02.twiny() #sediment
        ax02_2 = ax02.twiny()
        ax02_3 = ax02.twiny()
#        ax02_4 = ax02.twiny()
                 
        ax10_1 = ax10.twiny() #water
        ax10_2 = ax10.twiny() 
        ax10_3 = ax10.twiny()        
        ax10_4 = ax10.twiny()
#        ax10_5 = ax10.twiny()
        
        ax11_1 = ax11.twiny() #bbl
        ax11_2 = ax11.twiny()
        ax11_3 = ax11.twiny()
        ax11_4 = ax11.twiny()  

        ax12_1 = ax12.twiny() #sediment
        ax12_2 = ax12.twiny()
        ax12_3 = ax12.twiny()
        ax12_4 = ax12.twiny() 
                 
        ax20_1 = ax20.twiny() 
        ax20_2 = ax20.twiny() 
        ax20_3 = ax20.twiny()        
#        ax20_4 = ax20.twiny() 
        
        ax21_1 = ax21.twiny() 
        ax21_2 = ax21.twiny() 
        ax21_3 = ax21.twiny()        
#        ax21_4 = ax21.twiny() 

        ax22_1 = ax22.twiny() 
        ax22_2 = ax22.twiny() 
        ax22_3 = ax22.twiny() 
                       
        ax30_1 = ax30.twiny() 
        ax30_2 = ax30.twiny() 
        ax30_3 = ax30.twiny()        
        ax30_4 = ax30.twiny()            
        ax30_5 = ax30.twiny()
        
        ax31_1 = ax31.twiny() 
        ax31_2 = ax31.twiny() 
        ax31_3 = ax31.twiny()        
        ax31_4 = ax31.twiny()            
        ax31_5 = ax31.twiny()        
 
        ax32_1 = ax32.twiny() 
        ax32_2 = ax32.twiny() 
        ax32_3 = ax32.twiny()        
        ax32_4 = ax32.twiny()            
        ax32_5 = ax32.twiny()  
       
        ax40_1 = ax40.twiny() 
        ax40_2 = ax40.twiny() 
        ax40_3 = ax40.twiny()        
        ax40_4 = ax40.twiny()            
 
        ax41_1 = ax41.twiny() 
        ax41_2 = ax41.twiny() 
        ax41_3 = ax41.twiny()        
        ax41_4 = ax41.twiny() 

        ax42_1 = ax42.twiny() 
        ax42_2 = ax42.twiny() 
        ax42_3 = ax42.twiny()        
        ax42_4 = ax42.twiny() 
       
        ax50_1 = ax50.twiny() #water
        ax50_2 = ax50.twiny() 
        ax50_3 = ax50.twiny()        
        ax50_4 = ax50.twiny() 
               
        ax51_1 = ax51.twiny() #bbl
        ax51_2 = ax51.twiny() 
        ax51_3 = ax51.twiny()        
        ax51_4 = ax51.twiny()       

        ax52_1 = ax52.twiny() #bbl
        ax52_2 = ax52.twiny() 
        ax52_3 = ax52.twiny()        
        ax52_4 = ax52.twiny()
               
        def spines(axis):        
            for spinename, spine in axis.spines.iteritems():
                if spinename != 'top':
                    spine.set_visible(False)
            if axis in (ax00_1,ax02_1,ax10_1,ax12_1,ax20_1,ax22_1,ax30_1,ax32_1,ax40_1,ax42_1,ax50_1,ax52_1):
                axis.spines['top'].set_position(('outward', axis1))
                axis.spines['top'].set_color('g')                   
            elif axis in (ax00_2,ax02_2,ax10_2,ax12_2,ax20_2,ax22_2,ax30_2,ax32_2,ax40_2,ax42_2,ax50_2,ax52_2):    
                axis.spines['top'].set_position(('outward', axis2))
                axis.spines['top'].set_color('r')   
            elif axis in (ax00_3,ax02_3,ax10_3,ax12_3,ax20_3,ax22_3,ax30_3,ax32_3,ax40_3,ax42_3,ax50_3,ax52_3):    
                axis.spines['top'].set_position(('outward', axis3))
                axis.spines['top'].set_color('b') 
            elif axis in (ax10_4,ax12_4,ax30_4,ax32_4,ax40_4,ax42_4,ax50_4,ax52_4):    #ax20_4,
                axis.spines['top'].set_position(('outward', axis4))
                axis.spines['top'].set_color('m')     
            elif axis in (ax30_5, ax32_5) :    
                axis.spines['top'].set_position(('outward', axis5))
                axis.spines['top'].set_color('c')    
            elif axis in (ax00,ax01,ax02,ax01_1,ax01_2,ax01_3,ax10,#ax01_4,
                          ax11,ax11_1,ax11_2,ax11_3,ax11_4,ax12,ax20,
                          ax21,ax21_1,ax21_2,ax21_3,ax22,ax30,#ax21_4,
                          ax31,ax31_1,ax31_2,ax31_3,ax31_4,ax31_5,ax32,ax40,
                          ax41,ax41_1,ax41_2,ax41_3,ax41_4,ax42,ax50,ax51,
                          ax51_1,ax51_2,ax51_3,ax51_4,ax52):  
                plt.setp(axis.get_xticklabels(), visible=False)   
                 
        #call function to place spines                         
        spines(ax00)               
        spines(ax00_1) 
        spines(ax00_2)      
        spines(ax00_3)
        spines(ax01)         
        spines(ax01_1)
        spines(ax01_2)
        spines(ax01_3)
#        spines(ax01_4)
        spines(ax02)         
        spines(ax02_1)
        spines(ax02_2)
        spines(ax02_3)
#        spines(ax02_4)
        spines(ax10)                            
        spines(ax10_1) 
        spines(ax10_2)
        spines(ax10_3)      
        spines(ax10_4)           
        spines(ax11)                            
        spines(ax11_1) 
        spines(ax11_2)
        spines(ax11_3)      
        spines(ax11_4)        
        spines(ax12)                            
        spines(ax12_1) 
        spines(ax12_2)
        spines(ax12_3)      
        spines(ax12_4)         
        spines(ax20)                
        spines(ax20_1) 
        spines(ax20_2)
        spines(ax20_3)      
#        spines(ax20_4)        
        spines(ax21)                
        spines(ax21_1) 
        spines(ax21_2)
        spines(ax21_3)      
#        spines(ax21_4)
        spines(ax22)                
        spines(ax22_1) 
        spines(ax22_2)
        spines(ax22_3)        
        spines(ax30)               
        spines(ax30_1) 
        spines(ax30_2)
        spines(ax30_3)      
        spines(ax30_4)                
        spines(ax30_5)
        spines(ax31)               
        spines(ax31_1) 
        spines(ax31_2)
        spines(ax31_3)      
        spines(ax31_4)                
        spines(ax31_5)
        spines(ax32)               
        spines(ax32_1) 
        spines(ax32_2)
        spines(ax32_3)      
        spines(ax32_4)                
        spines(ax32_5)         
        spines(ax40)         
        spines(ax40_1) 
        spines(ax40_2)
        spines(ax40_3)      
        spines(ax40_4) 
        spines(ax41)         
        spines(ax41_1) 
        spines(ax41_2)
        spines(ax41_3)      
        spines(ax41_4) 
        spines(ax42)         
        spines(ax42_1) 
        spines(ax42_2)
        spines(ax42_3)      
        spines(ax42_4)         
        spines(ax50)                      
        spines(ax50_1) 
        spines(ax50_2)
        spines(ax50_3)      
        spines(ax50_4)
        spines(ax51)                      
        spines(ax51_1) 
        spines(ax51_2)
        spines(ax51_3)      
        spines(ax51_4)
        spines(ax52)                      
        spines(ax52_1) 
        spines(ax52_2)
        spines(ax52_3)      
        spines(ax52_4)                            
        # discards the old graph
#        ax.hold(False)
#        ax1.hold(False)

        #call function to define limits for all axis        
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
                

     
        
        def minmax(axis): #define xlimits and ticks positions 
            if axis in ( ax00, ax00_1,  ax01_1):   
                axis.set_xlim([tempmin,tempmax])
                axis.set_xticks(np.arange(tempmin,tempmax+((tempmax - tempmin)/2.),
                                ((tempmax - tempmin)/2.))) 
            elif axis ==  ax02_1:  
                axis.set_xlim([sed_tempmin,sed_tempmax])
                axis.set_xticks(np.arange(sed_tempmin,sed_tempmax+
                                ((sed_tempmax -sed_tempmin)/2.),((sed_tempmax - sed_tempmin)/2.)))                  
                
#                mpl.rc('xtick', direction = 'out')
                #        mpl.rc('xtick.major',pad = 0 ) 
            elif axis in ( ax00_2, ax01_2):  
                axis.set_xlim([salmin,salmax])
                axis.set_xticks(np.arange(salmin,salmax+((salmax -salmin)/2.),((salmax -salmin)/2.))) 

            elif axis in ( ax02, ax02_2):  
                axis.set_xlim([sed_salmin,sed_salmax])
                axis.set_xticks(np.arange(sed_salmin,sed_salmax+((sed_salmax -sed_salmin)/2.),((sed_salmax -sed_salmin)/2.)))  
                axis.annotate(r'$\rm S $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize, color='r')                   
            elif axis in ( ax10, ax10_1,  ax11_1, ax11):  
                axis.set_xlim([o2min,o2max])
                axis.set_xticks(np.arange(o2min,o2max+((o2max - o2min)/2.),((o2max - o2min)/2.)))   
            elif axis in ( ax12, ax12_1):  
                axis.set_xlim([sed_o2min,sed_o2max])
                axis.set_xticks(np.arange(sed_o2min,sed_o2max+
                                ((sed_o2max - sed_o2min)/2.),((sed_o2max - sed_o2min)/2.)))  
                axis.annotate(r'$\rm O _2 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='g')                
            elif axis in ( ax10_2,  ax11_2):  
                axis.set_xlim([0,nh4max])
                axis.set_xticks(np.arange(0,nh4max+(nh4max /2.),(nh4max/2.)))   
            elif axis ==  ax12_2:   
                axis.set_xlim([0,sed_nh4max])
                axis.set_xticks(np.arange(0,sed_nh4max+(sed_nh4max /2.),(sed_nh4max/2.)))   
                axis.annotate(r'$\rm NH _4 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize, color='r')                          
            elif axis in ( ax10_3,  ax11_3):  
                axis.set_xlim([0,no2max])
                axis.set_xticks(np.arange(0,no2max+(no2max /2.),(no2max/2.))) 
            elif axis ==  ax12_3:
                axis.set_xlim([0,sed_no2max])
                axis.set_xticks(np.arange(0,sed_no2max+(sed_no2max /2.),(sed_no2max/2.))) 
                axis.annotate(r'$\rm NO _2 $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='b')                                  
            elif axis in ( ax10_4,  ax11_4):  
                axis.set_xlim([0,no3max])
                axis.set_xticks(np.arange(0,no3max+(no3max /2.),(no3max/2.)))  
            elif axis ==  ax12_4: 
                axis.set_xlim([0,sed_no3max])
                axis.set_xticks(np.arange(0,sed_no3max+(sed_no3max /2.),(sed_no3max/2.)))                             
            elif axis in ( ax20, ax20_1,  ax21_1, ax21):  
                axis.set_xlim([0,po4max])
                axis.set_xticks(np.arange(0,po4max+(po4max /2.),(po4max /2.)))   
            elif axis in ( ax22,  ax22_1):
                axis.set_xlim([0,sed_po4max])
                axis.set_xticks(np.arange(0,sed_po4max+(sed_po4max /2.),(sed_po4max /2.)))  
                axis.annotate(r'$\rm PO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='g')                  
            elif axis in ( ax20_2,  ax21_2):  
                axis.set_xlim([0,ponmax])
                axis.set_xticks(np.arange(0,ponmax+(ponmax /2.),(ponmax/2.))) 
            elif axis ==  ax22_2:  
                axis.set_xlim([0,sed_ponmax])
                axis.set_xticks(np.arange(0,sed_ponmax+(sed_ponmax /2.),(sed_ponmax/2.))) 
                axis.annotate(r'$\rm PON $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='r')                 
            elif axis in ( ax20_3,  ax21_3):  
                axis.set_xlim([0,donmax])
                axis.set_xticks(np.arange(0,donmax+(donmax /2.),(donmax/2.)))                
            elif axis ==  ax22_3:
                axis.set_xlim([0,sed_donmax])
                axis.set_xticks(np.arange(0,sed_donmax+(sed_donmax /2.),(sed_donmax/2.)))    
                axis.annotate(r'$\rm DON $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
                xycoords='axes fraction',  fontsize = xlabel_fontsize,color='b')                                                                                                                                                 
            elif axis in ( ax30, ax30_1,  ax31_1, ax31):  
                axis.set_xlim([0,mn2max])
                axis.set_xticks(np.arange(0,mn2max+(mn2max/2.),(mn2max/2.)))    
            elif axis in ( ax32,  ax32_1):  
                axis.set_xlim([0,sed_mn2max])
                axis.set_xticks(np.arange(0,sed_mn2max+(sed_mn2max/2.),(sed_mn2max/2.)))                              
            elif axis in ( ax30_2,  ax31_2):  
                axis.set_xlim([0,mn3max])
                axis.set_xticks(np.arange(0,mn3max+(mn3max /2.),(mn3max/2.))) 
            elif axis ==  ax32_2: 
                axis.set_xlim([0,sed_mn3max])
                axis.set_xticks(np.arange(0,sed_mn3max+(sed_mn3max /2.),(sed_mn3max/2.)))                                   
            elif axis in ( ax30_3,  ax31_3):  
                axis.set_xlim([0,mn4max])
                axis.set_xticks(np.arange(0,mn4max+(mn4max /2.),(mn4max/2.)))    
            elif axis ==  ax32_3: 
                axis.set_xlim([0,sed_mn4max])
                axis.set_xticks(np.arange(0,sed_mn4max+(sed_mn4max /2.),(sed_mn4max/2.)))                                
            elif axis in ( ax30_4,  ax31_4):  
                axis.set_xlim([0,mnsmax])
                axis.set_xticks(np.arange(0,mnsmax+(mnsmax /2.),(mnsmax/2.)))   
            elif axis ==  ax32_4:   
                axis.set_xlim([0,sed_mnsmax])
                axis.set_xticks(np.arange(0,sed_mnsmax+(sed_mnsmax /2.),(sed_mnsmax/2.)))                                   
            elif axis in ( ax30_5, ax31_5):  
                axis.set_xlim([0,mnco3max])
                axis.set_xticks(np.arange(0,mnco3max+(mnco3max /2.),(mnco3max/2.)))    
            elif axis == ax32_5: 
                axis.set_xlim([0,sed_mnco3max])
                axis.set_xticks(np.arange(0,sed_mnco3max+(sed_mnco3max /2.),(sed_mnco3max/2.)))                 
            elif axis in (ax40,ax40_1, ax41_1,ax41):  
                axis.set_xlim([0,fe2max])
                axis.set_xticks(np.arange(0,fe2max+(fe2max/2.),(fe2max/2.))) 
            elif axis in (ax42, ax42_1):     
                axis.set_xlim([0,sed_fe2max])
                axis.set_xticks(np.arange(0,sed_fe2max+(sed_fe2max/2.),(sed_fe2max/2.)))                                
            elif axis in (ax40_2, ax41_2):  
                axis.set_xlim([0,fe3max])
                axis.set_xticks(np.arange(0,fe3max+(fe3max /2.),(fe3max/2.))) 
            elif axis == ax42_2:   
                axis.set_xlim([0,sed_fe3max])
                axis.set_xticks(np.arange(0,sed_fe3max+(sed_fe3max /2.),(sed_fe3max/2.)))                                 
            elif axis in (ax40_3, ax41_3):  
                axis.set_xlim([0,fesmax])
                axis.set_xticks(np.arange(0,fesmax+(fesmax /2.),(fesmax/2.))) 
            elif axis == ax42_3: 
                axis.set_xlim([0,sed_fesmax])
                axis.set_xticks(np.arange(0,sed_fesmax+(sed_fesmax /2.),(sed_fesmax/2.)))                                    
            elif axis in (ax40_4, ax41_4):  
                axis.set_xlim([0,fes2max])
                axis.set_xticks(np.arange(0,fes2max+(fes2max /2.),(fes2max/2.)))  
            elif axis == ax42_4: 
                axis.set_xlim([0,sed_fes2max])
                axis.set_xticks(np.arange(0,sed_fes2max+(sed_fes2max /2.),(sed_fes2max/2.)))                 
            elif axis in (ax50,ax50_1, ax51_1,ax51):  
                axis.set_xlim([0,so4max])
                axis.set_xticks(np.arange(0,so4max+(so4max/2.),(so4max/2.)))  
            elif axis in (ax52, ax52_1):
                axis.set_xlim([0,sed_so4max])
                axis.set_xticks(np.arange(0,sed_so4max+(sed_so4max/2.),(sed_so4max/2.)))                                    
            elif axis in (ax50_2, ax51_2):  
                axis.set_xlim([0,s0max])
                axis.set_xticks(np.arange(0,s0max+(s0max /2.),(s0max/2.)))
            elif axis == ax52_2:
                axis.set_xlim([0,sed_s0max])
                axis.set_xticks(np.arange(0,sed_s0max+(sed_s0max /2.),(sed_s0max/2.)))                       
            elif axis in (ax50_3, ax51_3):  
                axis.set_xlim([0,h2smax])
                axis.set_xticks(np.arange(0,h2smax+(h2smax /2.),(h2smax/2.))) 
            elif axis == ax52_3:
                axis.set_xlim([0,sed_h2smax])
                axis.set_xticks(np.arange(0,sed_h2smax+(sed_h2smax /2.),(sed_h2smax/2.)))                        
            elif axis in (ax50_4, ax51_4):  
                axis.set_xlim([0,s2o3max])
                axis.set_xticks(np.arange(0,s2o3max+(s2o3max /2.),(s2o3max/2.)))
            elif axis == ax52_4:
                axis.set_xlim([0,sed_s2o3max])
                axis.set_xticks(np.arange(0,sed_s2o3max+(sed_s2o3max /2.),(sed_s2o3max/2.)))                


                     
        # plot data
        ax00_1.plot(temp[numday],depth,'g-') 
        ax01_1.plot(temp[numday],depth,'g-')  
        ax02_1.plot(temp[numday],depth_sed,'g-')                       
        ax00_2.plot(sal[numday],depth,'r-')   
        ax01_2.plot(sal[numday],depth,'r-')   
        ax02_2.plot(sal[numday],depth_sed,'r-')  
                    
        ax10_1.plot(o2[numday], depth, 'g-')
        ax11_1.plot(o2[numday], depth, 'g-')
        ax12_1.plot(o2[numday], depth_sed, 'g-')                 
        ax10_2.plot(nh4[numday], depth, 'r-')
        ax11_2.plot(nh4[numday], depth, 'r-') 
        ax12_2.plot(nh4[numday], depth_sed, 'r-')                
        ax10_3.plot(no2[numday], depth, 'b-')
        ax11_3.plot(no2[numday], depth, 'b-') 
        ax12_3.plot(no2[numday], depth_sed, 'b-')                 
        ax10_4.plot(no3[numday], depth, 'm-')        
        ax11_4.plot(no3[numday], depth, 'm-')  
        ax12_4.plot(no3[numday], depth_sed, 'm-') 
                       
        ax20_1.plot(po4[numday], depth, 'g-') 
        ax21_1.plot(po4[numday], depth, 'g-') 
        ax22_1.plot(po4[numday], depth, 'g-')                
        ax20_2.plot(pon[numday], depth_sed, 'r-')
        ax21_2.plot(pon[numday], depth, 'r-')
        ax22_2.plot(pon[numday], depth_sed, 'r-')                
        ax20_3.plot(don[numday], depth, 'b-') 
        ax21_3.plot(don[numday], depth, 'b-')  
        ax22_3.plot(don[numday], depth_sed, 'b-')                
               
        ax30_1.plot(mn2[numday], depth, 'g-') 
        ax31_1.plot(mn2[numday], depth, 'g-') 
        ax32_1.plot(mn2[numday], depth_sed, 'g-')               
        ax30_2.plot(mn3[numday], depth, 'r-')
        ax31_2.plot(mn3[numday], depth, 'r-') 
        ax32_2.plot(mn3[numday], depth_sed, 'r-')                
        ax30_3.plot(mn4[numday], depth, 'b-') 
        ax31_3.plot(mn4[numday], depth, 'b-') 
        ax32_3.plot(mn4[numday], depth_sed, 'b-')                
        ax30_4.plot(mns[numday], depth, 'm-')  
        ax31_4.plot(mns[numday], depth, 'm-') 
        ax32_4.plot(mns[numday], depth_sed, 'm-')                     
        ax30_5.plot(mnco3[numday], depth, 'c-')   
        ax31_5.plot(mnco3[numday], depth, 'c-')  
        ax32_5.plot(mnco3[numday], depth_sed, 'c-')                       

        ax40_1.plot(fe2[numday], depth, 'g-') 
        ax41_1.plot(fe2[numday], depth, 'g-')  
        ax42_1.plot(fe2[numday], depth_sed, 'g-')               
        ax40_2.plot(fe3[numday], depth, 'r-')
        ax41_2.plot(fe3[numday], depth, 'r-') 
        ax42_2.plot(fe3[numday], depth_sed, 'r-')                
        ax40_3.plot(fes[numday], depth, 'b-') 
        ax41_3.plot(fes[numday], depth, 'b-')  
        ax42_3.plot(fes[numday], depth_sed, 'b-')              
        ax40_4.plot(fes2[numday], depth, 'm-')  
        ax41_4.plot(fes2[numday], depth, 'm-')
        ax42_4.plot(fes2[numday], depth_sed, 'm-')
        ax50_1.plot(so4[numday], depth, 'g-') 
        ax51_1.plot(so4[numday], depth, 'g-') 
        ax52_1.plot(so4[numday], depth_sed, 'g-')                
        ax50_2.plot(s0[numday], depth, 'r-')
        ax51_2.plot(s0[numday], depth, 'r-') 
        ax52_2.plot(s0[numday], depth_sed, 'r-')                
        ax50_3.plot(h2s[numday], depth, 'b-') 
        ax51_3.plot(h2s[numday], depth, 'b-')  
        ax52_3.plot(h2s[numday], depth_sed, 'b-')              
        ax50_4.plot(s2o3[numday], depth, 'm-')  
        ax51_4.plot(s2o3[numday], depth, 'm-')
        ax52_4.plot(s2o3[numday], depth_sed, 'm-')

        minmax(ax00)        
        minmax(ax00_1)                
        minmax(ax00_2) 
        minmax(ax01_1)        
        minmax(ax01_2)        
        minmax(ax01_3) 
        minmax(ax02)       
        minmax(ax02_1)        
        minmax(ax02_2)                        
        minmax(ax10)
        minmax(ax10_1) 
        minmax(ax10_2)    
        minmax(ax10_3)  
        minmax(ax10_4)
        minmax(ax11)                                                           
        minmax(ax11_1)        
        minmax(ax11_2)        
        minmax(ax11_3)        
        minmax(ax11_4)       
        minmax(ax12)                                                           
        minmax(ax12_1)        
        minmax(ax12_2)        
        minmax(ax12_3)        
        minmax(ax12_4)  
              
        minmax(ax20)
        minmax(ax20_1) 
        minmax(ax20_2)    
        minmax(ax20_3) 
        minmax(ax21)                                                          
        minmax(ax21_1)        
        minmax(ax21_2)        
        minmax(ax21_3)
        minmax(ax22)                                                          
        minmax(ax22_1)        
        minmax(ax22_2)        
        minmax(ax22_3)                
        minmax(ax30)
        minmax(ax30_1) 
        minmax(ax30_2)    
        minmax(ax30_3)
        minmax(ax30_4)
        minmax(ax30_5)
        minmax(ax31)                                                                           
        minmax(ax31_1)        
        minmax(ax31_2)        
        minmax(ax31_3)      
        minmax(ax31_4)        
        minmax(ax31_5) 
        minmax(ax32)                                                                           
        minmax(ax32_1)        
        minmax(ax32_2)        
        minmax(ax32_3)      
        minmax(ax32_4)        
        minmax(ax32_5)  
        
        minmax(ax40)
        minmax(ax40_1) 
        minmax(ax40_2)    
        minmax(ax40_3)  
        minmax(ax40_4)
        minmax(ax41)                                                           
        minmax(ax41_1)        
        minmax(ax41_2)        
        minmax(ax41_3)        
        minmax(ax41_4)        
        minmax(ax42)                                                           
        minmax(ax42_1)        
        minmax(ax42_2)        
        minmax(ax42_3)        
        minmax(ax42_4) 
        
        minmax(ax50)
        minmax(ax50_1) 
        minmax(ax50_2)    
        minmax(ax50_3)  
        minmax(ax50_4)
        minmax(ax51)                                                           
        minmax(ax51_1)        
        minmax(ax51_2)        
        minmax(ax51_3)        
        minmax(ax51_4) 
        minmax(ax52)                                                           
        minmax(ax52_1)        
        minmax(ax52_2)        
        minmax(ax52_3)        
        minmax(ax52_4) 
            
#        QDesktopWidget * QApplication::desktop ()        
#        figManager = plt.get_current_fig_manager()
#        figManager.window.showMaximized()
                                      
        # refresh canvas
        self.canvas.draw()





































if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    
    main = Window()
    main.show()

    sys.exit(app.exec_())