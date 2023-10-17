# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        prev = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            
            # Don't forget to move the prev pointer to the end of the merged list
            prev = prev.next
        
        # Handling the remaining nodes of either list1 or list2
        prev.next = list1 if list1 is not None else list2
        
        return dummy.next
