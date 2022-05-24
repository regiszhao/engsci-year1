#%%
# PROBLEM 1

def count_evens(L):
    num_even_ints = 0
    for num in L:
        if num % 2 == 0:
            num_even_ints += 1
    return num_even_ints



# %%
# PROBLEM 2

def list_to_str(lis):
    string_rep = ''
    for i in range(len(lis)):
        if i == 0:
            string_rep += str(lis[i])
        else:
            string_rep += ', ' + str(lis[i])
    return '[' + string_rep + ']'



# %%
# PROBLEM 3

def lists_are_same(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True



# %%
# PROBLEM 4

def simplify_fraction(n, m):
    for i in range(n, 0, (n // abs(n)) * -1):
        if (n % i == 0) and (m % i == 0):
            return str(n // abs(i)) + '/' + str(m // abs(i))


# %%
# PROBLEM 5

import math

def num_terms(n):
    real_pi = int(math.pi * (10 ** (n - 1)))
    compared_num = 0
    fake_pi = 0
    term = 0
    while compared_num != real_pi:
        # print("hello")
        fake_pi += ((-1) ** term) / (2 * term + 1)
        # print(fake_pi*4)
        compared_num = int((fake_pi * 4) * (10 ** (n - 1)))
        # print(compared_num)
        term += 1
    return term

def pi(precision):
    x = 0
    for i in range(0,precision):
        x += ((-1) ** i) / (2 * i + 1)
    return x*4

# %%
# PROBLEM 6

def euclid_gcd(n, m):
    a, b = abs(n), abs(m)
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return str(n // b) + '/' + str(m // b)
