import efficiency as ef
import matplotlib.pyplot as plt
import numpy as np

energies = np.arange(1, 500, 1) # x ranges from 1 -> 500 with stepsize 1

# plots two data sets (2 detectors), add more if you want
plt.plot(energies, ef.quantum_ef(z_w=4, z_c=14, dens_w=1.848, thck_w=0.25, 
                              dens_c=2.33, thck_c=1, energies=energies), label="Si detector")
plt.plot(energies, ef.quantum_ef(z_w=4, z_c=32, dens_w=1.848, thck_w=0.005, 
                              dens_c=5.323, thck_c=2, energies=energies), label="Ge detector")
# plt.axvline(x=30)
plt.xlabel("Energy [KeV]")
plt.ylabel("$\epsilon$")
plt.title("") # edit title
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.show()
