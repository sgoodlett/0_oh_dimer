import psi4
import sys
import numpy as np
import os

par = sys.argv[1]
os.chdir(f'{par}')
g = np.loadtxt('file.txt')
psi4.set_memory('4 GB')
strang = '0 3\nO {} {} {}\nO {} {} {}\nH {} {} {}\nH {} {} {}'.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11])
oh = psi4.geometry(strang)
#psi4.core.be_quiet()
psi4.set_options({'reference': 'uhf','basis':'aug-cc-pvdz','maxiter':500, 'scf_type': 'pk', 'e_convergence':9,'basis_guess':True,'stability_analysis':'follow','soscf':True,'soscf_max_iter':25})
psi4.set_module_options('ccenergy',{'maxiter':100})
e = psi4.energy('ccsd(t)')

np.savetxt('energy.txt',e)


