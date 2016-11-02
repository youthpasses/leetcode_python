# coding:utf-8
# @sinner
# 16/9/17

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes = []
        res = []
        ind = []
        nodes.insert(0, root)
        ind.append(0)
        while len(nodes) != 0:
            n = nodes.pop()
            index = ind.pop()
            if len(res) < index + 1:
                res.append([n.val])
            else:
                res[index].append(n.val)
            if n.left:
                nodes.insert(0, n.left)
                ind.insert(0, index + 1)
            if n.right:
                nodes.insert(0, n.right)
                ind.insert(0, index + 1)
        return res


root = TreeNode(3)
n10 = TreeNode(9)
n11 = TreeNode(20)
n20 = TreeNode(15)
n21 = TreeNode(7)
root.left = n10
root.right = n11
n11.left = n20
n11.right = n21
print Solution().levelOrder(root)









