import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#matplotlib.rc('text', usetex=True)
#matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
#mpl.rcParams['text.latex.preamble'] = [r'\boldmath']

y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)   #format y scales to be scalar
majorLocator = MultipleLocator(0.02)
majorFormatter = y_formatter #FormatStrFormatter('%d')
minorLocator = MultipleLocator(0.01)
#minorFormatter = FormatStrFormatter('%d')

style.use('ggplot')

values=[]                                  # create empty matrix for storing data

#f = open('output_60_day.dat', 'rb')       #open model output file, 'read binary' 
#f = open('output_100_day.dat', 'rb')
#f = open('output_110_day.dat', 'rb')
f = open('output_150_day.dat', 'rb')
#f = open('output_160_day.dat', 'rb')
#f = open('output_170_day.dat', 'rb')
#f = open('output_180_day.dat', 'rb')
#f = open('output_190_day.dat', 'rb')
#f = open('output_330_day.dat', 'rb')


num_lines = sum(1 for l  in f)
num = num_lines - 1                        # calculate number of lines 
f.seek(0)                                  # return to the beginning of the file 

#delete = f.readline()
#print delete

for _ in range(1):                        # skip two unneeded lines 
    line = f.readline()
    
for _ in range(num):
    line = f.readline()                   # read line for heading
    foo = line.split()
    values.append(foo) 
data = zip(*values)                       #transpose the matrix of data
#print data
#Variables to plot:
depth = data[2][2:]

depth_sed = list(depth)
#depth_sed = [map(float, x) for x in depth]
#depth_sed = [[int(column) for column in row] for row in depth]
#for i in depth_sed:
#    depth_sed[i] -= 110 
print type(depth_sed)
temp = data[3][2:]
sal = data[4][2:]
kz = data[5][2:]
dic = data[8][2:]
alk = data[9][2:]
phy = data[10][2:]
het = data[11][2:]
no3 = data[12][2:]
po4 = data[13][2:]
nh4 = data[14][2:]
pon = data[15][2:]
don = data[16][2:]
o2  = data[17][2:]
mn2 = data[18][2:]
mn3 = data[19][2:]
mn4 = data[20][2:] 
h2s = data[21][2:] 
mns = data[22][2:]
mnco3 = data[23][2:]
fe2 = data[24][2:] 
fe3 = data[25][2:]
fes = data[26][2:]
feco3 = data[27][2:]
no2 = data[28][2:]
s0 = data[29][2:] 
s2o3 = data[30][2:]
so4 = data[31][2:]
si = data[32][2:] 
si_part = data[33][2:]
baae = data[34][2:] 
bhae = data[35][2:]
baan = data[36][2:] 
bhan = data[37][2:] 
caco3 = data[38][2:]
fes2 = data[39][2:] 
ch4 = data[40][2:]
ph = data[55][2:]
pco2 = data[56][2:]
om_ca = data[58][2:]
om_ar = data[59][2:]
co3 = data[60][2:]
ca = data[61][2:]


#limits for Water,BBL, and Sediment
y1min = 0
y1max = 109
y2min = 109
y2max = 110
y3min = 109.91
y3max = 110.10

yticksmin = 110# 109.91
yticksmax = 110.09

#for filling the font
y2min_fill_bbl = y2max_fill_water = 109.5
y3max_fill_bbl = y3min_fill_sed = 110
xticks =(np.arange(0,50000)) 
wat_color = '#c9ecfd' #f6f0db' #'white'#'c'
bbl_color = '#d2a87e'
sed_color = '#916012' #'k'

alpha_fill = 0.2
alpha_wat = 0.2
alpha_bbl = 0.2
alpha_sed = 0.4 
#limits for x   WatBBL axes:
kzmin = 0
kzmax = 12 
#kzmax =  8
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
dicmin = 1100
dicmax = 6000
alkmin = 2100
alkmax = 3000
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
sed_kzmax = 0.04
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
sed_alkmin = 2100
sed_alkmax = 15000
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
axis2 = 25
axis3 = 50
axis4 = 75
axis5 = 100

labelaxis_x =  1.10
labelaxis1_y = 1.02
labelaxis2_y = 1.15
labelaxis3_y = 1.26
labelaxis4_y = 1.38
labelaxis5_y = 1.48


####################################
############# Figure 1 ############# 
####################################

fig1 = plt.figure(figsize = (15,15))
rect = 1,1,3,3
fig1.add_axes(rect, label='axes1')

gs = gridspec.GridSpec(2, 4)  #determine grid of subplots (BBL and Water)
gs.update(left=0.08, right=0.92,top = 0.86,bottom = 0.4, wspace=0.35,hspace=0.02)

xlabel_fontsize = 17
xlabel_size = 13
ylabel_size = 13
mpl.rcParams['xtick.labelsize'] = xlabel_size
mpl.rcParams['ytick.labelsize'] = ylabel_size
#mpl.rcParams['xtick.fontsize'] = xlabel_fontsize
mpl.rcParams['lines.linewidth'] = 2

y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)   #format y scales to be scalar


