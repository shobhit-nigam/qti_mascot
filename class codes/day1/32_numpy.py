import numpy as np
na = np.array([90, 120, 150, 180])
nb = np.array([10, 20, 30, 40])

nc = np.array([[90, 85, 95], [70, 95, 85]])

nz = na + nb
print(nc)

nd = nc.reshape(-1)
print(nd)

# np.mean()    np.std()   np.median() 
