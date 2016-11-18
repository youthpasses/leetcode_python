# coding:utf-8
# @sinner
# 16/11/10

'''
82. Remove Duplicates from Sorted List II   QuestionEditorial Solution  My Submissions
Total Accepted: 90070
Total Submissions: 317935
Difficulty: Medium
Contributors: Admin
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        p1 = h
        while p1.next and p1.next.next:
        	if p1.next.val == p1.next.next.val:
        		p2 = p1.next.next
        		while p2.next and p2.next.val == p2.val:
        			p2 = p2.next
        		p1.next = p2.next
        	else:
        		p1 = p1.next
        h = h.next
        return h

n0 = ListNode(1)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(3)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

Solution().deleteDuplicates(n0)