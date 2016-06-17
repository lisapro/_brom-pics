import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter,LogLocator
import matplotlib.patches as mpatches





#matplotlib.rc('text', usetex=True)
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
#mpl.rcParams['text.latex.preamble'] = [r'\boldmath']

y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)   #format y scales to be scalar
majorLocator = MultipleLocator(2.)
majorFormatter = y_formatter #FormatStrFormatter('%d')
minorLocator = MultipleLocator(1.)
#minorFormatter = FormatStrFormatter('%d')


style.use('ggplot')

values=[]                                  # create empty matrix for storing data

#f = open('output_60_day.dat', 'rb')       #open model output file, 'read binary' 
#f = open('output_100_day.dat', 'rb')
#f = open('output_110_day.dat', 'rb')
#f = open('output_150_day.dat', 'rb')
#f = open('output_160_day.dat', 'rb')
#f = open('output_170_day.dat', 'rb')
#f = open('output_180_day.dat', 'rb')
f = open('output_190_day.dat', 'rb')
#f = open('output_330_day.dat', 'rb')


num_lines = sum(1 for l  in f)
num = num_lines - 3                        # calculate number of lines 
f.seek(0)                                  # return to the beginning of the file 


a = f.readline()
date = a.split()   

numday = date[2]

for _ in range(2):                        # skip two unneeded lines 
    line = f.readline() 
    
for _ in range(num):
    line = f.readline()                   # read line for heading
    foo = line.split()
    values.append(foo) 
data=zip(*values)                       #transpose the matrix of data

#Variables to plot:
depth = data[2][0:]
to_float = []
for item in depth:
    to_float.append(float(item)) #make a list of floats from tuple 
depth_sed = [] # list for storing final depth data for sediment 
v=0  
for i in to_float:
    v = (i- 110)*100 #(sed_wat interface)
    depth_sed.append(v)
temp = data[3][0:]
sal = data[4][0:]
kz = data[5][0:]
dic = data[8][0:]
alk = data[9][0:]
phy = data[10][0:]
het = data[11][0:]
no3 = data[12][0:]
po4 = data[13][0:]
nh4 = data[14][0:]
pon = data[15][0:]
don = data[16][0:]
o2  = data[17][0:]
mn2 = data[18][0:]
mn3 = data[19][0:]
mn4 = data[20][0:] 
h2s = data[21][0:] 
mns = data[22][0:]
mnco3 = data[23][0:]
fe2 = data[24][0:] 
fe3 = data[25][0:]
fes = data[26][0:]
feco3 = data[27][0:]
no2 = data[28][0:]
s0 = data[29][0:] 
s2o3 = data[30][0:]
so4 = data[31][0:]
si = data[32][0:]
si_part = data[33][0:]
baae = data[34][0:] 
bhae = data[35][0:]
baan = data[36][0:] 
bhan = data[37][0:] 
caco3 = data[38][0:]
fes2 = data[39][0:] 
ch4 = data[40][0:]
ph = data[55][0:]
pco2 = data[56][0:]
om_ca = data[58][0:]
om_ar = data[59][0:]
co3 = data[60][0:]
ca = data[61][0:]


#limits for Water,BBL, and Sediment
y1min = 0
y1max = 109
y2min = 109
y2max = 110
y3min = -10 #109.91
y3max = 10 #110.10
ysedmin = -8 #for depth in cm 
ysedmax = 10


#for filling the font
y2min_fill_bbl = y2max_fill_water = 109.5
y3max_fill_bbl = 0
y3min_fill_sed = 0
xticks =(np.arange(0,100000)) 

wat_color = '#c9ecfd' 
bbl_color = '#2873b8' #'#d2a87e'
sed_color = '#916012'

alpha_wat = 0.3
alpha_bbl = 0.3
alpha_sed = 0.5 

#limits for x   WatBBL axes:
kzmin = 1.e-7
kzmax = 1.e-0 
salmin = 32
salmax = 36
tempmin = 5
tempmax = 25
so4min = 10000
so4max = 30000
h2smax = 3
s0max = 3
s2o3max = 3 
o2max = 500
nh4max = 10
no2max = 2
no3max = 100
mnco3max = 1
mnsmax = 0.5
mn4max = 1
mn3max = 0.5
mn2max = 1
phymax = 2
hetmax = 10
baaemax = 1
bhaemax = 2
bhanmax = 1
baanmax = 2
nh4max = 50
ponmax = 80
donmax = 20
po4max = 20
fes2max = 5
fesmax = 5
fe3max = 5
fe2max = 5 
ch4max = 1
dicmin = 1000
dicmax = 6000
alkmin = 2200
alkmax = 2800
simax = 500
si_partmax = 100
ch4max = 0.5
phmin = 5
phmax = 9
pco2max = 8000
om_camax = 10
om_armax = 10
co3max = 10
camax = 10
#limits for x Sediment axes:
sed_kzmin = 0#1.e-11
sed_kzmax = 1.e-5
sed_tempmin = 5
sed_tempmax = 25
sed_salmin = 32
sed_salmax = 36
sed_so4min = 10000
sed_so4max = 30000
sed_h2smax = 1200
sed_s0max = 200
sed_s2o3max = 160 
sed_o2max = 200
sed_nh4max = 1500
sed_no2max = 10
sed_no3max = 50
sed_mnco3max = 10
sed_mnsmax = 10
sed_mn4max = 100
sed_mn3max = 10
sed_mn2max = 12
sed_phymax = 10
sed_hetmax = 20
sed_baaemax = 10
sed_bhaemax = 1000
sed_bhanmax = 4500
sed_baanmax = 500
sed_ponmax = 50000
sed_donmax = 250
sed_po4max = 200
sed_fes2max = 50
sed_fesmax = 50
sed_fe3max = 500
sed_fe2max = 100
sed_ch4max = 10
sed_dicmin = 1100
sed_dicmax = 15000
sed_alkmin = 2000
sed_alkmax = 14000
sed_simax = 2600 
sed_si_partmax = 75000
sed_ch4max = 0.5
sed_phmin = 5
sed_phmax = 9
sed_pco2max = 25000
sed_om_camax = 10
sed_om_armax = 5
sed_co3max = 10
sed_camax = 10
#positions for axes
axis1 = 0
axis2 = 27
axis3 = 53
axis4 = 79
axis5 = 105

labelaxis_x =  1.10
labelaxis1_y = 1.02
labelaxis2_y = 1.15
labelaxis3_y = 1.26
labelaxis4_y = 1.38
labelaxis5_y = 1.48

#define grid of subplots (BBL and Water)
wspace=0.40
hspace = 0.05
gs = gridspec.GridSpec(2, 6)  
gs.update(left=0.06, right=0.93,top = 0.86,bottom = 0.4, wspace=wspace,hspace=hspace)
gs1 = gridspec.GridSpec(1, 6)
gs1.update(left=0.06, right=0.93, top = 0.26, bottom = 0.02, wspace=wspace,hspace=hspace)

xlabel_fontsize = 17
xlabel_size = 16
ylabel_size = 16
mpl.rcParams['xtick.labelsize'] = xlabel_size
mpl.rcParams['ytick.labelsize'] = ylabel_size
mpl.rcParams['lines.linewidth'] = 2
y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)   #format y scales to be scalar

####################################
############# Figure 1 ############# 
####################################
fig1 = plt.figure(figsize = (24,15))
''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Water 
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y2min, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_xlim([kzmin,kzmax])
ax1.set_xticks(np.arange(kzmin,2*kzmax ,(kzmax)))
plt.text(0, 1.5,'Day '+ numday , fontweight='bold', #Write number of day to Figure
         bbox={'facecolor':'#c9ecfd', 'alpha':0.5, 'pad':10}, fontsize=14,
    transform=ax1.transAxes)
#Fig1  water Kz
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
plt.semilogx(kz, depth,'g-')
plt.grid(True)
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax11.set_xticks(np.arange(kzmin,kzmax +(kzmax- kzmin)/2. ,(kzmax- kzmin)/2.))
#ax11.xaxis.set_major_locator(ticker.LogLocator(base = 1.e-10))
ax11.set_xlim(kzmin, kzmax)
#ax11.set_xticks(np.arange(1.e-6,(1.e-0)+ ((1.e-0 - 1.e-6)/2.),((1.e-0 - 1.e-6)/2.)))
ax11.set_ylim([y1max, 0])
ax11.annotate(r'$\rm Kz $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')
ax11.tick_params(direction='out', pad=0) # remove distance between labels and axis

#Fig1 Water 1/1 Salinity  
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', axis2))
ax12.spines['top'].set_color('r')
ax12.plot(sal, depth, 'r-',sal, depth, 'r-') 
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xlim([salmin, salmax])
ax12.set_xticks(np.arange(salmin,salmax+((salmax -salmin)/4),((salmax -salmin)/4)))
ax12.set_ylim([y1max, 0])
ax12.annotate(r'$\rm S $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')
ax12.tick_params(direction='out', pad=0) # remove distance berween labels and axis
#Fig1 Water Temperature 
ax13 = ax1.twiny()
for spinename, spine in ax13.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax13.spines['top'].set_position(('outward',axis3))
ax13.spines['top'].set_color('b')
ax13.plot(temp,depth,'b-',temp,depth,'b-')
ax13.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax13.set_xlim([tempmin,tempmax ])
ax13.set_ylim([y1max, 0]) 
ax13.annotate(r'$\rm T $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')   
ax13.tick_params(direction='out', pad=0) # remove distance berween labels and axis   
                    
