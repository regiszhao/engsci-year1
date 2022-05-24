################################################################################
#Q1

def most_productive_elf(toys_produced):
    most_toys = max(toys_produced.values())
    for elf, toys_produced in toys_produced.items():
        if toys_produced == most_toys:
            return elf
            
################################################################################
#Q2
            
def two_smallest(L):
    m1, m2 = max(L[0], L[1]), min(L[0], L[1])
    for i in range(2, len(L)):
        if L[i] < m1:
            m1, m2 = max(m2, L[i]), min(m2, L[i])
    
    return [m1, m2]

#Complexity: O(n), since the loop repeats n-2 times and each iteration
#takes the same amount of time
################################################################################
#Q3

def col_sum(M, col):
    s = 0
    for row in range(len(M)):
        s += M[row][col]
    return s
        
def largest_col_sum(M):
    sums = []
    for col in range(len(M[0])):
        sums.append(col_sum(M, col))
    return max(sums)
    
################################################################################
#Q4
#Run it in Python
################################################################################

#Q5a:
# L is a list with n = len(L)
total = 0.0
for item in L:
  if item > 0.0:     #line 4
    total += item    #line 5
# In the worst case, line 4 and line 5 are repeated n times, since we go through
# the entire list, which is of length n. If addition and assignment are a 
# constant-time operations (which we can assume here), the block consisting of 
# lines 4 and 5 takes the same amount of time every time it runs. So the runtime 
# is proportion to n, i.e., it is O(n).
#  
#  
#Q5b:
# L is a list with n = len(L)
a = 5
for i in range(n):
  for j in range(5):
    a = i*j               #line 5
 
# The block inside the innermost loop (line 5) is repeated 5n times, since the 
# outer loop repeats n times, and the inner loop repeats 5 times every time. 
# Assuming (as we should) that multiplication and assignment are constant time 
# operations, that means that the runtime is proportional to 5n, i.e., it is 
# proportion to n as well. That means that the runtime is O(n).
#  
 
# Q5c is just print_all() from the Dec. 7 lecture: 
# http://www.cs.toronto.edu/~guerzhoy/180/lectures/W13/lec1/print_all.py

################################################################################
  
def filter_out_odds(L):
    if len(L) == 0:
        return []
    if L[0] % 2 == 0:
    	return [L[0]] + filter_out_odds(L[1:])
    else:
	    return filter_out_odds(L[1:])
################################################################################
#Q7
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

#The function splits the string s over the elements of L, and returns
#a list with all the elements and the splitters in it, in the order
#that they appear in s. For example,
#f("23+3-10", ["+", "-"]) returns ["23", "+", "3", "-", "10"]    

        
        
################################################################################
#Q8

def consume_all(decomp, op):
    def mult(a, b):
        return a * b
    
    def add(a, b):
        return a + b
        
    ops = {"+": add, "*": mult}
    
    while op in decomp:
        i = decomp.index(op)
        
        decomp[i-1:i+2] = [str(ops[op](int(decomp[i-1]), int(decomp[i+1])))]
    
    return decomp

def ev(expr):
    decomp = f(expr, ["*", "+"])
    decomp = consume_all(decomp, "*")
    decomp = consume_all(decomp, "+")
    return int(decomp[0])
    
ev("1*4+2*3*2+2")    
        
################################################################################
#Q9a
#mystery(L, e) returns True iff e in L


#Q9b
#Note that initally, mystery is called with j-i = len(L), and then each time
#there are two (or three, but the third call is smaller, similarly to the
#analysis of mergeSort) calls that mystery makes to itself, with j-i = len(L)//2

#The call tree is (with the numbers equal to j-i)

#            1   1 1   1 1    1    1   1     1   1 1  1 1  1  1
#
#                      ....................................
#                            n/4   n/4    ..  ..
#                               \/         \/
#                                n/2     n/2
#                                   \  / 
#                                     n   

#Each call takes the same amount of time, so we just need to add up the numbers
#of calls on each level. This is the same as the number of calls in
#MergeSort, which is O(n)
#https://www.youtube.com/watch?v=Owbm_iYDWxs&feature=youtu.be
#
#In this case, the number of calls is proportional to the runtime, so the 
#complexity is O(n) as well.






                               
