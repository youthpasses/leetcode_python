# coding:utf-8
# @sinner
# 16/6/7

'''
Total Accepted: 101535 Total Submissions: 285611 Difficulty: Easy
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        h = ListNode(-1)
        h.next = head
        header = h
        while p and p.next:
            q = p.next
            h.next = q
            p.next = q.next
            q.next = p
            h = p
            p = p.next
        return header.next

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

res = Solution().swapPairs(head)
while res:
    print res.val
    res = res.next


