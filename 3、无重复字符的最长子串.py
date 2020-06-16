#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 3、无重复字符的最长子串.py
    Author      : Charles zhang
    Created date: 2020/6/16 8:51
    Description :
       给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        longestSubstring = ''
        substring = ''
        for i in range(len(s)):  # 遍历字符串
            if s[i] in substring:  # 如果字符和子串中的字符重复，则从重复字符的后面开始算作新子串
                substring = substring[substring.index(s[i])+1:]
            substring += s[i]
            if len(substring) > len(longestSubstring):  # 如果子串大于最长子串，则进行替换
                longestSubstring = substring

        return len(longestSubstring)


if __name__ == '__main__':
    '''
        先审题， 不含重复字符的最长子串， 意味着子串中不能存在重复字符，
         所以可以从头开始计算， 遇到重复字符就算是一个新的子串， 将最长子串单独保存，遍历结束后返回最长子串
        
        第二次修改： 当遇到重复字符时，应该从重复字符的下一位开始计算，而不是从头开始
    '''

    s = "dvdf"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)