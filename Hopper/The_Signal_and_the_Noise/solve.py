#!/usr/bin/env python3

# get list of words
with open('haystack.ef77fe451087.txt') as f:
    haystack = f.read()
    haystack = haystack.replace('\n', ' ')
    haystack = haystack.split(' ')

# print words that are non-alphanumeric
for word in haystack:
    if not word.isalnum():
        print(word.encode())
