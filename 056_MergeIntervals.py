# coding:utf-8
# @sinner
# 16/9/5

'''
56. Merge Intervals  QuestionEditorial Solution  My Submissions
Total Accepted: 79268
Total Submissions: 295704
Difficulty: Hard
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ordic = {}
        for inte in intervals:
            start = inte.start
            end = inte.end
            if start in ordic.keys():
                if end > ordic[start].end:
                    ordic[start] = inte
            else:
                ordic[start] = inte
        ordic = sorted(ordic.iteritems(), key=lambda asd: asd[0])

        intervals = []
        for x in ordic:
            inte = Interval(x[1].start, x[1].end)
            intervals.append(inte)
        dele = []
        for x in xrange(1, len(intervals)):
            in1 = intervals[x - 1]
            in2 = intervals[x]
            if in1.end >= in2.start:
                intervals[x].start = intervals[x - 1].start
                intervals[x].end = max(in1.end, in2.end)
                intervals[x - 1].start = -1
                intervals[x - 1].end = -1
                dele.insert(0, x - 1)
        for x in dele:
            del intervals[x]
        return intervals

'''
超时。。

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        for i in xrange(n - 1, 0, -1):
            for j in xrange(0, i):
                in1 = intervals[j]
                in2 = intervals[j + 1]
                if in1.start > in2.start:
                    intervals[j] = in2
                    intervals[j + 1] = in1
        dele = []
        for x in xrange(1, len(intervals)):
            in1 = intervals[x - 1]
            in2 = intervals[x]
            if in1.end >= in2.start:
                intervals[x].start = intervals[x - 1].start
                intervals[x].end = max(in1.end, in2.end)
                intervals[x - 1].start = -1
                intervals[x - 1].end = -1
                dele.insert(0, x - 1)
        for x in dele:
            del intervals[x]
        return intervals
'''

int1 = Interval(2, 3)
int2 = Interval(4, 5)
int3 = Interval(6, 7)
int4 = Interval(8, 9)
int5 = Interval(1, 10)
# int6 = Interval(0, 2)

intervals = Solution().merge([int1, int2, int3, int4, int5])

for x in intervals:
    print x.start, x.end








