# print all strings of length n over alphabet alphabet

def print_all(alphabet, n, start_str = ""):
    '''Print all strings over alphabet alphabet of length n,
    pre-pend the string start_str to every str'''
    if n == 0:
        print(start_str)
        return
    
    for letter in alphabet:
        print_all(alphabet, n-1, start_str + letter)

# Complexity:
# number of calls each level: 1 call, k calls, k^2 calls, ..., k^n calls
# total number of calls = 1 + k + k^2 + ... + k^n calls = (k^(n+1)-1)/(k-1)
# therefore approx O(k^n)

#%%
def all_combinations(alphabet, n, start_str = ""):
    '''Return a list of all strings over the alphabet alphabet, of length n,
    with start_str pre-pended'''

    if n == 0:
        return [start_str]
    
    res = []
    for letter in alphabet:
        res.extend(all_combinations(alphabet, n-1, start_str + letter))
    return res



# %%
# write a function that gets a list of all the subsets of a list L

def get_all_subsets(L):
    if len(L) == 0:
        return [[]]
    
    # all the subsets that contain L[0]
    # all the subsets that don't contain L[0]
    all0 = get_all_subsets(L[1:])
    res = []
    for subset in all0:
        res.append([L[0]] + subset)
    res.extend(all0)
    return res

a = get_all_subsets([1,2,3,4,5])
# %%
