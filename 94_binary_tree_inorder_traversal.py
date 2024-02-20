from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        return dfs(root)

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

# Construct the binary tree [1,null,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create an instance of the Solution class
test = Solution()
# Call inorderTraversal with the root of the tree
result = test.inorderTraversal(root)
result2 = test.inorderTraversal2(root)
print(result)  # This should print [1, 3, 2]
print(result2)