#!/usr/bin/env python
import sys
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, wordpunct_tokenize
from collections import Counter
import re

# take all the words from mapper and count the existence of the word

fdist = FreqDist()

# lines passed from the mapper.py program
for line in sys.stdin:
    # remove leading and trailing whitespace, convert to lowercase
    line = line.lower().strip()

    for sentence in nltk.tokenize.sent_tokenize(line):
        # for word in nltk.tokenize.word_tokenize(sentence):
        for word in nltk.tokenize.wordpunct_tokenize(sentence):
           # word1 = re.findall(match_punct_and_words, word)
            if re.match(r'(\d+)', word):  # drop numbers from being counted
                continue
            elif re.match(r'\w+', word):
                # use freqdist to count frequency of each word
                fdist[word] += 1
            elif re.match(r"[.,!?;']", word):
                fdist[word] += 1
            else:
                continue

# now that fdist holds all the values, loop thru and print
# for word in fdist.keys():
for word in fdist.most_common(None):
    times = fdist[word]
    # print(" -- %s occurred %s times" % (word, times))
    print(word)

# Using None with most_common returns all of the words with counts
# print(fdist.most_common(None))

# print to see how many samples and outcomes there were
print(fdist)
