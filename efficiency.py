import xraylib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

energies = np.arange(0.1, 200, 0.01)  # x (energies) ranges from 0.1 to 200 keV with stepsize 0.01

def quantum_ef(z_w, z_c, dens_w, thck_w, dens_c, thck_c, energies): 
    qe_list = []
    for energy in energies:
        # window parameters
        att_w = xraylib.CS_Total(z_w, energy)  # mass attenuation coefficient of window material(cm^2 /g)
        lin_w = att_w * dens_w  # linear attenuation coefficient of the window material (1/cm)
        window = lin_w * (thck_w * (10**(-4)))
        
        # crystal parameters
        att_c = xraylib.CS_Total(z_c, energy)  # mass attenuation coefficient of the crystal material (cm^2 /g)
        lin_c = att_c * dens_c  # linear attenuation coefficient of the crystal material(1/cm)
        crystal = lin_c * thck_c * 10**(-1)
        
        # dead layer parameters
        dead_layer = lin_c * (0.15 * (10**(-4)))
        
        qe = np.exp(-window - dead_layer) * (1 - np.exp(-crystal))  # estimation of the quantum efficiency using the formula
        qe_list.append(qe)
    return qe_list

"""
z_w = atomic number of window element (for example Be would be 4)

z_c = atomic number of crystal element (for example Si would be 14)

dens_w = density of the window (g/cm3)

thck_w = thickness of the window (mm)

dens_c = density of the crystal (g/cm3)

thck_c = thickness of the crystal (mm)

energies = array of energies for example from 1 to 500 keV with stepsize 1 -> np.arange(1, 500, 1)
"""

# Plots
plt.plot(energies, quantum_ef(z_w=4, z_c=14, dens_w=1.848, thck_w=25, 
                              dens_c=2.329, thck_c=1, energies=energies), label="SDD", linewidth=1)
plt.plot(energies, quantum_ef(z_w=4, z_c=32, dens_w=1.848, thck_w=125, 
                              dens_c=5.323, thck_c=6, energies=energies), label="HPGe", linewidth=1)

# Set labels and scaling
ax = plt.gca()  # get axes
plt.title("")  # edit title
plt.legend()

# x-axis formatting
plt.xlabel("Energy [KeV]")
plt.xscale('log')
plt.xlim((0.5, 200))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:g}'.format(x)))  # show 1 instead of 10^0 etc

# y-axis formatting
plt.ylabel("$\epsilon$")
plt.yscale('log')
plt.ylim((0.01, 1))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))  # show 1 instead of 10^0 etc

plt.show()
