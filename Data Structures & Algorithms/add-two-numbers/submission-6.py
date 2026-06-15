# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        dummy = ListNode()
        carry_over = 0
        tail = dummy

        while head1 or head2 or carry_over:
            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0

            val = v1 + v2 + carry_over
            carry_over = val // 10
            val = val % 10

            node = ListNode(val, None)
            tail.next = node
            tail = node
            
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        return dummy.next