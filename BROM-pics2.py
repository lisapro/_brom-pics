import matplotlib.pyplot as plt


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
transposed = zip(*values)




#plt.show()

depth = transposed[2][2:]
temp = transposed[3][2:]
sal = transposed[4][2:]
templabel = transposed[3][0]




fig1 = plt.figure()
#plt.figure.SubplotParams(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)
ax1 = fig1.add_subplot(311)
#ax1.get_xaxis().get_major_formatter().set_useOffset(False)

ax1.plot(temp,depth,'o-')
ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')

ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)


ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-') 
ax2.set_xlabel('Salinity(psu)', color='r') 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top


#BBL
ax1 = fig1.add_subplot(312)

ax1.plot(temp,depth,'o-')
ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')

ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)


ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-') 
ax2.set_xlabel('Salinity(psu)', color='r') 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top



#SEDIMENT
ax1 = fig1.add_subplot(313)

ax1.plot(temp,depth,'o-')
ax1.set_xlabel('Temperature (C)',color='b')
ax1.set_ylabel('Depth (m)')

ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)


ax2 = ax1.twiny()
ax2.plot(sal, depth, 'ro-') 
ax2.set_xlabel('Salinity(psu)', color='r') 
ax2.xaxis.set_label_position('top') # this moves the label to the top
ax2.xaxis.set_ticks_position('top') # this moves the ticks to the top



plt.show()
