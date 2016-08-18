# coding:utf-8
# @sinner
# 16/6/21

'''
25. Reverse Nodes in k-Group My Submissions QuestionEditorial Solution
Total Accepted: 61956 Total Submissions: 221759 Difficulty: Hard
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Subscribe to see which companies asked this question
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 1:
            return head
        hehe = h = ListNode(0)
        h.next = head
        p1 = h.next
        p2 = p1.next
        i = 0
        while p2:
            p = h.next
            h.next = p2
            p1.next = p2.next
            p2.next = p
            p2 = p1.next
            i += 1
            if i == k - 1:
                i = 0
                if p1.next:
                    h = p1
                    p1 = p1.next
                    p2 = p1.next
                else:
                    break
        if i != 0:
            p1 = h.next
            p2 = p1.next
            while p2:
                p = h.next
                h.next = p2
                p1.next = p2.next
                p2.next = p
                p2 = p1.next
        return hehe.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)
l10 = ListNode(10)
l11 = ListNode(11)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = l10
# l10.next = l11

l = Solution().reverseKGroup(l1, 12)
while l:
    print l.val
    l = l.next