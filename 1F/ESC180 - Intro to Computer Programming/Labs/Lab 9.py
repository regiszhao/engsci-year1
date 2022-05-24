#%%
# PROBLEM 1

p_and_p = open('prideprejudice_lab9.txt', encoding='latin-1').read().split()

def word_freq(word_list):
    freq = {}
    for word in word_list:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def top10(L):
    L_sorted = sorted(L, reverse=True)
    return L_sorted[:10]

def top10_words(d):
    value_dict = {}
    for word, freq in d.items():
        if freq in value_dict:
            value_dict[freq].append(word)
        else:
            value_dict[freq] = [word]
    top_values = top10(value_dict.items())
    res = []
    for freq, word_list in top_values:
        res.extend(word_list)
    return res


# %%
# PROBLEM 2 - refer to Hello, World_lab9.html

# PROBLEM 3
import urllib.request

def num_results_yahoo(search_term):
    search_term = search_term.replace(' ', '+')
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=" + search_term + "&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
    page = f.read().decode("utf-8")
    end_i = page.index('results</span>') - 1
    start_i = end_i
    while page[start_i-1] != '>':
        start_i -= 1
    num_results = int(page[start_i:end_i].replace(',', ''))
    f.close()
    print(num_results)
    return num_results

def choose_variant(variants):
    res_high = -1
    most_freq_var = ''
    for variant in variants:
        print('"' + variant + '"')
        num_res = num_results_yahoo('"' + variant + '"')
        print(variant, num_res)
        if num_res > res_high:
            res_high = num_res
            most_freq_var = variant
    return most_freq_var

print(choose_variant(["top ranked school uoft", "top ranked school waterloo"]))
