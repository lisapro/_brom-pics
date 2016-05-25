import matplotlib.pyplot as plt
from matplotlib import style

#style.use('ggplot')

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


fig1 = plt.figure()

''' Water 1/1 '''
ax1 = fig1.add_subplot(331) 
ax1.plot(temp,depth,'-',temp,depth,'o-')
ax1.set_xlabel('Water')
ax1.set_ylabel('Depth (m)')
#ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top

#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
ax1.set_xlim([5, 14])
ax1.set_ylim([ymin_bbl, 0])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([33, 36])
ax2.set_ylim([ymin_bbl, 0])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
#ax3.set_xlabel('Kz(m^2/sec)', color='g',) 
ax3.xaxis.set_label_position('top') # this moves the label to the top
ax3.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_bbl, 0])



#    plt.figure.SubplotParams(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)
''' Water 2/1 '''
ax1 = fig1.add_subplot(332) 
#Water - SO4
ax1.plot(so4,depth,'b',so4,depth,'b')
ax1.set_xlabel('Water')
ax1.set_ylabel('Depth (m)')
#ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
ax1.set_xlim([20000, 26000])
ax1.set_ylim([ymin_bbl, 0])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'r',sal, depth, 'r') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([33, 36])
ax2.set_ylim([ymin_bbl, 0])


ax3 = ax1.twiny()
ax3.plot(kz, depth, 'g',kz, depth, 'g') 
#ax3.set_xlabel('Kz(m^2/sec)', color='g',) 
ax3.xaxis.set_label_position('top') # this moves the label to the top
ax3.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_bbl, 0])

###

''' Water 3/1 '''
ax1 = fig1.add_subplot(333)
ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_xlabel('Water')
ax1.set_ylabel('Depth (m)')
#ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
ax1.set_xlim([5, 14])
ax1.set_ylim([ymin_bbl, 0])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax2.set_xlim([33, 36])
ax2.set_ylim([ymin_bbl, 0])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
#ax3.set_xlabel('Kz(m^2/sec)', color='g',) 
ax3.xaxis.set_label_position('top') # this moves the label to the top
ax3.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_bbl, 0])

''' BBL 1/2'''
ax1 = fig1.add_subplot(334)
ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('BBL')
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
ax1.set_xlim([5, 14])
ax1.set_ylim([ymin_sed, ymin_bbl])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax2.set_xlim([33, 36])
ax2.set_ylim([ymin_sed, ymin_bbl])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_sed, ymin_bbl])


''' BBL 2/2 '''
ax1 = fig1.add_subplot(335)
# BBL - SO4
ax1.plot(so4,depth,'b',so4,depth,'b')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('BBL')
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax1.set_xlim([20000, 26000])
ax1.set_ylim([ymin_sed, ymin_bbl])
ax2 = ax1.twiny()
ax2.plot(sal, depth, 'r',sal, depth, 'r') 
ax2.set_xlim([33, 36])
ax2.set_ylim([ymin_sed, ymin_bbl])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'g',kz, depth, 'g') 
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_sed, ymin_bbl])

''' BBL 3/2''' 
ax1 = fig1.add_subplot(336)
ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('BBL')
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax1.set_xlim([5, 14])
ax1.set_ylim([ymin_sed, ymin_bbl])
ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax2.set_xlim([33, 36])
ax2.set_ylim([ymin_sed, ymin_bbl])

ax3 = ax1.twiny()
ax3.plot(kz, depth, 'go-',kz, depth, 'go-') 
#ax3.set_xlim([33, 36])
ax3.set_ylim([ymin_sed, ymin_bbl])

'''Sediment 1/3 '''
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

'''Sediment  2/3 '''
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

'''Sediment  3/3 '''
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




plt.tight_layout()
plt.show()
