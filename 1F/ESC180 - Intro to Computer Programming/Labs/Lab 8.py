# PROBLEM 1
#%%
f = open('Lab8.txt', 'r')
for line in f.readlines():
    if line.lower().find('lol') != -1:
        print(line[:-1])
f.close()


#%%
# PROBLEM 2

d = {3:6, 7:2, 88:13, -44:2}

def dict_to_str(d):
    '''Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated by a 
    newline character from each other.'''
    str_dict = ''
    for key, value in d.items():
        str_dict += str(key) + ', ' + str(value) + '\n'
    return str_dict



# %%
# PROBLEM 3

d = {3:6, 7:2, 88:13, -44:2}

def dict_to_str_sorted(d):
    '''Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated by a 
    newline character from each other, and are sorted in ascending order
    by key.'''
    unsorted_pairs = []
    for key, value in d.items():
        string_rep = str(key) + ', ' + str(value) + '\n'
        unsorted_pairs.append(string_rep)
    sorted_pairs = sorted(unsorted_pairs)
    res = ''
    for pair in sorted_pairs:
        res += pair
    return res



# %%
# PROBLEM 4
cmudict = open('cmudict-0.7b', 'r')
dictionary = {}
line = cmudict.readline()
while line:
    if line[:3] != ';;;':
        word_phones = line.split('  ')
        dictionary[word_phones[0]] = word_phones[1].split()
    line = cmudict.readline()
cmudict.close()

for item in dictionary.items():
    print(item)
# %%
