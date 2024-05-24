class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containskey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            if not node.containskey(i):
                node.put(i, Node())
            node = node.get(i)
        node.setEnd()

    def checkifexists(self, word):
        node = self.root
        for i in word:
            if node.containskey(i):
                node = node.get(i)
                if node.isEnd() == False:
                    return False
            else:
                return False

        return True


def longestCommonPrefix(arr, n):
    trie = Trie()
    for i in arr:
        trie.insert(i)
    longest = ""
    for i in arr:
        if trie.checkifexists(i):
            if len(i) > len(longest):
                longest = i
            elif len(i) == len(longest) and i < longest:
                longest = i
    if longest == "":
        return ""
    return longest


words = ["flower", "flour", "flow", "flew"]
result = longestCommonPrefix(words, len(words))
print(result)  # Output: "flo"
