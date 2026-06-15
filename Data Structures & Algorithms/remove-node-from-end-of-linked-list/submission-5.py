# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        dummy = ListNode()
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        curr = head
        target = len(nodes) - n
        if target == 0:
            if target + 1 < len(nodes):
                dummy.next = nodes[target + 1]
                return dummy.next
            else:
                return None
        elif target == len(nodes) - 1:
            if target - 1 >= 0:
                nodes[target - 1].next = None
                return curr
            else:
                nodes[target].next = None
                return dummy.next
        else:
            nodes[target - 1].next = nodes[target + 1]
            return curr

