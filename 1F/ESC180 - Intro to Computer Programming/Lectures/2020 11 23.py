def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# Complexity:
# each level's number of calls increases: 1, 2, 4, etc...
# but (n-1) branch is much longer than (n-2) branch
# pretend that there are n levels in total
# 1 + 2 + 4 + ... + 2^n = 2^(n+1)-1     (geometric series)
# Complexity: O(2^(n+1))

# OR define T(n) as runtime of fib(n)
# T(n) = const + T(n-1) + T(n-2)
# Therefore T(n) ~ a*fib(n)
# So we can say that worst-case complexity of fib(n) is itself:
# O(fib(n))

import math

def fib_formula(n):
    phi = (1 + math.sqrt(5)) / 2
    return int(phi**n/math.sqrt(5) + 0.5)



# Caching: storing values that the recursive function computes

def fib_cache(n, cache):
    # Cache: dictionary of fib seq values
    if n in cache:
        return cache[n]
    cache[n] = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    return cache[n]


def fib_iter(n):
    fib_prev = 1
    fib_cur = 1
    if n <= 2:
        return 1
    for i in range(3, n+1):
        # fib_prev = fib(i-1)
        # fib_cur = fib(i)
        fib_prev, fib_cur = fib_cur, fib_prev+fib_cur
    return fib_cur

############################################################################
############################################################################
############################################################################

def deep_copy(obj):
    '''Return a deep copy of a list of lists of ... lists of integers'''
    # base case:
    if type(obj) != list:
        return(obj)
    
    # recursive step: obj is a list
    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))
    
    return copy




# Built-in deep copy function:

import copy

L = [[1,2,3],[4,5,[7,8]]]
L1 = copy.deepcopy(L)
