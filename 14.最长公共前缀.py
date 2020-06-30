#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 14.最长公共前缀.py
    Author      : Charles zhang
    Created date: 2020/6/30 8:33
    Description :
       编写一个函数来查找字符串数组中的最长公共前缀。

        如果不存在公共前缀，返回空字符串 ""。

        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"
        示例 2:

        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。
        说明:

        所有输入只包含小写字母 a-z 。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/longest-common-prefix
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
思路： 最长公共前缀，应该是从开头算起，遍历每个字符串，看是否相同

能否使用切片的形式呢

这个解法的官方说法是： 纵向比较法  >_<
'''


class Solution:
    def longestCommonPrefix(self, strs):
        commonPrefix = ''
        index = 0
        while index >= 0:
            # 需要判断index 小于每个字符
            characters = ''
            for item in strs:
                if index < len(item):
                    characters += item[index]
                else:
                    break
            # 如果字符集合都相等， 那么就添加到公共前缀中, 否则就跳出
            if len(characters) > 0 and characters == (characters[0] * len(strs)):
                commonPrefix += characters[0]
            else:
                break
            index += 1
        return commonPrefix


if __name__ == '__main__':
    strs = []
    solution = Solution()
    res = solution.longestCommonPrefix(strs)
    print(res)
