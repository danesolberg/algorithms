class TrieNode:
 def __init__(self):
     self.children = [None] * 26
     self.terminating = False

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        cur_node = self.root
        for i in range(len(word)):
            idx = self.get_index(word[i])
            if cur_node.children[idx] is None:
                cur_node.children[idx] = self.get_node()
            cur_node = cur_node.children[idx]
        cur_node.terminating = True

    def search(self, word):
        cur_node = self.root
        for i in range(len(word)):
            idx = self.get_index(word[i])
            if cur_node.children[idx] is None:
                return False
            cur_node = cur_node.children[idx]
        return cur_node.terminating

    def find_endings(self, prefix):
        cur_node = self.root
        for i in range(len(prefix)):
            idx = self.get_index(prefix[i])
            if cur_node.children[idx] is None:
                return False
            cur_node = cur_node.children[idx]
        
        endings = []
        stack = [(cur_node, prefix)]
        while stack:
            cur_node, word = stack.pop()
            if cur_node.terminating:
                endings.append(word)
            for i, child in enumerate(cur_node.children):
                if child is not None:
                    stack.append((child, word + chr(i + ord('a'))))
        return endings

    def delete(self, word):
        cur_node = self.root
        for i in range(len(word)):
            idx = self.get_index(word[i])
            if cur_node.children[idx] is None:
                return
            cur_node = cur_node.children[idx]
        cur_node.terminating = False

if __name__ == "__main__":

    strings = ["pop", "poptart", "program", "atz", "cumin"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print(t.search("pop"))
    print(t.search("atz"))
    print(t.find_endings("pop"))
    t.insert("pothole")
    t.insert("po")
    t.insert("popsicle")
    t.insert("poppop")
    t.delete("pop")
    print(t.find_endings("pop"))
    print(t.search("pop"))
    print(t.search("poptart"))
