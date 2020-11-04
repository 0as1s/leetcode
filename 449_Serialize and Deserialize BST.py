# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize_helper(self, root):
        d = dict()
        d['v'] = root.val
        if root.left:
            d['left'] = self.serialize_helper(root.left)
        if root.right:
            d['right'] = self.serialize_helper(root.right)
        return d


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        import json
        return json.dumps(self.serialize_helper(root))

    def deserialize_helper(self, d):
        node = TreeNode(d['v'])
        if 'left' in d and d['left']:
            node.left = self.deserialize_helper(d['left'])
        if 'right' in d and d['right']:
            node.right = self.deserialize_helper(d['right'])
        return node


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        import json
        d = json.loads(data)
        return self.deserialize_helper(d)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))