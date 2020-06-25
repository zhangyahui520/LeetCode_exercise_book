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
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i, j 分别是s, p的索引
        i, j = 0, 0
        res = ''
        while i < len(s) and j < len(p):
            if p[j:j + 2] == '.*':  # 如果出现.*，需要判断p后面是否还有字符
                if j + 2 != len(p):  # 后面还有数，向下遍历，找到s[i] ==p[j]的地方
                    while i < len(s):
                        if s[i] == s[j]:
                            break
                        else:
                            res += s[i]
                            i += 1
                else:
                    return True

            # 先判断 p的下一位是 * , 如果两个字符相等，则匹配S的下一个字符
            # 否则就跳过p的两位
            if j + 1 < len(p) and p[j + 1] == '*':
                if s[i] == p[j]:
                    res += s[i]
                    i += 1
                else:
                    j += 2
            else:
                # 进行字符匹配
                if s[i] == p[j]:
                    res +=s[i]
                    i += 1
                    j += 1
                elif p[j] == '.':
                    res += s[i]
                    i += 1
                    j += 1
                else:
                    return False
            print(i, j)
        print(res)
        return i == len(s)


if __name__ == '__main__':
    s = 'aaaa'
    p = 'aaaaa'
    solution = Solution()
    res = solution.isMatch(s, p)
    print(res)
