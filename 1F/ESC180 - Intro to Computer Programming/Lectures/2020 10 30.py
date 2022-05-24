# EFFICIENCY OF ALGORITHMS

def find_i(L, e):
    '''Return the index of the element that's equal to e
     in the list L, or None if e is not in L'''
    
    for i in range(len(L)):     # 1 operation
        if L[i] == e:           # 2 operations
            return i            # 1 operation
    return None                 # 1 operation

# Worst-case runtime complexity, in OPERATIONS
# The number of operations that the computer will perform for a given input,
# in the worst case, for an input of size n (e.g. n = len(L))

# Approximation:
#   each operation takes t seconds
#   then in worst case we take (2*n + 2) * t seconds (roughly 2*t*n seconds)

#In this case, worst case: we perform (2*n + 2) operations
# the worst-case runtime complexity of find_i(L, e) is O(n)

# if the runtime is proportional to (2*n + 2) we say the runtime is O(n)
# Intuitively: the runtime is proportional to the size of the input n

# DEFINITION - big O notation
# Suppose f(n) is the worst-case runtime for an input of size n
# f(n) is O(f(n)) if lim     sup   f(n)/g(n) < infinity
                #   N->inf   n>=N
# Looking at ratio between f(n) and g(n)
# g(n) must not grow slower than f(n)

# 2n + 1 is O(n)
# 0.5n is O(n^2)
# sqrt(100000*n) is O(n)    (also O(sqrt(n)))

# the worst-case runtime complexity of find_i(L, e) is O(len(L))
#                                                      O(n) for n = len(L)

# Usually we want to give a tight asymtotic bound on the
# worst-case runtime complexity (meaning O(g(n)) where g(n) grows as slowly
# as possible
# 2n + 1 is O(n^2) (but we want to say O(n))

# n is not O(sqrt(n))
# 2^n is not O(n^2)

# 0.00001n^2 + 28n + 1000 is O(n^2)


# BINARY SEARCH
# Task: given a sorted list L of length n, determine whether element e
#       is in the list

# L = [1, 10, 20, 25, 30, 100, 1000]
# e = 22
# is e smaller than the middle element of L?
#   if yes: just look in the first half
#   if no: look in the second half
#   repeat with the half list

#%%
def binary_search(L, e):
    low = 0     # lowest index of current list
    high = len(L) - 1   # highest index

    #currently looking at L[low:(high)+1]
    # keep track of high - low
    # initially: high-low = n-1
    # 2nd iteration: high-low < (n-1)/2
    # 3rd iteration: high-low < (n-1)/4
    # ......
    # stop when high-low < 2

    # 1,2,4,8......., n-1
    # takes log2(n-1) steps

    while high - low >= 2:
        mid = (low + high) // 2
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid
    
    # high - low < 2
    if L[low] == e:
        return low
    elif L[high] == e:
        return e
    return None

# worst-case runtime complexity: O(log(n))
# log2(n) = log(n)/log(2)