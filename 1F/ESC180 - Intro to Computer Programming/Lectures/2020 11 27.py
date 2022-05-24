# MERGE SORT
# Sort first half, then second half of list, then merge two halves

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    mid = len(L) // 2
    sorted1 = merge_sort(L[:mid])
    sorted2 = merge_sort(L[mid:])
    return merge(sorted1, sorted2)

def merge(L1, L2):
    '''Return the sorted version of L1 + L2, where
    L1 + L2 are sorted lists of ints'''
    i1 = 0  # index of L1
    i2 = 0  # index of L2
    res = []
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            res.append(L1[i1])
            i1 += 1
        else:
            res.append(L2[i2])
    res.extend(L1[i1:])
    res.extend(L2[i2:])
    return res

# Complexity:
# Number of calls to merge: 1 + 2 + 4 + 8 + ... + 2^log2n
#                  O(n) calls
# but each call to merge takes different amt of time depending on length of L
# merge has linear complexity, O(len(L1)+len(L2))
# a merge call at each level takes:
#   k*len(L) seconds
# so first level takes k*n seconds, 2nd level takes 2*k*(n/2) seconds
# 3rd level takes 4*k*(n/4), so each level takes k*n seconds
# since there are log2n levels:
# Complexity is O(nlogn)

###########################################################################
###########################################################################
###########################################################################

# Comparison-based sort algorithms:

# Decisions about how to arrange the sorted version of the list are based on
# code in the format: 
# if L[i] < L[j]:
# ...
# else:
# ....
# In total, for a given len(L) = n, we have n! possible solutions to the
# problem of sorting the list L (n! possible arrangements of the list)

# if-statement #1: ideally narrow down possible solutions to n!/2
# if-statement #2: ideally .............................. to n!/4
# ...
# in best case, we need log2(n!) if-statements to narrow down the possible
# solutions to 1

# Stirling's approxiamtion: log2(n!) is O(nlogn)
# therefore the best complexity a comparsion based sort can achieve is O(nlogn)