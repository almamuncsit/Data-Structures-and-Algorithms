from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Insert word into trie
    def insert(self, word):
        root = self.root
        for index in word:
            if index not in root.children:
                root.children[index] = TrieNode()
            root = root.children.get(index)
        root.terminating = True

    # Search a word in the trie
    def search(self, word):
        root = self.root
        for index in word:
            if not root:
                return False
            root = root.children.get(index)
        return True if root and root.terminating else False

    # Delete a word form the trie
    def delete(self, word):
        root = self.root
        for index in word:
            if not root:
                print('Word not found')
                return -1
            root = root.children.get(index)
        if not root:
            print('Word not found')
            return -1
        else:
            root.terminating = False
            return 0

    # Update a word of a trie
    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)


if __name__ == "__main__":

    strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]

    t = Trie()
    for wrd in strings:
        t.insert(wrd)

    print(t.search("pqrs"))
    print(t.search("pprt"))

    t.delete("pprt")

    print(t.search("pprt"))

    t.update("mnop", "pprt")
