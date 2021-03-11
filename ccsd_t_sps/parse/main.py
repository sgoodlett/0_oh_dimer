import numpy as np
import os

arr = np.loadtxt('geoms.txt')
l = len(arr[:,0])
#k = 6000
#m = l // k
#for i in range(k-1):
#	os.mkdir(f'arrdir/{i}')
#	a = m*i
#	b = a + m
#	np.savetxt(f'arrdir/{i}/file.txt',arr[a:b,:])
#os.mkdir(f'arrdir/{k-1}')
#last = (k-1)*m
#np.savetxt(f'arrdir/{k-1}/file.txt',arr[last:,:])

limit = 2000
iter1 = 0
iter2 = 0
for i in range(l):
	if iter2 >= limit:
		iter2 = 0
		iter1 += 1
	if iter2 == 0:
		os.mkdir(f'arrdir/{iter1}')
	os.mkdir(f'arrdir/{iter1}/{iter2}')
	np.savetxt(f'arrdir/{iter1}/{iter2}/file.txt',arr[i])
	iter2 += 1
