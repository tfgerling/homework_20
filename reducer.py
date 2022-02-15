#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None
# take all the words from mapper and count the existence of the word

# lines passed from the mapper.py program
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # break word and count up
    word, count = line.split("\t", 1)

    # aggregate together
    try:
        count = int(count)
    except ValueError:
        # count was not a number
        continue

    # sorted values from command line are passed, and
    # if we have two of the same word, we increment the count per instance of the word
    if current_word == word:
        current_count += count

    else:
        # if there is a current word and its not None (which was how we instantiated it)
        if current_word:
            print(current_word + "\t" + str(current_count))

        current_count = count
        current_word = word

if current_word == word:
    print(current_word + "\t" + str(current_count))
