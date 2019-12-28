class Node(object):

    def __init__(self, end=False):
        self.end = end
        self.nodes = dict()


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for i in range(len(word) - 1):
            if word[i] in cur.nodes.keys():
                cur = cur.nodes[word[i]]
            else:
                cur.nodes[word[i]] = Node()
                cur = cur.nodes[word[i]]
        l = len(word) - 1
        if word[l] in cur.nodes.keys():
            cur.nodes[word[l]].end = True
        else:
            cur.nodes[word[l]] = Node(end=True)

    def search(self, word):
        if not word:
            return False
        cur = self.root
        for i in range(len(word) - 1):
            if not word[i] in cur.nodes.keys():
                return False
            cur = cur.nodes[word[i]]
        l = len(word) - 1
        if word[l] in cur.nodes.keys() and cur.nodes[word[l]].end:
            return True
        return False

    def startsWith(self, prefix):
        cur = self.root
        for i in range(len(prefix)):
            if not prefix[i] in cur.nodes.keys():
                return False
            cur = cur.nodes[prefix[i]]
        return True


obj = Trie()
obj.insert("oasis")
print obj.search("oasis")
print obj.search("oasi")
print obj.startsWith("oasis")
print obj.startsWith("oasi")
print obj.startsWith("")
