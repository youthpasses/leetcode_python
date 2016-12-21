# coding:utf-8
# @sinner
# 16/11/20

'''
86. Partition List   QuestionEditorial Solution  My Submissions
Total Accepted: 82844
Total Submissions: 265206
Difficulty: Medium
Contributors: Admin
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        l = ListNode(-1)
        l.next = head
        head = l
        p1 = head
        p2 = p1.next
        while p2 and p2.val < x:
        	p1 = p1.next
        	p2 = p2.next
        if not p2:
        	return head.next
        p3 = p2
        while p3.next:
        	p4 = p3.next
        	if p4.val < x:
        		p3.next = p4.next
        		p4.next = p2
        		p1.next = p4
        		p1 = p4
        	else:
        		p3 = p3.next
        return head.next


l1 = ListNode(1)
l2 = ListNode(1)
# l3 = ListNode(3)
# l4 = ListNode(2)
# l5 = ListNode(5)
# l6 = ListNode(2)
l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
a = Solution().partition(l1, 1)
while a:
	print a.val,
	a = a.next