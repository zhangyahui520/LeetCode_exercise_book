#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 15.三数之和.py
    Author      : Charles zhang
    Created date: 2020/7/1 8:34
    Description :
       给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
        注意：答案中不可以包含重复的三元组。

        示例：
        给定数组 nums = [-1, 0, 1, 2, -1, -4]，
        满足要求的三元组集合为：
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/3sum
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

'''
解题思路： 先两两组合， 然后再判断第三个， 要求不重复，用字典作为容器


'''
from collections import defaultdict


class Solution:
    def threeSum(self, nums):  # 超时
        res = set()
        nums_dict = defaultdict(list)
        for i, v in enumerate(nums):
            nums_dict[v].append(i)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums_dict:
                    # 如果这个值的index与i,j不同
                    index_list = nums_dict[-(nums[i] + nums[j])]
                    for index in index_list:
                        if index != i and index != j:
                            three_num = tuple(sorted([nums[i], nums[j], nums[index]]))
                            # print(three_num)
                            # 判断三个数是否存在
                            res.add(three_num)
                            break

        return [list(item) for item in res]

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''先对数组进行排序， 然后按照左右指针的方法， 找到对应的解'''
        nums.sort()
        self.ans = []
        left, right = 0, len(nums) - 1
        for a in range(len(nums) - 2):
            # 前一个和它相等就重复了
            if a > 0 and nums[a - 1] == nums[a]:
                continue

            left = a + 1
            self.sumTwo(nums, left, right, -nums[a])

        return self.ans

    def sumTwo(self, nums, left, right, target):
        while left < right:
            summation = nums[left] + nums[right]
            if summation == target:
                self.ans.append((-target, nums[left], nums[right]))

                left, right = left + 1, right - 1
                # 如果和前一个一样，就重复了， 相同数字的判断只需要一次
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif summation < target:
                left += 1
            else:
                right -= 1

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.threeSum1(nums)
    print(res)
