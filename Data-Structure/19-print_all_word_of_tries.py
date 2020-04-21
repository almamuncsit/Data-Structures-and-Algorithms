from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False
        self.counter = 1


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.bad_node = None

    # Insert word into trie
    def insert(self, word):
        root = self.root
        for index in word:
            if index not in root.children:
                root.children[index] = TrieNode()
            else:
                root.children[index].counter += 1
            root = root.children.get(index)
        root.terminating = True

    def print_worlds(self, node, word):
        if node is None:
            return
        if node.terminating:
            if node.children:
                print('BAD SET')
                self.bad_node = node
                self.print_bad_word(node, word)
        for child in node.children.items():
            temp_word = word + child[0]
            self.print_worlds(child[1], temp_word)

    def print_bad_word(self, node, word):
        if node.terminating and node != self.bad_node:
            print(word)
        for child in node.children.items():
            temp_word = word + child[0]
            self.print_bad_word(child[1], temp_word)


if __name__ == "__main__":

    strings = ["pqrs", "pprt", "psst", "qqrs", "psr"]

    t = Trie()
    for wrd in strings:
        t.insert(wrd)

    t.print_worlds(t.root, '')
    if t.bad_node is None:
        print('GOOD SET')
