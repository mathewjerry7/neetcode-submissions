# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        None <-  0 -> 1 -> 2 -> 3 -> None
        prev     H 
                Curr

        None <- 0 <- 1 <- 2 <- 3

        """

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr        # prev = curr first
            curr = next_node   # then move curr forward

        return prev


