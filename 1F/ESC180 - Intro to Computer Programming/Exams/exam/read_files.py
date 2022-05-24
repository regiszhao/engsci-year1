
#%%
import os
filenames = os.listdir("diseases") # Obtain a list of the files in the folder
                                   # diseases
f = open("diseases/" + filenames[0]) # Open the first file in the folder diseases
text0 = f.read()
f.close()
print(text0[:2000])  # Output the first 2000 characters in the file we opened

def process_text(filename):
    punctuation = [".", ",", "!", "?", "-"]
    infile = open(filename, 'r')
    txt = infile.read()
    for punc in punctuation:
        txt = txt.replace(punc, '')
    txt = txt.lower()
    txt = txt.replace("\n", " ")
    l = txt.split()
    return l

def word_dict(L):
    d = {}
    for word in L:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d

def most_freq_word(d):
    highest_freq = 0
    most_word = ''
    for word, freq in d.items():
        if freq > highest_freq:
            most_word = word
            highest_freq = freq
    return most_word

def most_common_frequent_word(files):
    most_freq_list = []
    for filename in files:
        processed_text = process_text(filename)
        word_freq = word_dict(processed_text)
        most_frequent_word = most_freq_word(word_freq)
        most_freq_list.append(most_frequent_word)
    print(most_freq_list)
    mcfw_dict = word_dict(most_freq_list)
    print(mcfw_dict)
    return most_freq_word(mcfw_dict)
# %%
