from os import *
from sys import *
from collections import *
from math import *


class Node:
    def __init__(self):
        self.links = [None]*26
        self.cntendwith = 0
        self.cntprefix = 0

    def containskey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def increaseEnd(self):
        self.cntendwith += 1

    def increasePrefix(self):
        self.cntprefix += 1

    def deleteEnd(self):
        self.cntendwith -= 1

    def reducePrefix(self):
        self.cntprefix -= 1

    def getEnd(self):
        return self.cntendwith

    def getPrefix(self):
        return self.cntprefix


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            if not node.containskey(i):
                node.put(i, Node())
            node = node.get(i)
            node.increasePrefix()
        node.increaseEnd()

    def countWordsEqualTo(self, word):
        node = self.root
        for i in word:
            if node.containskey(i):
                node = node.get(i)
            else:
                return 0
        return node.getEnd()

    def countWordsStartingWith(self, word):
        node = self.root
        for i in word:
            if node.containskey(i):
                node = node.get(i)
            else:
                return 0
        return node.getPrefix()

    def erase(self, word):
        # Write your code here.
        node = self.root
        for i in word:
            if node.containskey(i):
                node = node.get(i)
                node.reducePrefix()
            else:
                return 0
        node.deleteEnd()
