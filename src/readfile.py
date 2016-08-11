'''
Created on 24. jun. 2016

@author: ELP
'''

#!/usr/bin/python
# Filename: readfile.py
# Import standard (i.e., non GOTM-GUI) modules.
import sys,os
from netCDF4 import Dataset
import numpy as np


numday = 100
my_example_nc_file = 'BROM_out.nc'
fh = Dataset(my_example_nc_file, mode='r')

depth = fh.variables['z'][:] #middle points
depth2 = fh.variables['z2'][:] #at interfaces 
kz = fh.variables['Kz'][:]
kz_par = fh.variables['Kz_par'][:]
kz_sol = fh.variables['Kz_sol'][:]


def calculate_watmax():
    for n in range(0,(len(depth2)-1)):
#        if depth[_]-depth[_?]
        if depth2[n+1] - depth2[n] >= 0.5:
            pass
        elif depth2[n+1] - depth2[n] < 0.50:
#            watmax =  depth[n],depth[n]-depth[n+1],n
#            y1max =np.ceil(depth2[n])    
            y1max = (depth2[n])                     
#            print y1max,depth[n+1],depth[n],depth[n+1]-depth[n]
#            print 'y1max', y1max
#            print 'ynmax', ynmax             
            return y1max
            break

      
#print kz[numday,n]
def calculate_bblmax():
    for n in range(0,(len(depth2)-1)):
        if kz[1,n] == 0:
            y2max =depth2[n]    
#            print 'y2max', y2max       
            return y2max
            break        
 
def y2max_fill_water():
    for n in range(0,(len(depth2)-1)):
#        if depth[_]-depth[_?]
        if depth2[n+1] - depth2[n] >= 0.5:
            pass
        elif depth2[n+1] - depth2[n] < 0.50:
#            watmax =  depth[n],depth[n]-depth[n+1],n
            y2max_fill_water = depth2[n]            
#            print y1max,depth[n+1],depth[n],depth[n+1]-depth[n]
#            print 'y2max_fill_water',y2max_fill_water
            return y2max_fill_water
            break 
   
y1min = 0
y1max = calculate_watmax()

#y2min = y1max #109 #depth[len(depth[:])-19]#108.5
y2max = calculate_bblmax() #110.0 #(sed_wat interface)#depth[len(depth[:])-13]#
y2min = y2max - 2*(y2max - y1max)   #calculate the position of y2min, for catching part of BBL 
#print 'y2min', y2min
y2min_fill_bbl = y2max_fill_water = y1max #y2max_fill_water() #109.5 #BBL-water interface
ysedmax_fill_bbl = ysedmin_fill_sed = 0

#y2max = 110 #(sed_wat interface)
to_float = []
for item in depth:
    to_float.append(float(item)) #make a list of floats from tuple 
depth_sed = [] # list for storing final depth data for sediment 
v=0  
for i in to_float:
    v = (i- y2max)*100  #convert depth from m to cm
    depth_sed.append(v)

to_float2 = []
for item in depth2:
    to_float2.append(float(item)) #make a list of floats from tuple 
depth_sed2 = [] # list for storing final depth data for sediment 
v2=0  
for i in to_float2:
    v2 = (i- y2max)*100  #convert depth from m to cm
    depth_sed2.append(v2) 

def calculate_sedmin():
    for n in range(0,(len(depth_sed)-1)):
        if kz[1,n] == 0:
            ysed = depth_sed[n]  
            ysedmin =  ysed - 10                
#            print ysed    
            return ysedmin
            break   
        
def calculate_sedmax():
    for n in range(0,(len(depth_sed)-1)):
        if kz[1,n] == 0:
            ysed = depth_sed[n]    
            ysedmax =  ysed + 10              
#            print ysed    
            return ysedmax
            break          
#calculate_sedmin()        
        
#y3min = -10 #109.91
#y3max = 10 #110.10
ysedmin = calculate_sedmin()
#print ysedmin #-10#depth[len(depth[:])-15]#109.9 #for depth in m
ysedmax = calculate_sedmax()    #10#depth[len(depth[:])-1]#110.1
#print depth[len(depth[:])-12]
#print depth_sed2#ysedmin


#for filling the font


#ysedmin_fill_bbl = 0
#y3max_fill_bbl = 0
#y3min_fill_sed = 0


xticks =(np.arange(0,100000))

wat_color = '#c9ecfd' #colors for filling water,bbl and sedimnet 
bbl_color = '#2873b8' 
sed_color = '#916012'
alpha_wat = 0.3 # saturation of color (from 0 to 1) 
alpha_bbl = 0.3
alpha_sed = 0.5


#positions for different axes, sharing one subplot
axis1 = 0
axis2 = 27
axis3 = 53
axis4 = 79
axis5 = 105

