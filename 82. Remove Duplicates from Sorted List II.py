# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  # 创建一个虚拟节点
        dummy.next = head  # 将虚拟节点指向头节点
        prev = dummy  # 初始化prev为虚拟节点
        
        while prev.next and prev.next.next:  # 确保prev.next和prev.next.next不是None
            if prev.next.val == prev.next.next.val:  # 如果找到重复的节点
                duplicate_val = prev.next.val  # 记录重复的值
                while prev.next and prev.next.val == duplicate_val:  # 删除所有重复的节点
                    prev.next = prev.next.next
            else:
                prev = prev.next  # 如果没有找到重复节点，则移动prev指针
                
        return dummy.next  # 返回新链表的头节点
