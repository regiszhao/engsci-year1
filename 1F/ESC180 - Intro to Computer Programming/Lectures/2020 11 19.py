# FROM LAST LECTURE:
# Race to 21 Game

# start at 0
# 2 plyaers can alternately say +1 or +2
# first player to get to 21 wins

def is_win21(n):
    ''' Return true if being at sum n and having the turn results in a guaranteed win
    with optimal play'''
    if n == 19 or n == 20:
        return True
    if n == 21:
        return False
    return not is_win21(n+1) or not is_win21(n+2)

# SIMPLER VERSION TO HELP UNDERSTAND:

def is_win21_simple(n):
    '''Return True if being at sum n leads to winning the game where each player
    can only go +1 (first to reach 21 wins'''
    if n == 20:
        return True
    return not is_win21_simple(n+1)

    # 20: True
    # 19: False
    # 18: True
    # etc.....

# For the original version of iswin:
# 20: True
# 19: True
# 18: False
# 17: True (we can make opponent lose by adding 1 and their turn will be 18)
# 16: True (we can make number 18 by adding 2)
# 15: False (15+1 and 15+2 both result in a number that wins, so I lose)
# Pattern: True True False True True False etc.....
# If number is divisible by 3, it's False

# Writing strategy for computer to play Race 21:
import random

def move21(n):
    '''Return a move that wins the Race to 21 Game (with optimal play) if possible,
    otherwise return a random move'''
    if not is_win21(n+1):
        return 1
    elif not is_win21(n+2):
        return 2
    else:
        return random.randint(1,2)


# To play the game:

def game21():
    n = 0
    print('n = ', n)

    while True:
        user_move = int(input("USER'S MOVE: "))
        n += user_move
        print('n = ', n)
        if n == 21:
            print('USER WON')
            return

        computer_move = move21(n)
        n += computer_move
        print('n = ', n)
        if n == 21:
            print('COMPUTER WON')
            return

# kind of repetitious code, to make it nicer:

def game21_nice(cur_player):
    n = 0
    print('n = ', n)
    
    while n != 21:
        if cur_player == "USER":
            move = int(input("USER'S MOVE: "))
            cur_player = "COMPUTER"
        else:
            move = move21(n)
            cur_player = "USER"
        
        n += move
        print('n = ', n)
    
    if cur_player == "USER":
        print("COMPUTER WON")
    else:
        print("USER WON")


if __name__ == "__main__":
    game21()

#############################################################################
#############################################################################
#############################################################################

# MORE EXAMPLES OF RECURSION:

L = [12,10,2,10,2]

def sum_list(L):
    '''Return the sum of the list of integers L
    Define the sum of the empty list to be 0'''
    if len(L) == 0:
        return 0
    return L[0] + sum_list(L[1:])

# Complexity:
# we call sumlist len(L) + 1 times
# each call (given that value of internal call to 
#            sumlist is already known) takes same amount of time
# Runtime complexity: O(len(L)) or O(n) where n = len(L)
# we are assuming (incorrectly) that L[1:] takes a constant amt of time


# another way is:

def sum_list2(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    
    mid = len(L) // 2
    return sum_list2(L[:mid]) + sum_list2(L[mid:])