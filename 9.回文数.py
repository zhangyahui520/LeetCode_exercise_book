#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 9.回文数.py
    Author      : Charles
    Created date: 2020/6/25 8:23 上午
    Description :
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

        示例 1:

        输入: 121
        输出: true
        示例 2:

        输入: -121
        输出: false
        解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
        示例 3:

        输入: 10
        输出: false
        解释: 从右向左读, 为 01 。因此它不是一个回文数。
        进阶:

        你能不将整数转为字符串来解决这个问题吗？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/palindrome-number
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 不转为字符形式求解
        # 负数一定不是回文数
        if x < 0:
            return False

        # 将个位数变为最高位，如果还相等，就是回文数
        res = 0
        tmp = x
        while tmp / 10:
            res = res * 10 + tmp % 10
            tmp = tmp // 10
            print(f'res:{res}, x:{tmp}')
        return res == x

if __name__ == '__main__':
    x = 121
    solution = Solution()
    res = solution.isPalindrome(x)
    print(res)