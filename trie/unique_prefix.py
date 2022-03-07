from types import SimpleNamespace
from functools import reduce


def build_trie(words):
    END = "__end__"
    trie = {}

    for word in words:
        t = trie
        for c in word:
            if c in t:
                t[c].count += 1
            else:
                t[c] = SimpleNamespace(count=1, node={})
            t = t[c].node
        t[END] = True

    return trie

def find_unique_prefixes(words):
    trie = build_trie(words)
    res = []
    for word in words:
        t = trie
        for i, c in enumerate(word):
            if t[c].count == 1:
                res.append(word[:i+1])
                break
            t = t[c].node
        else:
            res.append(word)
    return res


if __name__ == "__main__":
    assert find_unique_prefixes(["dog", "dogs", "dove", "duck", "zebra"]) == ["dog", "dogs", "dov", "du", "z"]
