# coding:utf-8
# @makai
# 17/2/12

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findValueMostElement(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        res = {}
        self.bt(res, root, 0)
        return res.values()

    def bt(self, res, root, depth_now):
    	if (depth_now not in res.keys()) or (res[depth_now] < root.val):
    		res[depth_now] = root.val
    	if root.left: self.bt(res, root.left, depth_now + 1)
    	if root.right: self.bt(res, root.right, depth_now + 1)


n0 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n0.left = n1
n0.right = n2
print Solution().findValueMostElement(n0)
