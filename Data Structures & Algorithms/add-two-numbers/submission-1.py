# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num_str = ""
        l2_num_str = ""
        curr = l1
        while (curr):
            l1_num_str = str(curr.val) + l1_num_str  # prepend instead of append
            curr = curr.next

        curr = l2
        while (curr):
            l2_num_str = str(curr.val) + l2_num_str
            curr = curr.next
        
        _sum = int(l1_num_str) + int(l2_num_str)
        _sum_str = str(_sum)[::-1]  # reverse again for output
        
        dummy = ListNode()
        curr = dummy
        for char in _sum_str:
            curr.next = ListNode(int(char))
            curr = curr.next
        

        return dummy.next
