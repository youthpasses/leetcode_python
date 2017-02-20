# coding:utf-8
# @makai
# 17/2/19

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 2 and 97 <= ord(word[0]) and ord(word[0]) <= 122 and ord(word[1]) >= 65 and ord(word[1]) <= 90: return False
        if len(word) <= 2: return True
        lower = True
        if 65 <= ord(word[0]) and ord(word[0]) <= 90 and ord(word[1]) >= 65 and ord(word[1]) <= 90: lower = False
    	elif 65 <= ord(word[0]) and ord(word[0]) <= 90 and ord(word[1]) >= 97 and ord(word[1]) <= 122: lower = True
    	elif 97 <= ord(word[0]) and ord(word[0]) <= 122 and ord(word[1]) >= 97 and ord(word[1]) <= 122: lower = True
    	else: return False
    	for x in xrange(2, len(word)):
    		if lower and 65 <= ord(word[x]) and ord(word[x]) <= 90: return False
    		if not lower and 97 <= ord(word[x]) and ord(word[x]) <= 122: return False
    	return True

print Solution().detectCapitalUse('USA')