#PROBLEM 2
#%%
def sum_cubes(n):
    result = 0
    for i in range(1, n+1):
        result += i**3
    return result

def sum_cubes2(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result**2

def check_sum(n):
    return sum_cubes(n) == sum_cubes2(n)

def check_sums_up_to_n(N):
    for i in range(1, N+1):
        if sum_cubes(i) != sum_cubes2(i):
            return False
    return True
# %%
#PROBLEM 3
def pi(precision):
    x = 0
    for i in range(0,precision+1):
        x += ((-1)**i) / (2*i + 1)
    return x*4
# %%
