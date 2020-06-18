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
import functools
import time


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



def print_execute_time(func):
    '''定义一个计算执行时间的函数作装饰器，传入参数为装饰的函数或方法'''

    # 定义嵌套函数，用来打印出装饰的函数的执行时间
    @functools.wraps(func)
    def call_func(*args, **kwargs):
        # 定义开始时间和结束时间，将func夹在中间执行，取得其返回值
        start = time.time()
        func_return = func(*args, **kwargs)
        cost = time.time() - start
        cost = round(cost, 3)
        # 打印方法名称和其执行时间
        print('方法{}的运行时间是：{}s'.format(func.__name__, cost))
        # 返回func的返回值
        return func_return

    # 返回嵌套的函数
    return call_func