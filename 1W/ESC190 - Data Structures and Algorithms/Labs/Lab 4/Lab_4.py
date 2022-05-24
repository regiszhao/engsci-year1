#%%
def find(L, e):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (high + low) // 2
        if e == L[mid]:
            if L[mid-1] != e:
                return mid
            high = mid - 1
        elif e < L[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def find2(L, e):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (high + low) // 2
        if e == L[mid]:
            if L[mid+1] != e:
                return mid
            low = mid + 1
        elif e < L[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# %%
