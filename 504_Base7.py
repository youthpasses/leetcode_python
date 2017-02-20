# coding:utf-8

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.convert(num)

    def convert(self, num):
    	if num < 0: return '-' + self.convert(-num)
    	if num < 7: return str(num)
    	return self.convert(num / 7) + str(num % 7)


print Solution().convertToBase7(-7)