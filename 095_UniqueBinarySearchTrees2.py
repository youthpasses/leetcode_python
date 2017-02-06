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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        allpl = []
        nn = [x for x in xrange(1, n + 1)]
        self.getAllpl(allpl, nn, [], 0)
        res = []
        res_l = []
        for pl in allpl:
        	root = TreeNode(pl[0])
        	l = [pl[0]]
        	for i in xrange(1, len(pl)):
        		p1 = p2 = root
        		while p2:
        			p1 = p2
        			if pl[i] < p2.val: p2 = p2.left
        			else: p2 = p2.right
        		n = TreeNode(pl[i])
        		if pl[i] < p1.val:
        			p1.left = n
        			l.append(pl[i])
        		else:
        			p1.right = n
        			l += [0, pl[i]]
        	print l
        	if l not in res_l:
        		res.append(root)
        		res_l.append(l)
        return res

    def getAllpl(self, allpl, nn, tmp, index):
    	if index == len(nn): allpl.append(tmp)
    	else:
    		for x in nn:
    			if x not in tmp:
    				self.getAllpl(allpl, nn, tmp + [x], index + 1)

Solution().generateTrees(3)