labelaxis_x =  1.10 #positions of labels 
labelaxis1_y = 1.02
labelaxis2_y = 1.15
labelaxis3_y = 1.26
labelaxis4_y = 1.38
labelaxis5_y = 1.48


wat_color = '#c9ecfd' #colors for filling water,bbl and sedimnet 
bbl_color = '#2873b8' 
sed_color = '#916012'

xlabel_fontsize = 14






#numday = fh.variables['time'][:] 

alk = fh.variables['Alk'][:] 
temp = fh.variables['T'][:]
sal = fh.variables['S'][:]
#print depth[len(depth[:])-13]
#print len(depth[:])-13
def watmax(variable):
    n = variable[:,y1min:-13].max()#+ ((variable[:,y1min:y2max].max())/10))

    if n > 10000:
        n = 30000#np.ceil(n)
    elif n > 5000 and n <= 10000:  
        n = 10000         
    elif n > 1000 and n <= 5000:  
        n = 5000        
    elif n > 500 and n <= 1000:  
        n = 1000 
    elif n > 350 and n <= 500:  
        n = 500                       
    elif n > 200 and n <= 350:  
        n = 350          
    elif n > 100 and n <= 200:  
        n = 200         
    elif n > 10 and n <= 100:
        n = 100     
    elif n > 0.5 and n <= 10:
        n = 10          
    elif n > 0.05 and n <= 0.5:
        n = 0.5           
    elif n > 0.005 and n <= 0.05:
        n = 0.05         
    elif n > 0.0005 and n <= 0.005:
        n = 0.005
    elif n > 0.00005 and  n  <= 0.0005 :
        n = 0.0005   
    elif n <= 0.00005  :
        n = 0.00005               
    return n 


def watmin(variable):
    n = np.round(variable[:,y1min:-13].min())
    return n
#print depth [:-12]
def sedmax(variable):
    n = variable[:,-15:].max()# + ((variable[:,ysedmin:ysedmax].max()))) #np.ceil

    if n > 10000:
        n = 30000#np.ceil(n)
    elif n > 5000 and n <= 10000:  
        n = 10000         
    elif n > 1000 and n <= 5000:  
        n = 5000        
    elif n > 500 and n <= 1000:  
        n = 1000 
    elif n > 350 and n <= 500:  
        n = 500                       
    elif n > 200 and n <= 350:  
        n = 350          
    elif n > 100 and n <= 200:  
        n = 200         
    elif n > 10 and n <= 100:
        n = 100     
    elif n > 0.5 and n <= 10:
        n = 10          
    elif n > 0.05 and n <= 0.5:
        n = 0.5           
    elif n > 0.005 and n <= 0.05:
        n = 0.05         
    elif n > 0.0005 and n <= 0.005:
        n = 0.005
    elif n > 0.00005 and  n  <= 0.0005 :
        n = 0.0005   
    elif n <= 5.e-5:#   0.00005  :
        n = 5.e-5#0.00005             
    return n 



def sedmin(variable):
    n = np.ceil(variable[:,-15:].min())
    return n


    
    
time = fh.variables['time']



dic = fh.variables['DIC'][:]
phy = fh.variables['Phy'][:]
het = fh.variables['Het'][:]
no3 = fh.variables['NO3'][:]
po4 = fh.variables['PO4'][:]
nh4 = fh.variables['NH4'][:]
pon = fh.variables['PON'][:]
don = fh.variables['DON'][:]
o2  = fh.variables['O2'][:]
mn2 = fh.variables['Mn2'][:]
mn3 = fh.variables['Mn3'][:]
mn4 = fh.variables['Mn4'][:]
h2s = fh.variables['H2S'][:]
mns = fh.variables['MnS'][:]
mnco3 = fh.variables['MnCO3'][:]
fe2 = fh.variables['Fe2'][:]
fe3 = fh.variables['Fe3'][:]
fes = fh.variables['FeS'][:]
feco3 = fh.variables['FeCO3'][:]
no2 = fh.variables['NO3'][:]
s0 = fh.variables['S0'][:]
s2o3 = fh.variables['S2O3'][:]
so4 = fh.variables['SO4'][:]
si = fh.variables['Si'][:]
si_part = fh.variables['Sipart'][:]
baae = fh.variables['Baae'][:]
bhae = fh.variables['Bhae'][:]
baan = fh.variables['Baan'][:]
bhan = fh.variables['Bhan'][:]
caco3 = fh.variables['CaCO3'][:]
fes2 = fh.variables['FeS2'][:]
ch4 = fh.variables['CH4'][:]
ph = fh.variables['pH'][:]
pco2 = fh.variables['pCO2'][:]
om_ca = fh.variables['Om_Ca'][:]
om_ar = fh.variables['Om_Ar'][:]
co3 = fh.variables['CO3'][:]
ca = fh.variables['Ca'][:]
time = fh.variables['time'][:]


