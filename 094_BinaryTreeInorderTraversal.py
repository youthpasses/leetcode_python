# coding:utf-8
# @makai
# 16/12/26

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.getTra(res, root)
        return res

    def getTra(self, res, root):
    	if root:
    		self.getTra(res, root.left)
    		res.append(root.val)
    		self.getTra(res, root.right)

