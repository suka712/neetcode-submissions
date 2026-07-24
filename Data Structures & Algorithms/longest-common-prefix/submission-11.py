class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.is_word = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = Trie()

        for i in range(len(strs)):
            t.insert(strs[i])

        longest = ""

        curr = t.root
        while len(curr.children) == 1 and curr.is_word == False:
            char = list(curr.children.keys())[0] # gets char
            longest += char
            curr = curr.children[char] # nav to that char

        return longest

        