# coding:utf-8
# @sinner
# 16/9/12

'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        begin = 0
        end = 1
        allLen = 0
        ra = []
        for i, word in enumerate(words):
            if allLen + len(word) + 1 <= maxWidth + 1:
                end = i + 1
                allLen += len(word) + 1
            else:
                ra.append([begin, end])
                begin = i
                end = begin + 1
                allLen = len(word) + 1
        if end == len(words):
            ra.append([begin, end])
        res = []
        for ran in ra:
            begin = ran[0]
            end = ran[1]
            allLen = 0
            for x in xrange(begin, end):
                allLen += len(words[x])
            if end != len(words):
                s = ''
                a = 1
                b = 0
                if (end - begin >= 2):
                    numOfSpaces = maxWidth - allLen
                    a = numOfSpaces / (end - begin - 1)
                    b = numOfSpaces % (end - begin - 1)
                for x in xrange(begin, end):
                    s += words[x]
                    if x - begin >= b:
                        s += a * ' '
                    else:
                        s += (a + 1) * ' '
                s = s.strip()
                s += ' ' * (maxWidth - len(s))
                res.append(s)
            else:
                s = ''
                for x in xrange(begin, end):
                    s += words[x]
                    s += ' '
                s = s.strip()
                s += ' ' * (maxWidth - len(s))
                res.append(s)
        return res

print Solution().fullJustify(['I', 'do', 'not', 'know.', 'So', 'you', 'had', 'better', 'to', 'ask', 'the', 'Dean.', 'You', 'know', 'that.'], 17)


















