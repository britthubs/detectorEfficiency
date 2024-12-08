import xraylib
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

energies = np.arange(1, 500, 1) # x ranges from 1 -> 500 with stepsize 1

def quantum_ef(z_w, z_c, dens_w, thck_w, dens_c, thck_c, energies): 
    qe_list = []
    for i in energies:
        e = int(i) 
        att = xraylib.CS_Total(z_w, e) # mass attenuation coefficient of window material(cm^2 /g)
        lin_w = att * dens_w # linear attenuation coefficient of the window material (1/cm)
        att = xraylib.CS_Total(z_c, e) # mass attenuation coefficient of the crystal material (cm^2 /g)
        lin_c = att * dens_c # linear attenuation coefficient of the crystal material(1/cm)
        qe = np.exp(-lin_w* thck_w *10**(-1)) * (1 - np.exp(-lin_c * thck_c *10**(-1))) # estimation of the quantum efficiency using the formula
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
plt.plot(energies, quantum_ef(z_w=4, z_c=14, dens_w=1.848, thck_w=0.25, 
                              dens_c=2.33, thck_c=1, energies=energies), label="Si detector")
plt.plot(energies, quantum_ef(z_w=4, z_c=32, dens_w=1.848, thck_w=0.005, 
                              dens_c=5.323, thck_c=2, energies=energies), label="Ge detector")
# plt.axvline(x=30)
plt.xlabel("Energy [KeV]")
plt.ylabel("$\epsilon$")
plt.title("") # edit title
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.show()
