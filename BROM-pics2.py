import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl


style.use('ggplot')

values=[]
f = open('output_240_day.dat', 'rb')       #open model output file

num_lines = sum(1 for l  in f)
num = num_lines - 1                        # calculate number of lines 
f.seek(0)                                  # return to the beginning of the file 

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
feS = data[26][2:]
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
ymin_bbl = 107
ymin_sed = 109.00
ymax_sed = 109.1







#limits for x   WatBBL axes:
kzmin = 0
kzmax = 0.05
salmax = 36
so4max = 26000
h2smax = 2000
s0max = 250
s2o3max = 200 
o2max = 400
nh4max = 10
no2max = 1
no3max = 100
mnco3max = 0.0001
mnsmax = 0.02
mn4max = 1
mn3max = 0.04
mn2max = 1

#limits for x Sediment axes:
sed_kz = 1
sed_salmax = 36
sed_so4max = 26000
sed_h2smax = 2000
sed_s0max = 250
sed_s2o3max = 200 
sed_o2max = 10
sed_nh4max = 1600
sed_no2max = 1
sed_no3max = 50
sed_mnco3max = 0.0001
sed_mnsmax = 0.02
sed_mn4max = 5
sed_mn3max = 0.5
sed_mn2max = 10

#positions for axes
axis1 = 0
axis2 = 25
axis3 = 50
axis4 = 75
axis5 = 100

labelaxis_x = -0.35
labelaxis1_y = 1.09
labelaxis2_y = 1.24
labelaxis3_y = 1.39
labelaxis4_y = 1.54
labelaxis5_y = 1.69


fig1 = plt.figure(figsize = (15,13))
rect = 1,1,3,3
fig1.add_axes(rect, label='axes1')

gs = gridspec.GridSpec(2, 4)  #determine grid of subplots (BBL and Water)
gs.update(left=0.08, right=0.95,top = 0.815,bottom = 0.4, wspace=0.65,hspace=0.05)

label_size = 13
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['lines.linewidth'] = 2

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Water Kz
#ax1.plot(kz, depth, 'go-',kz, depth, 'go-') # (111 = nxy)
ax1.set_ylabel('Depth (m)')
ax1.set_ylim([ymin_bbl, 0])
plt.setp(ax1.get_xticklabels(), visible=False)
#Double water Kz
ax11 = ax1.twiny()
for spinename, spine in ax11.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax11.spines['top'].set_position(('outward', axis1))
ax11.spines['top'].set_color('g')
ax11.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax11.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax11.set_xlim([kzmin, kzmax])
ax11.set_ylim([ymin_bbl, 0])

