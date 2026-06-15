# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        dummy = ListNode()
        carry_over = []
        tail = dummy

        while head1 and head2:
            if carry_over:
                val = head1.val + head2.val + carry_over.pop()
            else:
                val = head1.val + head2.val

            if val > 9:
                node = ListNode(val % 10, None)
                carry_over.append(int(str(val)[:1]))
                tail.next = node
                tail = node
            else:
                node = ListNode(val, None)
                tail.next = node
                tail = node
            
            head1 = head1.next
            head2 = head2.next
        
        while head1:
            if carry_over:
                val = head1.val + carry_over.pop()
            else:
                val = head1.val

            if val > 9:
                node = ListNode(val % 10, None)
                carry_over.append(int(str(val)[:1]))
                tail.next = node
                tail = node
            else:
                node = ListNode(val, None)
                tail.next = node
                tail = node
            
            head1 = head1.next

        while head2:
            if carry_over:
                val = head2.val + carry_over.pop()
            else:
                val = head2.val

            if val > 9:
                node = ListNode(val % 10, None)
                carry_over.append(int(str(val)[:1]))
                tail.next = node
                tail = node
            else:
                node = ListNode(val, None)
                tail.next = node
                tail = node
        
            head2 = head2.next
            
        if carry_over:
            node = ListNode(carry_over.pop(), None)
            tail.next = node
            tail = node

        return dummy.next