''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Water 
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y2min, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_xlim([0, kzmax])
ax1.set_xticks(np.arange(0,2*kzmax ,(kzmax)))
#ax1.set_xticks(np.arange(0,kzmax+(kzmax/3)),(kzmax/3))
#Fig1  water Kz
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
ax11.plot(kz, depth, 'g-',kz, depth, 'g-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax11.set_xlim([0, kzmax])
ax11.set_xticks(np.arange(0,kzmax+ (kzmax/4),(kzmax/4)))
ax11.set_ylim([y1max, 0])

#ticklabelpad = mpl.rcParams['xtick.major.pad']
ax11.annotate(r'$\rm Kz $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

################################################################################ ax11.tick_params(direction='out', pad=0)
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
#Fig1 Water 2/1   
ax2 = plt.subplot(gs[1])
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
ax21.annotate(r'$\rm S ^0$', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')

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

#Fig1 Water 3/1 
ax3 = plt.subplot(gs[2])
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
ax32.set_xticks(np.arange(0,no3max+no3max/5.,no3max/5.))
ax34.set_ylim([y1max, 0])
ax34.annotate(r'$\rm NO _3 $',fontweight='bold', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 

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
# r'$\boldsymbol{\phi}$' 
  
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
#ax32.set_xticks(np.arange(0,1500,500))
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

##Fig1  BBL 1/2
##Fig1  BBL 1/2 - Temperature
ax5 = plt.subplot(gs[4])
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
ax53.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax53.set_xlim([0, kzmax])
ax53.set_xticks(np.arange(0,2*kzmax ,(kzmax)))
ax53.set_ylim([y2max, y2min])
plt.setp(ax53.get_xticklabels(), visible=False)


#Fig1  BBL 2/2 
ax6 = plt.subplot(gs[5])
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
ax7 = plt.subplot(gs[6])
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
ax72.set_xticks(np.arange(0,no2max+no2max/5.,no2max/5.))
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
ax8 = plt.subplot(gs[7])
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

gs1 = gridspec.GridSpec(1, 4)
gs1.update(left=0.08, right=0.92, top = 0.26, bottom = 0.02, wspace=0.35,hspace=0.02)
#gs.update(left=0.08, right=0.92,top = 0.86,bottom = 0.4, wspace=0.35,hspace=0.02)
#Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (m)')
ax9.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
ax9.yaxis.set_major_locator(majorLocator)
ax9.yaxis.set_major_formatter(majorFormatter)
ax9.yaxis.set_minor_locator(minorLocator)
ax9.yaxis.grid(True,'minor')
ax9.yaxis.grid(True,'major')
plt.setp(ax9.get_xticklabels(), visible=False)
ax9.set_xticks(np.arange(0,sed_kzmax+ (sed_kzmax),(sed_kzmax)))

#Fig1 sediment Kz
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('g')
ax91.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([0, sed_kzmax])
ax91.set_xticks(np.arange(0,sed_kzmax+ (sed_kzmax/2),(sed_kzmax/2)))
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
ax92.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
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
ax93.plot(temp,depth,'bo-',temp,depth,'bo-')
ax93.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax93.set_xlim([tempmin, tempmax])
ax93.set_ylim([y3max, y3min])
ax93.annotate(r'$\rm T $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment - 2/3 
ax10 = plt.subplot(gs1[0, 1])
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

#Fig1 Sediment - 2/3 SO4
ax101 = ax10.twiny()
ax101.plot(so4,depth,'go-',so4,depth,'go-')
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
ax102.plot(s0,depth,'ro-',s0,depth,'ro-') 
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
ax103.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
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
ax104.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax104.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax104.set_xlim([0, sed_s2o3max])
ax104.set_xticks(np.arange(0,sed_s2o3max+sed_s2o3max/4,sed_s2o3max/4))
ax104.set_ylim([y3max, y3min])
ax104.annotate(r'$\rm S _2 O _3 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig1 Sediment - 3/3
ax11 = plt.subplot(gs1[0,2])
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([y3max, y3min])
# draw minor gridlines
ax11.yaxis.set_major_locator(majorLocator)
ax11.yaxis.set_major_formatter(majorFormatter)
ax11.yaxis.set_minor_locator(minorLocator)
ax11.yaxis.grid(True,'minor')
ax11.yaxis.grid(True,'major')   
ax111 = ax11.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('g')
ax111.plot(o2,depth,'go-',o2,depth,'go-')
ax111.set_xlim([0, sed_o2max])
ax111.set_xticks(np.arange(0,sed_o2max+sed_o2max/5,sed_o2max/5))
ax111.annotate(r'$\rm O _2 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig1 Sediment -  3/3 - NH4
ax112 = ax11.twiny()
for spinename, spine in ax112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax112.spines['top'].set_position(('outward', axis2))
ax112.spines['top'].set_color('r')
ax112.plot(nh4,depth,'ro-',nh4,depth,'ro-') 
ax112.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax112.set_xlim([0, sed_nh4max])
ax112.set_xticks(np.arange(0,sed_nh4max+sed_nh4max/5,sed_nh4max/5))
ax112.set_ylim([y3max, y3min])
ax112.annotate(r'$\rm NH _4 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment -  3/3 NO2 
ax113 = ax11.twiny()
for spinename, spine in ax113.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax113.spines['top'].set_position(('outward', axis3))
ax113.spines['top'].set_color('b')
ax113.plot(no2, depth, 'bo-',no2, depth, 'bo-') 
ax113.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax113.set_xlim([0, sed_no2max])
ax113.set_xticks(np.arange(0,sed_no2max+sed_no2max/5.,sed_no2max/5.))
ax113.set_ylim([y3max, y3min])
ax113.annotate(r'$\rm NO _2 $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment -  3/3 NO3
ax114 = ax11.twiny()
for spinename, spine in ax114.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax114.spines['top'].set_position(('outward', axis4))
ax114.spines['top'].set_color('m')
ax114.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax114.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax114.set_xlim([0, sed_no3max])
ax114.set_xticks(np.arange(0,sed_no3max+sed_no3max/5.,sed_no3max/5.))
ax114.set_ylim([y3max, y3min])
ax114.annotate(r'$\rm NO _3 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig1 Sediment - 4/3 
ax12 = plt.subplot(gs1[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([y3max, y3min])
# draw minor gridlines
ax12.yaxis.set_major_locator(majorLocator)
ax12.yaxis.set_major_formatter(majorFormatter)
ax12.yaxis.set_minor_locator(minorLocator)
ax12.yaxis.grid(True,'minor')
ax12.yaxis.grid(True,'major')

ax121 = ax12.twiny()
ax121.plot(mn2,depth,'go-',mn2,depth,'go-')
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
ax122 = ax12.twiny()
for spinename, spine in ax122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax122.spines['top'].set_position(('outward', axis2))
ax122.spines['top'].set_color('r')
ax122.plot(mn3,depth,'ro-',mn3,depth,'ro-') 
ax122.xaxis.set_label_position('top') # this moves the label to the top
ax122.set_xlim([0, sed_mn3max])
ax122.set_xticks(np.arange(0,sed_mn3max+sed_mn3max/2,sed_mn3max/2))
#ax32.set_xticks(np.arange(0,1500,500))
ax122.set_ylim([y3max, y3min])
ax122.annotate(r'$\rm MnIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig1 Sediment - 4/3  Mn IV
ax123 = ax12.twiny()
for spinename, spine in ax123.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax123.spines['top'].set_position(('outward', axis3))
ax123.spines['top'].set_color('b')
ax123.plot(mn4, depth, 'bo-',mn4, depth, 'bo-') 
ax123.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax123.set_xlim([0, sed_mn4max])
ax123.set_xticks(np.arange(0,sed_mn4max+sed_mn4max/2,sed_mn4max/2))
ax123.set_ylim([y3max, y3min])
ax123.annotate(r'$\rm MnIV $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig1 Sediment - 4/3 MnS
ax124 = ax12.twiny()
for spinename, spine in ax124.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax124.spines['top'].set_position(('outward', axis4))
ax124.spines['top'].set_color('m')
ax124.plot(mns, depth, 'mo-',mns, depth, 'mo-') 
ax124.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax124.set_xlim([0, sed_mnsmax])
ax124.set_xticks(np.arange(0,sed_mnsmax+sed_mnsmax/2.,sed_mnsmax/2.))
ax124.set_ylim([y3max, y3min])
ax124.annotate(r'$\rm MnS $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig1 Sediment - 4/3  MnCO3
ax125 = ax12.twiny()
for spinename, spine in ax125.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax125.spines['top'].set_position(('outward', axis5))
ax125.spines['top'].set_color('c')
ax125.plot(mnco3, depth, 'co-',mnco3, depth, 'co-') 
ax125.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax125.set_xlim([0, sed_mnco3max])
ax125.set_xticks(np.arange(0,sed_mnco3max+sed_mnco3max/2.,sed_mnco3max/2.))
ax125.set_ylim([y3max, y3min])
ax125.annotate(r'$\rm MnCO _3 $', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='c')


#fill the font 
#wat
ax1.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax2.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax3.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax4.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
#bbl
ax5.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax5.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
ax6.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax6.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax7.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax7.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax8.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax8.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
#sed
ax12.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed) 
ax12.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl) 
ax11.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax11.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax10.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax10.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax9.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax9.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)

####################################
############# Figure 2 ############# 
####################################
fig2 = plt.figure(figsize = (15,15))
#label_size = 13
#mpl.rcParams['xtick.labelsize'] = label_size
#mpl.rcParams['lines.linewidth'] = 2

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Fig 2 Water 1/1
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y1max, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_xticks(np.arange(0,phymax+phymax/2,phymax/2))
#Fig 2 Double water Phy
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

#Fig2 Water 3/1 
ax3 = plt.subplot(gs[2])
#Fig2 Water -  3/1 PO4
plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([y1max, 0])
ax3.set_xlim([0, po4max])
ax31 = ax3.twiny()
for spinename, spine in ax31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
#ax31.spines['top'].set_position(('outward', axis1))
ax31.spines['top'].set_color('g')
ax31.plot(po4, depth, 'g-',po4, depth, 'g-') 
ax31.set_xlim([0, po4max])
ax31.set_xticks(np.arange(0,po4max+po4max/4,po4max/4))
#ax31.set_xticks(np.arange(0,po4max+100,100))
ax31.annotate(r'$\rm PO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#Fig2 Water -  3/1 - pon
ax32 = ax3.twiny()
for spinename, spine in ax32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax32.spines['top'].set_position(('outward', axis2))
ax32.spines['top'].set_color('r')
ax32.plot(pon,depth,'r-',pon,depth,'r-') 
ax32.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax32.set_xlim([0,ponmax])
ax32.set_xticks(np.arange(0,ponmax+ponmax/4,ponmax/4))
ax32.set_ylim([y1max, 0])
ax32.annotate(r'$\rm PON $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')   
#Fig2 Water -  3/1 don 
ax33 = ax3.twiny()
for spinename, spine in ax33.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax33.spines['top'].set_position(('outward', axis3))
ax33.spines['top'].set_color('b')
ax33.plot(don, depth, 'b-',don, depth, 'b-') 
ax33.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax33.set_xlim([0, donmax])
ax33.set_xticks(np.arange(0,donmax+donmax/4,donmax/4))
ax33.set_ylim([y1max, 0])
ax33.annotate(r'$\rm DON $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')   

#Fig2 Water - 4/1 
ax4 = plt.subplot(gs[3])
#Fig2 Water -  4/1 FeII

plt.setp(ax4.get_xticklabels(), visible=False)
ax4.set_ylim([y1max, 0])
ax41 = ax4.twiny()
for spinename, spine in ax41.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax41.spines['top'].set_position(('outward', axis1))
ax41.spines['top'].set_color('g')
ax41.set_xlim([0, fe2max])
ax41.plot(fe2,depth,'g-',fe2,depth,'g-')
ax41.annotate(r'$\rm FeII $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#Fig2 Water -  4/1 - FeIII

ax42 = ax4.twiny()
for spinename, spine in ax42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax42.spines['top'].set_position(('outward', axis2))
ax42.spines['top'].set_color('r')
ax42.plot(fe3,depth,'r-',fe3,depth,'r-') 
ax42.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax42.set_xlim([0, fe3max])
#ax42.set_xticks(np.arange(0,fe3max+fe3max/2,fe3max/2))
#ax32.set_xticks(np.arange(0,1500,500))
ax42.set_ylim([y1max, 0])
ax42.annotate(r'$\rm FeIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')  
#Fig2 Water -  4/1 FeS
ax43 = ax4.twiny()
for spinename, spine in ax43.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax43.spines['top'].set_position(('outward', axis3))
ax43.spines['top'].set_color('b')
ax43.plot(fes, depth, 'b-',fes, depth, 'b-') 
ax43.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax43.set_xlim([0, fesmax])
ax43.set_ylim([y1max, 0])
ax43.annotate(r'$\rm FeS $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')  
#Fig2 Water - 4/1 FeS2
ax44 = ax4.twiny()
for spinename, spine in ax44.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax44.spines['top'].set_position(('outward', axis4))
ax44.spines['top'].set_color('m')
ax44.plot(fes2, depth, 'm-',fes2, depth, 'm-') 
ax44.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax44.set_xlim([0, fes2max])
ax44.set_ylim([y1max, 0])
ax44.annotate(r'$\rm FeS _2 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 


##Fig2  BBL 1/2
 #Fig2  BBL 1/2 - Phyto
ax5 = plt.subplot(gs[4])
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
ax6 = plt.subplot(gs[5])
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

##Fig2 BBL 3/2
ax7 = plt.subplot(gs[6])
#Fig2 BBL 3/2 - PO4
ax7.plot(po4,depth,'go-',po4,depth,'go-')
#ax7.set_ylabel('Depth (m)')
plt.setp(ax7.get_xticklabels(), visible=False)
ax7.set_xlim([0,po4max])
ax7.set_xticks(np.arange(0,po4max+po4max/4,po4max/4))
ax7.set_ylim([y2max, y2min])
#Fig2  3/2 - PON
ax72 = ax7.twiny()
ax72.plot(pon, depth, 'ro-',pon, depth, 'ro-') 
ax72.set_xlim([0, ponmax])
ax72.set_xticks(np.arange(0,ponmax+ponmax/4,ponmax/4))
ax72.set_ylim([y2max, y2min])
plt.setp(ax72.get_xticklabels(), visible=False)
#Fig2 BBL 3\2 - don
ax73 = ax7.twiny()
ax73.plot(don, depth, 'b-',don, depth, 'b-') 
ax73.set_xlim([0, donmax])
ax73.set_xticks(np.arange(0,donmax+donmax/4,donmax/4))
ax73.set_ylim([y2max, y2min])
plt.setp(ax73.get_xticklabels(), visible=False)

##Fig2 BBL - 4/2
ax8 = plt.subplot(gs[7])
#Fig2 BBL - 4/2 - Fe II
ax8.plot(fe2,depth,'go-',fe2,depth,'go-')
plt.setp(ax8.get_xticklabels(), visible=False)
ax8.set_xlim([0,fe2max])
ax8.set_ylim([y2max, y2min])

#Fig2 BBL - 4/2 - Fe III
ax82 = ax8.twiny()
ax82.plot(fe3, depth, 'ro-',fe3, depth, 'ro-') 
ax82.set_xlim([0, fe3max])
ax82.set_ylim([y2max, y2min])
plt.setp(ax82.get_xticklabels(), visible=False)
#Fig2 BBL 4\2 - FeS
ax83 = ax8.twiny()
ax83.plot(fes, depth, 'bo-',fes, depth, 'bo-') 
ax83.set_xlim([0, fesmax])
ax83.set_ylim([y2max, y2min])
plt.setp(ax83.get_xticklabels(), visible=False)
#Fig2 BBL - 4/2 fes2
ax84 = ax8.twiny()
ax84.plot(fes2, depth, 'mo-',fes2, depth, 'mo-') 
ax84.set_xlim([0, fes2max])
ax84.set_ylim([y2max, y2min])
plt.setp(ax84.get_xticklabels(), visible=False)

gs1 = gridspec.GridSpec(1, 4)
gs1.update(left=0.08, right=0.92, top = 0.28, bottom = 0.04, wspace=0.35,hspace=0.02)

#Fig2 Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (m)')
plt.setp(ax9.get_xticklabels(), visible=False)
ax9.set_xticks(np.arange(0,sed_phymax+sed_phymax,sed_phymax))
# draw minor gridlines and ticks in scalar mode
ax9.yaxis.set_major_locator(majorLocator)
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
ax91.plot(phy, depth, 'go-',phy, depth, 'go-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([0, phymax])
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
ax92.plot(het, depth, 'ro-',het, depth, 'ro-') 
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
ax101.plot(baan,depth,'go-',baan,depth,'go-')
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
ax102.plot(bhan,depth,'ro-',bhan,depth,'ro-') 
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
ax103.plot(bhae, depth, 'bo-',bhae, depth, 'bo-') 
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
ax104.plot(baae, depth, 'mo-',baae, depth, 'mo-') 
ax104.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax104.set_xlim([0, sed_baaemax])
ax104.set_xticks(np.arange(0,sed_baaemax+(sed_baaemax/2),(sed_baaemax/2)))
ax104.set_ylim([y3max, y3min])
ax104.annotate(r'$\rm Baae $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#Fig2 Sediment - 3/3 PO4
ax11 = plt.subplot(gs1[0,2])
#ax11.plot(po4,depth,'go-',po4,depth,'go-')
#ax3.set_ylabel('Depth (m)')
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([y3max, y3min])
# draw minor gridlines
ax11.yaxis.set_major_locator(majorLocator)
ax11.yaxis.set_major_formatter(majorFormatter)
ax11.yaxis.set_minor_locator(minorLocator)
ax11.yaxis.grid(True,'minor')
ax11.yaxis.grid(True,'major')  
ax11.set_xlim([0, sed_ponmax])
ax11.set_xticks(np.arange(0,sed_ponmax+sed_ponmax/4,sed_ponmax/4))
ax111 = ax11.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('g')
ax111.plot(po4,depth,'go-',po4,depth,'go-')
ax111.set_xlim([0, sed_po4max])
ax111.set_xticks(np.arange(0,sed_po4max+sed_po4max/4,sed_po4max/4))
ax111.annotate(r'$\rm PO _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig2 Sediment -  3/3 - PON
ax112 = ax11.twiny()
for spinename, spine in ax112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax112.spines['top'].set_position(('outward', axis2))
ax112.spines['top'].set_color('r')
ax112.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax112.plot(pon,depth,'ro-',pon,depth,'ro-') 
ax112.set_xlim([0, sed_ponmax])
ax112.set_xticks(np.arange(0,sed_ponmax+sed_ponmax/2,sed_ponmax/2))
ax112.set_ylim([y3max, y3min])
ax112.annotate(r'$\rm PON $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig2 Sediment -  3/3 don 
ax113 = ax11.twiny()
for spinename, spine in ax113.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax113.spines['top'].set_position(('outward', axis3))
ax113.spines['top'].set_color('b')
ax113.plot(don, depth, 'bo-',don, depth, 'bo-') 
ax113.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax113.set_xlim([0, sed_donmax])
ax113.set_xticks(np.arange(0,sed_donmax+sed_donmax/2,sed_donmax/2))
ax113.set_ylim([y3max, y3min])
ax113.annotate(r'$\rm DON $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig2 Sediment - 4/3 
ax12 = plt.subplot(gs1[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
ax12.yaxis.set_major_locator(majorLocator)
ax12.yaxis.set_major_formatter(majorFormatter)
ax12.yaxis.set_minor_locator(minorLocator)
ax12.yaxis.grid(True,'minor')
ax12.yaxis.grid(True,'major')   
ax121 = ax12.twiny()
ax121.plot(fe2,depth,'go-',fe2,depth,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_fe2max])
ax121.annotate(r'$\rm FeII $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#Fig2 Sediment - 4/3 - fe III
ax122 = ax12.twiny()
for spinename, spine in ax122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax122.spines['top'].set_position(('outward', axis2))
ax122.spines['top'].set_color('r')
ax122.plot(fe3,depth,'ro-',fe3,depth,'ro-') 
ax122.xaxis.set_label_position('top') # this moves the label to the top
ax122.set_xlim([0, sed_fe3max])
ax122.set_xticks(np.arange(0,sed_fe3max+sed_fe3max/5,sed_fe3max/5))
#ax32.set_xticks(np.arange(0,1500,500))
ax122.set_ylim([y3max, y3min])
ax122.annotate(r'$\rm FeIII $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 
#Fig2 Sediment - 4/3 FeS
ax123 = ax12.twiny()
for spinename, spine in ax123.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax123.spines['top'].set_position(('outward', axis3))
ax123.spines['top'].set_color('b')
ax123.plot(fes, depth, 'bo-',fes, depth, 'bo-') 
ax123.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax123.set_xlim([0, sed_fesmax])
ax123.set_ylim([y3max, y3min])
ax123.annotate(r'$\rm FeS $', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#Fig2 Sediment - 4/3 fes2
ax124 = ax12.twiny()
for spinename, spine in ax124.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax124.spines['top'].set_position(('outward', axis4))
ax124.spines['top'].set_color('m')
ax124.plot(fes2, depth, 'mo-',fes2, depth, 'mo-') 
ax124.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax124.set_xlim([0, sed_fes2max])
ax124.set_ylim([y3max, y3min])
ax124.annotate(r'$\rm FeS _2 $', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 


#fill the font 
#wat
ax1.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax2.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax3.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax4.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
#bbl
ax5.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax5.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
ax6.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax6.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax7.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax7.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax8.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax8.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
#sed
ax12.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed) 
ax12.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl) 
ax11.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax11.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax10.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax10.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax9.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax9.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)

####################################
############# Figure 3 ############# 
####################################
fig3 = plt.figure(figsize = (15,15))
#fig3.set_facecolor('w')
gs2 = gridspec.GridSpec(2, 4)  #determine grid of subplots (BBL and Water)
gs2.update(left=0.08, right=0.92,top = 0.86,bottom = 0.4, wspace=0.35,hspace=0.02)
label_size = 13
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['lines.linewidth'] = 2

# Water 1/1
ax1 = plt.subplot(gs2[0])
#fig 3 Water 1/1 pH
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y1max, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_xlim([phmin, phmax]) 
ax1.set_xticks(np.arange(phmin,phmax+((phmax-phmin)/3),(phmax-phmin)/3))
#fig 3 water pH
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('b')
ax11.plot(ph, depth, 'b-',ph, depth, 'b-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax11.set_xlim([phmin, phmax])
#ax11.set_xticks(np.arange(phmin,phmax+(phmax/3),phmax/3))
ax11.set_xticks(np.arange(phmin,phmax+((phmax-phmin)/3),(phmax-phmin)/3))
ax11.set_ylim([y1max, 0])
ax11.annotate(r'$\rm pH $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')
#fig 3 Water pCO2
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', axis2))
ax12.spines['top'].set_color('r')
ax12.plot(pco2, depth, 'r-',pco2, depth, 'r-') 
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xticks(np.arange(0,pco2max+pco2max/4,pco2max/4))
ax12.set_xlim([0, pco2max])
ax12.set_ylim([y1max, 0])
ax12.annotate(r'$\rm pCO _2 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')
                    
#fig 3 Water 2/1   
ax2 = plt.subplot(gs2[1])
#fig 3 Water - 2/1 Alk
ax2.set_ylim([y1max, 0])
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.set_xlim([alkmin, alkmax])
ax2.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
#ax2.set_xticks(np.arange(20000,so4max,2000))
ax21 = ax2.twiny()
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)        
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.plot(alk,depth,'g-',alk,depth,'g-')
ax21.set_xlim([alkmin, alkmax])
ax21.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
ax21.annotate(r'$\rm Alk $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#fig 3 Water -  2/1 DIC
ax22 = ax2.twiny()
for spinename, spine in ax22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax22.spines['top'].set_position(('outward', axis2))
ax22.spines['top'].set_color('m')
ax22.plot(dic,depth,'m-',dic,depth,'m-') 
ax22.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax22.set_xlim([dicmin, dicmax ])
ax22.set_xticks(np.arange(dicmin,dicmax+((dicmax - dicmin)/2),((dicmax - dicmin)/2)))
ax22.set_ylim([y1max, 0])
ax21.annotate(r'$\rm DIC $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m')

#fig 3 Water 3/1 
ax3 = plt.subplot(gs2[2])
#fig 3 Water -  3/1 CH4
plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([y1max, 0])
ax3.set_xlim([0, ch4max])
ax3.set_xticks(np.arange(0,ch4max+ch4max/5,ch4max/5))
ax31 = ax3.twiny()
for spinename, spine in ax31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
#ax31.spines['top'].set_position(('outward', axis1))
ax31.spines['top'].set_color('b')
ax31.plot(ch4, depth, 'b-',ch4, depth, 'b-') 
ax31.set_xlim([0, ch4max])
ax31.set_xticks(np.arange(0,ch4max+ch4max/5,ch4max/5))
#ax31.set_xticks(np.arange(0,po4max+100,100))
ax31.annotate(r'$\rm CH _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b')

#fig 3 Water -  3/1 - Om_ar
ax32 = ax3.twiny()
for spinename, spine in ax32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax32.spines['top'].set_position(('outward', axis2))
ax32.spines['top'].set_color('r')
ax32.plot(om_ar,depth,'r-',om_ar,depth,'r-') 
ax32.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax32.set_xlim([0,om_armax])
ax32.set_xticks(np.arange(0,om_armax+om_armax/5,om_armax/5))
ax32.set_ylim([y1max, 0])
ax32.annotate(r'$\rm \Omega Ar $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r')  

#fig 3 Water - 4/1 
ax4 = plt.subplot(gs2[3])
#fig 3 Water -  4/1 Si
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.set_ylim([y1max, 0])
ax4.set_xticks(np.arange(0,si_partmax+si_partmax,si_partmax))
ax41 = ax4.twiny()
for spinename, spine in ax41.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax41.spines['top'].set_position(('outward', axis1))
ax41.spines['top'].set_color('g')
ax41.set_xlim([0, simax])
ax41.set_xticks(np.arange(0,simax+simax/2,simax/2))
ax41.plot(si,depth,'g-',si,depth,'g-')
ax41.annotate(r'$\rm Si $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g')

#fig 3 Water -  4/1 - Si_part
ax42 = ax4.twiny()
for spinename, spine in ax42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax42.spines['top'].set_position(('outward', axis2))
ax42.spines['top'].set_color('m')
ax42.plot(si_part,depth,'m-',si_part,depth,'m-') 
ax42.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax42.set_xlim([0, si_partmax])
ax42.set_xticks(np.arange(0,2*si_partmax,si_partmax))
#ax42.set_xticks(np.arange(0,fe3max+fe3max/2,fe3max/2))
ax42.set_ylim([y1max, 0])
ax42.annotate(r'$\rm Si part $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 

##fig 3  BBL 1/2
 #fig 3  BBL 1/2 - pH
ax5 = plt.subplot(gs2[4])
ax5.plot(ph,depth,'bo-',ph,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([phmin, phmax])
ax5.set_xticks(np.arange(phmin,phmax+((phmax-phmin)/4),(phmax-phmin)/4))
ax5.set_ylim([y2max, y2min])
#fig 3 BBL 1/2 - pco2
ax52 = ax5.twiny()
ax52.plot(pco2, depth, 'ro-',pco2, depth, 'ro-') 
ax52.set_xlim([0, pco2max])
ax52.set_xticks(np.arange(0,pco2max+((pco2max)/4),(pco2max)/4))
ax52.set_ylim([y2max, y2min])
plt.setp(ax52.get_xticklabels(), visible=False)


#fig 3  BBL 2/2 
ax6 = plt.subplot(gs2[5])
#fig 3  BBL - alk
ax6.plot(alk,depth,'go-',alk,depth,'go-')
ax6.set_xlim([alkmin, alkmax])
ax6.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
ax6.set_ylim([y2max, y2min])
plt.setp(ax6.get_xticklabels(), visible=False)
#fig 3 BBL -  2/2 dic
ax62 = ax6.twiny()
ax62.plot(dic, depth, 'mo-',dic, depth, 'mo-') 
ax62.set_xlim([dicmin, dicmax])
ax62.set_xticks(np.arange(dicmin,dicmax+((dicmax - dicmin)/2),((dicmax - dicmin)/2)))
ax62.set_ylim([y2max, y2min])
plt.setp(ax62.get_xticklabels(), visible=False)

##fig 3 BBL 3/2
ax7 = plt.subplot(gs2[6])
#fig 3 BBL 3/2 - ch4
ax7.plot(ch4,depth,'bo-',ch4,depth,'bo-')
plt.setp(ax7.get_xticklabels(), visible=False)
ax7.set_xlim([0,ch4max])
ax7.set_ylim([y2max, y2min])
#fig 3  3/2 - om_ar
ax72 = ax7.twiny()
ax72.plot(om_ar, depth, 'ro-',om_ar, depth, 'ro-') 
ax72.set_xlim([0, om_armax])
ax72.set_ylim([y2max, y2min])
plt.setp(ax72.get_xticklabels(), visible=False)


##fig 3 BBL - 4/2
ax8 = plt.subplot(gs2[7])
#fig 3 BBL - 4/2 - Si
ax8.plot(si,depth,'go-',si,depth,'go-')
plt.setp(ax8.get_xticklabels(), visible=False)
ax8.set_xlim([0,simax])
ax8.set_xticks(np.arange(0,simax+simax/2,simax/2))
ax8.set_ylim([y2max, y2min])

#fig 3 BBL - 4/2 - Si_part
ax82 = ax8.twiny()
ax82.plot(si_part, depth, 'mo-',si_part, depth, 'mo-') 
ax82.set_xlim([0, si_partmax])
ax82.set_xticks(np.arange(0,si_partmax+si_partmax,si_partmax))
ax82.set_ylim([y2max, y2min])
plt.setp(ax82.get_xticklabels(), visible=False)




gs2 = gridspec.GridSpec(1, 4)
gs2.update(left=0.08, right=0.92, top = 0.34, bottom = 0.10, wspace=0.35,hspace=0.02)

#fig 3 Sediment - 1/3 
ax9 = plt.subplot(gs2[0,0])
ax9.set_ylabel('Depth (m)')
plt.setp(ax9.get_xticklabels(), visible=False)
# draw minor gridlines and ticks in scalar mode
ax9.yaxis.set_major_locator(majorLocator)
ax9.yaxis.set_major_formatter(majorFormatter)
ax9.yaxis.set_minor_locator(minorLocator)
ax9.yaxis.grid(True,'minor')
ax9.yaxis.grid(True,'major')
ax9.set_xticks(np.arange(sed_phmin,sed_phmax+((sed_phmax-sed_phmin)/4),(sed_phmax-sed_phmin)/4))
ax9.set_xlim([sed_phmin, sed_phmax])
#fig 3 sediment  1/3 pH
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('b')
ax91.plot(ph, depth, 'bo-',ph, depth, 'bo-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([sed_phmin, sed_phmax])
ax91.set_xticks(np.arange(sed_phmin,sed_phmax+((sed_phmax-sed_phmin)/4),(sed_phmax-sed_phmin)/4))
#ax91.set_xticks(np.arange(sed_phmin,sed_phmax+(sed_phmax/3),sed_phmax/3))
ax91.set_ylim([y3max, y3min])
ax91.annotate(r'$\rm pH $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#fig 3 Sediment - 1/3 pco2
ax92 = ax9.twiny()
for spinename, spine in ax92.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax92.spines['top'].set_position(('outward', axis2))
ax92.spines['top'].set_color('r')
ax92.plot(pco2, depth, 'ro-',pco2, depth, 'ro-') 
ax92.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax92.set_xlim([0, sed_pco2max])
ax92.set_xticks(np.arange(0,sed_pco2max+sed_pco2max/4,sed_pco2max/4))
ax92.set_ylim([y3max, y3min])
ax92.annotate(r'$\rm pCO _2 $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 

            
#fig 3 Sediment - 2/3 
ax10 = plt.subplot(gs2[0, 1])
ax10.set_ylim([y3max, y3min])
# draw minor gridlines and ticks in scalar mode
ax10.yaxis.set_major_locator(majorLocator)
ax10.yaxis.set_major_formatter(majorFormatter)
ax10.yaxis.set_minor_locator(minorLocator)
ax10.yaxis.grid(True,'minor')
ax10.yaxis.grid(True,'major')

plt.setp(ax10.get_xticklabels(), visible=False)
ax10.set_xlim([sed_dicmin, sed_dicmax])
ax10.set_xticks(np.arange(sed_dicmin,sed_dicmax+((sed_dicmax - sed_dicmin)),((sed_dicmax - sed_dicmin))))

#fig 3 Sediment - 2/3 alk
ax101 = ax10.twiny()
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.plot(alk,depth,'go-',alk,depth,'go-')
ax101.set_xlim([sed_alkmin, sed_alkmax])
ax101.set_xticks(np.arange(sed_alkmin,sed_alkmax+((sed_alkmax - sed_alkmin)/2),((sed_alkmax - sed_alkmin)/2)))
#ax101.set_xticks(np.arange(alkmin,alkmax+((alkmax - alkmin)/2),((alkmax - alkmin)/2)))
ax101.annotate(r'$\rm Alk $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#fig 3 sediment -  2/3 dic
ax102 = ax10.twiny()
for spinename, spine in ax102.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax102.spines['top'].set_position(('outward', axis2))
ax102.spines['top'].set_color('m')
ax102.plot(dic,depth,'mo-',dic,depth,'mo-') 
ax102.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax102.set_xlim([sed_dicmin, sed_dicmax])
ax102.set_xticks(np.arange(sed_dicmin,sed_dicmax+((sed_dicmax - sed_dicmin)/2),((sed_dicmax - sed_dicmin)/2)))
ax102.set_ylim([y3max, y3min])
ax102.annotate(r'$\rm DIC $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = xlabel_fontsize,
            color='m') 

#fig 3 Sediment 
ax11 = plt.subplot(gs2[0,2])

#ax3.set_ylabel('Depth (m)')
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([y3max, y3min])
# draw minor gridlines
ax11.yaxis.set_major_locator(majorLocator)
ax11.yaxis.set_major_formatter(majorFormatter)
ax11.yaxis.set_minor_locator(minorLocator)
ax11.yaxis.grid(True,'minor')
ax11.yaxis.grid(True,'major')

#grid(b=True, which='minor', color='r', linestyle='--')
ax11.set_xlim([0, ch4max])
#fig 3 Sediment - 3/3 ch4
ax111 = ax11.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('b')
ax111.plot(ch4,depth,'bo-',ch4,depth,'bo-')
ax111.set_xlim([0, sed_ch4max])
ax111.set_xticks(np.arange(0,sed_ch4max+sed_ch4max/5,sed_ch4max/5))
#ax111.set_xticks(np.arange(0,sed_o2max+100,100))
ax111.annotate(r'$\rm CH _4 $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='b') 
#fig 3 Sediment -  3/3 - om_ar
ax112 = ax11.twiny()
for spinename, spine in ax112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax112.spines['top'].set_position(('outward', axis2))
ax112.spines['top'].set_color('r')
ax112.plot(om_ar,depth,'ro-',om_ar,depth,'ro-') 
ax112.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax112.set_xlim([0, sed_om_armax])
ax112.set_xticks(np.arange(0,sed_om_armax+sed_om_armax/5,sed_om_armax/5))
ax112.set_ylim([y3max, y3min])
ax112.annotate(r'$\rm \Omega Ar $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='r') 

            
#fig 3 Sediment - 4/3 Si
ax12 = plt.subplot(gs2[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([y3max, y3min])
# draw minor gridlines
ax12.yaxis.set_major_locator(majorLocator)
ax12.yaxis.set_major_formatter(majorFormatter)
ax12.yaxis.set_minor_locator(minorLocator)
ax12.yaxis.grid(True,'minor')
ax12.yaxis.grid(True,'major')

#ax12.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax12.set_xticks(np.arange(0,sed_si_partmax+sed_si_partmax,sed_si_partmax))
 # This makes axis label to be written in full scalar mode
ax12.yaxis.set_major_formatter(y_formatter) # ( not exp as default)   
ax121 = ax12.twiny()
ax121.plot(si,depth,'go-',si,depth,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_simax])
ax121.set_xticks(np.arange(0,sed_simax+sed_simax/2,sed_simax/2))
ax121.annotate(r'$\rm Si $', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='g') 
#fig 3 Sediment - 4/3 - si_part
ax122 = ax12.twiny()
for spinename, spine in ax122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax122.spines['top'].set_position(('outward', axis2))
ax122.spines['top'].set_color('m')
ax122.plot(si_part,depth,'mo-',si_part,depth,'mo-') 
ax122.xaxis.set_label_position('top') # this moves the label to the top
ax122.set_xlim([0, sed_si_partmax])
ax122.set_xticks(np.arange(0,sed_si_partmax+sed_si_partmax,sed_si_partmax))
ax122.set_ylim([y3max, y3min])
ax122.annotate(r'$\rm Si part $', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = xlabel_fontsize,
            color='m') 
#fill the font 
#wat
ax1.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax2.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax3.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
ax4.fill_between(xticks, y1max, y1min, facecolor= wat_color, alpha=alpha_wat) 
#bbl
ax5.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax5.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
ax6.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax6.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax7.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax7.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl)
ax8.fill_between(xticks, y2max_fill_water, y2min, facecolor= wat_color, alpha=alpha_wat) 
ax8.fill_between(xticks, y2max, y2min_fill_bbl, facecolor= bbl_color, alpha=alpha_bbl) 
#sed
ax12.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed) 
ax12.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl) 
ax11.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax11.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax10.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax10.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)
ax9.fill_between(xticks, y3max, y3min_fill_sed, facecolor= sed_color, alpha=alpha_sed)
ax9.fill_between(xticks, y3max_fill_bbl, y3min, facecolor= bbl_color, alpha=alpha_bbl)

# save the figure to file
fig1.savefig('fig1O2H2S.png')   
fig2.savefig('fig2PhyHet.png')
fig3.savefig('fig3pHDIC.png')


plt.show()

plt.close(fig1)
plt.close(fig2)
#plt.close(fig3)