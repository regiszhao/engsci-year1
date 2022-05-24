#RECALL MERGE SORT:
# MERGE SORT
# Sort first half, then second half of list, then merge two halves

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    mid = 1
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

# what if we set mid = 1?
# Total runtime: k*(n + (n-1) + (n-2) + ... + 1) = kn(n+1)/2
# Complexity: O(n^2)
# This is called INSERTION SORT


# Python's algorithm for sorting: TimSort
# Combination of merge and insertion sort:
#       merge for large lists
#       insertion for small lists


# REVIEW OF COMPLEXITY AND CALL TREES ON COURSE WEBSITE