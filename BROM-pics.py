import matplotlib.pyplot as plt
<<<<<<< HEAD
#import numpy as np

 #open model output file

f = open("output_240_day-april.dat","rb")
for _ in range(3):         # skip 3 lines of heading 
    line = f.readline()
line = f.readline()
foo = line.split()
    
f.close   
print foo

 
#for line in f:
    
            


=======

d = {}
value=[]

f = open('output_240_day-april.dat', 'rb')  #open model output file

num_lines = sum(1 for l  in f)
num = num_lines - 4  # calculate number of lines 
f.seek(0)                      # return to the beginning of the file 

for _ in range(1):            # skip two unneeded lines 
    line = f.readline()
    
line = f.readline()           # read line for heading
foo = line.split()

for item in foo:             # print keys to dictionary = headings
    d[item] = ''
       
line = f.readline()           # add 1 lines values to dict
loo = line.split()
item = 0
for k, v in d.iteritems(): 
    v = loo[item]
    item += 1
    d[k] = [v]
 
               
for n in range(num):   # add all lines values to dict
    item = 0
    line = f.readline()
    koo = line.split()
    for k, v in d.iteritems(): 
        v.append(koo[item])
        item += 1

#    for i in range(42):
#        [v].append(loo[1])


    
#print d
>>>>>>> 80cdd0116d128c60f0c8b7566710d32c5e12e224
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



plt.figure(2)
plt.subplot()
plt.title('Water')            # subplot Temperature title
plt.xlabel('$\mu$M') 
plt.ylabel('M')
plt.axis([0, 160, 0, 110])
#plt(d['Depth'],['t'])
plt.show()