#Fig1 Water 2/1   
ax2 = plt.subplot(gs[5])
plt.text(1.1, 0.5,'Water ', fontweight='bold', #Write number of day to Figure
         bbox={'facecolor':'#c9ecfd', 'alpha':0.5, 'pad':10}, fontsize=14, rotation=90, 
    transform=ax2.transAxes)
ax2.set_ylim([y2min, 0])
ax2.set_xlim([0, s0max])
ax2.set_xticks(np.arange(0,s0max+s0max,s0max))
plt.setp(ax2.get_xticklabels(), visible=False)
#Fig1 Water - 2/1 SO4
ax21 = ax2.twiny()
ax21.plot(so4,depth,'g-',so4,depth,'g-')
ax21.set_xlim([so4min, so4max])
ax21.set_xticks(np.arange(so4min,so4max+((so4max - so4min)/2.),((so4max - so4min)/2.)))
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.annotate(r'$\rm SO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')
ax21.tick_params(direction='out', pad=0) # remove distance berween labels and axis
#Fig1 Water -  2/1 S0
ax22 = ax2.twiny()
for spinename, spine in ax22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax22.spines['top'].set_position(('outward', axis2))
ax22.spines['top'].set_color('r')
ax22.plot(s0,depth,'r-',s0,depth,'r-') 
ax22.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax22.set_xlim([0, s0max ])
ax22.set_xticks(np.arange(0,s0max+s0max/2.,s0max/2.))
ax22.set_ylim([y1max, 0])
ax22.annotate(r'$\rm S ^0$', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')
ax22.tick_params(direction='out', pad=0) # remove distance berween labels and axis
#Fig1 Water -  2/1 H2S
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', axis3))
ax23.spines['top'].set_color('b')
ax23.plot(h2s, depth, 'b-',h2s, depth, 'b-') 
ax23.annotate(r'$\rm H _2 S$', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')

ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, h2smax])
ax23.set_xticks(np.arange(0,h2smax+h2smax/2.,h2smax/2.))
ax23.set_ylim([y1max, 0])
ax23.tick_params(direction='out', pad=0) # remove distance berween labels and axis
#Fig1 Water - 2/1 s2o3
ax24 = ax2.twiny()
for spinename, spine in ax24.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax24.spines['top'].set_position(('outward', axis4))
ax24.spines['top'].set_color('m')
ax24.plot(s2o3, depth, 'm-',s2o3, depth, 'm-') 
ax24.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax24.set_xlim([0,s2o3max ])
ax24.set_xticks(np.arange(0,s2o3max+s2o3max/2.,s2o3max/2.))
ax24.set_ylim([y1max, 0])
ax24.annotate(r'$\rm S _2 O_ 3$', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m')            
ax24.tick_params(direction='out', pad=0) # remove distance berween labels and axis
#Fig1 Water 3/1 
ax3 = plt.subplot(gs[1])
plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([y1max, 0])
ax3.set_xticks(np.arange(0,o2max+o2max/5,o2max/5))
#Fig1 Water -  3/1 O2
ax31 = ax3.twiny()
for spinename, spine in ax31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax31.spines['top'].set_position(('outward', axis1))
ax31.spines['top'].set_color('g')
ax31.plot(o2, depth, 'g-',o2, depth, 'g-') 
ax31.set_xlim([0, o2max])
#ax31.set_xticks(np.arange(0,o2max+100,100))
ax31.set_xticks(np.arange(0,o2max+o2max/5.,o2max/5.))
ax31.annotate(r'$\rm O _2 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')
ax31.tick_params(direction='out', pad=0) # remove distance between labels and axis
#Fig1 Water -  3/1 - NH4
ax32 = ax3.twiny()
for spinename, spine in ax32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax32.spines['top'].set_position(('outward', axis2))
ax32.spines['top'].set_color('r')
ax32.plot(nh4,depth,'r-',nh4,depth,'r-') 
ax32.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax32.set_xlim([0, nh4max])
ax32.set_xticks(np.arange(0,nh4max+nh4max/5.,nh4max/5.))
ax32.set_ylim([y1max, 0])
ax32.annotate(r'$\rm NH _4 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')  
ax32.tick_params(direction='out', pad=0) # remove distance between labels and axis
#Fig1 Water -  3/1 NO2 
ax33 = ax3.twiny()
for spinename, spine in ax33.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax33.spines['top'].set_position(('outward', axis3))
ax33.spines['top'].set_color('b')
ax33.plot(no2, depth, 'b-',no2, depth, 'b-') 
ax33.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax33.set_xlim([0, no2max])
ax33.set_xticks(np.arange(0,no2max+no2max/5.,no2max/5.))
ax33.set_ylim([y1max, 0])
ax33.annotate(r'$\rm NO _2 $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
ax33.tick_params(direction='out', pad=0) # remove distance between labels and axis
#Fig1 Water - 3/1 NO3
ax34 = ax3.twiny()
for spinename, spine in ax34.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax34.spines['top'].set_position(('outward', axis4))
ax34.spines['top'].set_color('m')
ax34.plot(no3, depth, 'm-',no3, depth, 'm-') 
ax34.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax34.set_xlim([0, no3max])
ax34.set_xticks(np.arange(0,no3max+no3max/5.,no3max/5.))
ax34.set_ylim([y1max, 0])
ax34.annotate(r'$\rm NO _3 $',fontweight='bold', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
ax34.tick_params(direction='out', pad=0) # remove distance between labels and axis

#Fig1 Water - 4/1 
ax4 = plt.subplot(gs[3])
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.set_ylim([y1max, 0])
#Fig1 Water -  4/1 MnII
ax41 = ax4.twiny()
ax41.plot(mn2,depth,'g-',mn2,depth,'g-')
for spinename, spine in ax41.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax41.spines['top'].set_position(('outward', axis1))
ax41.spines['top'].set_color('g')
ax41.set_xlim([0, mn2max])
#ax41.set_xticks(np.arange(0,(mn2max+mn2max/4),mn2max/4))
#ax41.set_xlabel('Mn II',color = 'g')
ax41.annotate(r'$\rm MnII $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 16,
            color='g')

#Fig1 Water -  4/1 - Mn III
ax42 = ax4.twiny()
for spinename, spine in ax42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax42.spines['top'].set_position(('outward', axis2))
ax42.spines['top'].set_color('r')
ax42.plot(mn3,depth,'r-',mn3,depth,'r-') 
ax42.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax42.set_xlim([0, mn3max])
#ax42.set_xticks(np.arange(0,mn3max+mn3max/2,mn3max/2))
ax42.set_ylim([y1max, 0])
ax42.annotate(r'$\rm MnIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')  
#Fig1 Water -  4/1 Mn IV
ax43 = ax4.twiny()
for spinename, spine in ax43.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax43.spines['top'].set_position(('outward', axis3))
ax43.spines['top'].set_color('b')
ax43.plot(mn4, depth, 'b-',mn4, depth, 'b-') 
ax43.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax43.set_xlim([0, mn4max])
ax43.set_ylim([y1max, 0])
ax43.annotate(r'$\rm MnIV $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')  
#Fig1 Water - 4/1 MnS
ax44 = ax4.twiny()
for spinename, spine in ax44.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax44.spines['top'].set_position(('outward', axis4))
ax44.spines['top'].set_color('m')
ax44.plot(mns, depth, 'm-',mns, depth, 'm-') 
ax44.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax44.set_xlim([0, mnsmax])
##ax44.set_xticks(np.arange(0,mnsmax+mnsmax/2,mnsmax/2))
ax44.set_ylim([y1max, 0])
ax44.annotate(r'$\rm MnS $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
##Fig1 Water - 3/1 MnCO3
ax45 = ax4.twiny()
for spinename, spine in ax45.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax45.spines['top'].set_position(('outward', axis5))
ax45.spines['top'].set_color('c')
ax45.plot(mnco3, depth, 'c-',mnco3, depth, 'c-') 
ax45.xaxis.set_label_position('top') # this moves the label to the top
ax45.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax45.set_xlim([0, mnco3max])
#ax45.set_xticks(np.arange(0,mnco3max+mnco3max/5,mnco3max/5))
ax45.set_ylim([y1max, 0])
ax45.annotate(r'$\rm MnCO _3 $', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='c') 

#Fig1 Water 6/1 
axn3 = plt.subplot(gs[2])
plt.setp(axn3.get_xticklabels(), visible=False)
axn3.set_ylim([y1max, 0])
axn3.set_xlim([0, po4max])
#Fig1 Water -  6/1 PO4
axn31 = axn3.twiny()
for spinename, spine in axn31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
#axn31.spines['top'].set_position(('outward', axis1))
axn31.spines['top'].set_color('g')
axn31.plot(po4, depth, 'g-',po4, depth, 'g-') 
axn31.set_xlim([0, po4max])
axn31.set_xticks(np.arange(0,po4max+po4max/4,po4max/4))
axn31.annotate(r'$\rm PO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')
#Fig1 Water -  6/1 - pon
axn32 = axn3.twiny()
for spinename, spine in axn32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn32.spines['top'].set_position(('outward', axis2))
axn32.spines['top'].set_color('r')
axn32.plot(pon,depth,'r-',pon,depth,'r-') 
axn32.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn32.set_xlim([0,ponmax])
axn32.set_xticks(np.arange(0,ponmax+ponmax/4,ponmax/4))
axn32.set_ylim([y1max, 0])
axn32.annotate(r'$\rm PON $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')   
#Fig1 Water -  3/1 don 
axn33 = axn3.twiny()
for spinename, spine in axn33.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn33.spines['top'].set_position(('outward', axis3))
axn33.spines['top'].set_color('b')
axn33.plot(don, depth, 'b-',don, depth, 'b-') 
axn33.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn33.set_xlim([0, donmax])
axn33.set_xticks(np.arange(0,donmax+donmax/4,donmax/4))
axn33.set_ylim([y1max, 0])
axn33.annotate(r'$\rm DON $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')   

#Fig1 Water - 4/1 
axn4 = plt.subplot(gs[4])
#Fig1 Water -  4/1 FeII

plt.setp(axn4.get_xticklabels(), visible=False)
axn4.set_ylim([y1max, 0])
axn41 = axn4.twiny()
for spinename, spine in axn41.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn41.spines['top'].set_position(('outward', axis1))
axn41.spines['top'].set_color('g')
axn41.set_xlim([0, fe2max])
axn41.plot(fe2,depth,'g-',fe2,depth,'g-')
axn41.annotate(r'$\rm FeII $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#Fig1 Water -  4/1 - FeIII

axn42 = axn4.twiny()
for spinename, spine in axn42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn42.spines['top'].set_position(('outward', axis2))
axn42.spines['top'].set_color('r')
axn42.plot(fe3,depth,'r-',fe3,depth,'r-') 
axn42.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn42.set_xlim([0, fe3max])
#axn42.set_xticks(np.arange(0,fe3max+fe3max/2,fe3max/2))
#axn32.set_xticks(np.arange(0,1500,500))
axn42.set_ylim([y1max, 0])
axn42.annotate(r'$\rm FeIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')  
#Fig1 Water -  4/1 FeS
axn43 = axn4.twiny()
for spinename, spine in axn43.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn43.spines['top'].set_position(('outward', axis3))
axn43.spines['top'].set_color('b')
axn43.plot(fes, depth, 'b-',fes, depth, 'b-') 
axn43.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn43.set_xlim([0, fesmax])
axn43.set_ylim([y1max, 0])
axn43.annotate(r'$\rm FeS $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')  
#Fig1 Water - 4/1 FeS2
axn44 = axn4.twiny()
for spinename, spine in axn44.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn44.spines['top'].set_position(('outward', axis4))
axn44.spines['top'].set_color('m')
axn44.plot(fes2, depth, 'm-',fes2, depth, 'm-') 
axn44.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn44.set_xlim([0, fes2max])
axn44.set_ylim([y1max, 0])
axn44.annotate(r'$\rm FeS _2 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 


#############################
##Fig1  BBL 1/2
##Fig1  BBL 1/2 - Temperature
ax5 = plt.subplot(gs[6])
ax5.plot(temp,depth,'bo-',temp,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([tempmin,tempmax])
ax5.set_xticks(np.arange(tempmin,tempmax+((tempmax - tempmin)/4.),((tempmax - tempmin)/4.)))
ax5.set_ylim([y2max, y2min])
#Fig1 BBL 1/2 - Salinity
ax52 = ax5.twiny()
ax52.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax52.set_xlim([salmin, salmax])
ax52.set_xticks(np.arange(salmin,salmax+((salmax - salmin)/4.),((salmax - salmin)/4.)))
ax52.set_ylim([y2max, y2min])
plt.setp(ax52.get_xticklabels(), visible=False)
#Fig1 BBL 1/2 Kz
ax53 = ax5.twiny()
ax53.set_xscale('log')
#ax53.set_xlim([1.e-6, 1.e-1])
ax53.set_xlim([kzmin, kzmax])
ax53.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax53.set_xticks(np.arange(kzmin,kzmax +(kzmax- kzmin)/2. ,(kzmax- kzmin)/2.))
ax53.set_ylim([y2max, y2min])
plt.setp(ax53.get_xticklabels(), visible=False)


#Fig1  BBL 2/2 
ax6 = plt.subplot(gs[11])

plt.text(1.1, 0.7,'Water ', fontweight='bold', #Write number of day to Figure
         bbox={'facecolor': wat_color, 'alpha':0.5, 'pad':10}, fontsize=14, rotation=90,
    transform=ax6.transAxes)
plt.text(1.1, 0.3,'BBL ', fontweight='bold', #Write number of day to Figure
         bbox={'facecolor': bbl_color , 'alpha':0.6, 'pad':10}, fontsize=14, rotation=90,
    transform=ax6.transAxes)

#Fig1  BBL - SO4
ax6.plot(so4,depth,'go-',so4,depth,'go-')
ax6.set_xlim([so4min, so4max])
ax6.set_xticks(np.arange(so4min,so4max+((so4max - so4min)/2.),((so4max - so4min)/2.)))
ax6.set_ylim([y2max, y2min])
plt.setp(ax6.get_xticklabels(), visible=False)
#Fig1 BBL -  2/2 S0
ax62 = ax6.twiny()
ax62.plot(s0, depth, 'ro-',s0, depth, 'ro-') 
ax62.set_xlim([0, s0max])
ax62.set_xticks(np.arange(0,s0max+s0max/2.,s0max/2.))
ax62.set_ylim([y2max, y2min])
plt.setp(ax62.get_xticklabels(), visible=False)

#Fig1 BBL -  2/2 h2S
ax63 = ax6.twiny()
ax63.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
ax63.set_xlim([0, h2smax])
ax63.set_xticks(np.arange(0,h2smax+h2smax/2.,h2smax/2.))
ax63.set_ylim([y2max, y2min])
plt.setp(ax63.get_xticklabels(), visible=False)

#Fig1 BBL -  2/2 s2o3
ax64 = ax6.twiny()
ax64.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax64.set_xlim([-0, s2o3max])
ax64.set_xticks(np.arange(0,s2o3max+s2o3max/2.,s2o3max/2.))
ax64.set_ylim([y2max, y2min])
plt.setp(ax64.get_xticklabels(), visible=False)

##Fig1 BBL 3/2
ax7 = plt.subplot(gs[7])
#Fig1 BBL 3/2 - o2
ax7.plot(o2,depth,'go-',o2,depth,'go-')
#Fig1 ax7.set_ylabel('Depth (m)')
plt.setp(ax7.get_xticklabels(), visible=False)
ax7.set_xlim([0,o2max])
ax7.set_ylim([y2max, y2min])
ax7.set_xticks(np.arange(0,o2max+o2max/5,o2max/5))
#Fig1 BBL 3/2 - nh4
ax72 = ax7.twiny()
ax72.plot(nh4, depth, 'ro-',nh4, depth, 'ro-') 
ax72.set_xlim([0, nh4max])
ax72.set_xticks(np.arange(0,nh4max+nh4max/5.,nh4max/5.))
ax72.set_ylim([y2max, y2min])
plt.setp(ax72.get_xticklabels(), visible=False)
#Fig1 BBL 3\2 - no2
ax73 = ax7.twiny()
ax73.plot(no2, depth, 'b-',no2, depth, 'b-') 
ax73.set_xlim([0, no2max])
ax73.set_xticks(np.arange(0,no2max+no2max/5.,no2max/5.))
ax73.set_ylim([y2max, y2min])
plt.setp(ax73.get_xticklabels(), visible=False)
#Fig1 BBL - 3/2 NO3
ax74 = ax7.twiny()
ax74.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax74.set_xlim([0, no3max])
ax74.set_xticks(np.arange(0,no3max+no3max/5.,no3max/5.))
ax74.set_ylim([y2max, y2min])
plt.setp(ax74.get_xticklabels(), visible=False)

##Fig1 BBL - 4/2
ax8 = plt.subplot(gs[9])
#Fig1 BBL - 4/2 - Mn II
ax8.plot(mn2,depth,'go-',mn2,depth,'go-')
plt.setp(ax8.get_xticklabels(), visible=False)
ax8.set_xlim([0,mn2max])
ax8.set_ylim([y2max, y2min])

#Fig1 BBL - 4/2 - Mn III
ax82 = ax8.twiny()
ax82.plot(mn3, depth, 'ro-',mn3, depth, 'ro-') 
ax82.set_xlim([0, mn3max])
ax82.set_ylim([y2max, y2min])
plt.setp(ax82.get_xticklabels(), visible=False)
#Fig1 BBL 4\2 - mn IV
ax83 = ax8.twiny()
ax83.plot(mn4, depth, 'bo-',mn4, depth, 'bo-') 
ax83.set_xlim([0, mn4max])
ax83.set_ylim([y2max, y2min])
plt.setp(ax83.get_xticklabels(), visible=False)
#Fig1 BBL - 4/2 MnS
ax84 = ax8.twiny()
ax84.plot(mns, depth, 'mo-',mns, depth, 'mo-') 
ax84.set_xlim([0, mnsmax])
ax84.set_ylim([y2max, y2min])
plt.setp(ax84.get_xticklabels(), visible=False)
#Fig1 BBL - 4/2 MnCO3
ax85 = ax8.twiny()
ax85.plot(mnco3, depth, 'co-',mnco3, depth, 'co-') 
ax85.set_xlim([0, mnco3max])
ax85.set_ylim([y2max, y2min])
plt.setp(ax85.get_xticklabels(), visible=False)

##Fig1 BBL 3/2
axn7 = plt.subplot(gs[8])
#Fig1 BBL 3/2 - PO4
axn7.plot(po4,depth,'go-',po4,depth,'go-')
#axn7.set_ylabel('Depth (m)')
plt.setp(axn7.get_xticklabels(), visible=False)
axn7.set_xlim([0,po4max])
axn7.set_xticks(np.arange(0,po4max+po4max/4,po4max/4))
axn7.set_ylim([y2max, y2min])
#Fig1  3/2 - PON
axn72 = axn7.twiny()
axn72.plot(pon, depth, 'ro-',pon, depth, 'ro-') 
axn72.set_xlim([0, ponmax])
axn72.set_xticks(np.arange(0,ponmax+ponmax/4,ponmax/4))
axn72.set_ylim([y2max, y2min])
plt.setp(axn72.get_xticklabels(), visible=False)
#Fig1 BBL 3\2 - don
axn73 = axn7.twiny()
axn73.plot(don, depth, 'b-',don, depth, 'b-') 
axn73.set_xlim([0, donmax])
axn73.set_xticks(np.arange(0,donmax+donmax/4,donmax/4))
axn73.set_ylim([y2max, y2min])
plt.setp(axn73.get_xticklabels(), visible=False)

##Fig1 BBL - 4/2
axn8 = plt.subplot(gs[10])
#Fig1 BBL - 4/2 - Fe II
axn8.plot(fe2,depth,'go-',fe2,depth,'go-')
plt.setp(axn8.get_xticklabels(), visible=False)
axn8.set_xlim([0,fe2max])
axn8.set_ylim([y2max, y2min])

#Fig1 BBL - 4/2 - Fe III
axn82 = axn8.twiny()
axn82.plot(fe3, depth, 'ro-',fe3, depth, 'ro-') 
axn82.set_xlim([0, fe3max])
axn82.set_ylim([y2max, y2min])
plt.setp(axn82.get_xticklabels(), visible=False)
#Fig1 BBL 4\2 - FeS
axn83 = axn8.twiny()
axn83.plot(fes, depth, 'bo-',fes, depth, 'bo-') 
axn83.set_xlim([0, fesmax])
axn83.set_ylim([y2max, y2min])
plt.setp(axn83.get_xticklabels(), visible=False)
#Fig1 BBL - 4/2 fes2
axn84 = axn8.twiny()
axn84.plot(fes2, depth, 'mo-',fes2, depth, 'mo-') 
axn84.set_xlim([0, fes2max])
axn84.set_ylim([y2max, y2min])
plt.setp(axn84.get_xticklabels(), visible=False)








###############
#Fig1 Sediment#
###############
#Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (cm)')
ax9.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
ax9.yaxis.set_major_locator(majorLocator)
ax9.yaxis.set_major_formatter(majorFormatter)
ax9.yaxis.set_minor_locator(minorLocator)
ax9.yaxis.grid(True,'minor')
ax9.yaxis.grid(True,'major')
plt.setp(ax9.get_xticklabels(), visible=False)
ax9.set_xticks(np.arange(0,sed_salmax+ (sed_salmax),(sed_salmax)))

#Fig1 sediment Kz
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('g')
ax91.plot(kz, depth_sed, 'go-',kz, depth_sed, 'go-') 
#ax91.set_xscale('log')
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([sed_kzmin, sed_kzmax])
#locator=LogLocator.set_params(base=None, subs=None, numdecs=None, numticks=3)
#ax91.xaxis.set_major_locator(ticker.LogLocator(numticks=2))
#ax91.xaxis.set_major_locator(ticker.LogLocator(base = 10))
#ax91.xaxis.set_major_locator(locator)
ax91.set_xticks(np.arange(sed_kzmin,sed_kzmax +(sed_kzmax- sed_kzmin)/2. ,(sed_kzmax- sed_kzmin)/2.))
#ax91.set_xticks(np.arange(0,sed_kzmax+ (sed_kzmax/2),(sed_kzmax/2)))
ax91.set_ylim([y3max, y3min])
ax91.annotate(r'$\rm Kz $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig1 Sediment - 1/3 SAlinity
ax92 = ax9.twiny()
for spinename, spine in ax92.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax92.spines['top'].set_position(('outward', axis2))
ax92.spines['top'].set_color('r')
ax92.plot(sal, depth_sed, 'ro-',sal, depth_sed, 'ro-') 
ax92.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax92.set_xlim([sed_salmin, sed_salmax])
ax92.set_xticks(np.arange(sed_salmin,sed_salmax+((sed_salmax -sed_salmin)/4),((sed_salmax -sed_salmin)/4)))
ax92.set_ylim([y3max, y3min])

ax92.annotate(r'$\rm S $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment 1/3 Temperature
ax93 = ax9.twiny()
for spinename, spine in ax93.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax93.spines['top'].set_position(('outward', axis3))
ax93.spines['top'].set_color('b')
ax93.plot(temp,depth_sed,'bo-',temp,depth_sed,'bo-')
ax93.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax93.set_xlim([tempmin, tempmax])
ax93.set_ylim([y3max, y3min])
ax93.annotate(r'$\rm T $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment - 2/3 
ax10 = plt.subplot(gs1[0, 5])
plt.setp(ax10.get_xticklabels(), visible=False)
ax10.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
ax10.yaxis.set_major_locator(majorLocator)
ax10.yaxis.set_major_formatter(majorFormatter)
ax10.yaxis.set_minor_locator(minorLocator)
ax10.yaxis.grid(True,'minor')
ax10.yaxis.grid(True,'major')
ax10.set_xlim([sed_so4min, sed_so4max])
ax10.set_xticks(np.arange(sed_so4min,sed_so4max,(sed_so4max - sed_so4min)))

plt.text(1.1, 0.7,'BBL ', fontweight='bold', #Write number of day to Figure
         bbox={'facecolor': bbl_color, 'alpha':0.5, 'pad':10}, fontsize=14, rotation=90,
    transform=ax10.transAxes)
plt.text(1.1, 0.3,'Sediment ', fontweight='bold', #Write number of day to Figure
         bbox={'facecolor': sed_color , 'alpha':0.6, 'pad':10}, fontsize=14, rotation=90,
    transform=ax10.transAxes)


#Fig1 Sediment - 2/3 SO4
ax101 = ax10.twiny()
ax101.plot(so4,depth_sed,'go-',so4,depth_sed,'go-')
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.set_xlim([sed_so4min, sed_so4max])
ax101.set_xticks(np.arange(sed_so4min,sed_so4max + ((sed_so4max - sed_so4min)/2),((sed_so4max - sed_so4min)/2)))
ax101.annotate(r'$\rm SO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig1 sediment -  2/3 S0
ax102 = ax10.twiny()
for spinename, spine in ax102.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax102.spines['top'].set_position(('outward', axis2))
ax102.spines['top'].set_color('r')
ax102.plot(s0,depth_sed,'ro-',s0,depth_sed,'ro-') 
ax102.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax102.set_xlim([0, sed_s0max ])
ax102.set_xticks(np.arange(0, sed_s0max+ sed_s0max/4, sed_s0max/4))
ax102.set_ylim([y3max, y3min])
ax101.annotate(r'$\rm S ^0 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment -  2/3 H2S
ax103 = ax10.twiny()
for spinename, spine in ax103.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax103.spines['top'].set_position(('outward', axis3))
ax103.spines['top'].set_color('b')
ax103.plot(h2s, depth_sed, 'bo-',h2s, depth_sed, 'bo-') 
ax103.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax103.set_xlim([0, sed_h2smax])
ax103.set_xticks(np.arange(0,sed_h2smax+sed_h2smax/4,sed_h2smax/4))
ax103.set_ylim([y3max, y3min])

ax103.annotate(r'$\rm H _2 S $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment - 2/3 s2o3
ax104 = ax10.twiny()
for spinename, spine in ax104.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax104.spines['top'].set_position(('outward', axis4))
ax104.spines['top'].set_color('m')
ax104.plot(s2o3, depth_sed, 'mo-',s2o3, depth_sed, 'mo-') 
ax104.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax104.set_xlim([0, sed_s2o3max])
ax104.set_xticks(np.arange(0,sed_s2o3max+sed_s2o3max/4,sed_s2o3max/4))
ax104.set_ylim([y3max, y3min])
ax104.annotate(r'$\rm S _2 O _3 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig1 Sediment - 3/3
ax11n = plt.subplot(gs1[0,1])
plt.setp(ax11n.get_xticklabels(), visible=False)
ax11n.set_ylim([y3max, y3min])
# draw minor gridlines
ax11n.yaxis.set_major_locator(majorLocator)
ax11n.yaxis.set_major_formatter(majorFormatter)
ax11n.yaxis.set_minor_locator(minorLocator)
ax11n.yaxis.grid(True,'minor')
ax11n.yaxis.grid(True,'major')   
ax111 = ax11n.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('g')
ax111.plot(o2,depth_sed,'go-',o2,depth_sed,'go-')
ax111.set_xlim([0, sed_o2max])
ax111.set_xticks(np.arange(0,sed_o2max+sed_o2max/5,sed_o2max/5))
ax111.annotate(r'$\rm O _2 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig1 Sediment -  3/3 - NH4
ax112 = ax11n.twiny()
for spinename, spine in ax112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax112.spines['top'].set_position(('outward', axis2))
ax112.spines['top'].set_color('r')
ax112.plot(nh4,depth_sed,'ro-',nh4,depth_sed,'ro-') 
ax112.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax112.set_xlim([0, sed_nh4max])
ax112.set_xticks(np.arange(0,sed_nh4max+sed_nh4max/5,sed_nh4max/5))
ax112.set_ylim([y3max, y3min])
ax112.annotate(r'$\rm NH _4 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment -  3/3 NO2 
ax113 = ax11n.twiny()
for spinename, spine in ax113.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax113.spines['top'].set_position(('outward', axis3))
ax113.spines['top'].set_color('b')
ax113.plot(no2, depth_sed, 'bo-',no2, depth_sed, 'bo-') 
ax113.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax113.set_xlim([0, sed_no2max])
ax113.set_xticks(np.arange(0,sed_no2max+sed_no2max/5.,sed_no2max/5.))
ax113.set_ylim([y3max, y3min])
ax113.annotate(r'$\rm NO _2 $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment -  3/3 NO3
ax114 = ax11n.twiny()
for spinename, spine in ax114.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax114.spines['top'].set_position(('outward', axis4))
ax114.spines['top'].set_color('m')
ax114.plot(no3, depth_sed, 'mo-',no3, depth_sed, 'mo-') 
ax114.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax114.set_xlim([0, sed_no3max])
ax114.set_xticks(np.arange(0,sed_no3max+sed_no3max/5.,sed_no3max/5.))
ax114.set_ylim([y3max, y3min])
ax114.annotate(r'$\rm NO _3 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig1 Sediment - 4/3 
ax12n = plt.subplot(gs1[0,3])
plt.setp(ax12n.get_xticklabels(), visible=False)
ax12n.set_ylim([y3max, y3min])
# draw minor gridlines
ax12n.yaxis.set_major_locator(majorLocator)
ax12n.yaxis.set_major_formatter(majorFormatter)
ax12n.yaxis.set_minor_locator(minorLocator)
ax12n.yaxis.grid(True,'minor')
ax12n.yaxis.grid(True,'major')

ax121 = ax12n.twiny()
ax121.plot(mn2,depth_sed,'go-',mn2,depth_sed,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_mn2max])
ax121.set_xticks(np.arange(0,sed_mn2max+sed_mn2max/2,sed_mn2max/2))
ax121.annotate(r'$\rm MnII $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig1 Sediment - 4/3 - Mn III
ax122 = ax12n.twiny()
for spinename, spine in ax122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax122.spines['top'].set_position(('outward', axis2))
ax122.spines['top'].set_color('r')
ax122.plot(mn3,depth_sed,'ro-',mn3,depth_sed,'ro-') 
ax122.xaxis.set_label_position('top') # this moves the label to the top
ax122.set_xlim([0, sed_mn3max])
ax122.set_xticks(np.arange(0,sed_mn3max+sed_mn3max/2,sed_mn3max/2))
#ax32.set_xticks(np.arange(0,1500,500))
ax122.set_ylim([y3max, y3min])
ax122.annotate(r'$\rm MnIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment - 4/3  Mn IV
ax123 = ax12n.twiny()
for spinename, spine in ax123.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax123.spines['top'].set_position(('outward', axis3))
ax123.spines['top'].set_color('b')
ax123.plot(mn4, depth_sed, 'bo-',mn4, depth_sed, 'bo-') 
ax123.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax123.set_xlim([0, sed_mn4max])
ax123.set_xticks(np.arange(0,sed_mn4max+sed_mn4max/2,sed_mn4max/2))
ax123.set_ylim([y3max, y3min])
ax123.annotate(r'$\rm MnIV $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment - 4/3 MnS
ax124 = ax12n.twiny()
for spinename, spine in ax124.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax124.spines['top'].set_position(('outward', axis4))
ax124.spines['top'].set_color('m')
ax124.plot(mns, depth_sed, 'mo-',mns, depth_sed, 'mo-') 
ax124.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax124.set_xlim([0, sed_mnsmax])
ax124.set_xticks(np.arange(0,sed_mnsmax+sed_mnsmax/2.,sed_mnsmax/2.))
ax124.set_ylim([y3max, y3min])
ax124.annotate(r'$\rm MnS $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig1 Sediment - 4/3  MnCO3
ax125 = ax12n.twiny()
for spinename, spine in ax125.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax125.spines['top'].set_position(('outward', axis5))
ax125.spines['top'].set_color('c')
ax125.plot(mnco3, depth_sed, 'co-',mnco3, depth_sed, 'co-') 
ax125.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax125.set_xlim([0, sed_mnco3max])
ax125.set_xticks(np.arange(0,sed_mnco3max+sed_mnco3max/2.,sed_mnco3max/2.))
ax125.set_ylim([y3max, y3min])
ax125.annotate(r'$\rm MnCO _3 $', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='c')





#Fig1 Sediment - 3/3 PO4 
axn11n = plt.subplot(gs1[0,2])
#axn11.plot(po4,depth,'go-',po4,depth,'go-')
#axn3.set_ylabel('Depth (m)')
plt.setp(axn11n.get_xticklabels(), visible=False)
axn11n.set_ylim([y3max, y3min])
# draw minor gridlines
axn11n.yaxis.set_major_locator(majorLocator)
axn11n.yaxis.set_major_formatter(majorFormatter)
axn11n.yaxis.set_minor_locator(minorLocator)
axn11n.yaxis.grid(True,'minor')
axn11n.yaxis.grid(True,'major')  
axn11n.set_xlim([0, sed_ponmax])
axn11n.set_xticks(np.arange(0,sed_ponmax+sed_ponmax/4,sed_ponmax/4))
axn111 = axn11n.twiny()
for spinename, spine in axn111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn111.spines['top'].set_position(('outward', axis1))
axn111.spines['top'].set_color('g')
axn111.plot(po4,depth_sed,'go-',po4,depth_sed,'go-')
axn111.set_xlim([0, sed_po4max])
axn111.set_xticks(np.arange(0,sed_po4max+sed_po4max/4,sed_po4max/4))
axn111.annotate(r'$\rm PO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig1 Sediment -  3/3 - PON
axn112 = axn11n.twiny()
for spinename, spine in axn112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn112.spines['top'].set_position(('outward', axis2))
axn112.spines['top'].set_color('r')
axn112.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn112.plot(pon,depth_sed,'ro-',pon,depth_sed,'ro-') 
axn112.set_xlim([0, sed_ponmax])
axn112.set_xticks(np.arange(0,sed_ponmax+sed_ponmax/2,sed_ponmax/2))
axn112.set_ylim([y3max, y3min])
axn112.annotate(r'$\rm PON $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 

#Fig1 Sediment -  3/3 don 
axn113 = axn11n.twiny()
for spinename, spine in axn113.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn113.spines['top'].set_position(('outward', axis3))
axn113.spines['top'].set_color('b')
axn113.plot(don, depth_sed, 'bo-',don, depth_sed, 'bo-') 
axn113.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn113.set_xlim([0, sed_donmax])
axn113.set_xticks(np.arange(0,sed_donmax+sed_donmax/2,sed_donmax/2))
axn113.set_ylim([y3max, y3min])
axn113.annotate(r'$\rm DON $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 

#Fig1 Sediment - 4/3 
axn12n = plt.subplot(gs1[0,4])
plt.setp(axn12n.get_xticklabels(), visible=False)
axn12n.set_ylim([ysedmax, ysedmin])
# draw minor gridlines and ticks in scalar mode
axn12n.yaxis.set_major_locator(majorLocator)
axn12n.yaxis.set_major_formatter(majorFormatter)
axn12n.yaxis.set_minor_locator(minorLocator)
axn12n.yaxis.grid(True,'minor')
axn12n.yaxis.grid(True,'major')  
#Sediment - 4/3 FeII
axn121 = axn12n.twiny()
axn121.plot(fe2,depth_sed,'go-',fe2,depth_sed,'go-')
for spinename, spine in axn121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn121.spines['top'].set_position(('outward', axis1))
axn121.spines['top'].set_color('g')
axn121.set_xlim([0, sed_fe2max])
axn121.set_xticks(np.arange(0,sed_fe2max+sed_fe2max/5,sed_fe2max/5))
axn121.set_ylim([ysedmax, y3min])
axn121.annotate(r'$\rm FeII $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 

#Fig1 Sediment - 4/3 - fe III
axn122 = axn12n.twiny()
for spinename, spine in axn122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn122.spines['top'].set_position(('outward', axis2))
axn122.spines['top'].set_color('r')
axn122.plot(fe3,depth_sed,'ro-',fe3,depth_sed,'ro-') 
axn122.xaxis.set_label_position('top') # this moves the label to the top
axn122.set_xlim([0, sed_fe3max])
axn122.set_xticks(np.arange(0,sed_fe3max+sed_fe3max/5,sed_fe3max/5))
axn122.set_ylim([ysedmax, y3min])
axn122.annotate(r'$\rm FeIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment - 4/3 FeS
axn123 = axn12n.twiny()
for spinename, spine in axn123.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn123.spines['top'].set_position(('outward', axis3))
axn123.spines['top'].set_color('b')
axn123.plot(fes,depth_sed, 'bo-',fes,depth_sed, 'bo-') 
axn123.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn123.set_xlim([0, sed_fesmax])
axn123.set_ylim([ysedmax, y3min])
axn123.annotate(r'$\rm FeS $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment - 4/3 fes2
axn124 = axn12n.twiny()
for spinename, spine in axn124.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn124.spines['top'].set_position(('outward', axis4))
axn124.spines['top'].set_color('m')
axn124.plot(fes2,depth_sed, 'mo-',fes2,depth_sed, 'mo-') 
axn124.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn124.set_xlim([0, sed_fes2max])
axn124.set_ylim([ysedmax, y3min])
axn124.annotate(r'$\rm FeS _2 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m')
#ysedmax, ysedmin
#fill the font 
#wat
ax1.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax2.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax3.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax4.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
axn3.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
axn4.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 

#bbl
ax5.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat)
ax6.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat)
ax7.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
axn7.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax8.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
axn8.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
  
ax5.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
ax6.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax7.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
axn7.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax8.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
axn8.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)

#sed
ax9.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax10.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
axn11n.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax11n.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
axn12n.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax12n.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)

ax9.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax10.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
axn11n.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax11n.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax12n.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
axn12n.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)


####################################
############# Figure 2 ############# 
####################################
fig2 = plt.figure(figsize = (24,15))

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
plt.text(0, 1.5,'Day '+ numday , fontweight='bold', #Write number of day to Figure
         bbox={'facecolor':'#c9ecfd', 'alpha':0.5, 'pad':10}, fontsize=14,
    transform=ax1.transAxes)
#Fig 2 Water 1/1
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y1max, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_xticks(np.arange(0,phymax+phymax/2,phymax/2))
#Fig 2  water Phy
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
ax11.plot(phy, depth, 'g-',phy, depth, 'g-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax11.set_xlim([0, phymax])
ax11.set_xticks(np.arange(0,phymax+phymax/2,phymax/2))
ax11.set_ylim([y1max, 0])
ax11.annotate(r'$\rm Phy $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')
#Fig2 Water Het
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', axis2))
ax12.spines['top'].set_color('r')
ax12.plot(het, depth, 'r-',het, depth, 'r-') 
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xlim([0, hetmax])
ax12.set_xticks(np.arange(0,hetmax+hetmax/2,hetmax/2))
ax12.set_ylim([y1max, 0])
ax12.annotate(r'$\rm Het $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')
                    
#Fig2 Water 2/1   
ax2 = plt.subplot(gs[1])
ax2.set_ylim([y1max, 0])
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.set_xticks(np.arange(0,baaemax+baaemax,baaemax))
#Fig2 Water - 2/1 Bacteria autotropohic anaerobic Baan
ax21 = ax2.twiny()
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)        
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.plot(baan,depth,'g-',baan,depth,'g-')
ax21.set_xlim([0, baanmax])
ax21.set_xticks(np.arange(0,baanmax+baanmax/4.,baanmax/4.))
ax21.annotate(r'$\rm Baan $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#Fig2 Water -  2/1 Bacteria heterotropohic anaerobic Bhan
ax22 = ax2.twiny()
for spinename, spine in ax22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax22.spines['top'].set_position(('outward', axis2))
ax22.spines['top'].set_color('r')
ax22.plot(bhan,depth,'r-',bhan,depth,'r-') 
ax22.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax22.set_xlim([0, bhanmax ])
ax22.set_xticks(np.arange(0,bhanmax+bhanmax/4.,bhanmax/4.))
ax22.set_ylim([y1max, 0])
ax21.annotate(r'$\rm Bhan $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')
#Fig2 Water -  2/1 Bacteria heterotropohic aerobic Bhae
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', axis3))
ax23.spines['top'].set_color('b')
ax23.plot(bhae, depth, 'b-',bhae, depth, 'b-') 
ax23.annotate(r'$\rm Bhae $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')
ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, bhaemax])
ax23.set_xticks(np.arange(0,bhaemax+bhaemax/4.,bhaemax/4.))
ax23.set_ylim([y1max, 0])

#Fig2 Water - 2/1 Bacteria autotropohic aerobic Baae
ax24 = ax2.twiny()
for spinename, spine in ax24.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax24.spines['top'].set_position(('outward', axis4))
ax24.spines['top'].set_color('m')
ax24.plot(baae, depth, 'm-',baae, depth, 'm-') 
ax24.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax24.set_xlim([0, baaemax])
ax24.set_xticks(np.arange(0,baaemax+baaemax/4.,baaemax/4.))
ax24.set_ylim([y1max, 0])
ax24.annotate(r'$\rm Baae $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m')            
# Water 1/1
axn1 = plt.subplot(gs[2])
#fig 3 Water 1/1 pH
axn1.set_ylim([y1max, 0])
plt.setp(axn1.get_xticklabels(), visible=False)
axn1.set_xlim([phmin, phmax]) 
axn1.set_xticks(np.arange(phmin,phmax+((phmax-phmin)/3),(phmax-phmin)/3))
#fig 3 water pH
axn11 = axn1.twiny()
for spinename, spine in axn11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn11.spines['top'].set_position(('outward', axis1))
axn11.spines['top'].set_color('b')
axn11.plot(ph, depth, 'b-',ph, depth, 'b-') 
axn11.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn11.set_xlim([phmin, phmax])
axn11.set_xticks(np.arange(phmin,phmax+((phmax-phmin)/3),(phmax-phmin)/3))
axn11.set_ylim([y1max, 0])
axn11.annotate(r'$\rm pH $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')
#fig 3 Water pCO2
axn12 = axn1.twiny()
for spinename, spine in axn12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn12.spines['top'].set_position(('outward', axis2))
axn12.spines['top'].set_color('r')
axn12.plot(pco2, depth, 'r-',pco2, depth, 'r-') 
axn12.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn12.set_xticks(np.arange(0,pco2max+pco2max/4,pco2max/4))
axn12.set_xlim([0, pco2max])
axn12.set_ylim([y1max, 0])
axn12.annotate(r'$\rm pCO _2 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')
                    
#fig 2 Water 2/1   
axn2 = plt.subplot(gs[3])
#fig 2 Water - 2/1 Alk
axn2.set_ylim([y1max, 0])
plt.setp(axn2.get_xticklabels(), visible=False)
axn2.set_xlim([alkmin, alkmax])
axn2.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
#ax2.set_xticks(np.arange(20000,so4max,2000))
axn21 = axn2.twiny()
for spinename, spine in axn21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)        
axn21.spines['top'].set_position(('outward', axis1)) #move 
axn21.spines['top'].set_color('g')
axn21.plot(alk,depth,'g-',alk,depth,'g-')
axn21.set_xlim([alkmin, alkmax])
axn21.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
axn21.annotate(r'$\rm Alk $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#fig 3 Water -  2/1 DIC
axn22 = axn2.twiny()
for spinename, spine in axn22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn22.spines['top'].set_position(('outward', axis2))
axn22.spines['top'].set_color('m')
axn22.plot(dic,depth,'m-',dic,depth,'m-') 
axn22.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn22.set_xlim([dicmin, dicmax ])
axn22.set_xticks(np.arange(dicmin,dicmax+((dicmax - dicmin)/2),((dicmax - dicmin)/2)))
axn22.set_ylim([y1max, 0])
axn21.annotate(r'$\rm DIC $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m')

#fig 2 Water 3/1 
axn3 = plt.subplot(gs[4])
#fig 2 Water -  3/1 CH4
plt.setp(axn3.get_xticklabels(), visible=False)
axn3.set_ylim([y1max, 0])
axn3.set_xlim([0, ch4max])
axn3.set_xticks(np.arange(0,ch4max+ch4max/5,ch4max/5))
axn31 = axn3.twiny()
for spinename, spine in axn31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn31.spines['top'].set_position(('outward', axis1))
axn31.spines['top'].set_color('b')
axn31.plot(ch4, depth, 'b-',ch4, depth, 'b-') 
axn31.set_xlim([0, ch4max])
axn31.set_xticks(np.arange(0,ch4max+ch4max/5,ch4max/5))
axn31.annotate(r'$\rm CH _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')

#fig 2 Water -  3/1 - Om_ar
axn32 = axn3.twiny()
for spinename, spine in axn32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn32.spines['top'].set_position(('outward', axis2))
axn32.spines['top'].set_color('r')
axn32.plot(om_ar,depth,'r-',om_ar,depth,'r-') 
axn32.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn32.set_xlim([0,om_armax])
axn32.set_xticks(np.arange(0,om_armax+om_armax/5,om_armax/5))
axn32.set_ylim([y1max, 0])
axn32.annotate(r'$\rm \Omega Ar $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')  

#fig 2 Water - 4/1 
axn4 = plt.subplot(gs[5])
#fig 2 Water -  4/1 Si
plt.setp(axn4.get_xticklabels(), visible=False)
axn4.set_ylim([y1max, 0])
axn4.set_xticks(np.arange(0,si_partmax+si_partmax,si_partmax))
axn41 = axn4.twiny()
for spinename, spine in axn41.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn41.spines['top'].set_position(('outward', axis1))
axn41.spines['top'].set_color('g')
axn41.set_xlim([0, simax])
axn41.set_xticks(np.arange(0,simax+simax/2,simax/2))
axn41.plot(si,depth,'g-',si,depth,'g-')
axn41.annotate(r'$\rm Si $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#fig 2 Water -  4/1 - Si_part
axn42 = axn4.twiny()
for spinename, spine in axn42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn42.spines['top'].set_position(('outward', axis2))
axn42.spines['top'].set_color('m')
axn42.plot(si_part,depth,'m-',si_part,depth,'m-') 
axn42.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn42.set_xlim([0, si_partmax])
axn42.set_xticks(np.arange(0,2*si_partmax,si_partmax))
#axn42.set_xticks(np.arange(0,fe3max+fe3max/2,fe3max/2))
axn42.set_ylim([y1max, 0])
axn42.annotate(r'$\rm Si part $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 

##Fig2  BBL 1/2
 #Fig2  BBL 1/2 - Phyto
ax5 = plt.subplot(gs[6])
ax5.plot(phy,depth,'go-',phy,depth,'go-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([0, phymax])
ax5.set_xticks(np.arange(0,phymax+phymax/2,phymax/2))
ax5.set_ylim([y2max, y2min])
#Fig2 BBL 1/2 - Het
ax52 = ax5.twiny()
ax52.plot(het, depth, 'ro-',het, depth, 'ro-') 
ax52.set_xlim([0, hetmax])
ax52.set_xticks(np.arange(0,hetmax+hetmax/2,hetmax/2))
ax52.set_ylim([y2max, y2min])
plt.setp(ax52.get_xticklabels(), visible=False)

#Fig2  BBL 2/2 
ax6 = plt.subplot(gs[7])
#Fig2  BBL - Baan
ax6.plot(baan,depth,'go-',baan,depth,'go-')
ax6.set_xlim([0, baanmax])
ax6.set_xticks(np.arange(0,baanmax+baanmax/4.,baanmax/4.))
ax6.set_ylim([y2max, y2min])
plt.setp(ax6.get_xticklabels(), visible=False)
#Fig2 BBL -  2/2 Bhan
ax62 = ax6.twiny()
ax62.plot(bhan, depth, 'ro-',bhan, depth, 'ro-') 
ax62.set_xlim([0, bhanmax])
ax62.set_xticks(np.arange(0,bhanmax+bhanmax/4.,bhanmax/4.))
ax62.set_ylim([y2max, y2min])
plt.setp(ax62.get_xticklabels(), visible=False)
#Fig2 BBL -  2/2 Bhae
ax63 = ax6.twiny()
ax63.plot(bhae, depth, 'bo-',bhae, depth, 'bo-') 
ax63.set_xlim([0, bhaemax])
ax63.set_xticks(np.arange(0,bhaemax+bhaemax/4.,bhaemax/4.))
ax63.set_ylim([y2max, y2min])
plt.setp(ax63.get_xticklabels(), visible=False)
#Fig2 BBL -  2/2 Baae
ax64 = ax6.twiny()
ax64.plot(baae, depth, 'mo-',baae, depth, 'mo-') 
ax64.set_xlim([0, baaemax])
ax64.set_xticks(np.arange(0,baaemax+baaemax/4.,baaemax/4.))
ax64.set_ylim([y2max, y2min])
plt.setp(ax64.get_xticklabels(), visible=False)

##fig 2  BBL 1/2
 #fig 2  BBL 1/2 - pH
axn5 = plt.subplot(gs[8])
axn5.plot(ph,depth,'bo-',ph,depth,'bo-')
plt.setp(axn5.get_xticklabels(), visible=False)
axn5.set_xlim([phmin, phmax])
axn5.set_xticks(np.arange(phmin,phmax+((phmax-phmin)/4),(phmax-phmin)/4))
axn5.set_ylim([y2max, y2min])
#fig 2 BBL 1/2 - pco2
axn52 = axn5.twiny()
axn52.plot(pco2, depth, 'ro-',pco2, depth, 'ro-') 
axn52.set_xlim([0, pco2max])
axn52.set_xticks(np.arange(0,pco2max+((pco2max)/4),(pco2max)/4))
axn52.set_ylim([y2max, y2min])
plt.setp(axn52.get_xticklabels(), visible=False)
#fig2  BBL 2/2 
axn6 = plt.subplot(gs[9])
#fig2  BBL - alk
axn6.plot(alk,depth,'go-',alk,depth,'go-')
axn6.set_xlim([alkmin, alkmax])
axn6.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
axn6.set_ylim([y2max, y2min])
plt.setp(axn6.get_xticklabels(), visible=False)
#fig2 BBL -  2/2 dic
axn62 = axn6.twiny()
axn62.plot(dic, depth, 'mo-',dic, depth, 'mo-') 
axn62.set_xlim([dicmin, dicmax])
axn62.set_xticks(np.arange(dicmin,dicmax+((dicmax - dicmin)/2),((dicmax - dicmin)/2)))
axn62.set_ylim([y2max, y2min])
plt.setp(axn62.get_xticklabels(), visible=False)

#fig2 BBL 3/2
axn7 = plt.subplot(gs[10])
#fig2 BBL 3/2 - ch4
axn7.plot(ch4,depth,'bo-',ch4,depth,'bo-')
plt.setp(axn7.get_xticklabels(), visible=False)
axn7.set_xlim([0,ch4max])
axn7.set_ylim([y2max, y2min])
#fig 2  BBL 3/2 - om_ar
axn72 = axn7.twiny()
axn72.plot(om_ar, depth, 'ro-',om_ar, depth, 'ro-') 
axn72.set_xlim([0, om_armax])
axn72.set_ylim([y2max, y2min])
plt.setp(axn72.get_xticklabels(), visible=False)


##fig2 BBL - 4/2
axn8 = plt.subplot(gs[11])
#fig2 BBL - 4/2 - Si
axn8.plot(si,depth,'go-',si,depth,'go-')
plt.setp(axn8.get_xticklabels(), visible=False)
axn8.set_xlim([0,simax])
axn8.set_xticks(np.arange(0,simax+simax/2,simax/2))
axn8.set_ylim([y2max, y2min])
#fig 3 BBL - 4/2 - Si_part
axn82 = axn8.twiny()
axn82.plot(si_part, depth, 'mo-',si_part, depth, 'mo-') 
axn82.set_xlim([0, si_partmax])
axn82.set_xticks(np.arange(0,si_partmax+si_partmax,si_partmax))
axn82.set_ylim([y2max, y2min])
plt.setp(axn82.get_xticklabels(), visible=False)


###############
#Fig2 Sediment#
###############
#Fig2 Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (cm)')
plt.setp(ax9.get_xticklabels(), visible=False)
ax9.set_xticks(np.arange(0,sed_phymax+sed_phymax,sed_phymax))
ax9.yaxis.set_major_locator(majorLocator) # draw minor gridlines and ticks in scalar mode
ax9.yaxis.set_major_formatter(majorFormatter)
ax9.yaxis.set_minor_locator(minorLocator)
ax9.yaxis.grid(True,'minor')
ax9.yaxis.grid(True,'major') 
#Fig2 sediment  1/3 Phy
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('g')
ax91.plot(phy, depth_sed, 'go-',phy, depth_sed, 'go-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([0, sed_phymax])
ax91.set_xticks(np.arange(0,sed_phymax+sed_phymax/2,sed_phymax/2))
ax91.set_ylim([y3max, y3min])
ax91.annotate(r'$\rm Phy $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig2 Sediment - 1/3 het
ax92 = ax9.twiny()
for spinename, spine in ax92.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax92.spines['top'].set_position(('outward', axis2))
ax92.spines['top'].set_color('r')
ax92.plot(het, depth_sed, 'ro-',het, depth_sed, 'ro-') 
ax92.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax92.set_xlim([0, sed_hetmax])
ax92.set_xticks(np.arange(0,sed_hetmax+sed_hetmax/2,sed_hetmax/2))
ax92.set_ylim([y3max, y3min])
ax92.annotate(r'$\rm Het $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 

#Fig2 Sediment - 2/3 Baan
ax10 = plt.subplot(gs1[0, 1])
ax10.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
ax10.yaxis.set_major_locator(majorLocator)
ax10.yaxis.set_major_formatter(majorFormatter)
ax10.yaxis.set_minor_locator(minorLocator)
ax10.yaxis.grid(True,'minor')
ax10.yaxis.grid(True,'major')
plt.setp(ax10.get_xticklabels(), visible=False)
ax10.set_xticks(np.arange(0,sed_baaemax+(sed_baaemax),(sed_baaemax)))
ax101 = ax10.twiny()
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.plot(baan,depth_sed,'go-',baan,depth_sed,'go-')
ax101.set_xlim([0, sed_baanmax])
ax101.set_xticks(np.arange(0,sed_baanmax+(sed_baanmax/2),(sed_baanmax/2)))
ax101.annotate(r'$\rm Baan $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig2 sediment -  2/3 bhan
ax102 = ax10.twiny()
for spinename, spine in ax102.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax102.spines['top'].set_position(('outward', axis2))
ax102.spines['top'].set_color('r')
ax102.plot(bhan,depth_sed,'ro-',bhan,depth_sed,'ro-') 
ax102.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax102.set_xlim([0, sed_bhanmax])
ax102.set_xticks(np.arange(0,sed_bhanmax+(sed_bhanmax/2),(sed_bhanmax/2)))
ax102.set_ylim([y3max, y3min])
ax102.annotate(r'$\rm Bhan $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = xlabel_fontsize,
            color='r') 


#Fig2 Sediment -  2/3 bhae
ax103 = ax10.twiny()
for spinename, spine in ax103.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax103.spines['top'].set_position(('outward', axis3))
ax103.spines['top'].set_color('b')
ax103.plot(bhae, depth_sed, 'bo-',bhae, depth_sed, 'bo-') 
ax103.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax103.set_xlim([0, sed_bhaemax])
ax103.set_xticks(np.arange(0,sed_bhaemax+(sed_bhaemax/2),(sed_bhaemax/2)))
ax103.set_ylim([y3max, y3min])
ax103.annotate(r'$\rm Bhae $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig2 Sediment - 2/3 baae
ax104 = ax10.twiny()
for spinename, spine in ax104.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax104.spines['top'].set_position(('outward', axis4))
ax104.spines['top'].set_color('m')
ax104.plot(baae, depth_sed, 'mo-',baae, depth, 'mo-') 
ax104.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax104.set_xlim([0, sed_baaemax])
ax104.set_xticks(np.arange(0,sed_baaemax+(sed_baaemax/2),(sed_baaemax/2)))
ax104.set_ylim([y3max, y3min])
ax104.annotate(r'$\rm Baae $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 






#fig 3 Sediment 
#fig 3 Sediment - 1/3 
axn9 = plt.subplot(gs1[0,2])
plt.setp(axn9.get_xticklabels(), visible=False)
# draw minor gridlines and ticks in scalar mode
axn9.yaxis.set_major_locator(majorLocator)
axn9.yaxis.set_major_formatter(majorFormatter)
axn9.yaxis.set_minor_locator(minorLocator)
axn9.yaxis.grid(True,'minor')
axn9.yaxis.grid(True,'major')
axn9.set_xticks(np.arange(sed_phmin,sed_phmax+((sed_phmax-sed_phmin)/4),(sed_phmax-sed_phmin)/4))
axn9.set_xlim([sed_phmin, sed_phmax])
#fig 3 sediment  1/3 pH
axn91 = axn9.twiny()
for spinename, spine in axn91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn91.spines['top'].set_position(('outward', axis1))
axn91.spines['top'].set_color('b')
axn91.plot(ph, depth_sed, 'bo-',ph, depth_sed, 'bo-') 
axn91.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn91.set_xlim([sed_phmin, sed_phmax])
axn91.set_xticks(np.arange(sed_phmin,sed_phmax+((sed_phmax-sed_phmin)/4),(sed_phmax-sed_phmin)/4))
#axn91.set_xticks(np.arange(sed_phmin,sed_phmax+(sed_phmax/3),sed_phmax/3))
axn91.set_ylim([y3max, y3min])
axn91.annotate(r'$\rm pH $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#fig 3 Sediment - 1/3 pco2
axn92 = axn9.twiny()
for spinename, spine in axn92.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn92.spines['top'].set_position(('outward', axis2))
axn92.spines['top'].set_color('r')
axn92.plot(pco2, depth_sed, 'ro-',pco2, depth_sed, 'ro-') 
axn92.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn92.set_xlim([0, sed_pco2max])
axn92.set_xticks(np.arange(0,sed_pco2max+sed_pco2max/2,sed_pco2max/2))
axn92.set_ylim([y3max, y3min])
axn92.annotate(r'$\rm pCO _2 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 

            
#fig 3 Sediment - 2/3 
axn10 = plt.subplot(gs1[0, 3])
axn10.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
axn10.yaxis.set_major_locator(majorLocator)
axn10.yaxis.set_major_formatter(majorFormatter)
axn10.yaxis.set_minor_locator(minorLocator)
axn10.yaxis.grid(True,'minor')
axn10.yaxis.grid(True,'major')

plt.setp(axn10.get_xticklabels(), visible=False)
axn10.set_xlim([sed_dicmin, sed_dicmax])
axn10.set_xticks(np.arange(sed_dicmin,sed_dicmax+((sed_dicmax - sed_dicmin)),((sed_dicmax - sed_dicmin))))

#fig 3 Sediment - 2/3 alk
axn101 = axn10.twiny()
for spinename, spine in axn101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn101.spines['top'].set_position(('outward', axis1))
axn101.spines['top'].set_color('g')
axn101.plot(alk,depth_sed,'go-',alk,depth_sed,'go-')
axn101.set_xlim([sed_alkmin, sed_alkmax])
axn101.set_xticks(np.arange(sed_alkmin,sed_alkmax+((sed_alkmax - sed_alkmin)/2),((sed_alkmax - sed_alkmin)/2)))
#ax101.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
axn101.annotate(r'$\rm Alk $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#fig 3 sediment -  2/3 dic
axn102 = axn10.twiny()
for spinename, spine in axn102.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn102.spines['top'].set_position(('outward', axis2))
axn102.spines['top'].set_color('m')
axn102.plot(dic,depth_sed,'mo-',dic,depth_sed,'mo-') 
axn102.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn102.set_xlim([sed_dicmin, sed_dicmax])
axn102.set_xticks(np.arange(sed_dicmin,sed_dicmax+((sed_dicmax - sed_dicmin)/2),((sed_dicmax - sed_dicmin)/2)))
axn102.set_ylim([y3max, y3min])
axn102.annotate(r'$\rm DIC $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = xlabel_fontsize,
            color='m') 

#fig 3 Sediment 
axn11n = plt.subplot(gs1[0,4])

axn11n.set_ylim([y3max, y3min])
# draw minor gridlines
axn11n.yaxis.set_major_locator(majorLocator)
axn11n.yaxis.set_major_formatter(majorFormatter)
axn11n.yaxis.set_minor_locator(minorLocator)
axn11n.yaxis.grid(True,'minor')
axn11n.yaxis.grid(True,'major')
axn11n.set_xlim([0, ch4max])
plt.setp(axn11n.get_xticklabels(), visible=False)
#fig 3 Sediment - 3/3 ch4
axn111 = axn11n.twiny()
for spinename, spine in axn111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn111.spines['top'].set_position(('outward', axis1))
axn111.spines['top'].set_color('b')
axn111.plot(ch4,depth_sed,'bo-',ch4,depth_sed,'bo-')
axn111.set_xlim([0, sed_ch4max])
axn111.set_xticks(np.arange(0,sed_ch4max+sed_ch4max/5,sed_ch4max/5))
#axn111.set_xticks(np.arange(0,sed_o2max+100,100))
axn111.annotate(r'$\rm CH _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#fig 3 Sediment -  3/3 - om_ar
axn112 = axn11n.twiny()
for spinename, spine in axn112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn112.spines['top'].set_position(('outward', axis2))
axn112.spines['top'].set_color('r')
axn112.plot(om_ar,depth_sed,'ro-',om_ar,depth_sed,'ro-') 
axn112.xaxis.set_ticks_position('top') # this moves the ticks to the top
axn112.set_xlim([0, sed_om_armax])
axn112.set_xticks(np.arange(0,sed_om_armax+sed_om_armax/5,sed_om_armax/5))
axn112.set_ylim([y3max, y3min])
axn112.annotate(r'$\rm \Omega Ar $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
            
#fig 3 Sediment - 4/3 Si
axn12n = plt.subplot(gs1[0,5])
plt.setp(axn12n.get_xticklabels(), visible=False)
axn12n.set_ylim([y3max, y3min])
# draw minor gridlines
axn12n.yaxis.set_major_locator(majorLocator)
axn12n.yaxis.set_major_formatter(majorFormatter)
axn12n.yaxis.set_minor_locator(minorLocator)
axn12n.yaxis.grid(True,'minor')
axn12n.yaxis.grid(True,'major')
axn12n.set_xticks(np.arange(0,sed_si_partmax+sed_si_partmax,sed_si_partmax))
 # This makes axis label to be written in full scalar mode
axn12n.yaxis.set_major_formatter(y_formatter) # ( not exp as default)   
axn121 = axn12n.twiny()
axn121.plot(si,depth_sed,'go-',si,depth_sed,'go-')
for spinename, spine in axn121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn121.spines['top'].set_position(('outward', axis1))
axn121.spines['top'].set_color('g')
axn121.set_xlim([0, sed_simax])
axn121.set_xticks(np.arange(0,sed_simax+sed_simax/2,sed_simax/2))
axn121.annotate(r'$\rm Si $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#fig 3 Sediment - 4/3 - si_part
axn122 = axn12n.twiny()
for spinename, spine in axn122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
axn122.spines['top'].set_position(('outward', axis2))
axn122.spines['top'].set_color('m')
axn122.plot(si_part,depth_sed,'mo-',si_part,depth_sed,'mo-') 
axn122.xaxis.set_label_position('top') # this moves the label to the top
axn122.set_xlim([0, sed_si_partmax])
axn122.set_xticks(np.arange(0,sed_si_partmax+sed_si_partmax,sed_si_partmax))
axn122.set_ylim([y3max, y3min])
axn122.annotate(r'$\rm Si part $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 

#fill the font 
#wat
ax1.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax2.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
axn1.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
axn2.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
axn3.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
axn4.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat)
#bbl
axn5.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
axn5.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
axn6.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
axn6.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
axn7.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
axn7.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
axn8.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
axn8.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
ax5.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax5.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
ax6.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax6.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
#sed
ax10.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax10.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax9.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax9.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
axn12n.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed) 
axn12n.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl) 
axn11n.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
axn11n.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
axn10.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
axn10.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
axn9.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
axn9.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)

# save the figure to file
fig1.savefig('fig1O2H2S.png')   
fig2.savefig('fig2PhyHet.png')



plt.show()

plt.close(fig1)
plt.close(fig2)
