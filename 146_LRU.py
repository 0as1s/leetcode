class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(None)
        self.last = self.head
        self.dic = dict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            if self.last is not self.dic[key][1]:
                self.dic[key][1].pre.next = self.dic[key][1].next
                self.dic[key][1].next.pre = self.dic[key][1].pre
                self.last.next = self.dic[key][1]
                self.dic[key][1].pre = self.last
                self.last = self.dic[key][1]
            return self.dic[key][0]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) != -1:
            self.dic[key][0] = value
            return
        if len(self.dic) < self.capacity:
            node = Node(key)
            self.last.next = node
            node.pre = self.last
            self.last = node
            self.dic[key] = [value, node]
        else:
            node = Node(key)
            self.last.next = node
            node.pre = self.last
            self.last = node
            temp = self.head.next
            self.head.next = temp.next
            temp.next.pre = self.head
            del(self.dic[temp.val])
            del temp
            self.dic[key] = [value, node]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
seq = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
args = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
l = LRUCache(10)
for i, j in zip(seq, args):
    print(i, j)
    if i == "put":
        l.put(j[0], j[1])
    if i == "get":
        l.get(j[0])

