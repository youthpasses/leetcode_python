# coding:utf-8
# @sinner
# 16/9/6

'''
60. Permutation Sequence  QuestionEditorial Solution  My Submissions
Total Accepted: 63392
Total Submissions: 242902
Difficulty: Medium
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
'''
思路：
在n!个排列中，第一位的元素总是(n-1)!一组出现的，也就说如果p = k / (n-1)!，那么排列的最开始一个元素一定是nums[p]。

假设有n个元素，第K个permutation是
a1, a2, a3, .....   ..., an
那么a1是哪一个数字呢？
那么这里，我们把a1去掉，那么剩下的permutation为
a2, a3, .... .... an, 共计n-1个元素。 n-1个元素共有(n-1)!组排列，那么这里就可以知道
设变量K1 = K
a1 = K1 / (n-1)!
同理，a2的值可以推导为
a2 = K2 / (n-2)!
K2 = K1 % (n-1)!
 .......
a(n-1) = K(n-1) / 1!
K(n-1) = K(n-2) /2!
an = K(n-1)
'''


import math
# import itertools


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # plist = itertools.permutations([str(i) for i in range(1, n+1)])
        # for i in range(k-1):
        #     plist.next()
        # return ''.join(plist.next())

        nums = [str(x) for x in range(1, n + 1)]
        k -= 1
        ans = ""
        for i in range(n)[::-1]:
            ans += nums.pop(k / math.factorial(i))
            k %= math.factorial(i)
        return ans

        
print Solution().getPermutation(9, 322978)

'''
# 字典序全排列法
# Time Limit Exceeded

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = 1
        for i in xrange(2, n + 1):
            num = num * 10 + i
        while k > 1:
            num = self.getNext(num)
            k -= 1
        return str(num)

    def getNext(self, num):
        if len(str(num)) == 1:
            return num + 1
        s = str(num)
        l = len(s) - 1
        for x in xrange(len(s) - 1, 0, -1):
            if int(s[x - 1]) < int(s[x]):
                l = x - 1
                break
        r = l + 1
        while r <= len(s) - 1 and int(s[r]) > int(s[l]):
            r += 1
        r -= 1
        s = s[:l] + s[r] + s[l + 1:r] + s[l] + s[r + 1:]    # s[l]与s[r]交换
        l += 1
        r = len(s) - 1
        while l < r:
            s = s[:l] + s[r] + s[l + 1:r] + s[l] + s[r + 1:]
            l += 1
            r -= 1
        return int(s)

print Solution().getPermutation(9, 346261)
'''

'''
# 回溯法
# Time Limit Exceeded

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = []
        self.bt(l, '', n, k)
        print l
        l.sort()
        return l[k - 1]

    def bt(self, l, s, n, k):
        if len(s) == n:
            l.append(s)
            if len(l) == k:
                return
        else:
            for x in xrange(1, n + 1):
                if str(x) not in s:
                    self.bt(l, s + str(x), n, k)

print Solution().getPermutation(3, 2)
'''


