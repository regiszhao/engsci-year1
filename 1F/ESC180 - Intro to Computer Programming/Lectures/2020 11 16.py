# RECURSION

# Example with factorial

def fact(n):
    # we need base case - where we can return the answer directly
    if n == 0:
        return 1
    # recursive step - use the function with a diff. input
    return n * fact(n-1)

# Visualization:
#       fact(0) = 1
#       .
#       .
#       .
#   fact(4)
#   |
# fact(5)

# Proof by induction that fact(n) returns n!:
# Base case: n = 0
# fact(0) returns 1, which is equal to 0!
# Inductive step:
# Assume that fact(k) returns k!
# fact(k+1) returns (k+1)*fact((k+1)-1) = (k+1)*fact(k) = (k+1)!
# By induction, for all k >= 0, fact(k) returns k!

# 1. To get the answer, you must know the answer (to a simpler question)
# 2. You can't push on a rope (you must have a base case)
# 3. F = ma

#########################################################################

# Example: determining if a number is even

def is_even(n):
    '''Return True if n is even and False if n is odd
    n -- a non-negative integer'''
    if n == 0:
        return True
    return not(is_even(n-1))

#########################################################################

# Example: printing a list element by element

L = [12, 10, 23, 10, 34, 10]

def print_list(L):
    '''Print the list L element by element, one element per line'''
    if len(L) == 0:
        return
    
    print(L[0])
    print_list(L[1:])


# to print backwards, just need to switch order of print statements:

L = [12, 10, 23, 10, 34, 10]

def print_list_backwards(L):
    '''Print the list L backwards element by element, one element per line'''
    if len(L) == 0:
        return
    
    print_list_backwards(L[1:])
    print(L[0])


###########################################################################

# Race to 21 Game

# start at 0
# 2 plyaers can alternately say +1 or +2
# first player to get to 21 wins

def is_win21(n):
    ''' Return true if being at sum n and having the turn results in a guaranteed win
    with optimal play'''

    # base case:
    if n == 19 or n == 20:
        return True
    if n == 21:
        return False
    
    # for any other number: if I can make the next possible number a losing 
    # number, then I'm winning
    # otherwise (if the next possible number is a winning number), I'm losing

    # if is_win21(n+1) == False or is_win21(n+2) == False:
    #     return True
    # else:
    #     return False

    return not is_win21(n+1) or not is_win21(n+2)

# Basically: we are trying to win by making the opponent lose