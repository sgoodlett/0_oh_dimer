import psi4
import sys
import numpy as np
import os

par = sys.argv[1]
os.chdir(f'{par}')
arr = np.loadtxt('file.txt')
Es = np.empty(len(arr[:,0]))
for i in range(len(arr[:,0])):
	g = arr[i,:]
	psi4.set_memory('4 GB')
	strang = '0 3\nO {} {} {}\nO {} {} {}\nH {} {} {}\nH {} {} {}'.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11])
	oh = psi4.geometry(strang)
	#psi4.core.be_quiet()
	psi4.set_options({'reference': 'uhf','basis':'aug-cc-pvdz','maxiter':500, 'scf_type': 'pk', 'e_convergence':10})
	e = psi4.energy('ccsd(t)')
	psi4.core.clean()
	Es[i] = e
np.savetxt('energy.txt',Es)

