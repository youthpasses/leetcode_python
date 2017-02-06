# coding:utf-8
# @makai
# 16/12/26

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        p1 = head
        h = ListNode(0)
        h.next = head
        p1 = p2 = h
        for x in xrange(m - 1):
            p1 = p1.next
        p2 = p1.next
        p3 = p2.next
        for x in xrange(n - m):
            t = p3.next
            p3.next = p2
            p2 = p3
            p3 = t
        p1.next.next = p3
        p1.next = p2
        return h.next