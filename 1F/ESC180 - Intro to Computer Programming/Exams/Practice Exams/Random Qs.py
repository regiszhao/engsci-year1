# 2015 Q5
#%%

L1 = [4,8,10]
L2 = [2,5,7]

def merge(L1, L2):
    if len(L1) == 0:
        return L2
    if len(L2) == 0:
        return L1
    
    if L1[0] <= L2[0]:
        res = [L1[0]]
        res.extend(merge(L1[1:], L2))
    elif L1[0] > L2[0]:
        res = [L2[0]]
        res.extend(merge(L1, L2[1:]))
    return res




# 2016 Q10
# %%

friends = {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
"Gottfried Leibniz": ["Carl Gauss"],
"Isaac Newton": ["Carl Gauss", "Charles Babbage"],
"Ada Lovelace": ["Charles Babbage", "Michael Faraday"], 
"Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
"Michael Faraday":["Ada Lovelace"] }

def is_clique(group, friends):
    for person in group:
        for pot_friend in group:
            if pot_friend != person:
                if pot_friend not in friends[person]:
                    return False
    return True

def all_subsets(L):
    if len(L) == 0:
        return [[]]

    all0 = all_subsets(L[1:])
    new = []
    for subset in all0:
        new.append([L[0]] + subset)
    return new + all0

def max_clique(friends):
    all_possible_cliques = all_subsets(list(friends))
    biggest = []
    for group in all_possible_cliques:
        if is_clique(group, friends):
            if len(group) > len(biggest):
                biggest = group
    return biggest


# %%
