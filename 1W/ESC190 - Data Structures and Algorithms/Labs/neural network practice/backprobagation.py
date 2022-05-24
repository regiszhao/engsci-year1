import numpy as np
import copy
np.random.seed(1)


def testing_algorithm(input):
	return 2*(input**3)+1 # final input 2x^3+1

def sigma(z):
	return 1/(1+np.exp(-z))

#######################################################
layer0 = np.zeros((1,1))
layer0_sig = copy.deepcopy(layer0)
w0 = np.random.random((1,2))
b0 = np.random.random((1,1))
layer1 = np.zeros((2,1))
layer1_sig = copy.deepcopy(layer1)
w1 = np.random.random((2,2))
b1 = np.random.random((2,1))
layer2 = np.zeros((2,1))
layer2_sig = copy.deepcopy(layer2)
w2 = np.random.random((2,2))
b2 = np.random.random((2,1))

d_layer0 = np.zeros((1,1))
d_layer1 = np.zeros((2,1))
d_layer2 = np.zeros((2,1))

def net(x):
	global layer0,w0,b0,layer1,w1,b1,layer2,w2,b2,layer0_sig,layer1_sig,layer2_sig
	layer2 = np.matmul(w2,x)+b2
	for i in range(len(layer2)):
		layer2_sig[i] = sigma(layer2[i])
	layer1 = np.matmul(w1, layer2_sig)+b1
	for i in range(len(layer1)):
		layer1_sig[i] = sigma(layer1[i])
	layer0 = np.matmul(w0, layer1_sig)+b0
	for i in range(len(layer0)):
		layer0_sig[i] = sigma(layer0[i])

def backprop(y):
	a = 0.01
	global layer0, w0, b0, layer1, w1, b1, layer2, w2, b2, d_layer2, d_layer1, d_layer0,layer0_sig,layer1_sig,layer2_sig
	# calculate dCost/dl0
	for i in range(len(d_layer0)):
		d_layer0[i][0] = -2 * (y - layer0[0])
	# calculate dCost/dl1
	#d_layer1 2x1
	for i in range(len(d_layer1)):
		d_layer1[i][0] = d_layer0[0][0] * layer1_sig[i][0] * (1-layer1_sig[i][0]) * w0[0][i]
		w0[0][i] -= a* (d_layer0[0][0]) * (layer1_sig[i][0])
	net(x)
	# updated the w values
	for i in range(len(d_layer2)):
		for j in range(len(d_layer1)):
			d_layer2[i][0] += d_layer1[j][0] * layer2_sig[i][0] * (1-layer2_sig[i][0]) * w1[j][i]
			w1[j][i] -= a * (d_layer1[j][0]) * layer2_sig[i][0]
	net(x)

	for i in range(len(x)):
		for j in range(len(d_layer2)):
			w2[j][i] -= a * (d_layer2[j][0]) * x[i][0]

x = np.random.random((2,1))
y = x[0][0]**3+5*x[1][0]+9
print('input is', x, 'output is', y)
print()
net(x)
print('using weighted layer, output is', layer0)
for i in range(1000):
	backprop(y)
	print('compare correct:',y, 'output is', layer0)
########################################################

# def cost(x, w, b):
# 	'''take in x=> calculate output using both algorithm as well as NN'''
#     return (0.8-net(10, 15, w, b)[0])**2 +  (0.4-net(12, 8, w, b)[0])**2

# def dCostd():


# def dCostdW10(w, b):
#     y, h1, h2, h3, h4 = net(10, 15, w, b)
#     dCostdW10_1 = -2*(0.8-y) * y * (1 - y) * h4

#     y, h1, h2, h3, h4 = net(12, 8, w, b)
#     dCostdW10_2 = -2*(0.4-y) * y * (1 - y) * h4

#     return dCostdW10_1 + dCostdW10_2

# def dCostdW1_x(x1, x2, y, w, b):
#     yhat, h1, h2, h3, h4 = net(x1, x2, w, b)

#     dCostdh3 = -2*(y-yhat) * yhat * (1 - yhat) * w[9]
#     dCostdh4 = -2*(y-yhat) * yhat * (1 - yhat) * w[10]

#     dCostdh1 = h3*(1-h3) * w[5] * dCostdh3 + h4*(1-h4) * w[7] * dCostdh4
#     dCostdh2 = h3*(1-h3) * w[6] * dCostdh3 + h4*(1-h4) * w[8] * dCostdh4

#     dCostdW1 = h1 * (1-h1) * x1 * dCostdh1

#     return dCostdW1

# def dCostdW1(w, b):
#     return dCostdW1_x(10, 15, 0.8, w, b) + dCostdW1_x(12, 8, 0.4, w, b)

# w = np.random.random((11,))
# b = np.random.random((6,))

# w_h = w.copy()
# w_h[10] += 0.01
# print( (cost(w_h, b) - cost(w, b))/0.01  )
# print(dCostdW10(w, b))


# w_h = w.copy()
# w_h[1] += 0.0001
# print( (cost(w_h, b) - cost(w, b))/0.0001  )
# print(dCostdW1(w, b))
