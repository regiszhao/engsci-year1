#%%
# APPLICATIONS OF DICTIONARIES:
# SPARSE MATRICES:

a = [[1, 0, 0, 2],
     [0, 0, 0, 5]]

# this matrix can be represented as:
sparse_a = {(0,0): 1, (0,3):2, (1,3): 5}

def sparse_mat_to_mat(sparse, dims):
    # dims[0] rows, dims[1] colums
    mat = []
    for row in range(dims[0]):
        mat.append([0] * dims[1])

    for coord, value in sparse.items():
        mat[coord[0]][coord[1]] = value

    return mat

def mult_sparse_by_vec(sparse, vec, m):
    '''Multiply the sparse matrix sparse by the vector vec.
    matrix: m x n, vector: n x 1, product: m x 1'''
    out = [0] * m
    for coord, value in sparse.items():
        out[coord[0]] += value * vec[coord[1]]
    return out

###############################################################################
# %%
# FILES
# if file is in same directory as python file
f = open('mypoem.txt')
poem = f.read()  # .read() gives one big string
lines = poem.split('\n')

for line in lines:
    print(line)

# if you want to read lines 
f = open('mypoem.txt')
lines = f.readlines()   # .readlines() gives list of lines
for line in lines:
    print(line)

f = open('mypoem.txt')
for line in f.readlines():
    print(line)

# %%
f = open('proust.txt')
text = f.read()

sentences = text.replace('!',',').replace('?','.').split('.')
num_sentences = len(sentences)

words = text.split(' ')
num_words = len(words)


#%%
# WRITING TO FILES
f = open('hamlet.txt', 'w')
text = 'To be or not to be, that is the question'
f.write(text)
f.close()
#saves to same directory as python file