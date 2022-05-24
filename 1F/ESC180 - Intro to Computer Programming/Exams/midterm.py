# Test duration: 1 hour and 50 minutes (9:10am-11:00am)
#
# Aids allowed: any material on the course website http://www.cs.toronto.edu/~guerzhoy/180/
# You may use Pyzo (or another Python IDE) during the exam.
#
# You are responsible for submitting the file midterm.py on Gradescope.
#
# You can resubmit the file multiple times. Your last submission will be
# graded.
#
# You are responsible for making sure that the functions are named as specified
# and that there are no syntax errors. Gradescope will let you know if the
# file is incorrectly named or there are syntax errors, but you will not see
# whether the functions return the right values.
#
# Make sure that your functions RETURN, rather than PRINT, the required
# outputs.
#
# You may use
#  import math
# but you may not import other modules.
#
# Questions will be answered on Zoom: https://utoronto.zoom.us/j/92599671787

################################################################################
#
# 1 (15 pts). Write a function that returns the sum of the numbers
# 1^3 + 2^3 + ... + k^3. Assume that k >= 1
#
# For example sum_cubes(2) should return 9
#%%
def sum_cubes(k):
    result = 0
    for i in range(1, k+1):
        result += i**3
    return result


################################################################################
# 2 (15 pts). Write a function that takes in a number n, and returns the smallest
#    number k such that 1^3 + 2^3 + ... + k^3 >= n
#
#    For example, sum_cubes_num_terms(10) should return 3, since
#    1^3 + 2^3 < 10, and 1^3 + 2^3 + 3^3 >= 10

def sum_cubes_num_terms(n):
    compare = 0
    k = 0
    while compare < n:
        k += 1
        compare += k**3
    return k


################################################################################
# 3 (15 pts). A list contains 30 elements, representing the rainfall during a month. For
#    example, the following represents the rainfall data for Toronto in
#    September.
measurements = [10.4, 1.6, 2, 0.2, 0, 0, 5.2, 0, 0, 0, 0, 0, 3.8, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 2.0, 0, 0, 0, 8.4, 2.2, 5.0]

#    Write a function that returns a list that contains the three-day moving
#    average percipitation for days 2..(N-1), given a list of measurements of
#    length N. The three-day moving average for day d is the average
#    precepitation on days (d-1), d, (d+1). Assume the input list contains
#    at least three numbers.
#    If measurements is a list of length N, moving_average(measurements) should
#    return a list of length N-2.

def moving_average(measurements):
    if len(measurements) >= 3:
        result = []
        for i in range(1, len(measurements) - 1):
            average = (measurements[i-1] + measurements[i] + measurements[i+1]) / 3
            result.append(average)
        return result
    return 'Error.'


################################################################################
# 4. (15 pts) A pattern matches a string "with wraparound" if it is possible to match
#    the pattern to the string while possibly wrapping the pattern around.
#    For example, the pattern "abc" matches the string "zabcz"
#    with wraparound (though wrapping around was not used). The string "czz"
#    matches "zabcz" with wraparound, since it's possible to read czz by
#    starting at "zabcz"[3:5] and then continuing to the other z wrapping around.
#    On the other hand, "czy"  doesn't match "zabcz".
#    Write a function match(pattern, text) that returns True if pattern matches
#    text (possibly using wraparound), and False otherwise.
#
#    You can access the contents of a string similarly to lists:
#    >> my_str = "abc"
#    >> my_str[1:3]
#    "bc"
#    >> my_str[1]
#    "b"

def match(pattern, text):
    len_pattern = len(pattern)
    len_text = len(text)
    for i in range(len_text):
        if i + len_pattern <= len_text:
            if pattern == text[i:i+len_pattern]:
                return True
        else:
            if pattern == text[i:] + text[:len_pattern - (len_text - i)]:
                return True
    return False


################################################################################
# 5 (15 pts). Matrices can be represented as lists of lists. Write a function
#    that takes in two matrices of size m x n (m rows and n columns), and
#    returns True iff the matrices have at least n-1 of the same columns.
#    For example, consider the following:

M1 = [[1, 2, 3],
      [1, 5, 1],
      [1, 2, 2]]

M2 = [[3, 1, 0],
      [1, 1, 2],
      [2, 1, 0]]

#    M2 contains the first and the third column of M1, so M1 and M2 share
#    (3-1) columns, and so share_n1(M1, M2) should return True
#
#    The function should return True for matrices that are equal.
#
#    share_n1(M1, M2) should return False if M1 and M2 share fewer than
#    (n-1) columns, where n is the number of columns in M1

def switch_to_col(M):
    new = []
    for i in range(len(M[0])):
        column = []
        for j in range(len(M)):
            column.append(M[j][i])
        new.append(column)
    return(new)

def share_n1(M1, M2):
    M1_columns = switch_to_col(M1)
    M2_columns = switch_to_col(M2)
    num_matches = 0
    for column in M1_columns:
        if column in M2_columns:
            num_matches += 1
        if num_matches >= len(M1_columns) - 1:
            return True
    return False


# %%
