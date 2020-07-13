class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.count = 0
        self.dfs({}, 0, root, sum)
        return self.count
        
    def dfs(self, store, pathSum, node, sum):
        pathSum += node.val
        if pathSum == sum:
            self.count += 1
        diff = pathSum - sum
        self.count += store.get(diff, 0)
        store[pathSum] = store.get(pathSum, 0) + 1
        
        if node.left:
            self.dfs(store, pathSum, node.left, sum)
        if node.right:
            self.dfs(store, pathSum, node.right, sum)
        store[pathSum] -= 1
