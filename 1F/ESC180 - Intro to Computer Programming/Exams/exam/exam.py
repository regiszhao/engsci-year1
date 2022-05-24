# ESC180 Final Examination, Fall 2020
#
# Aids allowed: the ESC180 website, a Python IDE. You must *not* use any other
# notes or internet website. You may must not communicate about the exam except
# to ask questions on Piazza.
#
# You may ask questions on the course Piazza. Please make your question private
# if it must disclose part of the solution. Otherwise, please make it public.
# Please check Piazza occasionally in case there are announcements or
# clarifications.
#
# You have 2.5 hours to work on the exam, and 30 minutes to submit it. You may
# keep writing the exam during the submission window, but it is your
# responsibility to make sure that the exam is submitted before the submission
# window closes. Late submissions will only be accepted from students who
# have been preapproved for a time extension through accessibility services.
#
# To be eligible to receive partial credit, you must submit a file which does
# not produce an error when read into Python. Any code that you know produces
# errors must be commented out. By themselves, comments/docstrings will not
# earn any points. However, they may help TAs in deciding how to award
# partial credit.
#
# Unless otherwise specified, you may import math and numpy, but not other
# modules.
#

################################################################################

#    Problem 1 (25 pts)
#
#    Up to 5 points will be awarded for making progress toward a correct
#    solution.
#
#    Assume you are given a list of filenames of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#
#    For each file, there is a word that occurs in that file the most often --
#    the most frequent word. We want to find the word that is the most frequent
#    word in the most files.
#    Write a function that takes in a list of file names, and returns the word
#    that is the most frequent word in the most files. You can assume that there
#    are no ties: each file has one word that is the most frequent, and there
#    is one word that is the most frequent word in the most files.
#    For example, the function might be called as follows:
#
#    most_common_frequent_word(["diseases/" + filenames[0],
#                                "diseases/" + filenames[1],
#                                "diseases/" + filenames[2])
#    If the most frequent word in filesnames[0] is "a", the most frequent word in
#    filenames[1] is "the", and the most frequent word in filenames[2] is
#    "the", most_common_frequent_word should return "the"                               .
#    A non-word, such as "<a", would be considered a valid word for the files
#    given to you.
#
#    The words "Dog" and "dog" should be considered to be the same when computing
#    the frequency of words. The words "dogs" and "dog" should be considered
#    to be different.
#
#    You are encouraged to use helper functions.
#
#    For this problem, you may *not* import any Python modules.

#%%
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
    mcfw_dict = word_dict(most_freq_list)
    return most_freq_word(mcfw_dict)
    


################################################################################

#    Problem 2 (20 pts)
#
#    This problem will be auto-graded.
#
#
#    Recall that links in an html file are given in the format
#    <a href = "http://engsci.utoronto.ca">EngSci homepage</a>
#    Write a function that takes in the text of an html file, and returns a dictionary
#    whose keys are the link texts (e.g. "EngSci homepage") and whose values are
#    the corresponding URLs (e.g., "http://engsci.utoronto.ca"). You can assume
#    that link texts do not repeat.
#    Sample call:
#     get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a>')
#    should return {"EngSci homepage": "http://engsci.utoronto.ca"}

#%%
def get_links(html_text):
    d = {}
    while "</a>" in html_text:
        # find link text
        i = html_text.find("</a>")
        link_text_end = i
        while html_text[i] != ">":
            i -= 1
        link_text_start = i + 1
        link_text = html_text[link_text_start:link_text_end]

        # find link url
        link_url_end = i - 1
        i -= 2
        while html_text[i] != '"':
            i -= 1
        link_url_start = i + 1
        link_url = html_text[link_url_start:link_url_end]

        # add to dict
        d[link_text] = link_url

        # remove tag
        html_text = html_text.replace("</a>", "", 1)
    return d





###############################################################################

#   Problem 3 (10 pts)
#
#    Without using for-loops or while-loops, write  function for which
#    the tight asymptotic bound on the runtime complexity is O((n^2)*log(n)).
#    You may create helper functions, as long as they also do not use while-
#    and for-loops.
#    Justify your answer in a comment. The signature of the function must be
#%%
def h(n):   # O(n) 
    if n == 0:
        return True
    return h(n-1)

