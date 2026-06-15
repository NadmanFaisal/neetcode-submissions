# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()

        prev, curr = None, head

        while curr:
            if curr.next not in nodes:
                nodes.add(curr)
            else:
                return True
            curr = curr.next
        return False