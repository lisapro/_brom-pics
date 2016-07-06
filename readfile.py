'''
Created on 24. jun. 2016

@author: ELP
'''

#!/usr/bin/python
# Filename: readfile.py
# Import standard (i.e., non GOTM-GUI) modules.

from netCDF4 import Dataset

my_example_nc_file = 'BROM_out.nc'
try: 
    fh = Dataset(my_example_nc_file, mode='r')
#    process(fh)
    print fh.variables
#numday = fh.variables['time'][:] 
    alk = fh.variables['Alk'][:] 
    fickAlk = fh.variables['fick:Alk'][:]
    temp = fh.variables['T'][:]
    sal = fh.variables['S'][:]
    time = fh.variables['time']
    depth = fh.variables['z'][:] #middle points
    depth2 = fh.variables['z2'][:] #at interfaces 
    kz = fh.variables['Kz'][:]
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

    y2max = 110 #(sed_wat interface)
    to_float = []
    for item in depth:
        to_float.append(float(item)) #make a list of floats from tuple 
    depth_sed = [] # list for storing final depth data for sediment 
    v=0  
    for i in to_float:
        v = (i- y2max)*100  #convert depth from m to cm
        depth_sed.append(v)

finally: 
    if fh: 
        fh.close()