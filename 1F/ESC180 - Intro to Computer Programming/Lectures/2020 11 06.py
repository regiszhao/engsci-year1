# BOZOSORT
#%%
import random
def is_sorted_nondecreasing(L):
    '''Return True iff L is sorted in non-decreasing order'''

    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True

def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i, j = int(len(L)*random.random()), int(len(L)*random.random())
        L[i], L[j] = L[j], L[i]
    return L

# n = len(L)
# n! permutations of all
# we expect to go through every permutation of L once, on average
# informally, the algorithm runs in O(n!), on average
# %%
s = 0
n = 31842952
for i in range(n):
    for j in range(int(n/2)):
        s += i+j    # runs n^2/2 times
#%%
def fermat(p):
    n = 1
    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p + j**p == k**p:
                        return i, j, k
        n += 1

#%%
# the complexity of adding large integers: O(n), where n = num_digits of longer int
#                                        = O(log(x)), where x is larger number

# excpet for integers, all numerical variables in Python are limited in magnitude
# addition, multiplication of floats: can take to be a constant


# multiplicaiton of integers:
# long multiplication algorithm: O(n^2), where n = num_digits of larger number
# Karatsuba's algorithm: faster - O(n^1.6)