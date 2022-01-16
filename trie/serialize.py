# to save on disk
from implementation import Trie, TrieNode

def children_to_letter(node_array):
    character_array = []

    for i in range(len(node_array)):
        if node_array[i] is not None:
            character_array.append((chr(ord('a') + i), node_array[i]))

    return character_array


def serialize(root):
    def dfs(root):
        char_children = children_to_letter(root.children)

        s = ''
        for char, node in char_children:
            if s:
                s += ','
            s += char + str(len(children_to_letter(node.children))) + ('t' if node.terminating else 'f')
            t = dfs(node)
            if t:
                s += ',' + t

        return s

    return "_" + str(len(children_to_letter(root.children))) + ('t' if root.terminating else 'f') + ',' + dfs(root)


def deserialize(s):
    def dfs(i, root):
        if i < len(s):
            char, children, term = s[i]
            if children == 0:
                node = TrieNode()
                node.terminating = True if term == 't' else False
                root.children[ord(char) - ord('a')] = node
                return i
            else:
                offset = i
                node = TrieNode()
                node.terminating = True if term == 't' else False
                root.children[ord(char) - ord('a')] = node
                for _ in range(children):
                    offset = dfs(offset+1, node)
                return offset


    s = [(e[0], int(e[1:-1]), e[-1]) for e in s.split(',')]
    trie = Trie()
    root, children, term = s.pop(0)
    offset = 0
    for _ in range(children):
        offset = dfs(offset, trie.root) + 1

    return trie


if __name__ == "__main__":

    strings = ["pop", "poptart", "popcorn", "program", "atz", "cumin"]

    t1 = Trie()
    for word in strings:
        t1.insert(word)

    serial1 = serialize(t1.root)
    t2 = deserialize(serial1)
    serial2 = serialize(t2.root)

    assert serial1 == serial2