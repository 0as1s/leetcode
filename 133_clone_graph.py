
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def helper(origin, store):
    if id(origin) in store.keys():
        print("found")
        return store[id(origin)]
    new_node = Node(origin.val)
    store[id(origin)] = new_node
    for n in origin.neighbors:
        new_node.neighbors.append(helper(n, store))
    return new_node

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        store = {}
        if not node:
            return None
        return helper(node, store)
        