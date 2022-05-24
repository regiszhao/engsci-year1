#%%
# Return maximum number of a's followed by a b in the string s
def n_as_plus_b(s):
    for length in range(len(s), -1, -1):
        if 'a' * length + 'b' in s:
            return length

#more efficient method
def n_as_plus_b2(s):
    cur_run = 0 #number of a's in the current run
    cur_max_run = -1 #the max run of a's in aaa...aab sequence

    for i in range(len(s)):
        if s[i] == 'b':
            cur_max_run = max(cur_max_run, cur_run)
            cur_run = 0
        elif s[i] == 'a':
            cur_run += 1
        else:
            cur_run = 0
    return cur_max_run

# %% ####################################################################
# ALL POSSIBILITY/COMBINATION PROBLEMS
alpha = 'abcdefghij'
# gives all possible 3 character combinations
for c1 in alpha:
    for c2 in alpha:
        for c3 in alpha:
            print(c1 + c2 + c3)


# %% ##################################################################
# a way to change the code while running:

code = '''a = 5
b = a + 10
print(b)
'''
code = '''def f():
    return 5'''

s = 'I got {} on the calc midterm'.format(12)
# format inserts (parameter) into {} in string

code = '''def f():
    return {}'''.format(12)

# to run code: exec(code)


# %%

# Write a function with a nested loop with N levels that
# prints all passwords of length N
# Loop length changes based on value of N (possible because we are changing
# code within function)
N = 4

def gen_all_passwords_len(N):
    code = ''
    for i in range(N):
        code += 'for c{} in alpha:\n'.format(i)
        code += '   ' * (i + 1)
    code += 'print('
    for i in range(N-1):
        code += 'c{}'.format(i) + ' + '
    code += 'c{}'.format(N-1)
    code += ')'
    return code

alpha = 'abc'
code = gen_all_passwords_len(4)
# %%
