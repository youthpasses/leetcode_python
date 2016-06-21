# coding:utf-8
# @sinner
# 16/6/6

'''
Total Accepted: 112337 Total Submissions: 375898 Difficulty: Easy
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        p = ListNode(-1)
        p.next = head
        k = n
        fast = head
        slow = p
        while k > 1 and fast.next:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return p.next


head = ListNode(1)
next1 = ListNode(2)
next2 = ListNode(3)
next3 = ListNode(4)
next4 = ListNode(5)
head.next = next1
next1.next = next2
next2.next = next3
next3.next = next4

p = Solution().removeNthFromEnd(head, 5)
while p:
    print p.val
    p = p.next












