'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''
#%%
import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    dot_prod = 0
    sqrd_sum_vec1 = 0
    sqrd_sum_vec2 = 0
    for word, x in vec1.items():
        dot_prod += (x * vec2.get(word, 0))
        sqrd_sum_vec1 += x**2
    for y in vec2.values():
        sqrd_sum_vec2 += y**2
    return dot_prod / math.sqrt(sqrd_sum_vec1 * sqrd_sum_vec2)


def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        reduced_sentence = list(set(sentence))
        len_red_sent = len(reduced_sentence)
        for i in range(len_red_sent):
            if reduced_sentence[i] not in d:
                d[reduced_sentence[i]] = {}
            for j in range(i+1, len_red_sent):
                # adding reduced_sentence[j] to reduced_sentence[i]
                cur_value = d[reduced_sentence[i]].get(reduced_sentence[j], 0)
                d[reduced_sentence[i]][reduced_sentence[j]] = cur_value + 1
                # adding reduced[i] to reduced[j]
                if reduced_sentence[j] not in d:
                    d[reduced_sentence[j]] = {}
                cur_value = d[reduced_sentence[j]].get(reduced_sentence[i], 0)
                d[reduced_sentence[j]][reduced_sentence[i]] = cur_value + 1
    return d


def build_semantic_descriptors_from_files(filenames):
    punc = [',', '-', '--', ':', ';']
    sentences = []
    for f in filenames:
        txt = open(f, 'r', encoding='latin1').read().replace('!', '.').replace('?', '.').lower()
        for p in punc:
            txt = txt.replace(p, ' ')
        txt = txt.replace('  ', ' ')
        txt = txt.split('.')
        for i in range(len(txt)):
            txt[i] = txt[i].split()
        sentences.extend(txt)
    res = build_semantic_descriptors(sentences)
    return res


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    sem_sim_high = -1
    most_similar = choices[0]
    word_vec = semantic_descriptors.get(word, 0)
    if word_vec != 0:
        for w in choices:
            w_vec = semantic_descriptors.get(w, 0)
            if w_vec != 0:
                sem_sim = similarity_fn(word_vec, w_vec)
                if sem_sim > sem_sim_high:
                    sem_sim_high = sem_sim
                    most_similar = w
    return most_similar


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct_answers = 0
    total_qs = 0
    test = open(filename, 'r')
    for line in test.readlines():
        total_qs += 1
        q = line.split()
        if q[1] == most_similar_word(q[0], q[2:], semantic_descriptors, similarity_fn):
            correct_answers += 1
    test.close()
    grade = (correct_answers/total_qs) * 100
    return grade


# data_source = ['war_and_peace.txt', 'swanns_way.txt']
# semantic_descriptors = build_semantic_descriptors_from_files(data_source)
# grade = run_similarity_test('test.txt', semantic_descriptors, cosine_similarity)
# print(grade)
# %%

