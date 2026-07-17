# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #Initializing head's node is [0,None] and setting curr = head, so curr's next would be head's next
        head = ListNode(None)
        curr = head

        while list1 or list2:
            
            #Step 4
            if list1 is None:
                curr.next = list2
                return head.next
            #Step 5
            if list2 is None:
                curr.next = list1
                return head.next
            #Step 1
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            #Step 2
            else:
                curr.next = list2
                list2 = list2.next
            #Step 3
            curr = curr.next

        return head.next
        