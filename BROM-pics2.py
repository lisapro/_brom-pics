import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.gridspec as gridspec
import numpy as np


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
ymin_bbl = 108.5
ymin_sed = 109.00
ymax_sed = 109.1

#limits for x axes:
salmax = 36
so4max = 26000
h2smax = 2000
s0max = 250
s2o3max = 200 
o2max = 400
nh4max = 1600
no2max = 1
no3max = 100
mnco3max = 8*1.e-8
mnsmax = 0.02
mn4max = 1
mn3max = 0.04
mn2max = 1


fig1 = plt.figure(figsize = (12,13))
rect = 1,1,3,3
fig1.add_axes(rect, label='axes1')

gs = gridspec.GridSpec(3, 4)
gs.update(left=0.08, right=0.95,top = 0.84,bottom = 0.05, wspace=0.35,hspace=0.2)





ax8 = plt.subplot(gs[7])
ax9 = plt.subplot(gs[8])
ax10 = plt.subplot(gs[9])
ax11 = plt.subplot(gs[10])
ax12 = plt.subplot(gs[11])

''' Water 1/1 '''
ax1 = plt.subplot(gs[0])
#Water Kz
ax1.plot(kz, depth, 'go-',kz, depth, 'go-') # (111 = nxy)
ax1.set_xlabel('Kz(m^2/sec)', color='g') 
ax1.set_ylabel('Depth (m)')
ax1.xaxis.set_ticks_position('bottom') # this moves the ticks to the top
ax1.xaxis.set_label_position('bottom') # this moves the ticks to the top
ax1.set_xlim([0, 0.05])
ax1.set_ylim([ymin_bbl, 0])

#Water Salinity  
ax12 = ax1.twiny()
for spinename, spine in ax12.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax12.spines['top'].set_position(('outward', 0))
ax12.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax12.set_xlabel('Salinity(psu)', color='r') 
ax12.xaxis.set_label_position('top') # this moves the label to the top
ax12.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax12.set_xlim([33, salmax])
ax12.set_ylim([ymin_bbl, 0])
#Water Kz
ax13 = ax1.twiny()
for spinename, spine in ax13.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax13.spines['top'].set_position(('outward', 32))
ax13.plot(temp,depth,'bo-',temp,depth,'bo-')
ax13.set_xlabel('Temperature(C)', color = 'b')
ax13.xaxis.set_label_position('top') # this moves the label to the top
ax13.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax13.set_xlim([5, 14])
ax13.set_ylim([ymin_bbl, 0]) 
                              
#Water 2/1   
ax2 = plt.subplot(gs[1])
#Water - 2/1 SO4
ax2.plot(so4,depth,'go-',so4,depth,'go-')
ax2.set_xlabel('SO4',color = 'g')
ax2.set_ylabel('Depth (m)')
ax2.xaxis.set_label_position('bottom') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([20000, so4max])
ax2.set_ylim([ymin_bbl, 0])
ax2.set_xticks(np.arange(20000,27000,2000))

#Water -  2/1 S0
ax22 = ax2.twiny()
for spinename, spine in ax22.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax22.spines['top'].set_position(('outward', 0))
ax22.plot(s0,depth,'ro-',s0,depth,'ro-') 
ax22.xaxis.set_label_position('top') # this moves the label to the top
ax22.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax22.set_xlabel('S0', color='r',) 
ax22.set_xlim([0, s0max ])
ax22.set_ylim([ymin_bbl, 0])

#Water -  2/1 H2S
ax23 = ax2.twiny()
for spinename, spine in ax23.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax23.spines['top'].set_position(('outward', 32))
ax23.plot(h2s, depth, 'bo-',h2s, depth, 'bo-') 
ax23.set_xlabel('H2S', color='b',) 
ax23.xaxis.set_label_position('top') # this moves the label to the top
ax23.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax23.set_xlim([0, h2smax])
ax23.set_ylim([ymin_bbl, 0])

