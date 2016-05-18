import matplotlib.pyplot as plt
import numpy as np

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
a = values 
map(list, zip(*a))



print values
d.write(str([values])) 
d.close   
#print values[0][0]
#Draw model results

plt.figure(1)

plt.subplot(311)
plt.title('Water')            # subplot Temperature title
plt.xlabel('$\mu$M') 
plt.ylabel('M')
plt.axis([0, 160, 0, 110])

plt.subplot(312)
plt.title('BBL')             # subplot 312 title
plt.xlabel('mM')
plt.ylabel('M')

plt.subplot(313)
plt.title('Sediment')        # subplot 313 title
plt.xlabel('mM')
plt.ylabel('Cm')


#plt.show()


x = values[1]
y = values[2]

plt.figure(2)
plt.subplot()
plt.title(values[0][0])            # subplot Temperature title
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0, 160, 0, 110])
plt.plot(x, y, linewidth=2.0)
plt.show()