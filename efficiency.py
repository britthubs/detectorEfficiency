import xraylib
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

energies = np.arange(1, 500, 1) # x ranges from 1 -> 500 with stepsize 1

def quantum_ef(z_w, z_c, dens_w, thck_w, dens_c, thck_c, energies): 
    qe_list = []
    for i in energies:
        e = int(i) 
        # window parameters
        att_w = xraylib.CS_Total(z_w, e) # mass attenuation coefficient of window material(cm^2 /g)
        lin_w = att_w * dens_w # linear attenuation coefficient of the window material (1/cm)
        window = lin_w* thck_w
        
        # crystal parameters
        att_c = xraylib.CS_Total(z_c, e) # mass attenuation coefficient of the crystal material (cm^2 /g)
        lin_c = att_c * dens_c # linear attenuation coefficient of the crystal material(1/cm)
        crystal = lin_c * thck_c *10**(-1)
        
        # dead layer parameters
        dead_layer = lin_c * 0.15 * 10**(-4) 
        
        qe = np.exp(-window -dead_layer) * (1 - np.exp(-crystal)) # estimation of the quantum efficiency using the formula
        qe_list.append(qe)
    return(qe_list)

"""
z_w = atomic number of window element (for example Be would be 4)

z_c = atomic number of crystal element (for example Si would be 14)

dens_w = density of the window (g/cm3)

thck_w = thickness of the window (mm)

dens_c = density of the crystal (g/cm3)

thck_c = thickness of the crystal (mm)

energies = array of energies for example from 1 to 500 keV with stepsize 1 -> np.arange(1, 500, 1)
"""



# plots two data sets (2 detectors), add more if you want
plt.plot(energies, quantum_ef(z_w=4, z_c=14, dens_w=1.848, thck_w=0.025, 
                              dens_c=2.33, thck_c=1, energies=energies), label="Si detector")
plt.plot(energies, quantum_ef(z_w=4, z_c=32, dens_w=1.848, thck_w=0.125, 
                              dens_c=5.323, thck_c=6, energies=energies), label="Ge detector")
# plt.axvline(x=30)
plt.xlabel("Energy [KeV]")
plt.ylabel("$\epsilon$")
plt.title("") # edit title
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.show()