#Water - 2/1 s2o3
ax24 = ax2.twiny()
for spinename, spine in ax24.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax24.spines['top'].set_position(('outward', 65))
ax24.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax24.set_xlabel('S2O3', color='m',) 
ax24.xaxis.set_label_position('top') # this moves the label to the top
ax24.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax24.set_xlim([0, s2o3max])
ax24.set_ylim([ymin_bbl, 0])

#Water 3/1 
ax3 = plt.subplot(gs[2])
#Water -  3/1 O2
ax3.plot(o2,depth,'g-',o2,depth,'g-')
ax3.set_xlabel('O2',color = 'g')
ax3.set_ylabel('Depth (m)')
ax3.xaxis.set_label_position('bottom') # this moves the label to the top
ax3.xaxis.set_ticks_position('bottom') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
ax3.set_xlim([0, o2max])
ax3.set_ylim([ymin_bbl, 0])

#Water -  3/1 - NH4
ax32 = ax3.twiny()
for spinename, spine in ax32.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax32.spines['top'].set_position(('outward', 0))
ax32.plot(nh4,depth,'r-',nh4,depth,'r-') 
ax32.xaxis.set_label_position('top') # this moves the label to the top
ax32.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax32.set_xlabel('NH4', color='r',) 
ax32.set_xlim([0, nh4max])
#ax32.set_xticks(np.arange(0,1500,500))
ax32.set_ylim([ymin_bbl, 0])

#Water -  3/1 NO2
ax33 = ax3.twiny()
for spinename, spine in ax33.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax33.spines['top'].set_position(('outward', 32))
ax33.plot(no2, depth, 'b-',no2, depth, 'b-') 
ax33.set_xlabel('NO2', color='b',) 
ax33.xaxis.set_label_position('top') # this moves the label to the top
ax33.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax33.set_xlim([0, no2max])
ax33.set_ylim([ymin_bbl, 0])

#Water - 3/1 NO3
ax34 = ax3.twiny()
for spinename, spine in ax34.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax34.spines['top'].set_position(('outward', 65))
ax34.plot(no3, depth, 'm-',no3, depth, 'm-') 
ax34.set_xlabel('NO3', color='m',) 
ax34.xaxis.set_label_position('top') # this moves the label to the top
ax34.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax34.set_xlim([0, no3max])
ax34.set_ylim([ymin_bbl, 0])

#Water - 4/1 
ax4 = plt.subplot(gs[3])
#Water -  4/1 MnII
ax4.plot(mn2,depth,'g-',mn2,depth,'g-')
ax4.set_xlabel('Mn II',color = 'g')
ax4.set_ylabel('Depth (m)')
ax4.xaxis.set_label_position('bottom') # this moves the label to the top
ax4.xaxis.set_ticks_position('bottom') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
ax4.set_xlim([0, mn2max])
ax4.set_ylim([ymin_bbl, 0])

#Water -  4/1 - Mn III
ax42 = ax4.twiny()
for spinename, spine in ax42.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax42.spines['top'].set_position(('outward', 0))
ax42.plot(mn3,depth,'r-',mn3,depth,'r-') 
ax42.xaxis.set_label_position('top') # this moves the label to the top
ax42.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax42.set_xlabel('Mn III', color='r',) 
ax42.set_xlim([0, mn3max])
#ax32.set_xticks(np.arange(0,1500,500))
ax42.set_ylim([ymin_bbl, 0])

#Water -  4/1 Mn IV
ax43 = ax4.twiny()
for spinename, spine in ax43.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax43.spines['top'].set_position(('outward', 32))
ax43.plot(mn4, depth, 'b-',mn4, depth, 'b-') 
ax43.set_xlabel('Mn IV', color='b',) 
ax43.xaxis.set_label_position('top') # this moves the label to the top
ax43.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax43.set_xlim([0, mn4max])
ax43.set_ylim([ymin_bbl, 0])

