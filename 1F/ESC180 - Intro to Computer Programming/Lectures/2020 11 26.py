# Sets: like a list, but no order
# Like a dictionary without values
#%%
s1 = {131,4,2,55}
s2 = {'hi', 41}
for e in s1:
    print(e)

# Converting between list and set
L1 = list(s1)
L1 = set(L1)

# Sets are mutable
# For an immutable set:
s3 = frozenset(L1)

# to create an empty set:
L = set([])


# intersection method: finds elements in common between two objects
a = {1, 2, 3}
b = a.intersection({1, 3, 5})

# union method:
# update method:


# %%
#############################################################################
#############################################################################
#############################################################################

# useful dictionary methods:

d = {1:2, 3:4}

# .get(key, default)    returns value at key, or default if key is not in dict
print(d.get(1, 42))

def manual_get(d, k, default):
    if k in d:
        return d[k]
    else:
        return default

# if we want to add dictionary entries to a dictionary
d = {1:2, 3:4}
to_add = {5:6}
d.update(to_add)        # overwrites key value pairs if they already exist in d

def manual_update(d, to_add):
    for k, v in to_add.items():
        d[k] = v