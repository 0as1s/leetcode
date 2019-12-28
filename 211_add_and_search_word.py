from collections import defaultdict


class WordDictionary(object):

    def __init__(self):
        self.nodes = defaultdict(lambda: defaultdict(list))
        self.count = 1
        self.addedword = set()
        self.search_result = dict()

    def addWord(self, word):
        if word in self.addedword:
            return
        self.search_result = dict()
        self.addedword.add(word)
        for i in range(len(word)):
            if i == len(word) - 1:
                self.nodes[word[i]][self.count].append((i, None))
                self.count += 1
                return
            else:
                self.nodes[word[i]][self.count].append((i, word[i + 1]))

    def search(self, word):
        if not word:
            return False
        if word in self.addedword:
            return True
        if word in self.search_result.keys():
            return self.search_result[word]
        posible = range(self.count)
        for i in range(len(word) - 1):
            if word[i] != '.':
                if word[i + 1] != '.':
                    posible = filter(
                        lambda x: (i, word[i + 1]) in self.nodes[word[i]][x], posible)
                else:
                    posible = filter(lambda x: i in map(
                        lambda x_: x_[0], self.nodes[word[i]][x]), posible
                    )
        l = len(word) - 1
        if word[l] != '.':
            posible = filter(
                lambda x: (l, None) in self.nodes[word[l]][x], posible)
            if posible:
                self.search_result[word] = True
                return True
            else:
                self.search_result[word] = False
                return False
        else:
            for key in self.nodes.keys():
                result = filter(
                    lambda x: (l, None) in self.nodes[key][x], posible)
                if result:
                    self.search_result[word] = True
                    return True
            self.search_result[word] = False
            return False


w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
w.addWord("oasis")
print w.search("pad")
print w.search("bad")
print w.search(".ad")
print w.search("..d")
print w.search("b.d")
print w.search("b..")
print w.search("....")
print w.search("c..")
print w.search("...")
print w.search("o.s.s")
w.addWord("pad")
print w.search("pad")
