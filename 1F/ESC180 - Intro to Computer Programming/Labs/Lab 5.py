#%%
# PROBLEM 1
def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
    else:
        return False
    return True

def list1_start_with_list2_2(list1, list2):
    return (len(list1) >= len(list2)) and (list2 == list1[:len(list2)])


# %%
# PROBLEM 2
def match_pattern(list1, list2):
    len_list1 = len(list1)
    len_list2 = len(list2)
    if len_list1 >= len_list2:
        for i in range(len(list1) - len_list2 + 1):
            if list2 == list1[i:i+len_list2]:
                return True
    return False


# %%
# PROBLEM 3
def repeats(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True
    return False


# %%
# PROBLEM 4a
def matrix_dim(M):
    rows = len(M)
    columns = len(M[0])
    print(str(rows) + 'x' + str(columns))

# PROBLEM 4b
def mult_M_v(M, v):
    num_columns_M = len(M[0])
    if num_columns_M == len(v):
        result = []
        for row in M:
            entry = 0
            for i in range(num_columns_M):
                entry += row[i] * v[i]
            result.append(entry)
        return result
    return 'Error.'

# PROBLEM 4c
def matrix_mult(M1, M2):
    num_rows_M1 = len(M1)
    num_columns_M1 = len(M1[0])
    num_columns_M2 = len(M2[0])
    if num_columns_M1 == len(M2):
        result = [([0] * num_columns_M2) for i in range(num_rows_M1)]
        for i in range(num_rows_M1):
            for j in range(num_columns_M2):
                entry = 0
                for x in range(num_columns_M1):
                    entry += M1[i][x] * M2[x][j]
                result[i][j] = entry
        return result
    return 'Error.'