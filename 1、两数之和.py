#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 两数之和.py
    Author      : Charles zhang
    Created date: 2020/6/15 8:39
    Description :
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
       
"""


class Solution:
    def twoSum(self, nums, target):

        # 假设数组内的值都是不重复，把数组转为字典, value: index
        # nums = dict(zip(nums, range(len(nums))))
        # result = set()  # 定义一个集合，防止出现重复
        # for item in nums:
        #     # 如果 target - item 的值也在字典中，则两个值匹配完成。
        #     if (target - item) != item and target - item in nums:
        #         result.add(nums[item])
        #         result.add(nums[target - item])
        # return list(result)

        hash = {}  # 定义结果为hash字典， 将数组存入hash字典中， 如果target-num的值在字典中，则两个数匹配成功。
        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], i]
            hash[num] = i

        return [-1, -1]


# 第一次修改： 未考虑到两个数相等的情况， 增加相等判断
 # 第二次修改： 数组中可以存在重复值，将结果改为hash字典。


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
