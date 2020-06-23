#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 7.整数反转.py
    Author      : Charles zhang
    Created date: 2020/6/23 8:30
    Description :
       给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

        示例 1:

        输入: 123
        输出: 321
         示例 2:

        输入: -123
        输出: -321
        示例 3:

        输入: 120
        输出: 21
        注意:

        假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/reverse-integer
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
'''
思路一： 将数字转成字符， 然后反转遍历， 计算得到最后结果

思路二：按10取余，计算得到所有的数字，然后再计算得到最后结果
'''


class Solution:
    def reverse(self, x):
        # 判断是否越界
        if x >= 0:
            x_str = str(x)
            x_reverse = int(x_str[::-1])
        # 如果x是负数，如果对负号进行处理
        if x < 0:
            x_str = str(x)
            x_reverse = -int(x_str[1:][::-1])

        return self.cross_border_judgment(x_reverse)

    def cross_border_judgment(self, x):
        if x > (pow(2, 31) - 1):
            return 0
        elif x < -pow(2, 31):
            return 0
        else:
            return x


class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def func(x,res=0):
            x= x if x>=0 else -x
            if x==0:
                return res
            res = res*10+x%10
            w = func(x//10,res)
            if res > 2**31:
                return 0
            return w
        return func(x) if x>=0 else -1*func(x)



if __name__ == '__main__':
    x = -123
    solution = Solution2()
    result = solution.reverse(x)
    print(result)