#Water - 4/1 MnS
ax44 = ax4.twiny()
for spinename, spine in ax44.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax44.spines['top'].set_position(('outward', 65))
ax44.plot(mns, depth, 'm-',mns, depth, 'm-') 
ax44.set_xlabel('MnS', color='m',) 
ax44.xaxis.set_label_position('top') # this moves the label to the top
ax44.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax44.set_xlim([0, mnsmax])
ax44.set_ylim([ymin_bbl, 0])

#Water - 3/1 MnCO3
ax45 = ax4.twiny()
for spinename, spine in ax45.spines.iteritems():
    if spinename != 'top':
        spine.set_visible(False)
ax45.spines['top'].set_position(('outward', 96))
ax45.plot(mnco3, depth, 'm-',mnco3, depth, 'm-') 
ax45.set_xlabel('MnCo3', color='y',) 
ax45.xaxis.set_label_position('top') # this moves the label to the top
ax45.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax45.set_xlim([0, mnco3max])
ax45.set_ylim([ymin_bbl, 0])



## BBL 1/2
 # BBL 1/2 - Temperature
ax5 = plt.subplot(gs[4])
ax5.plot(temp,depth,'bo-',temp,depth,'bo-')
ax5.set_ylabel('Depth (m)')
plt.setp(ax5.get_xticklabels(), visible=False)
#ax5.set_xlabel('Temper')
#ax5.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
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
#ax3.set_xlim([33, 36])
ax53.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax53.get_xticklabels(), visible=False)


# BBL 2/2 
ax6 = plt.subplot(gs[5])
# BBL - SO4
ax6.plot(so4,depth,'go-',so4,depth,'go-')
ax6.set_ylabel('Depth (m)')
#ax6.xaxis.set_ticks_position('top') # this moves the ticks to the top
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

ax64 = ax6.twiny()
ax64.plot(s2o3, depth, 'mo-',s2o3, depth, 'mo-') 
ax64.set_xlim([0, s2o3max])
ax64.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax64.get_xticklabels(), visible=False)



 #BBL 3/2
ax7 = plt.subplot(gs[6])
ax7.plot(o2,depth,'go-',o2,depth,'go-')
ax7.set_ylabel('Depth (m)')
#ax7.set_xlabel('BBL')
ax7.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax7.set_xlim([0,o2max])
ax7.set_ylim([ymin_sed, ymin_bbl])
plt.setp(ax7.get_xticklabels(), visible=False)

ax71 = ax7.twiny()
ax71.plot(nh4, depth, 'ro-',nh4, depth, 'ro-') 
ax71.set_xlim([0, nh4max])
ax71.set_ylim([ymin_sed, ymin_bbl])
'''
ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_sed, ymin_bbl])

'''#Sediment 1/3 
'''
ax1 = fig1.add_subplot(337)
ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Sediment')
#ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.set_xlim([5, 14])
ax1.set_ylim([ymax_sed, ymin_sed])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([33, 36])
ax2.set_ylim([ymax_sed, ymin_sed])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax3.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymax_sed, ymin_sed])

'''#Sediment  2/3 
'''
ax1 = fig1.add_subplot(338)
# Sediment - SO4 
ax1.plot(so4,depth,'b',so4,depth,'b')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Sediment')
#ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.set_xlim([20000, 26000])
ax1.set_ylim([ymax_sed, ymin_sed])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'r',sal, depth, 'r') 
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([33, 36])
ax2.set_ylim([ymax_sed, ymin_sed])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'g',kz, depth, 'g') 
ax3.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymax_sed, ymin_sed])

'''#Sediment  3/3 
'''
ax1 = fig1.add_subplot(339)
ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Sediment')
#ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.set_xlim([5, 14])
ax1.set_ylim([ymax_sed, ymin_sed])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([33, 36])
ax2.set_ylim([ymax_sed, ymin_sed])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
ax3.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymax_sed, ymin_sed])
###
'''

#plt.tight_layout()
plt.show()