alkmax =  watmax(alk)
sed_alkmax = sedmax(alk)
alkmin =  watmin(alk)
sed_alkmin = sedmin(alk)

tempmax = np.ceil(temp[:,:-13].max())  # watmax(temp)
sed_tempmax =  np.ceil(temp[:,-15:].max())#sedmax(temp)
tempmin =  watmin(temp)
sed_tempmin =  sedmin(temp)

salmax =  np.ceil(sal[:,:-13].max())#watmax(sal)
sed_salmax = np.ceil(sal[:,-15:].max())#sedmax(sal)
salmin =  np.round(sal[:,-15:].min())#watmin(sal)
sed_salmin = np.round(sal[:,-15:].min())#sedmin(sal)

kzmax =  watmax(kz)
sed_kzmax = sedmax(kz)
kzmin =  0#watmin(kz)
sed_kzmin = 0#sedmin(kz)

dicmax =  watmax(dic)
dicmin =  watmin(dic)
sed_dicmax = sedmax(dic)
sed_dicmin = sedmin(dic)

phymax =  watmax(phy)
phymin =  watmin(phy)
sed_phymin = sedmin(phy)
sed_phymax = sedmax(phy)

hetmax =  watmax(het)
hetmin = watmin(het)
sed_hetmax =  sedmax(het)
sed_hetmin =  sedmin(het)

no3max =  watmax(no3)
sed_no3max =  sedmax(no3)

po4max =  watmax(po4)
sed_po4max =  sedmax(po4)

nh4max =  watmax(nh4)
sed_nh4max =  sedmax(nh4)

ponmax = watmax(pon)
sed_ponmax = sedmax(pon)

donmax = watmax(don)
sed_donmax = sedmax(don)

o2max = watmax(o2)
o2min = 0#watmin(o2)
sed_o2max = sedmax(o2)
sed_o2min = 0#sedmin(o2)

mn2max = watmax(mn2)
sed_mn2max = sedmax(mn2)

mn3max = watmax(mn3)
#print mn3max 
sed_mn3max = sedmax(mn3)
#print sed_mn3max
mn4max = watmax(mn4)
sed_mn4max = sedmax(mn4)

h2smax = watmax(h2s)
sed_h2smax = sedmax(h2s)

mnsmax = watmax(mns)
sed_mnsmax = sedmax(mns)

mnco3max = watmax(mnco3)
sed_mnco3max = sedmax(mnco3)

fe2max = watmax(fe2)
sed_fe2max = sedmax(fe2)

fe3max = watmax(fe3)
sed_fe3max = sedmax(fe3)

fesmax = watmax(fes)
sed_fesmax = sedmax(fes)

feco3max = watmax(feco3)
sed_feco3max = sedmax(feco3)

no2max = watmax(no2)
sed_no2max = sedmax(no2)

s0max = watmax(s0)
sed_s0max = sedmax(s0)

s2o3max = watmax(s2o3)
sed_s2o3max = sedmax(s2o3)

so4max = watmax(so4)
sed_so4max = sedmax(so4)
so4min = watmin(so4)
sed_so4min = sedmin(so4)

simax = watmax(si)
sed_simax = sedmax(si)

si_partmax = watmax(si_part)
sed_si_partmax = sedmax(si_part)

baaemax = watmax(baae)
sed_baaemax = sedmax(baae)

bhaemax = watmax(bhae)
sed_bhaemax = sedmax(bhae)


sed_baanmin = 0#sedmin(baan)
baanmin = 0#watmin(baan)
baanmax = watmax(baan)
sed_baanmax = sedmax(baan)

bhanmax = watmax(bhan)
sed_bhanmax = sedmax(bhan)

caco3smax = watmax(caco3)
sed_caco3smax = sedmax(caco3)

fes2max = watmax(fes2)
sed_fes2max = sedmax(fes2)

ch4max = watmax(ch4)
sed_ch4max = sedmax(ch4)

phmax = watmax(ph)
phmin = watmin(ph)
sed_phmax = sedmax(ph)
sed_phmin = sedmin(ph)

pco2max = watmax(pco2)
sed_pco2max = sedmax(pco2)

om_camax = watmax(om_ca)
sed_om_camax = sedmax(om_ca)

om_armax = watmax(om_ar)
sed_om_armax = sedmax(om_ar)

co3max = watmax(co3)
sed_co3max = sedmax(co3)

camax = watmax(ca)
sed_camax = sedmax(ca)




    



#print kz
fh.close()