#ticklabelpad = mpl.rcParams['xtick.major.pad']
ax11.annotate('Kz', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g')
            
################################################################################ ax11.tick_params(direction='out', pad=0)
#Water Salinity  
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', axis2))
ax12.spines['top'].set_color('r')
ax12.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xlim([33, salmax])
ax12.set_ylim([ymin_bbl, 0])
ax12.annotate('S', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r')
#Water Temperature
ax13 = ax1.twiny()
for spinename, spine in ax13.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax13.spines['top'].set_position(('outward',axis3))
ax13.spines['top'].set_color('b')
ax13.plot(temp,depth,'bo-',temp,depth,'bo-')
ax13.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax13.set_xlim([5, 14])
ax13.set_ylim([ymin_bbl, 0]) 
ax13.annotate('T', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b')                           
#Water 2/1   
ax2 = plt.subplot(gs[1])
#Water - 2/1 SO4
ax2.plot(so4,depth,'go-',so4,depth,'go-')

ax2.set_xlim([20000, so4max])
ax2.set_ylim([ymin_bbl, 0])
plt.setp(ax2.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,so4max,2000))
ax21 = ax2.twiny()
for spinename, spine in ax21.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax21.spines['top'].set_position(('outward', axis1)) #move 
ax21.spines['top'].set_color('g')
ax21.annotate('SO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g')

#Water -  2/1 S0
ax22 = ax2.twiny()
for spinename, spine in ax22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax22.spines['top'].set_position(('outward', axis2))
ax22.spines['top'].set_color('r')
ax22.plot(s0,depth,'ro-',s0,depth,'ro-') 
ax22.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax22.set_xlim([0, s0max ])
ax22.set_ylim([ymin_bbl, 0])
ax21.annotate('S0', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r')
#Water -  2/1 H2S
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', axis3))
ax23.spines['top'].set_color('b')
ax23.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
ax23.annotate('H2S', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b')
ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, h2smax])
ax23.set_ylim([ymin_bbl, 0])

#Water - 2/1 s2o3
ax24 = ax2.twiny()
for spinename, spine in ax24.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax24.spines['top'].set_position(('outward', axis4))
ax24.spines['top'].set_color('m')
ax24.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax24.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax24.set_xlim([0, s2o3max])
ax24.set_ylim([ymin_bbl, 0])
ax24.annotate('S2O3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='m')            

#Water 3/1 
ax3 = plt.subplot(gs[2])
#Water -  3/1 O2
ax3.plot(o2,depth,'go-',o2,depth,'go-')
#ax3.set_ylabel('Depth (m)')
plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylim([ymin_bbl, 0])
ax31 = ax3.twiny()
for spinename, spine in ax31.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax31.spines['top'].set_position(('outward', axis1))
ax31.spines['top'].set_color('g')
ax31.set_xlim([0, o2max])
ax31.set_xticks(np.arange(0,o2max+100,100))
ax31.annotate('O2', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g')

#Water -  3/1 - NH4
ax32 = ax3.twiny()
for spinename, spine in ax32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax32.spines['top'].set_position(('outward', axis2))
ax32.spines['top'].set_color('r')
ax32.plot(nh4,depth,'ro-',nh4,depth,'ro-') 
ax32.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax32.set_xlim([0, nh4max])
ax32.set_xticks(np.arange(0,nh4max+nh4max/4,nh4max/4))
ax32.set_ylim([ymin_bbl, 0])
ax32.annotate('NH4', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r')   
#Water -  3/1 NO2 
ax33 = ax3.twiny()
for spinename, spine in ax33.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax33.spines['top'].set_position(('outward', axis3))
ax33.spines['top'].set_color('b')
ax33.plot(no2, depth, 'bo-',no2, depth, 'bo-') 
ax33.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax33.set_xlim([0, no2max])
ax33.set_ylim([ymin_bbl, 0])
ax33.annotate('NO2', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b')   
#Water - 3/1 NO3
ax34 = ax3.twiny()
for spinename, spine in ax34.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax34.spines['top'].set_position(('outward', axis4))
ax34.spines['top'].set_color('m')
ax34.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax34.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax34.set_xlim([0, no3max])
ax34.set_ylim([ymin_bbl, 0])
ax34.annotate('NO3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='m')   
#Water - 4/1 
ax4 = plt.subplot(gs[3])
#Water -  4/1 MnII
ax4.plot(mn2,depth,'go-',mn2,depth,'go-')
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.set_ylim([ymin_bbl, 0])
ax41 = ax4.twiny()
for spinename, spine in ax41.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax41.spines['top'].set_position(('outward', axis1))
ax41.set_xlim([0, mn2max])
#ax41.set_xlabel('Mn II',color = 'g')
ax41.annotate('MnII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g')

#Water -  4/1 - Mn III
ax42 = ax4.twiny()
for spinename, spine in ax42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax42.spines['top'].set_position(('outward', axis2))
ax42.spines['top'].set_color('r')
ax42.plot(mn3,depth,'r-',mn3,depth,'r-') 
ax42.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax42.set_xlim([0, mn3max])
ax42.set_xticks(np.arange(0,mn3max+mn3max/2,mn3max/2))
#ax32.set_xticks(np.arange(0,1500,500))
ax42.set_ylim([ymin_bbl, 0])
ax42.annotate('MnIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r')  
#Water -  4/1 Mn IV
ax43 = ax4.twiny()
for spinename, spine in ax43.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax43.spines['top'].set_position(('outward', axis3))
ax43.spines['top'].set_color('b')
ax43.plot(mn4, depth, 'bo-',mn4, depth, 'bo-') 
ax43.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax43.set_xlim([0, mn4max])
ax43.set_ylim([ymin_bbl, 0])
ax43.annotate('MnIV', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b')  
#Water - 4/1 MnS
ax44 = ax4.twiny()
for spinename, spine in ax44.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax44.spines['top'].set_position(('outward', axis4))
ax44.spines['top'].set_color('m')
ax44.plot(mns, depth, 'mo-',mns, depth, 'mo-') 
ax44.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax44.set_xlim([0, mnsmax])
ax44.set_ylim([ymin_bbl, 0])
ax44.annotate('MnS', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='m') 
#Water - 3/1 MnCO3
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
ax45.set_ylim([ymin_bbl, 0])
ax45.annotate('MnCO3', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='y') 

## BBL 1/2
 # BBL 1/2 - Temperature
ax5 = plt.subplot(gs[4])
ax5.plot(temp,depth,'bo-',temp,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
ax5.set_xlim([5, 14])
ax5.set_ylim([ymin_sed, ymin_bbl])
#BBL 1/2 - Salinity
ax52 = ax5.twiny()
ax52.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax52.set_xlim([33, 36])
ax52.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax52.get_xticklabels(), visible=False)
#BBL 1/2 Kz
ax53 = ax5.twiny()
ax53.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax3.set_xlim([kzmin, kzmax])
ax53.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax53.get_xticklabels(), visible=False)


# BBL 2/2 
ax6 = plt.subplot(gs[5])
# BBL - SO4
ax6.plot(so4,depth,'go-',so4,depth,'go-')
ax6.set_xlim([20000, so4max])
ax6.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax6.get_xticklabels(), visible=False)
#BBL -  2/2 S0
ax62 = ax6.twiny()
ax62.plot(s0, depth, 'ro-',s0, depth, 'ro-') 
ax62.set_xlim([0, s0max])
ax62.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax62.get_xticklabels(), visible=False)

#BBL -  2/2 h2S
ax63 = ax6.twiny()
ax63.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
ax63.set_xlim([0, h2smax])
ax63.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax63.get_xticklabels(), visible=False)

#BBL -  2/2 s2o3
ax64 = ax6.twiny()
ax64.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax64.set_xlim([0, s2o3max])
ax64.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax64.get_xticklabels(), visible=False)

##BBL 3/2
ax7 = plt.subplot(gs[6])
#BBL 3/2 - o2
ax7.plot(o2,depth,'go-',o2,depth,'go-')
#ax7.set_ylabel('Depth (m)')
plt.setp(ax7.get_xticklabels(), visible=False)
ax7.set_xlim([0,o2max])
ax7.set_ylim([ymin_sed, ymin_bbl])
#BBL 3/2 - nh4
ax72 = ax7.twiny()
ax72.plot(nh4, depth, 'ro-',nh4, depth, 'ro-') 
ax72.set_xlim([0, nh4max])
ax72.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax72.get_xticklabels(), visible=False)
#BBL 3\2 - no2
ax73 = ax7.twiny()
ax73.plot(no2, depth, 'b-',no2, depth, 'b-') 
ax73.set_xlim([0, no2max])
ax73.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax73.get_xticklabels(), visible=False)
#BBL - 3/2 NO3
ax74 = ax7.twiny()
ax74.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax74.set_xlim([0, no3max])
ax74.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax74.get_xticklabels(), visible=False)

