# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> int:
            if node is None:
                return 0
            
            lHeight = 1 + dfs(node.left)
            rHeight = 1 + dfs(node.right)
            
            return max(lHeight, rHeight)
        
        minHeight = 10
        maxHeight = 0

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)

                lHeight = dfs(node.left)
                rHeight = dfs(node.right)

                if abs(lHeight - rHeight) > 1:
                    return False
        return True