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
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = {}
        self.bt(res, root, 0)
        print res
        maxDepth = max(res.keys())
        return res[maxDepth][0]
    
    def bt(self, res, root, depth_now):
    	if not root.left and not root.right:
    		res[depth_now] = res.get(depth_now, []) + [root.val]
    	else:
    		if root.left: self.bt(res, root.left, depth_now + 1)
    		if root.right: self.bt(res, root.right, depth_now + 1)

n0 = TreeNode(1)
n1_0 = TreeNode(2)
n0.left = n1_0
n1_1 = TreeNode(3)
n0.right = n1_1
n2_0 = TreeNode(4)
n1_0.left = n2_0
n2_1 = TreeNode(5)
n1_1.left = n2_1
n2_2 = TreeNode(6)
n1_1.right = n2_2
n3_0 = TreeNode(7)
n2_1.left = n3_0

print Solution().findLeftMostNode(n0)
