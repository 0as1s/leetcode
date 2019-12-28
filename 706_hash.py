class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = [[] for _ in range(499)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        pos = key % 499
        l = self.bucket[pos]
        for i in range(len(l)):
            if l[i][0] == key:
                l[i] = (key, value)
                return
        l.append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        pos = key % 499
        l = self.bucket[pos]
        for i in range(len(l)):
            if l[i][0] == key:
                return l[i][1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        pos = key % 499
        l = self.bucket[pos]
        for i in range(len(l)):
            if l[i][0] == key:
                l[i] = l[-1]
                l.pop()
                return



        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)