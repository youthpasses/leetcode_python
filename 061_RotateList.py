# coding:utf-8
# @sinner
# 16/9/7

'''
61. Rotate List  QuestionEditorial Solution  My Submissions
Total Accepted: 80438
Total Submissions: 341325
Difficulty: Medium
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        n = 0
        p1 = head
        p2 = head
        i = 0
        while i < k and p1:
            i += 1
            n += 1
            p1 = p1.next
        if not p1 and i == k:
            return head
        if not p1 and i < k:
            k = k % n
            if k == 0:
                return head
            p1 = head
            i = 0
            while i < k:
                i += 1
                p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p3 = p2.next
        p2.next = None
        p1.next = head
        return p3


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

h = Solution().rotateRight(l1, 4)
while h:
    print h.val
    h = h.next