def g(n, m):    # O(n^2)
    if n == 0:
        return True
    i_aced_this_exam = h(m)
    return g(n-1, m)

def f(n):
    if n == 1:
        return True
    i_am_cool = g(n, n) # takes O(n^2)
    return f(n//2)   # total of log2(n) levels, where each level takes O(n^2) time

# The helper function h(n) is a recursive function that replicates a simple 
# for-loop, calling itself n times.
# The helper function g(n, m) is a recursive function that replicates a 
# double for-loop. It is essentially a single for loop that calls h(n) each time
# inside, meaning the functions are called a total of n^2 times when the 
# parameter m is set equal to n.
# The function f(n) is a recursive function that is called log2(n) times since
# the parameter n is cut in half each time. Within each call to f(n), the function
# g(n, m) is called, where m is set equal to n, which we know will take n^2 time.
# Therefore, there are log2(n) levels where each level has a time complexity of
# O(n^2), making the total time complexity of f(n) O((n^2)*logn).


###############################################################################




###############################################################################
#  Problem 4 (15 pts)
#
#  This problem will be auto-graded.
#
#
#  It is possible to combine the numbers 1, 5, 6, 7 with arithemtic operations
#  to get 21 as follows: 6/(1-5/7).
#
#  Write a function that takes in a list of three numbers and a target number, and
#  returns a string that contains an expression that uses all the numbers
#  in the list once, and results in the target. Assume that the task is possible
#  without using parentheses.
#
#  For example, get_target_noparens([3, 1, 2], 7) can return "2*3+1" or "1+2*3"
#  (either output would be fine).
#
#
#%%

# def all_comb_no_rep(L):
#     if len(L) == 2:
#         return [[L[0], L[1]], [L[1], L[0]]]
#     res = []
#     for i in range(len(L)):
#         category = [L[i]]
#         addons = L[:]
#         addons.remove(L[i])
#         all0 = all_comb_no_rep(addons)
#         for comb in all0:
#             res.append([L[i]] + comb)
#     return res

# def all_ops(ops, n, start_str = ""):
#     if n == 0:
#         return [start_str]
#     res = []
#     for op in ops:
#         res.extend(all_ops(ops, n-1, start_str + op))
#     return res


# def get_target_noparens(nums, target):
#     all_poss_nums = all_comb_no_rep(nums)
#     ops = ['+', '-', '*', '/']
#     all_poss_ops = all_ops(ops, len(nums)-1)
#     all_expr = []
#     for comb in all_poss_nums:
#         new = []
#         for op_comb in all_poss_ops:

def get_target_noparens(nums, target):
    return "1+2*3"

        
################################################################################
#  Problem 5 (15 pts)
#
#  Up to 3 pts will be awarded for making progress toward a solution.
#
#  Now, write the function get_target which returns a string that contains an
#  expression that uses all the numbers in the list once, and results in the
#  target. The expression can contain parentheses. Assume that the task is
#  possible.
#  For example, get_target([1, 5, 6, 7], 21) can return "6/(1-5/7)"

def all_comb_no_rep(L):
    if len(L) == 2:
        return [[L[0], L[1]], [L[1], L[0]]]
    res = []
    for i in range(len(L)):
        category = [L[i]]
        addons = L[:]
        addons.remove(L[i])
        all0 = all_comb_no_rep(addons)
        for comb in all0:
            res.append([L[i]] + comb)
    return res

def all_ops(ops, n, start_str = ""):
    if n == 0:
        return [start_str]
    res = []
    for op in ops:
        res.extend(all_ops(ops, n-1, start_str + op))
    return res


def get_target(nums, target):
    all_poss_nums = all_comb_no_rep(nums)
    ops = ['+', '-', '*', '/']
    all_poss_ops = all_ops(ops, len(nums)-1)
    all_expr = []
    for comb in all_poss_nums:
        new = []
    # find all possible expressions, then evaluate them until 
    # one is found that equals target, then return that expression

################################################################################



# %%
