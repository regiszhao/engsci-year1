#%%

import numpy as np #from numpy import *
import matplotlib.pyplot as plt

a1 = np.array([1, 2, 3])

def inv_x(x):
    return 1.0/x

rand_array = np.random.random([2,5])

# methods:
# a1 > 2 - gives back an array of bools
# np.random.random()
# np. where(condition) - gives where condition is true (don't use with 2D arrays)
# np.arange(m, n, step_size) - gives an array of range m to n
# a1[[1,3]] - can obtain values in an array at multiple indices

###############################################################################

# Review "NumPy and Monte Carlo integration" document on course website
# %%
