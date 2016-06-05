# coding:utf-8
# @sinner
# 16/6/4

'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

'''
思路：
将相加的结果保存在l1中；
node1标记l1的结点，node2标记l2的结点，一直循环直到node1, node2全为None；
在循环体中，若node1为None，则new之，并设置val为node2.val，然后判断zeng是否为True，zeng是上结点相加是否有进位的标记；
如果node1，node2都为空了，但是还有进位，还需要new一个新结点以保存进位；
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        # l3 = l1
        node1 = l1
        node2 = l2
        node1_p = l1
        # node2_p = l2
        zeng = False
        while node1 is not None or node2 is not None:
            if node1 is None:
                node1 = ListNode(node2.val)
                node1_p.next = node1
            elif node2 is None:
                pass
            else:
                node1.val = node1.val + node2.val

            if zeng is True:
                node1.val = node1.val + 1
            if node1.val > 9:
                node1.val = node1.val % 10
                zeng = True
            else:
                zeng = False

            node1_p = node1
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next
            if node1 is None and node2 is None and zeng is True:
                node1_p.next = ListNode(1)

        return l1

node0_0 = ListNode(5)
# node0_1 = ListNode(4)
# node0_2 = ListNode(3)
# node0_0.next = node0_1
# node0_1.next = node0_2

node1_0 = ListNode(5)
# node1_1 = ListNode(6)
# node1_2 = ListNode(4)
# node1_0.next = node1_1
# node1_1.next = node1_2

result = Solution().addTwoNumbers(node0_0, node1_0)

while result is not None:
    print result.val
    result = result.next















