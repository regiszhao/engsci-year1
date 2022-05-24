#%%
# Infinite loop - L is changing forever
L = [4,5,6]
for e in L:
    print(L)
    input("Press any key: ")
    L.append(e)

# could use 'continue' or 'break' to fix
# lesson is - don't modify list in a loop while going through elements
# of a loop
# %%

#remove all entries that equal 4.0
L = [2.3,3,9,4,0,1.3,2.3]
for i in range(len(L)):
    if L[i] == 4.0:
        del L[i]
# will produce error - index out of range
# since removed an element during the loop but range 
# was determined before the loop

#%%
L = [2.3, 3.9, 4.0, 4.0, 1.3, 2.3]
i = 0
while i < len(L):
    if L[i] == 4.0:
        del L[i]
    else:
        i += 1





# %%###########################################################################
# DICTIONARIES
grades = {'PHY':90, 'CIV':100, 'PRA':65, 'CSC':'TBD'}
grades['PRA'] = 66
    #key        #value   pairs

# KEYS MUST BE IMMUTABLE
# using list as a key produces error
for key in grades:
    print(key)

# ways to view elements of dictionary
print(list(grades.keys()))
print(list(grades.values()))
print(list(grades.items()))

for key in grades:
    print(key, grades[key])


#%%
grades = {'PHY': 'A', 'PRA': 'A-', 'CALC': 'A-', 'CSC': 'A+'}

def get_subj(grades, target_grade):
    subjects = []
    for subj, grade in grades.items():
        if grade == target_grade:
            subjects.append(subj)
    return subjects


# Invert a dictionary: make a new dictionary whose keys are the values
# of the input dictionary, and whose values are lists of keys in the input
# dict that correspond to particular values

def invert_grades(grades):
    inverted_grades = {}
    for grade in grades.values():
        inverted_grades[grade] = get_subj(grades, grade)
    return inverted_grades




# %%##########################################################################
# TUPLES
# like lists but immutable
# therefore a tuple as a key is allowed
a = (4,5,6)
grades[('a', 'b')] = 'hi'

for key, value in grades.items():
    print(key, value)

# unpacking a tuple
four, five, six = a        #four = 4, five = 5, six = 6

# %%
