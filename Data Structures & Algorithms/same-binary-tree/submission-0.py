# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        visited_1 = collections.deque()
        
        queue.append(p)
        visited_1.append(p)

        while queue:
            qLen = len(queue)
            node = queue.popleft()

            if node:
                queue.append(node.left)
                visited_1.append(node.left)
                queue.append(node.right)
                visited_1.append(node.right)
        
        queue = collections.deque()
        visited_2 = collections.deque()
        
        queue.append(q)
        visited_2.append(q)

        while queue:
            qLen = len(queue)
            node = queue.popleft()

            if node:
                queue.append(node.left)
                visited_2.append(node.left)
                queue.append(node.right)
                visited_2.append(node.right)
        
        if len(visited_1) != len(visited_2):
            return False
        
        for i in range(len(visited_1)):
            node1 = visited_1[i]
            node2 = visited_2[i]
    
            if not node1 and not node2:
                continue
        
            if not node1 or not node2:
                return False
        
            if node1.val != node2.val:
                return False

        return True