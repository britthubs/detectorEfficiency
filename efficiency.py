import xraylib
import numpy as np
import matplotlib.pyplot as plt

energies = np.arange(1, 500, 1) # x ranges from 1 -> 500 stepsize 1

def quantum_ef(z_w, z_c, dens_w, thck_w, dens_c, thck_c, energies): 
    qe_list = []
    for i in energies:
        e = int(i)
        att = xraylib.CS_Total(z_w, e) # mass attenuation window (cm^2 /g)
        lin_w = att * dens_w # linear attenuation coef window (1/cm)
        att = xraylib.CS_Total(z_c, e) # mass attenuation crystal (cm^2 /g)
        lin_c = att * dens_c # linear attenuation coef crystal (1/cm)
        qe = np.exp(-lin_w* thck_w *10**(-1)) * (1 - np.exp(-lin_c * thck_c *10**(-1)))
        qe_list.append(qe)
    return(qe_list)

"""
------
z_w = atomic number of window element (for example Be would be 4)

z_c = atomic number of crystal element (for example Si would be 14)

dens_w = density of the window (g/cm3)

thck_w = thickness of the window (mm)

dens_c = density of the crystal (g/cm3)

thck_c = thickness of the crystal (mm)

energies = array of energies for example from 0 to 500 keV with stepsize 1 -> np.arange(1, 500, 1)
------
"""