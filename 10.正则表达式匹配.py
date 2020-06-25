#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 10.正则表达式匹配.py
    Author      : Charles
    Created date: 2020/6/25 8:33 上午
    Description :
       
"""

'''
思路：
1/ 同时遍历两个字符串，如果出现"."，"*"，则进行处理
 
 2/注意，必须完全匹配， p不能多余。。。
 3/只是通过坐标，无法判断长度是否相等，所以定义一个变量，存储匹配结果
 
 
 以上全错， 本题考查动态规划的问题，哈哈哈！
'''

import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if not p: return not s
        if not s and len(p) == 1: return False

        m = len(s) + 1
        n = len(p) + 1

        dp = [[False for c in range(n)] for _ in range(m)]

        dp[0][0] = True
        dp[0][1] = False

        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for r in range(1, m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False

        return dp[m - 1][n - 1]



if __name__ == '__main__':
    s = 'aaa'
    p = 'ab*a*c*a'
    print(re.compile(p).findall(s))
    solution = Solution()
    res = solution.isMatch(s, p)
    print(res)
