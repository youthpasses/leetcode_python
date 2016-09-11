# coding:utf-8
# @sinner
# 16/9/5

'''
57. Insert Interval  QuestionEditorial Solution  My Submissions
Total Accepted: 67413
Total Submissions: 269170
Difficulty: Hard
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda asd: asd.start)

        # for x in intervals:
        #     print x.start, x.end
        # print '\n'

        if len(intervals) <= 1:
            return intervals
        i = 1
        stack = []
        stack.append(intervals[0])
        while i < len(intervals):
            in1 = stack[-1]
            in2 = intervals[i]
            if in1.end >= in2.start:
                in1.start = min(in1.start, in2.start)
                in1.end = max(in1.end, in2.end)
            else:
                stack.append(in2)
            i += 1
        return stack

int1 = Interval(1, 5)
int2 = Interval(6, 8)
# int3 = Interval(6, 7)
# int4 = Interval(8, 9)
# int5 = Interval(10, 13)
# int6 = Interval(14, 15)
# int7 = Interval(18, 20)
int8 = Interval(5, 6)

intervals = Solution().insert([int1, int2], int8)

for x in intervals:
    print x.start, x.end







