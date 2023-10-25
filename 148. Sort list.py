# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(second_head)

        return self.merge(left, right)
    
    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy
        while left and right:

            if left.val < right.val:

                current.next, left = left, left.next
            else:
                current.next, right = right, right.next
            current = current.next

        current.next = left if left else right
        return dummy.next

            