import matplotlib.pyplot as plt

d = {}
value=[]

f = open('output_240_day-april.dat', 'rb')  #open model output file

num_lines = sum(1 for l  in f)
num = num_lines - 3  # calculate number of lines 
f.seek(0)                      # return to the beginning of the file 

for _ in range(2):            # skip two unneeded lines 
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
    value.append(loo[item])
    item += 1
    d[k] = v
                    
#for n in range(num):
line = f.readline()
loo = line.split()
item = 0
#for item in loo:

for k, v in d.iteritems(): 
#        value.append(loo[item])
    item += 1
 #       v = value
    d[k] = v
#
#    for i in range(42):
#        [v].append(loo[1])
 

#print d
print d




#Draw model results

plt.figure(1)

plt.subplot(311)
plt.title('Water')            # subplot 313 title
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