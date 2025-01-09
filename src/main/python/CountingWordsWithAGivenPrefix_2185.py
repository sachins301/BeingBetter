from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1

    def count(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)
        return trie.count(pref)
