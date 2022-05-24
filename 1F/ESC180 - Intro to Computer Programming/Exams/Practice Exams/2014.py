
# QUESTION 1
#%%
toys_produced = {"Bob":4000, "Gloria":7000, "Hugo":6000, "Grumbles":42}

def most_productive_elf(toys_produced):
    elf_goat = ''
    most_toys = 0
    for name, num_toys in toys_produced.items():
        if num_toys > most_toys:
            elf_goat = name
            most_toys = num_toys
    return elf_goat



# QUESTION 2
# %%

L = [5, 3, 10, 4]

def two_smallest(L):
    res = [0,0]
    for i in range(1,-1,-1):
        lowest = L[0]
        for num in L:
            if num < lowest:
                lowest = num
        res[i] = lowest
        L.remove(lowest)
    return res

# The time complexity of this function is O(n)
# The inside loop loops through the list of integers one at a time.
# Assuming that L.remove costs O(n) time at the maximum (since it searches
# the list for the first occurence of some value), then the worst case
# scenario is that we loop through the list 4 times - O(4n) --> O(n)




# QUESTION 3
# %%

M = [[1, 2, 3, 4],  [5, 0, 5, 0], [6, 7, 8, 9]]

def sum_column(M, col_to_sum):
    total = 0
    for row in M:
        total += row[col_to_sum]
    return total

def largest_col_sum(M):
    num_columns = len(M[0])
    largest_sum = sum_column(M, 0)
    for i in range(1, num_columns):
        cur_sum = sum_column(M, i)
        if cur_sum > largest_sum:
            largest_sum = cur_sum
    return largest_sum



# QUESTION 5
# %%
# O(n)
# O(n)
# O(k^n)


# QUESTION 6
# %%

L = [5, -2, 4, 0, 3, 7, 8]

def filter_out_odds(L):
    if len(L) == 0:
        return []
    
    res = filter_out_odds(L[:-1])
    if L[-1] % 2 == 0:
        res.extend([L[-1]])
    return res



# QUESTION 7
# %%

def elem_in_elems(L, e):
    for sub in L:
        if e in sub:
            return True
    return False

def f(s, L):
    #s is a string, L is a list of strings
    res = [s]
    for e in L:
        if not elem_in_elems(res, e):
            continue
        prev_res = res[:]
        res = []
        for sub_res in prev_res:
            split_list = sub_res.split(e)
            for i in range(len(split_list)-1):
                res.extend([split_list[i], e])
            res.append(split_list[-1])
    return res

def ev(expr):
    L = ['+', '-', '*']
    split_expr = f(expr, L)
    for i in range(0, len(split_expr), 2):
        split_expr[i] = int(split_expr[i])
    if len(split_expr) == 1:
        return split_expr[0]
    while '*' in split_expr:
        i = split_expr.index('*')
        split_expr.insert(i-1, split_expr[i-1]*split_expr[i+1])
        for j in range(3):
            split_expr.pop(i)
    res = split_expr[0]
    for i in range(2, len(split_expr)):
        if split_expr[i-1] == '+':
            res += split_expr[i]
        else:
            res -= split_expr[i]
    return res

expr = '14-3*2'

# %%
