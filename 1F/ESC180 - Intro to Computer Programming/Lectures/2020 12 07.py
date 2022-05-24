def halt(function_text, function_input):
    '''Return True if the function halts (i.e. there is no infinite
    loop in it) and False otherwise'''

def confused(f):
    if halt(f, f):
        while True:
            pass
    else:
        return False

# What is confused(confused)
# Supoose halt(confused, confused) is True. So confused(confused) halts.
# Therefore confused(confused) doesn't halt.
# Contradiction.

# Supposed halt(confused, confused) is False. So confused(confused) does not
# halt. But if halt(confused, confused) is False. But also confused(confused)
# does halt. Contradiction.

# A computer cannot detect if a loop is infinite or not.

###############################################################################

# GOEDEL'S THEOREM:

# There are true statements that cannot be proven

# If any true statement can be proven, then we can write halt(function_text, function_input),
# but we can't, so not any true statement can be proven

# To determine whether halt(f, x) is True:
# Generate all strings s over the latin alphabet:
# For every s, check whether it's a proof that f(x) halts (if yes, return True)
#              check whether it's a proof that f(x) doesn't halt (if yes, return False)
# 
# If any true statement can be proven, eventually, I'll return either True or False when
# I find the appropriate proof