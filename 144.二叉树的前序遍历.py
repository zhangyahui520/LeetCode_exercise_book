#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 144.二叉树的前序遍历.py
    Author      : Charles
    Created date: 2020/7/11 2:46 下午
    Description :
       给定一个二叉树，返回它的 前序 遍历。

         示例:

        输入: [1,null,2,3]
           1
            \
             2
            /
           3

        输出: [1,2,3]
        进阶: 递归算法很简单，你可以通过迭代算法完成吗？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归算法, 根 -》左-》右， 36ms

class Solution:
    def preorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res


    def traverse(self, root):
        if root is None:
            return

        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


# 利用栈进行迭代, 前序遍历的特点是根，左，右. 56ms
class Solution:
    def preorderTraversal(self, root):
        self.res = []
        stack = [root]
        if root is None:
            return self.res

        # 如果结点不为0，或stack不为空
        while stack:
            node = stack.pop()
            self.res.append(node.val)
            # 先放置右子树，再放置左子树，这样可以保证左子树先被弹出
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return self.res


# 利用改进的算法， 加上标识符进行判断, WHITE表示未访问，GARY表示已访问.44ms
class Solution:
    def preorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                # 先放右结点，再放左结点，再放根节点，这样栈弹出的次序才会是根-左-右
                stack.append((WHITE, node.right)) # 先放右结点
                stack.append((WHITE, node.left)) # 先放左结点
                stack.append((GRAY, node)) # 先放根结点
            else:
                res.append(node.val)

        return res


# 在此代码上进一步优化，只是代码层面的优化, 40ms
class Solution:
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            # 如果是节点，就将该结点的信息存入栈中，按照弹出顺序进行压入
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.left, node.val])
            elif isinstance(node, int):
                res.append(node)
        return res
