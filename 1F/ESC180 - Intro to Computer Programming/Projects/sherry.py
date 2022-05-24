import copy
'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


def norm(vec):
    '''
    Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

#v1 = {"a":1,"b":2,"c":3}
#v2 = {"b":4,"c":5,"d":6}
def cosine_similarity(vec1, vec2):
    '''
    This function returns the cosine similarity between the sparse vectors vec1
    and vec2, stored as dictionaries.
    '''
    top = 0
    for key in vec1:
        if key in vec2:
            top += (vec1[key] * vec2[key])
    bot1 = 0
    bot2 = 0
    for key in vec1:
        bot1 += (vec1[key]**2)
    for key in vec2:
        bot2 += (vec2[key]**2)

    return (top/math.sqrt(bot1*bot2))


def build_semantic_descriptors(sentences):
    '''
    This function takes in a list sentences which contains lists of strings
    (words) representing sentences, and returns a dictionary d such that for
    every word w that appears in at least one of the sentences, d[w] is itself
    a dictionary which represents the semantic descriptor of w
    (note: the variable names here are arbitrary).
    '''
    d = {}

    for sentence in sentences: #sentence in list form
        #remove duplicates of words within words
        sentence = list(set(sentence))
        inside_d = {}
        for word in sentence:
            inside_d[word] = 1


        #add semantic descriptors to main dictionary (FIX THIS LATER)
        for word in sentence:
            temp_d = copy.deepcopy(inside_d)
            del temp_d[word]
            if word not in d:
                d[word] = temp_d
            else:
                for new_word in temp_d:
                    if new_word in d[word]:
                        d[word][new_word] += 1
                    else:
                        d[word][new_word] = 1

    #print(d.keys())
    return(d)


def build_semantic_descriptors_from_files(filenames):
    '''
    This function takes a list of filenames of strings, which contains the names
    of files (the first one can be opened using open(filenames[0], "r",
    encoding="latin1")), and returns the a dictionary of the semantic
    descriptors of all the words in the files filenames.
    You should assume that the following punctuation always separates sentences:
    ".", "!", "?", and that is the only punctuation that separates sentences. You
    should also assume that that is the only punctuation that separates sentences.
    Assume that only the following punctuation is present in the texts:
    [",", "-", "--", ":", ";"]
    '''

    punctuation = [",", "-", "--", ":", ";"]
    end = ["!","?"]
    text = ""

    for i in range (len(filenames)):
        #open file
        t = open(filenames[i], "r", encoding = "latin1").read()
        t = t.lower()
        text = text + t
    #print("Finished reading text")

    for i in punctuation:
        text = text.replace(i," ")
    #print("Finished replacing punctuation")

    text = text.replace("?",".").replace("!",".")
    #print("Finished replacing endings with periods")

    while "  " in text:
        text = text.replace("  ", " ")
    #print("removed all double spaces")
    while ".." in text:
        text = text.replace("..", ".")
    #print("removed all double periods")

    #all punctuation should be removed except periods which separate sentences
    sentences = text.split(".") #text should be split into a list of sentences
    #print("separated all sentences")
    for s in range(len(sentences)):
        sentences[s] = sentences[s].split() #text should be a list of lists of words
    #print("separated all words")

    #check semantic desc, append d to list of sem desc
    semantic_descriptors = build_semantic_descriptors(sentences)
    #print("build semantic descriptors")
    return(semantic_descriptors)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    #similarity fn is just cosine
    #word is the one word
    #choices is a list of strings
    #if semantic similarity NA it's -1
    #In case of a tie between several elements in choices, the one with the smallest index in choices should be returned
    #returns element of choices which has higest similarity
    #cosine similarity takes in the two vectors associated with the words

    similarities = {}
    sem_desc_of_word = semantic_descriptors[word]
    for i in range(len(choices)):
        if choices[i] not in semantic_descriptors:
            similarities[choices[i]] = -1
        else:
            similarities[choices[i]] = semantic_descriptors[choices[i]]

    max_similarity = -1
    most_similar = ""
    temp = 0
    for j in similarities:
        if similarities[j] != -1:
            #comparing 2 semantic descriptors
            temp = similarity_fn(sem_desc_of_word,similarities[j])
            if temp > max_similarity:
                max_similarity = temp
                most_similar = j
    if max_similarity == -1:
        return choices[0]
    else:
        return most_similar


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    #filename is a string: filename.txt
    #return percentage (float between 0 and 100 of questions where the most similar word is guessed correctly
    #1 word: word, 2 word: correct answer. 3 onward: options
    text = open(filename, "r", encoding = "latin1")
    num_lines = 0
    correct_guesses = 0

    for line in text:
        num_lines += 1
        list_of_words = line.split()
        word = list_of_words[0]
        answer = list_of_words[1]
        choices = list_of_words[2:]
        most_similar_guess = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if most_similar_guess == answer:
            correct_guesses += 1

    return((correct_guesses/num_lines)*100)

# if __name__ == "__main__":
#     input = [["i", "am", "a", "sick", "man"],
#      ["i", "am", "a", "spiteful", "man"],
#      ["i", "am", "an", "unattractive", "man"],
#      ["i", "believe", "my", "liver", "is", "diseased"],
#      ["however", "i", "know", "nothing", "at", "all", "about", "my",
#       "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
#
#     out = build_semantic_descriptors(input)
#     print(out)

    # sem_desc = build_semantic_descriptors_from_files(["test.txt"])
    # res = run_similarity_test("test.txt",sem_desc,cosine_similarity)
    # print(res)

    # sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
    # res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    # print(res, "of the guesses were correct")




