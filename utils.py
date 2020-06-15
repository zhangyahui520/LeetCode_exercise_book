#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : utils.py
    Author      : Charles zhang
    Created date: 2020/6/15 9:20
    Description :
       做题中常用的一些函数
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    while res:
        pre.next = ListNode(res % 10)
        pre = pre.next
        res = res // 10
    return dummy.next