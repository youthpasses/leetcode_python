# coding:utf-8
# @sinner
# 16/11/11

'''
83. Remove Duplicates from Sorted List   QuestionEditorial Solution  My Submissions
Total Accepted: 148926
Total Submissions: 387471
Difficulty: Easy
Contributors: Admin
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
        if not head:
        	return head
        p1 = head
        while p1.next:
        	if p1.next.val == p1.val:
        		p2 = p1.next
        		while p2.next and p2.next.val == p2.val:
        			p2 = p2.next
        		p1.next = p2.next
        	else:
        		p1 = p1.next
        return head

n0 = ListNode(1)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(2)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

Solution().deleteDuplicates(n0)