# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_head = l1
        l2_head = l2

        l1_num_list = []
        l2_num_list = []

        while (l1_head):
            l1_num_list.append(str(l1_head.val))
            l1_head = l1_head.next

        while (l2_head):
            l2_num_list.append(str(l2_head.val))
            l2_head = l2_head.next
        
        _sum = int("".join(l1_num_list)[::-1]) + int("".join(l2_num_list)[::-1])
        dummy = ListNode()
        curr = dummy
        for char in str(_sum)[::-1]:
            node = ListNode(char)
            curr.next = node
            curr = curr.next
        

        return dummy.next




