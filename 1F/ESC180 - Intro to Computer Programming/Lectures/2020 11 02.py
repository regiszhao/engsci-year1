#%%

# 'aasjdgazzzzzzbgebagzzzzzzzzzzzzzzzzzzjgr', 'z'

def longest_run1(s, c):
    run = 0
    max_run = 0

    if c == 'z':
        s += 'y'
    else:
        s += 'z'
    
    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else: run += 1
    
    return max_run
# Worst case complexity of this function?????
# overall runtime: b + a*n
# therefore runtime complexity: O(n) for n = len(s)


def longest_run2(s, ch):
    for longest in range(len(s), -1, -1):
        cur_run = 0
        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0
            if cur_run == longest:
                return longest
    return 0
#Runtime complexity: O(n^2)


import time
#100000000
def f(n):
    for i in range(n):
        pass

def apply_it(f, arg1):
    return f(arg1)

def g(n):
    return n+2

def time_it(f, arg1):
    t1 = time.time()
    f(arg1)
    t2 = time.time()
    return t2 - t1

def time_it2(f, arg1, arg2):
    t1 = time.time()
    f(arg1, arg2)
    t2 = time.time()
    return t2 - t1

s = 10000000 * 'a' + 'b'
c = 'a'
print(time_it2(longest_run1, s, c))


times = []
s_lengths = []
for s_length in range(10, 10000, 1000):
    s = s_length*'a' + 'b'
    c = 'z'
    times.append(time_it2(longest_run2, s, c))
    s_lengths.append(s_length)
    print(s_length)


import matplotlib.pyplot as plt 
plt.plot(s_lengths, times)
plt.show()

# %%
