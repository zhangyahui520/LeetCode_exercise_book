#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 429.N叉树的层序遍历.py
    Author      : Charles zhang
    Created date: 2020/7/20 8:41
    Description :
       给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

    例如，给定一个 3叉树 :
        返回其层序遍历:

        [
             [1],
             [3,2,4],
             [5,6]
        ]
         

        说明:

        树的深度不会超过 1000。
        树的节点总数不会超过 5000。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
思路： 层序遍历
    前序遍历的基础上， 增加一个节点的度level， 相同度的节点放在一个输出中

1、先尝试递归处理
2、再尝试用栈进行处理

'''

from collections import defaultdict


class Solution:  # 递归调用： 64ms
    def levelOrder(self, root):
        if root is None:
            return []

        self.res = defaultdict(list)
        level = 0
        self.traverse(root, level)
        # self.res = sorted(self.res.items(), key=lambda obj: obj[0])
        res = []
        for i in range(len(self.res)):
            res.append(self.res[i])
        return res

    def traverse(self, root, level):
        if root is None:
            return

        # 遍历所有孩子节点，添加到res中
        self.res[level].append(root.val)
        level += 1
        for children_node in root.children:
            self.traverse(children_node, level)


# 利用栈进行处理， 优化，利用队列进行处理，先进先出, 耗时76ms
from collections import defaultdict
class Solution:
    def levelOrder(self, root):
        level = 0
        res = defaultdict(list)
        queue = [(root, level)]
        while queue:
            node, level = queue.pop(0)
            if node is None: continue
            res[level].append(node.val)
            for children_node in node.children:
                queue.append((children_node, level+1))

        tmp = []
        for i in range(len(res)):
            tmp.append(res[i])
        return tmp


# 未执行通过
class Solution:
    def levelTraversal(self, root):
        level = 0
        queue = [(root, level)]
        rst = defaultdict(list)
        while queue:
            node, level = queue.pop(0)
            if isinstance(node, TreeNode):
                queue.append((node.val, level+1))
                for children_node in node.children:
                    queue.append((children_node, level + 1))
            elif isinstance(node, int):
                rst[level].append(node)
        res = []
        for i in range(len(rst)):
            res.append(rst[i])
        return res

