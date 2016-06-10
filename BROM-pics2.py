import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl


style.use('ggplot')

values=[]                                  # create empty matrix for storing data
f = open('output_240_day.dat', 'rb')       #open model output file, 'read binary' 

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

#Variables to plot:
depth = data[2][2:]
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

#limits for Water,BBL, and Sediment
#y2max = 107
#ymin_sed = 109.00
#ymax_sed = 109.1

y1max = y2min = 108.5
y2max = 110
y3min = 109.97
y3max = 110.09
yticksmin = 110 
yticksmax = 110.09

#limits for x   WatBBL axes:
kzmin = 0
kzmax = 0.05
salmin = 30
salmax = 36
tempmin = 5
tempmax = 25
so4min = 10000
so4max = 30000
h2smax = 2000
s0max = 250
s2o3max = 200 
o2max = 400
nh4max = 10
no2max = 1
no3max = 100
mnco3max = 1
mnsmax = 0.5
mn4max = 1
mn3max = 0.5
mn2max = 1
phymax = 1
hetmax = 1
baaemax = 1
bhaemax = 1
bhanmax = 1
baanmax = 1
nh4max = 50
ponmax = 20
donmax = 20
po4max = 20
fes2max = 5
fesmax = 5
fe3max = 5
fe2max = 5 
ch4max = 1
dicmax = 10
alkmax = 10
si = data[32][2:] 
si_part = data[33][2:]

#limits for x Sediment axes:
sed_kz = 1
sed_tempmin = 5
sed_tempmax = 25
sed_salmin = 30
sed_salmax = 36
sed_so4min = 10000
sed_so4max = 30000
sed_h2smax = 2000
sed_s0max = 250
sed_s2o3max = 200 
sed_o2max = 250
sed_nh4max = 1600
sed_no2max = 1
sed_no3max = 50
sed_mnco3max = 150
sed_mnsmax = 5
sed_mn4max = 20
sed_mn3max = 5
sed_mn2max = 50
sed_phymax = 10
sed_hetmax = 10
sed_baaemax = 10
sed_bhaemax = 10
sed_bhanmax = 50
sed_baanmax = 50
sed_ponmax = 200
sed_donmax = 200
sed_po4max = 200
sed_fes2max = 250
sed_fesmax = 100
sed_fe3max = 100
sed_fe2max = 100
sed_ch4max = 10
sed_dicmax = 10
sed_alkmax = 10

#positions for axes
axis1 = 0
axis2 = 25
axis3 = 50
axis4 = 75
axis5 = 100

labelaxis_x =  1.10
labelaxis1_y = 1.02
labelaxis2_y = 1.14
labelaxis3_y = 1.25
labelaxis4_y = 1.38
labelaxis5_y = 1.50


fig1 = plt.figure(figsize = (15,13))
rect = 1,1,3,3
fig1.add_axes(rect, label='axes1')

gs = gridspec.GridSpec(2, 4)  #determine grid of subplots (BBL and Water)
gs.update(left=0.08, right=0.92,top = 0.85,bottom = 0.4, wspace=0.65,hspace=0.02)

