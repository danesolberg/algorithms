from collections import defaultdict

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.terminating = False
        self.word_count = 0


class Trie:
    def __init__(self, wordlist):
        self.root = Node(None)

        self._load_words(wordlist)

    def _load_words(self, wordlist):
        cur_node = self.root
        for word in wordlist:
            for letter in word:
                if letter not in cur_node.children:
                    cur_node.children[letter] = Node(letter)
                cur_node = cur_node.children[letter]
            cur_node.terminating = True
            cur_node.word_count += 1


def escape(wordlist, keypads):
    def count_words_dfs(node, cur_keypads):
        nonlocal num_words

        if node.letter in first_map:
            for idx in first_map[node.letter]:
                first_used[idx] += 1

        if node.terminating:
            for keypad_idx in cur_keypads:
                if first_used[keypad_idx] > 0:
                    num_words[keypad_idx] += node.word_count

        for child in node.children.values():
            if child.letter in pad_map:
                count_words_dfs(child, cur_keypads & pad_map[child.letter])

        if node.letter in first_map:
            for idx in first_map[node.letter]:
                first_used[idx] -= 1

        return num_words

    # reduce functionally equivalent words down to reduce trie width and height
    trie = Trie([sorted(set(word)) for word in wordlist])
    num_words = [0] * len(keypads)

    pad_map = defaultdict(set)
    first_map = defaultdict(list)
    first_used = [0] * len(keypads)

    for i, keypad in enumerate(keypads):
        first_map[keypad[0]].append(i)
        for letter in keypad:
            pad_map[letter].add(i)

    count_words_dfs(trie.root, set(range(len(keypads))))

    return num_words


if __name__ == "__main__":
    assert (
              escape(
                  ["APPLE", "PLEAS", "PLEASE"],
                  ["AELWXYZ", "AELPXYZ", "AELPSXY", "SAELPRT", "XAEBKSY"],
              )
              == [0, 1, 3, 2, 0]
          )