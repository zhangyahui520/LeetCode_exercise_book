#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 2、两数相加.py
    Author      : Charles zhang
    Created date: 2020/6/15 9:09
    Description :
       给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        # 首先将两个值转为数字， 然后计算结果，再将结果转为链表
        num1 = self.linked_list_to_number(l1)
        num2 = self.linked_list_to_number(l2)
        print(num1, num2)
        res = num1 + num2
        return self.number_to_linked_list(res)

    def linked_list_to_number(self, linked_list):
        '''将逆序存储的链表转为数字'''
        num = 0
        e = 0
        while linked_list:
            num += linked_list.val * pow(10, e)
            e += 1
            linked_list = linked_list.next
        return num

    def number_to_linked_list(self, res):
        '''数字转为链表，按照逆序的方式存储'''
        dummy = ListNode(-1)
        pre = dummy
        # 对res为0的情况进行判断
        if res == 0:
            pre.next = ListNode(res % 10)
            return dummy.next

        while res:
            pre.next = ListNode(res % 10)
            pre = pre.next
            res = res // 10
        return dummy.next


if __name__ == '__main__':
    l1 = [0]
    l2 = [0]

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print(result)
