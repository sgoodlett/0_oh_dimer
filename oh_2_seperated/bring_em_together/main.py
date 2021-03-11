import psi4
import numpy as np

radii = np.linspace(5, 25, num = 100)
Es = np.empty(len(radii))
for i in range(len(radii)):
	psi4.set_memory('4 GB')
	oh = psi4.geometry('0 3\nsymmetry c2h\nO\nO 1 {}\nH 1 0.97 2 90.0\nH 2 0.97 1 90.0 3 180.0\n'.format(radii[i]))
	psi4.set_options({'reference':'uhf', 'basis':'aug-cc-pvtz', 'scf_type':'pk', 'e_convergence':10})
	psi4.set_module_options('ccenergy',{'maxiter':100})
	e = psi4.energy('ccsd(t)')
	psi4.core.clean()
	Es[i] = e

fred = np.column_stack((radii,Es))
np.savetxt('data2.dat', fred)

