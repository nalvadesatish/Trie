class Node:
    def __init__(self):
        self.links = [None, None]

    def containsKey(self, ind):
        return self.links[ind] is not None

    def get(self, ind):
        return self.links[ind]

    def put(self, ind, node):
        self.links[ind] = node


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node = node.get(bit)

    def findMax(self, num):
        node = self.root
        maxNum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.containsKey(1 - bit):
                maxNum = maxNum | (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return maxNum


def maxXorQueries(arr, queries):
    ans = [0] * len(queries)
    offlineQueries = []

    arr.sort()
    index = 0
    for q in queries:
        offlineQueries.append((q[1], (q[0], index)))
        index += 1

    offlineQueries.sort()
    i = 0
    n = len(arr)
    trie = Trie()

    for q in offlineQueries:
        while i < n and arr[i] <= q[0]:
            trie.insert(arr[i])
            i += 1
        if i != 0:
            ans[q[1][1]] = trie.findMax(q[1][0])
        else:
            ans[q[1][1]] = -1

    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        queries = []
        for _ in range(m):
            xi, ai = map(int, input().split())
            queries.append([xi, ai])

        ans = maxXorQueries(arr, queries)
        print(" ".join(map(str, ans)))
