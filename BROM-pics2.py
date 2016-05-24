import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

values=[]
f = open('output_240_day-april.dat', 'rb')  #open model output file

num_lines = sum(1 for l  in f)
num = num_lines - 1                        # calculate number of lines 
f.seek(0)                                  # return to the beginning of the file 

for _ in range(1):                        # skip two unneeded lines 
    line = f.readline()
    
for _ in range(num):
    line = f.readline()                   # read line for heading
    foo = line.split()
    values.append(foo) 
data = zip(*values)

#Variables to plot:

depth = data[2][2:]
temp = data[3][2:]
sal = data[4][2:]





fig1 = plt.figure()
#    plt.figure.SubplotParams(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)


ax1 = fig1.add_subplot(321)
ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')
ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)

ax1.set_xlim([5, 14])
ax1.set_ylim([109.5, 0])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax2.set_xlabel('Salinity(psu)', color='r',) 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax2.set_xlim([33, 36])
ax2.set_ylim([109.5, 0])
######


#    plt.figure.SubplotParams(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)
ax1 = fig1.add_subplot(322)
#ax1.get_xaxis().get_major_formatter().set_useOffset(False)

ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')

ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)

ax1.set_xlim([5, 14])
ax1.set_ylim([109.5, 0])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
ax2.set_xlabel('Salinity(psu)', color='r',) 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax2.set_xlim([33, 36])
ax2.set_ylim([109.5, 0])

"""
BBL
"""
ax1 = fig1.add_subplot(323)
#ax1.get_xaxis().get_major_formatter().set_useOffset(False)

ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_ylabel('Depth (m)')

#ax1.set_xlabel('Temperature (C)',color='b')
#ax1.xaxis.set_label_position('bottom') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)

ax1.set_xlim([5, 14])
ax1.set_ylim([110, 109.5])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
#ax2.xaxis.set_label_position('top') # this moves the label to the top
#ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax2.set_xlim([33, 36])
ax2.set_ylim([110, 109.5])
###
ax1 = fig1.add_subplot(324)
#ax1.get_xaxis().get_major_formatter().set_useOffset(False)

ax1.plot(temp,depth,'o-',temp,depth,'o-')
ax1.set_ylabel('Depth (m)')

#ax1.set_xlabel('Temperature (C)',color='b')
#ax1.xaxis.set_label_position('bottom') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)

ax1.set_xlim([5, 14])
ax1.set_ylim([110, 109.5])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
#ax2.xaxis.set_label_position('top') # this moves the label to the top
#ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax2.set_xlim([33, 36])
ax2.set_ylim([110, 109.5])
"""
Sediment
"""

ax1 = fig1.add_subplot(325)
#ax1.get_xaxis().get_major_formatter().set_useOffset(False)

ax1.plot(temp,depth,'o-',temp,depth,'o-')
#ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')

ax1.xaxis.set_label_position('top') # this moves the label to the top
#ax1.xaxis.set_ticks_position('bottom') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)

ax1.set_xlim([5, 14])
ax1.set_ylim([110.1, 110])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
#ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax2.set_xlim([33, 36])
ax2.set_ylim([110.1, 110])

##############

ax1 = fig1.add_subplot(326)
#ax1.get_xaxis().get_major_formatter().set_useOffset(False)

ax1.plot(temp,depth,'o-',temp,depth,'o-')
#ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')

ax1.xaxis.set_label_position('top') # this moves the label to the top
#ax1.xaxis.set_ticks_position('bottom') # this moves the ticks to the top
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)

ax1.set_xlim([5, 14])
ax1.set_ylim([110.1, 110])

ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-',sal, depth, 'ro-') 
#ax2.set_xlabel('Salinity(psu)', color='r',) 
#ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top

ax2.set_xlim([33, 36])
ax2.set_ylim([110.1, 110])

plt.tight_layout()
plt.show()







plt.tight_layout()
plt.show()
