#%%

def construct_D_arr(L1, L2):
    # initialize array:
    len1 = len(L1)
    len2 = len(L2)
    D = [[0 for i in range(len2)] for i in range(len1)]
    for i in range(len1):
        D[i][0] = i
    
    

# %%