xlabel_size = 13
ylabel_size = 13
mpl.rcParams['xtick.labelsize'] = xlabel_size
mpl.rcParams['ytick.labelsize'] = ylabel_size
mpl.rcParams['lines.linewidth'] = 2

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Water 
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y2min, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
#Fig1  water Kz
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
ax11.plot(kz, depth, 'g-',kz, depth, 'g-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax11.set_xlim([kzmin, kzmax])
ax11.set_ylim([y1max, 0])

#ticklabelpad = mpl.rcParams['xtick.major.pad']
ax11.annotate('Kz', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax12.set_ylim([y1max, 0])
ax12.annotate('S', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax13.annotate('T', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')                           
#Fig1 Water 2/1   
ax2 = plt.subplot(gs[1])
ax2.set_ylim([y2min, 0])
plt.setp(ax2.get_xticklabels(), visible=False)
#Fig1 Water - 2/1 SO4
ax21 = ax2.twiny()
ax21.plot(so4,depth,'g-',so4,depth,'g-')
ax21.set_xlim([so4min, so4max])
ax21.set_xticks(np.arange(so4min,so4max+((so4max -so4min)/2),((so4max -so4min)/2)))
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.annotate('SO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax22.set_ylim([y1max, 0])
ax21.annotate('S0', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r')
#Fig1 Water -  2/1 H2S
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', axis3))
ax23.spines['top'].set_color('b')
ax23.plot(h2s, depth, 'b-',h2s, depth, 'b-') 
ax23.annotate('H2S', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')
ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, h2smax])
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
ax24.set_xlim([0, s2o3max])

ax24.set_ylim([y1max, 0])
ax24.annotate('S2O3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m')            

#Fig1 Water 3/1 
ax3 = plt.subplot(gs[2])
#Fig1 Water -  3/1 O2

plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([y1max, 0])
ax31 = ax3.twiny()
for spinename, spine in ax31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax31.spines['top'].set_position(('outward', axis1))
ax31.spines['top'].set_color('g')
ax31.plot(o2, depth, 'g-',o2, depth, 'g-') 
ax31.set_xlim([0, o2max])
#ax31.set_xticks(np.arange(0,o2max+100,100))
ax31.set_xticks(np.arange(0,o2max+o2max/4,o2max/4))
ax31.annotate('O2', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax32.set_xticks(np.arange(0,nh4max+nh4max/4,nh4max/4))
ax32.set_ylim([y1max, 0])
ax32.annotate('NH4', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax33.set_ylim([y1max, 0])
ax33.annotate('NO2', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax34.set_ylim([y1max, 0])
ax34.annotate('NO3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax41.annotate('MnII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
#ax32.set_xticks(np.arange(0,1500,500))
ax42.set_ylim([y1max, 0])
ax42.annotate('MnIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax43.annotate('MnIV', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax44.annotate('MnS', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax45.annotate('MnCO3', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='c') 

##Fig1  BBL 1/2
##Fig1  BBL 1/2 - Temperature
ax5 = plt.subplot(gs[4])
ax5.plot(temp,depth,'bo-',temp,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([tempmin,tempmax])
ax5.set_ylim([y2max, y2min])
#Fig1 BBL 1/2 - Salinity
ax52 = ax5.twiny()
ax52.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax52.set_xlim([salmin, salmax])
ax52.set_ylim([y2max, y2min])
plt.setp(ax52.get_xticklabels(), visible=False)
#Fig1 BBL 1/2 Kz
ax53 = ax5.twiny()
ax53.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax53.set_xlim([kzmin, kzmax])
ax53.set_ylim([y2max, y2min])
plt.setp(ax53.get_xticklabels(), visible=False)


#Fig1  BBL 2/2 
ax6 = plt.subplot(gs[5])
#Fig1  BBL - SO4
ax6.plot(so4,depth,'go-',so4,depth,'go-')
ax6.set_xlim([so4min, so4max])
ax6.set_ylim([y2max, y2min])
plt.setp(ax6.get_xticklabels(), visible=False)
#Fig1 BBL -  2/2 S0
ax62 = ax6.twiny()
ax62.plot(s0, depth, 'ro-',s0, depth, 'ro-') 
ax62.set_xlim([-0.02, s0max])
ax62.set_ylim([y2max, y2min])
plt.setp(ax62.get_xticklabels(), visible=False)

#Fig1 BBL -  2/2 h2S
ax63 = ax6.twiny()
ax63.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
ax63.set_xlim([-0.02, h2smax])
ax63.set_ylim([y2max, y2min])
plt.setp(ax63.get_xticklabels(), visible=False)

#Fig1 BBL -  2/2 s2o3
ax64 = ax6.twiny()
ax64.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax64.set_xlim([-0.02, s2o3max])
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
#Fig1 BBL 3/2 - nh4
ax72 = ax7.twiny()
ax72.plot(nh4, depth, 'ro-',nh4, depth, 'ro-') 
ax72.set_xlim([0, nh4max])
ax72.set_ylim([y2max, y2min])
plt.setp(ax72.get_xticklabels(), visible=False)
#Fig1 BBL 3\2 - no2
ax73 = ax7.twiny()
ax73.plot(no2, depth, 'b-',no2, depth, 'b-') 
ax73.set_xlim([0, no2max])
ax73.set_ylim([y2max, y2min])
plt.setp(ax73.get_xticklabels(), visible=False)
#Fig1 BBL - 3/2 NO3
ax74 = ax7.twiny()
ax74.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax74.set_xlim([0, no3max])
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
gs1.update(left=0.08, right=0.92, top = 0.25, bottom = 0.05, wspace=0.65,hspace=0.9)

#Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (m)')
#ax9.ticklabel_format(axis='y', style='sci', scilimits=0,100))
plt.setp(ax9.get_xticklabels(), visible=False)

#Fig1 sediment Kz
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('g')
ax91.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([kzmin, kzmax])
ax91.set_ylim([y3max, y3min])
ax91.annotate('Kz', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax92.set_xlim([salmin, sed_salmax])
ax92.set_ylim([y3max, y3min])
ax92.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax92.annotate('S', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax93.annotate('T', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
#Fig1 Sediment - 2/3 
ax10 = plt.subplot(gs1[0, 1])
ax10.set_ylim([y3max, y3min])
ax10.set_yticks(np.arange(yticksmin,yticksmax,0.01))
plt.setp(ax10.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,so4max,2000))
ax101 = ax10.twiny()
ax101.plot(so4,depth,'go-',so4,depth,'go-')
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.set_xlim([sed_so4min, sed_so4max])
ax101.set_xticks(np.arange(sed_so4min,sed_so4max + ((sed_so4max - sed_so4min)/2),((sed_so4max - sed_so4min)/2)))
ax101.annotate('SO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax102.set_ylim([y3max, y3min])
ax101.annotate('SO', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = 14,
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
ax103.set_ylim([y3max, y3min])
ax103.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax103.annotate('H2S', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax104.set_ylim([y3max, y3min])
ax104.annotate('S2O3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 
#Fig1 Sediment - 3/3
ax11 = plt.subplot(gs1[0,2])
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([y3max, y3min])
ax11.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax111 = ax11.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('g')
ax111.plot(o2,depth,'go-',o2,depth,'go-')
ax111.set_xlim([0, sed_o2max])
#ax111.set_xticks(np.arange(0,sed_o2max+100,100))
ax111.annotate('O2', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax112.set_xticks(np.arange(0,sed_nh4max+sed_nh4max/4,sed_nh4max/4))
ax112.set_ylim([y3max, y3min])
ax112.annotate('NH4', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax113.set_ylim([y3max, y3min])
ax113.annotate('NO2', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax114.set_ylim([y3max, y3min])
ax114.annotate('NO3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 
#Fig1 Sediment - 4/3 
ax12 = plt.subplot(gs1[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([y3max, y3min])
ax12.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax121 = ax12.twiny()
ax121.plot(mn2,depth,'go-',mn2,depth,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_mn2max])
ax121.annotate('MnII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
#ax32.set_xticks(np.arange(0,1500,500))
ax122.set_ylim([y3max, y3min])
ax122.annotate('MnIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax123.set_ylim([y3max, y3min])
ax123.annotate('MnIV', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax124.set_xticks(np.arange(0,sed_mnsmax+sed_mnsmax/2,sed_mnsmax/2))
ax124.set_ylim([y3max, y3min])
ax124.annotate('MnS', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax125.set_xlim([-0.1, sed_mnco3max])
ax125.set_xticks(np.arange(0,sed_mnco3max+sed_mnco3max,sed_mnco3max))
ax125.set_ylim([y3max, y3min])
ax125.annotate('MnCO3', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='c') 


####################################
############# Figure 2 ############# 
####################################


fig2 = plt.figure(figsize = (15,13))

gs1 = gridspec.GridSpec(2, 4)  #determine grid of subplots (BBL and Water)
gs1.update(left=0.08, right=0.92,top = 0.83,bottom = 0.4, wspace=0.65,hspace=0.05)

label_size = 13
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['lines.linewidth'] = 2

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Fig 2 Water 1/1
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y1max, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
#Fig 2 Double water Heterotrophs
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
ax11.plot(het, depth, 'g-',het, depth, 'g-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax11.set_xlim([0, hetmax])
ax11.set_ylim([y1max, 0])
ax11.annotate('Het', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g')
#Fig2 Water Phytoplankton
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', axis2))
ax12.spines['top'].set_color('r')
ax12.plot(phy, depth, 'r-',phy, depth, 'r-') 
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xlim([0, phymax])
ax12.set_ylim([y1max, 0])
ax12.annotate('Phy', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r')
                    
#Fig2 Water 2/1   
ax2 = plt.subplot(gs[1])
#Fig2 Water - 2/1 Bacteria autotropohic anaerobic Baan
ax2.set_ylim([y1max, 0])
plt.setp(ax2.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,so4max,2000))
ax21 = ax2.twiny()
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)        
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.plot(baan,depth,'g-',baan,depth,'g-')
ax21.set_xlim([0, baanmax])
ax21.annotate('Baan', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax22.set_ylim([y1max, 0])
ax21.annotate('Bhan', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r')
#Fig2 Water -  2/1 Bacteria heterotropohic aerobic Bhae
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', axis3))
ax23.spines['top'].set_color('b')
ax23.plot(bhae, depth, 'b-',bhae, depth, 'b-') 
ax23.annotate('Bhae', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')
ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, bhaemax])
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
ax24.set_ylim([y1max, 0])
ax24.annotate('Baae', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax31.annotate('PO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax32.annotate('PON', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax33.annotate('DON', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')   
#Fig2 Water - 3/1 NO3
'''ax34 = ax3.twiny()
for spinename, spine in ax34.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax34.spines['top'].set_position(('outward', axis4))
ax34.spines['top'].set_color('m')
ax34.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax34.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax34.set_xlim([0, no3max])
ax34.set_ylim([y1max, 0])
ax34.annotate('NO3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m')   
'''
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
ax41.annotate('FeII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax42.annotate('FeIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax43.annotate('FeS', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax44.annotate('FeS2', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 

'''#Fig2 Water - 3/1 MnCO3
ax45 = ax4.twiny()
for spinename, spine in ax45.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax45.spines['top'].set_position(('outward', axis5))
ax45.spines['top'].set_color('y')
ax45.plot(mnco3, depth, 'yo-',mnco3, depth, 'yo-') 
#ax45.set_xlabel('MnCo3', color='y',) 
ax45.xaxis.set_label_position('top') # this moves the label to the top
ax45.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax45.set_xlim([0, mnco3max])
ax45.set_xticks(np.arange(0,mnco3max+mnco3max/2,mnco3max/2))
ax45.set_ylim([y1max, 0])
ax45.annotate('MnCO3', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='y') 
'''
##Fig2  BBL 1/2
 #Fig2  BBL 1/2 - Phyto
ax5 = plt.subplot(gs[4])
ax5.plot(phy,depth,'bo-',phy,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([0, phymax])
ax5.set_ylim([y2max, y2min])
#Fig2 BBL 1/2 - Het
ax52 = ax5.twiny()
ax52.plot(het, depth, 'ro-',het, depth, 'ro-') 
ax52.set_xlim([0, hetmax])
ax52.set_ylim([y2max, y2min])
plt.setp(ax52.get_xticklabels(), visible=False)
'''#Fig2 BBL 1/2 Kz
ax53 = ax5.twiny()
ax53.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax3.set_xlim([kzmin, kzmax])
ax53.set_ylim([y2max, y2min])
plt.setp(ax53.get_xticklabels(), visible=False)
'''

#Fig2  BBL 2/2 
ax6 = plt.subplot(gs[5])
#Fig2  BBL - Baan
ax6.plot(baan,depth,'go-',baan,depth,'go-')
ax6.set_xlim([0, baanmax])
ax6.set_ylim([y2max, y2min])
plt.setp(ax6.get_xticklabels(), visible=False)
#Fig2 BBL -  2/2 Bhan
ax62 = ax6.twiny()
ax62.plot(bhan, depth, 'ro-',bhan, depth, 'ro-') 
ax62.set_xlim([0, bhanmax])
ax62.set_ylim([y2max, y2min])
plt.setp(ax62.get_xticklabels(), visible=False)

#Fig2 BBL -  2/2 Bhae
ax63 = ax6.twiny()
ax63.plot(bhae, depth, 'bo-',bhae, depth, 'bo-') 
ax63.set_xlim([0, bhaemax])
ax63.set_ylim([y2max, y2min])
plt.setp(ax63.get_xticklabels(), visible=False)

#Fig2 BBL -  2/2 Bhan
ax64 = ax6.twiny()
ax64.plot(bhan, depth, 'mo-',bhan, depth, 'mo-') 
ax64.set_xlim([0, bhanmax])
ax64.set_ylim([y2max, y2min])
plt.setp(ax64.get_xticklabels(), visible=False)

##Fig2 BBL 3/2
ax7 = plt.subplot(gs[6])
#Fig2 BBL 3/2 - PO4
ax7.plot(po4,depth,'go-',po4,depth,'go-')
#ax7.set_ylabel('Depth (m)')
plt.setp(ax7.get_xticklabels(), visible=False)
ax7.set_xlim([0,po4max])
ax7.set_ylim([y2max, y2min])
#Fig2  3/2 - PON
ax72 = ax7.twiny()
ax72.plot(pon, depth, 'ro-',pon, depth, 'ro-') 
ax72.set_xlim([0, ponmax])
ax72.set_ylim([y2max, y2min])
plt.setp(ax72.get_xticklabels(), visible=False)
#Fig2 BBL 3\2 - don
ax73 = ax7.twiny()
ax73.plot(don, depth, 'b-',don, depth, 'b-') 
ax73.set_xlim([0, donmax])
ax73.set_ylim([y2max, y2min])
plt.setp(ax73.get_xticklabels(), visible=False)
#Fig2 BBL - 3/2 NO3
'''ax74 = ax7.twiny()
ax74.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax74.set_xlim([0, no3max])
ax74.set_ylim([y2max, y2min])
plt.setp(ax74.get_xticklabels(), visible=False)
'''

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
ax83.plot(fe3, depth, 'bo-',fe3, depth, 'bo-') 
ax83.set_xlim([0, fe3max])
ax83.set_ylim([y2max, y2min])
plt.setp(ax83.get_xticklabels(), visible=False)
#Fig2 BBL - 4/2 fes2
ax84 = ax8.twiny()
ax84.plot(fes2, depth, 'mo-',fes2, depth, 'mo-') 
ax84.set_xlim([0, fes2max])
ax84.set_ylim([y2max, y2min])
plt.setp(ax84.get_xticklabels(), visible=False)
'''#Fig2 BBL - 4/2 MnCO3
ax85 = ax8.twiny()
ax85.plot(mnco3, depth, 'yo-',mnco3, depth, 'yo-') 
ax85.set_xlim([-mnco3max, mnco3max])
ax85.set_ylim([y2max, y2min])
plt.setp(ax85.get_xticklabels(), visible=False)
'''
gs1 = gridspec.GridSpec(1, 4)
gs1.update(left=0.08, right=0.92, top = 0.25, bottom = 0.05, wspace=0.65,hspace=0.9)

#Fig2 Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (m)')
plt.setp(ax9.get_xticklabels(), visible=False)
ax9.set_yticks(np.arange(yticksmin,yticksmax,0.01))
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
ax91.set_ylim([y3max, y3min])
ax91.annotate('Phy', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax92.set_ylim([y3max, y3min])
ax92.annotate('Het', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r') 
'''#Fig2 Sediment 1/3 Phy
ax93 = ax9.twiny()
for spinename, spine in ax93.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax93.spines['top'].set_position(('outward', axis3))
ax93.spines['top'].set_color('b')
ax93.plot(phy,depth,'bo-',phy,depth,'bo-')
ax93.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax93.set_xlim([5, 14])
ax93.set_ylim([y3max, y3min])
ax93.annotate('Phy', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
            '''
#Fig2 Sediment - 2/3 Baan
ax10 = plt.subplot(gs1[0, 1])
ax10.set_ylim([y3max, y3min])
ax10.set_yticks(np.arange(yticksmin,yticksmax,0.01))
plt.setp(ax10.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,baanmax,2000))
ax101 = ax10.twiny()
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.plot(baan,depth,'go-',baan,depth,'go-')
ax101.set_xlim([0, sed_baanmax])
ax101.annotate('Baan', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax102.set_ylim([y3max, y3min])
ax102.annotate('Bhan', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = 14,
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
ax103.set_ylim([y3max, y3min])
ax103.annotate('Bhae', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax104.set_ylim([y3max, y3min])
ax104.annotate('Baae', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 
#Fig2 Sediment - 3/3 PO4
ax11 = plt.subplot(gs1[0,2])
#ax11.plot(po4,depth,'go-',po4,depth,'go-')
#ax3.set_ylabel('Depth (m)')
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([y3max, y3min])
ax11.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax11.set_xlim([0, po4max])
ax111 = ax11.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('g')
ax111.plot(po4,depth,'go-',po4,depth,'go-')
ax111.set_xlim([0, sed_po4max])
#ax111.set_xticks(np.arange(0,sed_o2max+100,100))
ax111.annotate('PO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g') 
#Fig2 Sediment -  3/3 - PON
ax112 = ax11.twiny()
for spinename, spine in ax112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax112.spines['top'].set_position(('outward', axis2))
ax112.spines['top'].set_color('r')
ax112.plot(pon,depth,'ro-',pon,depth,'ro-') 
ax112.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax112.set_xlim([0, sed_ponmax])
ax112.set_xticks(np.arange(0,sed_ponmax+sed_ponmax/4,sed_ponmax/4))
ax112.set_ylim([y3max, y3min])
ax112.annotate('PON', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax113.set_ylim([y3max, y3min])
ax113.annotate('DON', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
#Fig2 Sediment - 4/3 
ax12 = plt.subplot(gs1[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([y3max, y3min])
ax12.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax121 = ax12.twiny()
ax121.plot(fe2,depth,'go-',fe2,depth,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_fe2max])
ax121.annotate('FeII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
#ax32.set_xticks(np.arange(0,1500,500))
ax122.set_ylim([y3max, y3min])
ax122.annotate('FeIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax123.annotate('FeS', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
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
ax124.annotate('FeS2', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 

####################################
############# Figure 3 ############# 
####################################
fig3 = plt.figure(figsize = (15,13))

gs2 = gridspec.GridSpec(2, 4)  #determine grid of subplots (BBL and Water)
gs2.update(left=0.08, right=0.92,top = 0.83,bottom = 0.4, wspace=0.65,hspace=0.05)

label_size = 13
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['lines.linewidth'] = 2

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#fig 3 Water 1/1
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([y1max, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
#fig 3 water pH
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
ax11.plot(ch4, depth, 'g-',ch4, depth, 'g-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax11.set_xlim([0, hetmax])
ax11.set_ylim([y1max, 0])
ax11.annotate('Het', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g')
#fig 3 Water Phytoplankton
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', axis2))
ax12.spines['top'].set_color('r')
ax12.plot(phy, depth, 'r-',phy, depth, 'r-') 
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xlim([0, phymax])
ax12.set_ylim([y1max, 0])
ax12.annotate('Phy', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r')
                    
#fig 3 Water 2/1   
ax2 = plt.subplot(gs[1])
#fig 3 Water - 2/1 Bacteria autotropohic anaerobic Baan
ax2.set_ylim([y1max, 0])
plt.setp(ax2.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,so4max,2000))
ax21 = ax2.twiny()
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)        
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.plot(baan,depth,'g-',baan,depth,'g-')
ax21.set_xlim([0, baanmax])
ax21.annotate('Baan', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g')

#fig 3 Water -  2/1 Bacteria heterotropohic anaerobic Bhan
ax22 = ax2.twiny()
for spinename, spine in ax22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax22.spines['top'].set_position(('outward', axis2))
ax22.spines['top'].set_color('r')
ax22.plot(bhan,depth,'r-',bhan,depth,'r-') 
ax22.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax22.set_xlim([0, bhanmax ])
ax22.set_ylim([y1max, 0])
ax21.annotate('Bhan', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r')
'''
#fig 3 Water -  2/1 Bacteria heterotropohic aerobic Bhae
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', axis3))
ax23.spines['top'].set_color('b')
ax23.plot(bhae, depth, 'b-',bhae, depth, 'b-') 
ax23.annotate('Bhae', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')
ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, bhaemax])
ax23.set_ylim([y1max, 0])

#fig 3 Water - 2/1 Bacteria autotropohic aerobic Baae
ax24 = ax2.twiny()
for spinename, spine in ax24.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax24.spines['top'].set_position(('outward', axis4))
ax24.spines['top'].set_color('m')
ax24.plot(baae, depth, 'm-',baae, depth, 'm-') 
ax24.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax24.set_xlim([0, baaemax])
ax24.set_ylim([y1max, 0])
ax24.annotate('Baae', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m')            
'''
#fig 3 Water 3/1 
ax3 = plt.subplot(gs[2])
#fig 3 Water -  3/1 PO4
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
ax31.annotate('PO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g')

#fig 3 Water -  3/1 - pon
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
ax32.annotate('PON', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r')  
''' 
#fig 3 Water -  3/1 don 
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
ax33.annotate('DON', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')   
#fig 3 Water - 3/1 NO3

ax34 = ax3.twiny()
for spinename, spine in ax34.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax34.spines['top'].set_position(('outward', axis4))
ax34.spines['top'].set_color('m')
ax34.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax34.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax34.set_xlim([0, no3max])
ax34.set_ylim([y1max, 0])
ax34.annotate('NO3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m')   
'''
#fig 3 Water - 4/1 
ax4 = plt.subplot(gs[3])
#fig 3 Water -  4/1 FeII
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
ax41.annotate('FeII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g')

#fig 3 Water -  4/1 - FeIII
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
ax42.set_ylim([y1max, 0])
ax42.annotate('FeIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r') 
''' 
#fig 3 Water -  4/1 FeS
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
ax43.annotate('FeS', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b')  
#fig 3 Water - 4/1 FeS2
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
ax44.annotate('FeS2', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 


#fig 3 Water - 3/1 MnCO3
ax45 = ax4.twiny()
for spinename, spine in ax45.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax45.spines['top'].set_position(('outward', axis5))
ax45.spines['top'].set_color('y')
ax45.plot(mnco3, depth, 'yo-',mnco3, depth, 'yo-') 
#ax45.set_xlabel('MnCo3', color='y',) 
ax45.xaxis.set_label_position('top') # this moves the label to the top
ax45.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax45.set_xlim([0, mnco3max])
ax45.set_xticks(np.arange(0,mnco3max+mnco3max/2,mnco3max/2))
ax45.set_ylim([y1max, 0])
ax45.annotate('MnCO3', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='y') 
'''
##fig 3  BBL 1/2
 #fig 3  BBL 1/2 - Phyto
ax5 = plt.subplot(gs[4])
ax5.plot(phy,depth,'bo-',phy,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([0, phymax])
ax5.set_ylim([y2max, y2min])
#fig 3 BBL 1/2 - Het
ax52 = ax5.twiny()
ax52.plot(het, depth, 'ro-',het, depth, 'ro-') 
ax52.set_xlim([0, hetmax])
ax52.set_ylim([y2max, y2min])
plt.setp(ax52.get_xticklabels(), visible=False)
'''#fig 3 BBL 1/2 Kz
ax53 = ax5.twiny()
ax53.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax3.set_xlim([kzmin, kzmax])
ax53.set_ylim([y2max, y2min])
plt.setp(ax53.get_xticklabels(), visible=False)
'''

#fig 3  BBL 2/2 
ax6 = plt.subplot(gs[5])
#fig 3  BBL - Baan
ax6.plot(baan,depth,'go-',baan,depth,'go-')
ax6.set_xlim([0, baanmax])
ax6.set_ylim([y2max, y2min])
plt.setp(ax6.get_xticklabels(), visible=False)
#fig 3 BBL -  2/2 Bhan
ax62 = ax6.twiny()
ax62.plot(bhan, depth, 'ro-',bhan, depth, 'ro-') 
ax62.set_xlim([0, bhanmax])
ax62.set_ylim([y2max, y2min])
plt.setp(ax62.get_xticklabels(), visible=False)
'''
#fig 3 BBL -  2/2 Bhae
ax63 = ax6.twiny()
ax63.plot(bhae, depth, 'bo-',bhae, depth, 'bo-') 
ax63.set_xlim([0, bhaemax])
ax63.set_ylim([y2max, y2min])
plt.setp(ax63.get_xticklabels(), visible=False)

#fig 3 BBL -  2/2 Bhan
ax64 = ax6.twiny()
ax64.plot(bhan, depth, 'mo-',bhan, depth, 'mo-') 
ax64.set_xlim([0, bhanmax])
ax64.set_ylim([y2max, y2min])
plt.setp(ax64.get_xticklabels(), visible=False)
'''

##fig 3 BBL 3/2
ax7 = plt.subplot(gs[6])
#fig 3 BBL 3/2 - PO4
ax7.plot(po4,depth,'go-',po4,depth,'go-')
plt.setp(ax7.get_xticklabels(), visible=False)
ax7.set_xlim([0,po4max])
ax7.set_ylim([y2max, y2min])
#fig 3  3/2 - PON
ax72 = ax7.twiny()
ax72.plot(pon, depth, 'ro-',pon, depth, 'ro-') 
ax72.set_xlim([0, ponmax])
ax72.set_ylim([y2max, y2min])
plt.setp(ax72.get_xticklabels(), visible=False)
'''
#fig 3 BBL 3\2 - don
ax73 = ax7.twiny()
ax73.plot(don, depth, 'b-',don, depth, 'b-') 
ax73.set_xlim([0, donmax])
ax73.set_ylim([y2max, y2min])
plt.setp(ax73.get_xticklabels(), visible=False)
#fig 3 BBL - 3/2 NO3
ax74 = ax7.twiny()
ax74.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax74.set_xlim([0, no3max])
ax74.set_ylim([y2max, y2min])
plt.setp(ax74.get_xticklabels(), visible=False)
'''

##fig 3 BBL - 4/2
ax8 = plt.subplot(gs[7])
#fig 3 BBL - 4/2 - Fe II
ax8.plot(fe2,depth,'go-',fe2,depth,'go-')
plt.setp(ax8.get_xticklabels(), visible=False)
ax8.set_xlim([0,fe2max])
ax8.set_ylim([y2max, y2min])

#fig 3 BBL - 4/2 - Fe III
ax82 = ax8.twiny()
ax82.plot(fe3, depth, 'ro-',fe3, depth, 'ro-') 
ax82.set_xlim([0, fe3max])
ax82.set_ylim([y2max, y2min])
plt.setp(ax82.get_xticklabels(), visible=False)
'''
#fig 3 BBL 4\2 - FeS
ax83 = ax8.twiny()
ax83.plot(fe3, depth, 'bo-',fe3, depth, 'bo-') 
ax83.set_xlim([0, fe3max])
ax83.set_ylim([y2max, y2min])
plt.setp(ax83.get_xticklabels(), visible=False)
#fig 3 BBL - 4/2 fes2
ax84 = ax8.twiny()
ax84.plot(fes2, depth, 'mo-',fes2, depth, 'mo-') 
ax84.set_xlim([0, fes2max])
ax84.set_ylim([y2max, y2min])
plt.setp(ax84.get_xticklabels(), visible=False)
#fig 3 BBL - 4/2 MnCO3
ax85 = ax8.twiny()
ax85.plot(mnco3, depth, 'yo-',mnco3, depth, 'yo-') 
ax85.set_xlim([-mnco3max, mnco3max])
ax85.set_ylim([y2max, y2min])
plt.setp(ax85.get_xticklabels(), visible=False)
'''
gs2 = gridspec.GridSpec(1, 4)
gs2.update(left=0.08, right=0.92, top = 0.25, bottom = 0.05, wspace=0.65,hspace=0.9)

#fig 3 Sediment - 1/3 
ax9 = plt.subplot(gs2[0,0])
ax9.set_ylabel('Depth (m)')
plt.setp(ax9.get_xticklabels(), visible=False)
ax9.set_yticks(np.arange(yticksmin,yticksmax,0.01))
#fig 3 sediment  1/3 Phy
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('g')
ax91.plot(phy, depth, 'go-',phy, depth, 'go-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([0, phymax])
ax91.set_ylim([y3max, y3min])
ax91.annotate('Phy', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g') 
#fig 3 Sediment - 1/3 het
ax92 = ax9.twiny()
for spinename, spine in ax92.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax92.spines['top'].set_position(('outward', axis2))
ax92.spines['top'].set_color('r')
ax92.plot(het, depth, 'ro-',het, depth, 'ro-') 
ax92.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax92.set_xlim([0, sed_hetmax])
ax92.set_ylim([y3max, y3min])
ax92.annotate('Het', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r') 
'''#fig 3 Sediment 1/3 Phy
ax93 = ax9.twiny()
for spinename, spine in ax93.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax93.spines['top'].set_position(('outward', axis3))
ax93.spines['top'].set_color('b')
ax93.plot(phy,depth,'bo-',phy,depth,'bo-')
ax93.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax93.set_xlim([5, 14])
ax93.set_ylim([y3max, y3min])
ax93.annotate('Phy', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
            '''
            
#fig 3 Sediment - 2/3 Baan
ax10 = plt.subplot(gs2[0, 1])
ax10.set_ylim([y3max, y3min])
ax10.set_yticks(np.arange(yticksmin,yticksmax,0.01))
plt.setp(ax10.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,baanmax,2000))
ax101 = ax10.twiny()
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.plot(baan,depth,'go-',baan,depth,'go-')
ax101.set_xlim([0, sed_baanmax])
ax101.annotate('Baan', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g') 
#fig 3 sediment -  2/3 bhan
ax102 = ax10.twiny()
for spinename, spine in ax102.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax102.spines['top'].set_position(('outward', axis2))
ax102.spines['top'].set_color('r')
ax102.plot(bhan,depth,'ro-',bhan,depth,'ro-') 
ax102.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax102.set_xlim([0, sed_bhanmax])
ax102.set_ylim([y3max, y3min])
ax102.annotate('Bhan', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', fontsize = 14,
            color='r') 
'''
#fig 3 Sediment -  2/3 bhae
ax103 = ax10.twiny()
for spinename, spine in ax103.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax103.spines['top'].set_position(('outward', axis3))
ax103.spines['top'].set_color('b')
ax103.plot(bhae, depth, 'bo-',bhae, depth, 'bo-') 
ax103.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax103.set_xlim([0, sed_bhaemax])
ax103.set_ylim([y3max, y3min])
ax103.annotate('Bhae', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
#fig 3 Sediment - 2/3 baae
ax104 = ax10.twiny()
for spinename, spine in ax104.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax104.spines['top'].set_position(('outward', axis4))
ax104.spines['top'].set_color('m')
ax104.plot(baae, depth, 'mo-',baae, depth, 'mo-') 
ax104.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax104.set_xlim([0, sed_baaemax])
ax104.set_ylim([y3max, y3min])
ax104.annotate('Baae', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 
'''
#fig 3 Sediment - 3/3 PO4
ax11 = plt.subplot(gs2[0,2])
#ax11.plot(po4,depth,'go-',po4,depth,'go-')
#ax3.set_ylabel('Depth (m)')
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([y3max, y3min])
ax11.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax11.set_xlim([0, po4max])

ax111 = ax11.twiny()
for spinename, spine in ax111.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax111.spines['top'].set_position(('outward', axis1))
ax111.spines['top'].set_color('g')
ax111.plot(po4,depth,'go-',po4,depth,'go-')
ax111.set_xlim([0, sed_po4max])
#ax111.set_xticks(np.arange(0,sed_o2max+100,100))
ax111.annotate('PO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g') 
#fig 3 Sediment -  3/3 - PON
ax112 = ax11.twiny()
for spinename, spine in ax112.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax112.spines['top'].set_position(('outward', axis2))
ax112.spines['top'].set_color('r')
ax112.plot(pon,depth,'ro-',pon,depth,'ro-') 
ax112.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax112.set_xlim([0, sed_ponmax])
ax112.set_xticks(np.arange(0,sed_ponmax+sed_ponmax/4,sed_ponmax/4))
ax112.set_ylim([y3max, y3min])
ax112.annotate('PON', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r') 
'''
#fig 3 Sediment -  3/3 don 
ax113 = ax11.twiny()
for spinename, spine in ax113.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax113.spines['top'].set_position(('outward', axis3))
ax113.spines['top'].set_color('b')
ax113.plot(don, depth, 'bo-',don, depth, 'bo-') 
ax113.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax113.set_xlim([0, sed_donmax])
ax113.set_ylim([y3max, y3min])
ax113.annotate('DON', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
            '''
#fig 3 Sediment - 4/3 
ax12 = plt.subplot(gs2[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([y3max, y3min])
ax12.set_yticks(np.arange(yticksmin,yticksmax,0.01))
ax121 = ax12.twiny()
ax121.plot(fe2,depth,'go-',fe2,depth,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_fe2max])
ax121.annotate('FeII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='g') 
#fig 3 Sediment - 4/3 - fe III
ax122 = ax12.twiny()
for spinename, spine in ax122.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax122.spines['top'].set_position(('outward', axis2))
ax122.spines['top'].set_color('r')
ax122.plot(fe3,depth,'ro-',fe3,depth,'ro-') 
ax122.xaxis.set_label_position('top') # this moves the label to the top
ax122.set_xlim([0, sed_fe3max])
#ax32.set_xticks(np.arange(0,1500,500))
ax122.set_ylim([y3max, y3min])
ax122.annotate('FeIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='r') 
'''
#fig 3 Sediment - 4/3 FeS
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
ax123.annotate('FeS', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='b') 
#fig 3 Sediment - 4/3 fes2
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
ax124.annotate('FeS2', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction',  fontsize = 14,
            color='m') 
'''


'''fig1.savefig('fig1.png')   # save the figure to file
fig2.savefig('fig2.png')
fig3.savefig('fig3.png')   
'''

plt.show()

plt.close(fig1)
plt.close(fig2)
plt.close(fig3)

