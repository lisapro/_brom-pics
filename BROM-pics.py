import matplotlib.pyplot as plt
import numpy as np

 #open model output file
f = open('F:\canopy\brom_pics\output_240_day-april.dat', 'rb')
f.read(1)

print f
#Draw model results

plt.figure(1)

plt.subplot(311)
plt.title('Water') # subplot 313 title
plt.xlabel('$\mu$M')
plt.ylabel('M')
plt.axis([0, 160, 0, 110])

plt.subplot(312)
plt.title('BBL') # subplot 312 title
plt.xlabel('mM')
plt.ylabel('M')

plt.subplot(313)
plt.title('Sediment') # subplot 313 title
plt.xlabel('mM')
plt.ylabel('Cm')


#plt.show()