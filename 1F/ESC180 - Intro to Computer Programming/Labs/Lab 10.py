#%%
# PROBLEM 1

def power(x, n):
    # base case
    if n == 0:
        return 1
    
    return x * power(x, n-1)

def power2(x, n):
    # base case
    if n == 0:
        return 1
    
    a = n // 2
    b = n - a
    return power2(x, a) * power2(x, b)

# %%
# PROBLEM 2

a = [1,3,5,7,9]
b = [2,4,6,8,10]

def interleave(L1, L2):
    # base case
    if len(L1) == len(L2) == 1:
        return [L1[0], L2[0]]
    
    res = interleave(L1[:-1], L2[:-1])
    res.extend([L1[-1], L2[-1]])
    return res

# %%
# PROBLEM 3

l = [1,2,3,4,5,6,7,8,9,10]

def reverse_rec(L):
    # base case
    if len(L) == 1:
        return L
    
    res = reverse_rec(L[1:])
    res.extend([L[0]])
    return res

# %%
# PROBLEM 4

l = [1,2,3,4,5,6,7,8,9,10]

def zigzag(L):
    # base case
    if len(L) == 1:
        print(L[0])
    elif len(L) == 2:
        print(L[0])
        print(L[1])
    
    else:
        zigzag(L[1:-1])
        print(L[0])
        print(L[-1])

# %%
# PROBLEM 5

s = "(well (I think), recursion ()works like that (as far as I know))"

def is_balanced(s):
    if not "(" in s and not ")" in s:
        return True
    if  not "(" in s or not ")" in s:
        return False
    else:
        if s.find("(") < s.find(")"):
            s = s.replace("(", "", 1)
            s = s.replace(")", "", 1)
            return is_balanced(s)
        else:
            return False


# %%
def thank_samantha_for_being_an_amazing_ta(num_exclamation_marks):
    print("THANK YOU SAMANTHA" + num_exclamation_marks*"!")

# %%
