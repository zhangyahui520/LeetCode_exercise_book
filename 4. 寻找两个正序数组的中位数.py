#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 4. 寻找两个正序数组的中位数.py
    Author      : Charles zhang
    Created date: 2020/6/17 8:36
    Description :
       寻找两个正序数组的中位数

"""
import math

'''
找到两个正序数组中的中位数， 可以先比较两个数组的大小吗？先确定两个数组的长度， 即可知道中位数的大致位置

然后依然是利用二分查找法（二分查找法是找指定数，不是用来找中位数）， 不过要将两个数组结合起来
1、先判断两个数组的最小值和最大值， 找到两个数组中的最小值和最大值
2、找到


思路二：
    1、对两个数组分别求中位数，然后判断两个数组的中位数的大小，以及与各数组的最大值
    和最小值的比较， 然后确定保留的区域， 进行下一次判断。

思路三：
    将两个数组合并，合并之后就能很轻松的获取到中位数
    

'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # # 先判断两个数组的长度， 确定中位数的位置
        # len1, len2 = len(nums1), len(nums2)
        # if (len1 + len2) % 2 == 0:  # 两个数组长度和是偶数
        #     mid = (len1 + len2) / 2
        #     print('中位数有两个')
        # else:
        #     print('中位数有一个')
        #
        # # 判断两个数组的最大值和最小值
        # min1, max1 = nums1[0], nums1[len1 - 1]
        # min2, max2 = nums2[0], nums2[len2-1]
        # # 判断两个数组左右两边的大小
        # if min1

        # 解法1： 先暴力求解, 遍历两个数组，合并之后求出中位数
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:  # 如果i 小于 j， 将小的存入result， 继续下一个
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # 当循环结束后， 剩下的就是全部并入数组中
        result += nums1[i:]
        result += nums2[j:]

        print(result)
        # 判断整合数组的长度
        if len(result) % 2 == 0:  # 如果是偶数，那么中位数就是两个数之和
            mid = int(len(result) / 2)
            print(mid)
            return (result[mid-1] + result[mid]) / 2
        else:
            mid = math.floor(len(result) / 2)
            return result[mid]


if __name__ == '__main__':
    num1 = [1, 2]
    num2 = [3, 4]
    solution = Solution()
    result = solution.findMedianSortedArrays(num1, num2)
    print(result)
