from functools import reduce
from collections import defaultdict


words = 'test', 'tart', 'apple', 'pear', 'tests'

Trie=lambda:defaultdict(Trie)
trie=Trie()
END=True
for i, word in enumerate(words):
    # whole word is value of END key
    reduce(dict.__getitem__,word,trie)[END]=word
    # or the index of the word from the array is the value of END key
    # reduce(dict.__getitem__,word,trie)[END]=i

print(trie)
