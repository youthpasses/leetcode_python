# coding:utf-8
# @sinner
# 16/9/13


class Solution(object):
    def simplifyPath(self, path):
        path = path.split('/')
        res = []
        for p in path:
            if p == '.' or p == '':
                continue
            elif p == '..':
                if res:
                    res.pop()
            else:
                res.append(p)
        return '/' + '/'.join(res)

print Solution().simplifyPath("/...")