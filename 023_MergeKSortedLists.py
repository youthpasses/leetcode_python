# coding:utf-8
# @sinner
# 16/6/20

'''
23. Merge k Sorted Lists My Submissions QuestionEditorial Solution
Total Accepted: 90085 Total Submissions: 378084 Difficulty: Hard
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Subscribe to see which companies asked this question
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        left = 0
        right = len(lists) - 1
        while left != right or right != 0:
            if left >= right:
                left = 0
            else:
                lists[left] = self.merge(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]
        # while n != 1:
        #     # print n
        #     lists_now = []
        #     for x in xrange(n / 2):
        #         l = self.merge(lists[2 * x], lists[2 * x + 1])
        #         lists_now.append(l)
        #     if n % 2 == 1:
        #         lists_now.append(lists[n - 1])
        #     n = len(lists_now)
        #     lists = lists_now
        # return lists[0]

    def merge(self, l1, l2):
        head = l = ListNode(-1)
        while l1 and l2:
            node = ListNode(-1)
            node.next = None
            if l1.val < l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            l.next = node
            l = l.next
        l.next = l1 or l2
        return head.next

l1 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(3)
l1_3 = ListNode(5)
l1_4 = ListNode(7)
l1.next = l1_1
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = None

l2 = ListNode(2)
l2_1 = ListNode(4)
l2_2 = ListNode(6)
l2_3 = ListNode(9)
l2.next = l2_1
l2_1.next = l2_2
l2_2.next = l2_3
l2_3.next = None

l3 = ListNode(3)
l3_1 = ListNode(4)
l3.next = l3_1
l3_1.next = None

# l = Solution().mergeKLists([l1, l2, l3])

# l1 = ListNode(1)
# l1_1 = ListNode(2)
# l1_2 = ListNode(2)
# l1_3 = ListNode(3)
# l1_4 = ListNode(4)
# l1_5 = ListNode(5)
# l1_6 = ListNode(6)
# l1_7 = ListNode(7)
# l1_8 = ListNode(9)
# l1.next = l1_1
# l1_1.next = l1_2
# l1_2.next = l1_3
# l1_3.next = l1_4
# l1_4.next = l1_5
# l1_5.next = l1_6
# l1_6.next = l1_7
# l1_7.next = l1_8
# l1_8.next = None


# l = Solution().merge(l1, l3)
l = Solution().mergeKLists([None, l1, l3, None])
while l:
    print l.val
    l = l.next