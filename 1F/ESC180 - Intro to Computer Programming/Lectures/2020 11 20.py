# From last lecture:

def f(L):
    mid = len(L) // 2
    return f(L[:mid])

def g(L, start, end):
    mid = (start + end) // 2
    g(L, 0, mid)


# What's the complexity of this function:

def sum_list2(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    
    mid = len(L) // 2
    return sum_list2(L[:mid]) + sum_list2(L[mid:])


# if n = len(L)
# at base case level: sumlist is called n times
# the results of these calls are passed up to next level where
# sumlist is called n/2 times, then n/4, then n/8 etc...
# keeps happening - number of calls increases exponentially each level (base 2)
# so total number of calls is the sum of number of calls in each level: a geometric series
# Sum of the geometric series: 1 + r^1 + r^2 ... r^k = (1-r^(k+1))/(1-r)
# 1 + 2 + 4 ... n = 1 + 2^1 + 2^2 ... + n       (n = 2^log2(n))
# 1 + 2 + 4 ... 2^(log2(n)) = (1-2^(log2(n)+1)/(1-2)) = 2^(log2(n)+1) - 1
# = 2*2^log2(n) - 1 = 2n - 1
# therefore: complexity is O(n)

# another way to see it:
# number of calls = geometric series: n + n/2 + n/4 + n/8 .... + 1
# the infinite geometric series n + n/2 + n/4... = 1
# so total number of calls = n + 1      O(n)

#####################################################################################
#####################################################################################
#####################################################################################

# function to calculuate factorial
def fact_while(n):
    '''Return n!'''

    cur_prod = 1    # cur_prod = (i-1)!
    i = 1

    while i != n+1:
        cur_prod *= i
        i += 1
        # Invariant: cur_prod = (i-1)!

    return cur_prod





def func(a = 2, b = 3):        # you can set default values for functions
    return a + b

# Calculating factorial with recursion:

def fact_iter(n, cur_prod = 1, i = 1):
    '''Return n!
    Arguments: n -- an integer, cur_prod = (i-1)!'''

    if i == n + 1:
        return cur_prod
    return fact_iter(n, cur_prod*i, i+1)


def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n-1)

############################################################################
############################################################################
############################################################################
############################################################################

def power(x, n):
    '''Return x^n'''
    res = 1
    for i in range(n):
        res *= x
    return res
# O(n) time complexity

# Using recursion:
def power_rec(x, n):
    '''Return x^n'''
    if n == 0:
        return 1
    return x * power_rec(x, n-1)

# there are n + 1 calls of power_rec, so complexity is O(n)



# To compute x^n faster:
# instead of thinking of x^n = x*x^(n-1).....
# x^n = x^(n/2)^2, e.g. x^8 = (x^4)^2, and (x^4) = (x^2)^2, and (x^2) = (x^1)^2

def power_rec_fast(x, n):
    '''Return x^n'''

    if n == 0: 
        return 1
    if n == 1:
        return x
    
    half_power = power_rec_fast(x, n//2)
    # x^n = half_power*half_power      if n is even
    # x^n = half_power*half_power*x    if n is odd
    if n%2 == 0:
        return half_power ** 2
    else:
        return (half_power ** 2) * x

# levels: 1, 2, 4, 8, ....., n
# number of levels (number of calls) = log2(n)
# Complexity: O(log2(n))