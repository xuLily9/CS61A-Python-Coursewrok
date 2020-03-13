""" Typing Test implementation """
import re
from utils import *
from ucb import main

# BEGIN Q1-5


def lines_from_file(path):
    res = []
    file = open(path, mode='r')
    if readable(file):
        i = 0
        res = file.readlines()
        while i < len(res):
            res[i] = res[i].strip()
            i += 1

        return res


def new_sample(path, i):
    assert i >= 0
    lst = lines_from_file(path)
    para = ""
    for line in lst[i]:
        para += line

    return para


def analyze(sample_paragraph, typed_string, start_time, end_time):

    time = (end_time-start_time)/60
    speed = round(len(typed_string)/(time*5), 1)
    typed_str = split(typed_string)
    sample_para = split(sample_paragraph)
    count = 0

    length = min(len(sample_para), len(typed_str))
    if length != 0:
        for i in range(length):
            if typed_str[i] == sample_para[i]:
                count += 1
        accur = count/length*100
    else:
        accur = 0.0
    return [speed, accur]


def pig_latin(string):

    str = re.split(r'(a|e|i|o|u)s*', string)
    way = 'way'
    ay = 'ay'

    if len(string) > 0:
        word = string.lower()
        first_ap = word[0]
        first_cluster = str[0]
        if first_ap == 'a':
            new_word = word + way
            return new_word
        elif first_ap == 'e':
            new_word = word + way
            return new_word
        elif first_ap == 'i':
            new_word = word + way
            return new_word
        elif first_ap == 'o':
            new_word = word + way
            return new_word
        elif first_ap == 'u':
            new_word = word + way
            return new_word
        else:
            new_word = "".join(str[1:]) + "".join(first_cluster) + ay
            return new_word
    else:
        return ''


def autocorrect(user_input, words_list, score_function):

    lst = []
    for i in words_list:
        lst += [score_function(user_input, i)]
    min_mun = min(lst)

    for i in words_list:
        if user_input == i:
            return i

    for i in range(len(lst)):
        if lst[i] == min_mun:
            return words_list[i]


def swap_score(str1, str2):
    if str1 == str2:
        return 0
    if not str1 or not str2:
        return 0
    if str1[0] != str2[0]:
        return swap_score(str1[1:], str2[1:])+1
    else:
        return swap_score(str1[1:], str2[1:])
# END Q1-5

# Question 6


def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == word2:  # Fill in the condition
        # BEGIN Q6
        return 0
        # END Q6

    elif not word1:  # Feel free to remove or add additional cases
        # BEGIN Q6
        return len(word2)
        # END Q6

        # BEGIN Q6
    elif not word2:
        return len(word1)
    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])
    else:

        change_word1 = score_function(word1[1:], word2) + 1
        change_word2 = score_function(word1, word2[1:]) + 1
        change_both = score_function(word1[1:], word2[1:]) + 1

        return min(change_word1, change_word2, change_both)
        # END Q6


KEY_DISTANCES = get_key_distances()


# BEGIN Q7-8
def score_function_accurate(word1, word2):
    if not word1:
        return len(word2)
    elif not word2:
        return len(word1)
    elif word1 == word2:
        return 0
    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])
    else:
        change_word1 = score_function_accurate(
            word1[1:], word2[1:]) + KEY_DISTANCES[word1[0], word2[0]]
        change_word2 = score_function_accurate(word1[1:], word2)+1
        change_both = score_function_accurate(word1, word2[1:])+1

        return min(change_word2, change_word1, change_both)


dic = {}


def score_function_final(word1, word2):

    if (word2 + word1) in dic:
        return dic[word2 + word1]
    if (word1 + word2) in dic:
        return dic[word1 + word2]
    else:

        if not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        elif word1 == word2:
            return 0

        elif word1[0] == word2[0]:
            return score_function_final(word1[1:], word2[1:])

        else:
            change_word1 = score_function_final(
                word1[1:], word2[1:])+KEY_DISTANCES[word1[0], word2[0]]
            change_word2 = score_function_final(word1[1:], word2)+1
            change_both = score_function_final(word1, word2[1:])+1
            result = min(change_word1, change_word2, change_both)
            dic[word1 + word2] = result
        return result


# END Q7-8
