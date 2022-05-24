#%%
#Needed for array() and dot()
from numpy import *


#Printing matrices using NumPy:

# #Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# M = array(M_listoflists)
# #Now print it:
# print(M)

def print_matrix(M_lol):
    print(array(M_lol))
    return

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

def get_row_to_swap(M, start_i):
    row_to_swap = start_i
    lowest_lead_ind = get_lead_ind(M[start_i])
    for i in range(start_i, len(M)):
        lead_ind = get_lead_ind(M[i])
        if lead_ind < lowest_lead_ind:
            lowest_lead_ind = lead_ind
            row_to_swap = i
    return row_to_swap

def add_rows_coefs(r1, c1, r2, c2):
    len_row = len(r1)
    new_row = [0] * len_row
    for i in range(len_row):
        new_row[i] = (c1 * r1[i]) + (c2 * r2[i])
    return new_row

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        M[i] = add_rows_coefs(M[i], M[row_to_sub][best_lead_ind], M[row_to_sub], -M[i][best_lead_ind])
    return M

def forward_step(M):
    for i in range(len(M) - 1):
        print('Current matrix:')
        print_matrix(M)
        # Swapping rows
        row_to_swap = get_row_to_swap(M, i)
        M[i], M[row_to_swap] = M[row_to_swap], M[i]
        print('Looking at row ' + str(i))
        print('Swapping rows ' + str(i) + ' and ' + str(row_to_swap))
        print('Current matrix:')
        print_matrix(M)
        # Eliminating coefficients
        eliminate(M, i, get_lead_ind(M[i]))
        print('Adding row ' + str(i) + ' to rows below, eliminating coeffs in column' + str(get_lead_ind(M[i])))
        print('Current matrix:')
        print_matrix(M)
        print('===============================================================')
    return M

def backward_step(M):
    for i in range(len(M) - 1, -1, -1):
        print('Current matrix:')
        print_matrix(M)
        # Eliminating coefficients above
        print('Backward step:')
        col_to_el = get_lead_ind(M[i])
        for j in range(i):
            M[j] = add_rows_coefs(M[j], M[i][col_to_el], M[i], -M[j][col_to_el])
        print('Adding row ' + str(i) + ' to rows above, eliminating coeffs in column' + str(col_to_el))
        print('Current matrix:')
        print_matrix(M)
        print('==============================================================')

    print('Now dividing each row by leading coeff:')
    for i in range(len(M)):
        lead_coeff = M[i][get_lead_ind(M[i])]
        for j in range(len(M[i])):
            M[i][j] = M[i][j] / lead_coeff
    print('Current matrix:')
    print_matrix(M)
    return M

def solve(M, b):
    # Creating augmented matrix
    for i in range(len(M)):
        M[i].append(b[i])
    
    R = backward_step(forward_step(M))
    x = []
    for row in R:
        x.append(row[-1])
    
    return x


#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = [[1,-2,3],[3,10,1],[1,5,3]]
x = [75,10,-11]
b = dot(M,x)
b = [22, 314, 92]

# print(M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]

# #To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist() 

# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

# %%
M = [[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]]
M = [[1,-2,3,22],[3,10,1,314],[1,5,3,92]]