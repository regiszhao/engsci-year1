# SELECTION SORT

# at iteration i, find the max element in L[:(n-i)] and swap max value
# with value at end of list L[:(n-i)]

#%%
def max_i(L):
    '''Return the index of the largest element in L. If there is more than
    one max element,return the index of the first one.'''

    cur_max = L[0]
    cur_max_i = 0

    for i in range(1, len(L)):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_i = i
    return cur_max_i


def selection_sort(L):
    '''Modify L so that it's sorted in increasing (non-decreasing) order'''
    
    for j in range(len(L)):
        ind_of_max = max_i(L[:len(L)-j])
        L[ind_of_max], L[len(L)-j-1] = L[len(L)-j-1], L[ind_of_max]

# Worst-case complexity of selection sort:
# max_i has complexity of O(n)
# j = 0: time is proportional to k(n-1)
# j = 1: time is proportional to K(n-2)
# ..........
# total: k*(n-1) + k*(n-2) + ..... + 0
#      = k*(1 + 2 + 3 + .... + (n-1)) = k*n*(n-1)/2 = k*(n^2-n)/n
# Worst case complexity: O(n^2)

#%%
# COUNTING SORT/BUCKET SORT
# gets number of the same elements, spits it back out in order

def counting_sort(L):
    '''Return a sorted version of the list of non-negative integers L'''
    max_L = max(L)
    counts = [0] * (max_L + 1)
    for e in L:
        counts[e] += 1

    result = []
    for elem in range(len(counts)):
        count = counts[elem]
        if count > 0:
            result.extend([elem] * count)
            print(elem, result)
    return result


# Worst case time complexity:
# O(len(L) + max(L))
# depends on what max(L) is - could be much larger