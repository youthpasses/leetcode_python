# coding:utf-8
# @sinner
# 16/6/7

'''
Total Accepted: 131786 Total Submissions: 367934 Difficulty: Easy
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1

        # head = None
        # if l1.val < l2.val:
        #     head = l1
        #     head.next = self.mergeTwoLists(l1.next, l2)
        # else:
        #     head = l2
        #     head.next = self.mergeTwoLists(l1, l2.next)
        # return head

        p = header = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return header.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(5)
node4 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

node5 = ListNode(2)
# node6 = ListNode(4)
# node7 = ListNode(6)
# node8 = ListNode(8)
# node5.next = node6
# node6.next = node7
# node7.next = node8
# node8.next = None

head = Solution().mergeTwoLists(node1, node5)
while head:
    print head.val
    head = head.next





