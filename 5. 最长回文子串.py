#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 5. 最长回文子串.py
    Author      : Charles zhang
    Created date: 2020/6/18 8:19
    Description :
       给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

        示例 1：

        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。
        示例 2：

        输入: "cbbd"
        输出: "bb"

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/longest-palindromic-substring
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''

    注意： 回文串的特点是正序等于倒序
    
    解题思路： 暴力求解
        设定一个数组存储最长回文串
        定义一个数组存储已经遍历的字符
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    处理结果超时： 14.621s
    
    # 超时应该是选择判断回文串的时候耗费了太多时间， 对选择回文串的方法进行优化
    
    
'''


from LeetCode_exercise_book import utils


class Solution:
    # 第一种解法： 暴力求解： 0.486s
    @utils.print_execute_time
    def longestPalindrome(self, s):
        longest_palindrome = ''  # 最长回文串
        tmp = ''  # 临时变量，存储遍历过得租字符
        i = 0
        while i < len(s):
            tmp += s[i]
            # print('s[i]: {}, tmp: {}, longest_palindrome:{}'.format(s[i], tmp, longest_palindrome))
            # 遍历tmp， 如果包含回文串， 则与最长比较
            for j in range(len(tmp)):
                if tmp[j] == s[i]:  # 字符与tmp中的字符相等，则中间的部分可能是回文串
                    palindrome = tmp[j: len(tmp)]  # 因为s[i]已经添加到最后一位了
                    if self.determine_palindrome(palindrome) and len(palindrome) > len(longest_palindrome):
                        # 如果是回文串并且长度大于最长串， 则进行替换
                        longest_palindrome = palindrome
            i += 1  # 继续遍历下一个
        return longest_palindrome

    def determine_palindrome(self, substring):
        '''判断字符串是否是回文串
        优化： 回文串的特点是正序等于倒序， 所以这点可以优化
        '''
        return substring == substring[::-1]
        # for i in range(len(substring) // 2):  # 只循环到中间， 如果两边的结果都相等，则返回True，否则是False
        #     if substring[i] != substring[len(substring) - 1 - i]:
        #         return False
        # return True

    @utils.print_execute_time
    def longestPalindrome_2(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ''
        # 枚举子串的长度 1+1
        for l in range(n):
            # 枚举子串的起始位置i, 这样可以通过j=i+1 得到子串的结束位置
            for i in range(n):
                j = i + 1
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i]==s[j])
                if dp[i][j] and l+1 > len(ans):
                    ans = s[i:j+1]
        return ans




if __name__ == '__main__':
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = "babad"
    solution = Solution()
    # result = solution.longestPalindrome(s)
    result = solution.longestPalindrome_2(s)
    print(result)

