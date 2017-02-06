# coding:utf-8
# @makai
# 16/12/26

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.getValidIP(res, 1, 0, [], s)
        return res
    def getValidIP(self, res, index, begin, tmp, s):
    	if index == 4:
    		if s[begin] == '0' and len(s[begin:]) == 1: res.append('.'.join(tmp + [s[begin:]]))
    		elif s[begin] != '0' and int(s[begin:]) < 256: res.append('.'.join(tmp + [s[begin:]]))
    	else:
    		for i in xrange(0, 3):
    			if begin + i + 1 < len(s):
    				ss = s[begin:begin + i + 1]
    				if len(ss) == 1 or (ss[0] != '0' and int(ss) < 256):
    					self.getValidIP(res, index + 1, begin + i + 1, tmp + [ss], s)

print Solution().restoreIpAddresses('25525511135')
print Solution().restoreIpAddresses('19211005')