# coding:utf-8
# @makai
# 16/12/20

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        S = set(words)
        
        def great(word):
            stack = [0]
            seen = {0}
            M = len(word)
            while stack:
                node = stack.pop()
                if node == M: return True
                for j in xrange(M - node + 1):
                    if (word[node:node+j] in S and 
                            node+j not in seen and
                            (node > 0 or node + j != M)):
                        stack.append(node + j)
                        seen.add(node + j)
            return False
                
        ans = []
        for word in words:
            if word and great(word):
                ans.append(word)
        return ans
        '''
        words = list(set(words))
        words.sort(key=len)
        res = []
        prewords = []
        for i in xrange(0, len(words)):
        	word = words[i]
        	if self.wordBreak(word, prewords):
        		res.append(word)
        	prewords.append(word)
        return res

    def wordBreak(self, word, worddic):
    	if not worddic: return False
    	f = {x:False for x in xrange(len(word) + 1)}
    	f[0] = True
    	for i in xrange(1, len(word) + 1):
    		for j in xrange(0, i):
    			if f[j] and word[j:i] in worddic:
    				f[i] = True
    				break
    	return f[len(word)]
    	'''

print Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])