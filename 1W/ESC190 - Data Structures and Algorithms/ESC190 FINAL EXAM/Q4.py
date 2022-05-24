import math

def norm(v):
    '''Calculates magnitude of vector'''
    sqrd_sum = 0
    for component in v:
        sqrd_sum += component**2
    return math.sqrt(sqrd_sum)

def subtract_vecs(v1, v2):
    '''Subtracts v2 from v1'''
    res = []
    for i in range(len(v1)):
        difference = v1[i] - v2[i]
        res.append(difference)
    return res

def add_vecs(v1, v2, v3):
    '''Adds 3 vectors together'''
    res = []
    for i in range(len(v1)):
        add = v1[i] + v2[i] + v3[3]
        res.append(add)
    return res

def mult_vecs(alpha, v):
    res = []
    for i in range(len(v)):
        mult = alpha*v[i]
        res.append(mult)
    return res

def cost(v, u1, u2, u3):
    '''Calculates the "cost" to be minimized'''
    x1 = norm(subtract_vecs(v, u1))
    x2 = norm(subtract_vecs(v, u2))
    x3 = norm(subtract_vecs(v, u3))
    return x1**2 + x2**2 + x3**2

def dC_dv(v, u1, u2, u3):
    '''Calculate gradient of dC WRT dv'''
    return 2*(add_vecs(subtract_vecs(v, u1), subtract_vecs(v, u2), subtract_vecs(v, u3)))

def grad_descent(u1, u2, u3):
    EPS = 0.00001
    alpha = 0.01
    # initialize vector v as zero vector
    v = [0 for i in range(len(u1))]
    cur_cost = cost(v, u1, u2, u3)
    prev_cost = cur_cost - 2*EPS

    while abs(cur_cost - prev_cost) > EPS:
        prev_cost = cur_cost
        v = subtract_vecs(v, mult_vecs(alpha, v))
    
    return v


    