##BBL - 4/2
ax8 = plt.subplot(gs[7])
#BBL - 4/2 - Mn II
ax8.plot(mn2,depth,'go-',mn2,depth,'go-')
plt.setp(ax8.get_xticklabels(), visible=False)
ax8.set_xlim([0,mn2max])
ax8.set_ylim([ymin_sed, ymin_bbl])

#BBL - 4/2 - Mn III
ax82 = ax8.twiny()
ax82.plot(mn3, depth, 'ro-',mn3, depth, 'ro-') 
ax82.set_xlim([0, mn3max])
ax82.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax82.get_xticklabels(), visible=False)
#BBL 4\2 - mn IV
ax83 = ax8.twiny()
ax83.plot(mn4, depth, 'bo-',mn4, depth, 'bo-') 
ax83.set_xlim([0, mn4max])
ax83.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax83.get_xticklabels(), visible=False)
#BBL - 4/2 MnS
ax84 = ax8.twiny()
ax84.plot(mns, depth, 'mo-',mns, depth, 'mo-') 
ax84.set_xlim([0, mnsmax])
ax84.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax84.get_xticklabels(), visible=False)
#BBL - 4/2 MnCO3
ax85 = ax8.twiny()
ax85.plot(mnco3, depth, 'yo-',mnco3, depth, 'yo-') 
ax85.set_xlim([0, mnco3max])
ax85.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax85.get_xticklabels(), visible=False)

