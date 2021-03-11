import psi4
import numpy as np

radii = np.linspace(1.5, 5, num = 100)
Es = np.empty(len(radii))
for i in range(len(radii)):
	psi4.set_memory('4 GB')
	oh = psi4.geometry('0 3\nsymmetry c2v\nO\nH 1 0.961581\nH 1 0.961581 2 104.180105\nO 1 {} 2 127.9099475 3 180.0'.format(radii[i]))
	psi4.set_options({'reference':'uhf', 'basis':'aug-cc-pvtz', 'scf_type':'pk', 'e_convergence':10})
	psi4.set_module_options('ccenergy',{'maxiter':100})
	e = psi4.energy('ccsd(t)')
	psi4.core.clean()
	Es[i] = e

arrout = np.column_stack((radii,Es))
np.savetxt('data.dat', arrout)

