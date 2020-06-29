#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 13.罗马数字转整数.py
    Author      : Charles zhang
    Created date: 2020/6/29 9:12
    Description :
       罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

        通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

        示例 1:

        输入: "III"
        输出: 3
        示例 2:

        输入: "IV"
        输出: 4
        示例 3:

        输入: "IX"
        输出: 9
        示例 4:

        输入: "LVIII"
        输出: 58
        解释: L = 50, V= 5, III = 3.
        示例 5:

        输入: "MCMXCIV"
        输出: 1994
        解释: M = 1000, CM = 900, XC = 90, IV = 4.

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/roman-to-integer
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
简单遍历，判断是否是罗马数字

'''

from collections import OrderedDict


class Solution:
    def romanToInt(self, s):
        roman_dict = {'M': 1000,
                      'CM': 900,
                      'D': 500,
                      'CD': 400,
                      'C': 100,
                      'XC': 90,
                      'L': 50,
                      'XL': 40,
                      'X': 10,
                      'IX': 9,
                      'V': 5,
                      'IV': 4,
                      'I': 1}
        # 主要是判断六种特色情况
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == 'I' and i + 1 < n:
                if s[i + 1] == 'V' or s[i + 1] == 'X':
                    roman = s[i:i + 2]
                    i += 2
                else:
                    roman = s[i]
                    i += 1
            elif s[i] == 'X' and i + 1 < n:
                if s[i + 1] == 'L' or s[i + 1] == 'C':
                    roman = s[i:i + 2]
                    i += 2
                else:
                    roman = s[i]
                    i += 1
            elif s[i] == 'C' and i + 1 < n:
                if s[i + 1] == 'D' or s[i + 1] == 'M':
                    roman = s[i:i + 2]
                    i += 2
                else:
                    roman = s[i]
                    i += 1
            else:
                roman = s[i]
                i += 1

            res += roman_dict[roman]

        return res

    # 大佬的解法
    def romanToInt1(self, s: str) -> int:
        # 按照这种解法， 六种特殊情况的前面一位一定会被计算，所以将特殊情况的数字先减去对应值，再加上
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500, 'CM': 800, 'M': 1000}
        '''
        for i, n in enumerate(s):
            print(f'max(i - 1, 0):{max(i - 1, 0)}, i + 1:{i + 1}')
            print(f's[max(i - 1, 0):i + 1]:{s[max(i - 1, 0):i + 1]}, d[n]:{d[n]}')
            q = d.get(s[max(i - 1, 0):i + 1], d[n])  # 每次获取两个值， 如果该值在字典中没有，就取当前数
            print(q)
        '''
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


if __name__ == '__main__':
    s = "IMIM"
    solution = Solution()
    res = solution.romanToInt1(s)
    print(res)