gs1 = gridspec.GridSpec(1, 4)
gs1.update(left=0.08, right=0.95, top = 0.25, bottom = 0.05, wspace=0.65,hspace=0.9)

#Sediment - 1/3 
ax9 = plt.subplot(gs1[0,0])
ax9.set_ylabel('Depth (m)')
plt.setp(ax9.get_xticklabels(), visible=False)

#Double sediment Kz
ax91 = ax9.twiny()
for spinename, spine in ax91.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax91.spines['top'].set_position(('outward', axis1))
ax91.spines['top'].set_color('g')
ax91.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax91.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax91.set_xlim([0, 0.05])
ax91.set_ylim([ymax_sed, ymin_sed])
ax91.annotate('Kz', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g') 
#Sediment - 1/3 SAlinity
ax92 = ax9.twiny()
for spinename, spine in ax92.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax92.spines['top'].set_position(('outward', axis2))
ax92.spines['top'].set_color('r')
ax92.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax92.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax92.set_xlim([33, sed_salmax])
ax92.set_ylim([ymax_sed, ymin_sed])
ax92.annotate('S', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r') 
#Sediment 1/3 Temperature
ax93 = ax9.twiny()
for spinename, spine in ax93.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax93.spines['top'].set_position(('outward', axis3))
ax93.spines['top'].set_color('b')
ax93.plot(temp,depth,'bo-',temp,depth,'bo-')
ax93.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax93.set_xlim([5, 14])
ax93.set_ylim([ymax_sed, ymin_sed])
ax93.annotate('T', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b') 
#Sediment - 2/3 
ax10 = plt.subplot(gs1[0, 1])
ax10.plot(so4,depth,'go-',so4,depth,'go-')
ax10.set_xlim([20000, sed_so4max])
ax10.set_ylim([ymax_sed, ymin_sed])
plt.setp(ax10.get_xticklabels(), visible=False)
#ax2.set_xticks(np.arange(20000,so4max,2000))
ax101 = ax10.twiny()
for spinename, spine in ax101.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax101.spines['top'].set_position(('outward', axis1))
ax101.spines['top'].set_color('g')
ax101.annotate('SO4', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g') 
#sediment -  2/3 S0
ax102 = ax10.twiny()
for spinename, spine in ax102.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax102.spines['top'].set_position(('outward', axis2))
ax102.spines['top'].set_color('r')
ax102.plot(s0,depth,'ro-',s0,depth,'ro-') 
ax102.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax102.set_xlim([0, sed_s0max ])
ax102.set_ylim([ymax_sed, ymin_sed])
ax101.annotate('SO', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r') 
#SEdiment -  2/3 H2S
ax103 = ax10.twiny()
for spinename, spine in ax103.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax103.spines['top'].set_position(('outward', axis3))
ax103.spines['top'].set_color('b')
ax103.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
ax103.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax103.set_xlim([0, sed_h2smax])
ax103.set_ylim([ymax_sed, ymin_sed])
ax103.annotate('H2S', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b') 
#Sediment - 2/3 s2o3
ax104 = ax10.twiny()
for spinename, spine in ax104.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax104.spines['top'].set_position(('outward', axis4))
ax104.spines['top'].set_color('m')
ax104.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax104.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax104.set_xlim([0, sed_s2o3max])
ax104.set_ylim([ymax_sed, ymin_sed])
ax104.annotate('S2O3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='m') 
#Sediment - 3/3
ax11 = plt.subplot(gs1[0,2])
ax11.plot(o2,depth,'go-',o2,depth,'go-')
#ax3.set_ylabel('Depth (m)')
plt.setp(ax11.get_xticklabels(), visible=False)
ax11.set_ylim([ymax_sed, ymin_sed])
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
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g') 
#Sediment -  3/3 - NH4
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
ax112.set_ylim([ymax_sed, ymin_sed])
ax112.annotate('NH4', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r') 
#Sediment -  3/3 NO2 
ax113 = ax11.twiny()
for spinename, spine in ax113.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax113.spines['top'].set_position(('outward', axis3))
ax113.spines['top'].set_color('b')
ax113.plot(no2, depth, 'bo-',no2, depth, 'bo-') 
ax113.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax113.set_xlim([0, sed_no2max])
ax113.set_ylim([ymax_sed, ymin_sed])
ax113.annotate('NO2', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b') 
#Sediment -  3/3 NO3
ax114 = ax11.twiny()
for spinename, spine in ax114.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax114.spines['top'].set_position(('outward', axis4))
ax114.spines['top'].set_color('m')
ax114.plot(no3, depth, 'mo-',no3, depth, 'mo-') 
ax114.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax114.set_xlim([0, sed_no3max])
ax114.set_ylim([ymax_sed, ymin_sed])
ax114.annotate('NO3', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='m') 
#Sediment - 4/3 
ax12 = plt.subplot(gs1[0,3])
plt.setp(ax12.get_xticklabels(), visible=False)
ax12.set_ylim([ymax_sed, ymin_sed])
ax121 = ax12.twiny()
ax121.plot(mn2,depth,'go-',mn2,depth,'go-')
for spinename, spine in ax121.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax121.spines['top'].set_position(('outward', axis1))
ax121.spines['top'].set_color('g')
ax121.set_xlim([0, sed_mn2max])
ax121.annotate('MnII', xy=(labelaxis_x,labelaxis1_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='g') 
#Sediment - 4/3 - Mn III
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
ax122.set_ylim([ymax_sed, ymin_sed])
ax122.annotate('MnIII', xy=(labelaxis_x,labelaxis2_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='r') 
#Sediment - 4/3  Mn IV
ax123 = ax12.twiny()
for spinename, spine in ax123.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax123.spines['top'].set_position(('outward', axis3))
ax123.spines['top'].set_color('b')
ax123.plot(mn4, depth, 'bo-',mn4, depth, 'bo-') 
ax123.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax123.set_xlim([0, sed_mn4max])
ax123.set_ylim([ymax_sed, ymin_sed])
ax123.annotate('MnIV', xy=(labelaxis_x,labelaxis3_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='b') 
#Sediment - 4/3 MnS
ax124 = ax12.twiny()
for spinename, spine in ax124.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax124.spines['top'].set_position(('outward', axis4))
ax124.spines['top'].set_color('m')
ax124.plot(mns, depth, 'mo-',mns, depth, 'mo-') 
ax124.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax124.set_xlim([0, sed_mnsmax])
ax124.set_ylim([ymax_sed, ymin_sed])
ax124.annotate('MnS', xy=(labelaxis_x,labelaxis4_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='m') 
#Sediment - 4/3  MnCO3
ax125 = ax12.twiny()
for spinename, spine in ax125.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax125.spines['top'].set_position(('outward', axis5))
ax125.spines['top'].set_color('y')
ax125.plot(mnco3, depth, 'yo-',mnco3, depth, 'yo-') 
ax125.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax125.set_xlim([0, sed_mnco3max])
ax125.set_xticks(np.arange(0,sed_mnco3max+sed_mnco3max/2,sed_mnco3max/2))
ax125.set_ylim([ymax_sed, ymin_sed])
ax125.annotate('MnCO3', xy=(labelaxis_x,labelaxis5_y), ha='left', va='center',
            xycoords='axes fraction', textcoords='offset points', fontsize = 14,
            color='y') 
#plt.tight_layout()

plt.show()
