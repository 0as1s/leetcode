class MapSum(object):

    def __init__(self):
        self.keys = []
        self.vals = []

    def insert(self, key, val):
        left = 0
        right = len(self.keys)
        while right != left:
            mid = (left + right) // 2
            if self.keys[mid] == key:
                self.vals[mid] = val
                return
            if self.keys[mid] < key:
                left = mid + 1
            else:
                right = mid
        if right != len(self.keys):
            self.keys.insert(left, key)
            self.vals.insert(left, val)
        else:
            self.keys.insert(right, key)
            self.vals.insert(right, val)

    def sum(self, prefix):
        left = 0
        right = len(self.keys)
        flag = 0
        mid = (left + right) // 2
        while left != right:
            mid = (left + right) // 2
            if self.keys[mid].startswith(prefix):
                flag = 1
                break
            if self.keys[mid] < prefix:
                left = mid + 1
            else:
                right = mid
        if not flag:
            return 0
        total = 0
        for i in range(mid, -1, -1):
            if self.keys[i].startswith(prefix):
                total += self.vals[i]
            else:
                break
        if mid + 1 != len(self.keys):
            for i in range(mid+1, len(self.keys)):
                if self.keys[i].startswith(prefix):
                    total += self.vals[i]
                else:
                    break
        return total


obj =  MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
