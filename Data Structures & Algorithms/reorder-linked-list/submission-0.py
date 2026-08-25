# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow = head
        fast = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # by this point, after while loop, the slow is in the middle

        # cut down the slow.next for avoiding circular referencing
        second = slow.next
        slow.next = None
        # begin to reverse the slow part

        before = None
        curr = second
        while (curr):
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        # till this point before is the head of the right part of the list
        first = head
        second = before


        while (second):
            new_first = first.next
            new_second = second.next

            first.next = second
            second.next = new_first

            first = new_first
            second = new_second

        