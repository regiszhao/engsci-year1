#%%
import numpy as np
np.random.seed(0)

def sigma(z):
    return 1/(1 + np.exp(-z))

def calc_h(x1, x2, w1, w2, b):
    return sigma(x1*w1 + x2*w2 + b)

def net(x1, x2, w, b):
    '''Returns y, h1, h2, h3, h4. x1 and x2 are inputs, w and b are lists of weights and biases'''
    h1 = calc_h(x1, x2, w[1], w[2], b[1])
    h2 = calc_h(x1, x2, w[3], w[4], b[2])

    h3 = calc_h(h1, h2, w[5], w[6], b[3])
    h4 = calc_h(h1, h2, w[7], w[8], b[4])

    y = calc_h(h3, h4, w[9], w[10], b[5])
    return y, h1, h2, h3, h4

def cost(w, b):
    y1 = net(10, 15, w, b)[0]
    y2 = net(12, 8, w, b)[0]
    return (y1 - 0.8)**2 + (y2 - 0.4)**2

def dC_dw10(w10):
    pass

w = np.random.random((11,))
b = np.random.random((6,))
# %%
