import numpy as np
na = np.array([90, 120, 150, 180])
nb = np.array([10, 20, 30, 40])

nc = np.array([[90, 85, 95], [70, 95, 85]])

nz = na + nb
print(nz)
print("--------")
print(nc)
print("--------")
print(np.transpose(nc))
