#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 11.盛最多水的容器.py
    Author      : Charles zhang
    Created date: 2020/6/28 8:31
    Description :

        给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

        说明：你不能倾斜容器，且 n 的值至少为 2。

        图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

        示例：

        输入：[1,8,6,2,5,4,8,3,7]
        输出：49
"""

'''
思路： 
    1、貌似又是动态规划的问题， 需要找到所有的可能性， 然后再判断出其中最大的值
    
    2、遍历数组，依次计算每种可能的体积大小， 然后求出最大值




'''


class Solution:
    def maxArea(self, height):  # 超时
        # 定义一个变量保存最大的体积
        max_value = 0
        # dp = [[0] * len(height) for _ in range(len(height))]
        # 遍历数组
        for i in range(1, len(height)):
            for j in range(i):
                # dp[i][j] = min(height[i], height[j]) * (i - j)
                print(f'i:{i}, j:{j}, height[i]:{height[i]}, height[j]:{height[j]}, dp[i][j:{min(height[i], height[j]) * (i - j)}')
                max_value = max(min(height[i], height[j]) * (i - j), max_value)

        return max_value

    def maxArea2(self, height):  # 运算错误， 未能通过
        # 定义一个变量保存最大的体积
        max_value = 0
        # 定义两个变量保存两个最佳组合，每次只与最佳组合进行比较，如果超过最佳组合，则进行更新
        left_max, right_max = 0, 1
        n = len(height)
        index = 1
        while index < n:
            left_value = min(height[left_max], height[index]) * (index - left_max)
            right_value = min(height[right_max], height[index]) * (index - right_max)
            print(f'left_max:{left_max}, right_max:{right_max}, index:{index}, left_value:{left_value}, right_value:{right_value}')
            if left_value > right_value:
                max_value = left_value
                right_max = index
            else:
                max_value = right_value
                left_max = index
            index += 1
        return max_value

    def maxArea3(self, height): # 从两边向中间靠近， 双指针法
        max_area = -float('inf')
        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    height = [2, 3, 10, 5, 7, 8, 9]
    solution = Solution()
    result = solution.maxArea3(height)
    print(result)
