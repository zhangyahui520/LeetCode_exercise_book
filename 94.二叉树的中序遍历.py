#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 94.二叉树的中序遍历.py
    Author      : Charles
    Created date: 2020/7/11 1:52 下午
    Description :
       给定一个二叉树，返回它的中序 遍历。

        示例:

        输入: [1,null,2,3]
           1
            \
             2
            /
           3

        输出: [1,3,2]
        进阶: 递归算法很简单，你可以通过迭代算法完成吗？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
思路： 二叉树的中序遍历，先左，再根，后右，核心思想是递归
'''


class Solution:
    def inorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)


'''
利用栈来实现中序遍历
'''


class Solution:
    def inorderTraversal(self, root):

        stack = []
        res = []
        if root is None:
            return []

        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                n = stack.pop()
                res.append(n.val)
                if n.right is not None:
                    root = n.right
        return res


'''
其核心思想如下：

使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
如果遇到的节点为灰色，则将节点的值输出。

作者：hzhu212
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def inorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


# 优化写法：代码虽然更简洁，但是好像运行时间更长了，试了几次都是这样

class Solution:
    def inorderTraversal(self, root):
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst


# 大佬优化的层次遍历， 利用队列的思想，自上而下，自左至右，刚好符合队列的要求。
class Solution:
    def levelTraversal(self, root: TreeNode) -> List[int]:
        queue, rst = [root], []
        while queue:
            i = queue.pop(0)
            if isinstance(i, TreeNode):
                queue.extend([i.val, i.left, i.right])
            elif isinstance(i, int):
                rst.append(i)
        return rst
