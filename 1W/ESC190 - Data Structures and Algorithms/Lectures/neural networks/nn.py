import numpy as np
np.random.seed(1)



def sigma(z):
    return 1/(1+np.exp(-z))




def net(x1, x2, w, b):
    h1 = sigma(x1 * w[1] + x2*w[2] + b[1])
    h2 = sigma(x1 * w[3] + x2*w[4] + b[2])

    h3 = sigma(h1 * w[5] + h2*w[6] + b[3])
    h4 = sigma(h1 * w[7] + h2*w[8] + b[4])

    y = sigma(h3* w[9] + h4*w[10] + b[5])

    return y, h1, h2, h3, h4


def cost(w, b):
    return (0.8-net(10, 15, w, b)[0])**2 +  (0.4-net(12, 8, w, b)[0])**2


def dCostdW10(w, b):
    y, h1, h2, h3, h4 = net(10, 15, w, b)
    dCostdW10_1 = -2*(0.8-y) * y * (1 - y) * h4

    y, h1, h2, h3, h4 = net(12, 8, w, b)
    dCostdW10_2 = -2*(0.4-y) * y * (1 - y) * h4

    return dCostdW10_1 + dCostdW10_2

def dCostdW1_x(x1, x2, y, w, b):
    yhat, h1, h2, h3, h4 = net(x1, x2, w, b)

    dCostdh3 = -2*(y-yhat) * yhat * (1 - yhat) * w[9]
    dCostdh4 = -2*(y-yhat) * yhat * (1 - yhat) * w[10]

    dCostdh1 = h3*(1-h3) * w[5] * dCostdh3 + h4*(1-h4) * w[7] * dCostdh4
    dCostdh2 = h3*(1-h3) * w[6] * dCostdh3 + h4*(1-h4) * w[8] * dCostdh4

    dCostdW1 = h1 * (1-h1) * x1 * dCostdh1

    return dCostdW1

def dCostdW1(w, b):
    return dCostdW1_x(10, 15, 0.8, w, b) + dCostdW1_x(12, 8, 0.4, w, b)

w = np.random.random((11,))
b = np.random.random((6,))

w_h = w.copy()
w_h[10] += 0.01
print( (cost(w_h, b) - cost(w, b))/0.01  )
print(dCostdW10(w, b))


w_h = w.copy()
w_h[1] += 0.0001
print( (cost(w_h, b) - cost(w, b))/0.0001  )
print(dCostdW1(w, b))

