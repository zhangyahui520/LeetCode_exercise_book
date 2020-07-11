#!/usr/bin/env python
# coding=utf-8
"""
    Copyright (C) 2019 * Ltd. All rights reserved.
 
    Editor      : PyCharm
    File name   : 145.二叉树的后序遍历.py
    Author      : Charles
    Created date: 2020/7/11 3:25 下午
    Description :
       给定一个二叉树，返回它的 后序 遍历。

        示例:

        输入: [1,null,2,3]
           1
            \
             2
            /
           3

        输出: [3,2,1]
        进阶: 递归算法很简单，你可以通过迭代算法完成吗？

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归解法， 后序遍历的顺序是： 左 - 右 - 根. 44ms

class Solution:
    def postorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(root.val)


# 利用栈进行迭代, BFS，对一个节点，先找到它的叶子节点，然后再依次遍历。 36ms
class Solution:
    def postorderTraversal(self, root):
        self.res = []
        stack = []

        if root is None:
            return self.res

        while stack or root:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right

            root = stack.pop()
            self.res.append(root.val)
            if stack and stack[-1].left == root:
                root = stack[-1].right
            else:
                root = None
        return self.res

# 利用表示符进行判断, 40ms
class Solution:
    def postorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                # 先放置根节点，再放置右结点，最后放置左结点
                stack.append((GRAY, node)) # 根节点
                stack.append((WHITE, node.right)) # 右节点
                stack.append((WHITE, node.left)) # 左节点
            else:
                res.append(node.val)
        return res

# 表示符进一步改进, 44ms
class Solution:
    def postorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.val, node.right, node.left])
            if isinstance(node, int):
                res.append(node)
        return res

# DFS
class Solution:
    def postorderTraversal(self, root):
        res = []
        stack = []

        if root is None:
            return res

        while stack or root:
            # 先找到最左子节点
            while root.left:
                stack.append(root.left)
                root = root.left

            # 然后判断是否有右结点，如果有则压入，否则就输出结果
            if root.right:
                stack.append(root.right)
                root = root.right
            else:
                res.append(root.val)
                root = stack.pop()

        return res


'''
如果想理解这道题，首先我们需要了解二叉树的迭代遍历，这里以前序遍历为例：

如果小伙伴们已经掌握则可以跳到下一段

核心思想为：

每拿到一个 节点 就把它保存在 栈 中

继续对这个节点的 左子树 重复 过程1，直到左子树为 空

因为保存在 栈 中的节点都遍历了 左子树 但是没有遍历 右子树，所以对栈中节点 出栈 并对它的 右子树 重复 过程1

直到遍历完所有节点

详细代码及过程注释如下：

Scala

import scala.collection.mutable
obejct TraversalTree {
  // 二叉树的前序遍历
  def preorderTraversal(root: TreeNode): List[Int] = {
    // 用一个栈来保存中间结果
    val stack = new mutable.Stack[TreeNode]()
    val result = new mutable.ListBuffer[Int]()
    var temp = root
    while(temp != null || stack.nonEmpty) {
      if (temp != null) {
        // 每遇到一个节点，就把它加入结果集，并把该节点保存到中间结果中
        result.+=(temp.value)
        stack.push(temp)
        // 先遍历左子树，一直走到空
        temp = temp.left
      } else {
        // 左子树走到空，就从获取已经遍历过左子树的中间结果，将它出栈，并遍历它的右子树
        val node = stack.pop()
        temp = node.right
      }
    }

    result.toList
  }
}
接下来我们思考一下前序遍历和后序遍历之间的关系：

前序遍历顺序为：根 -> 左 -> 右

后序遍历顺序为：左 -> 右 -> 根

如果1： 我们将前序遍历中节点插入结果链表尾部的逻辑，修改为将节点插入结果链表的头部

那么结果链表就变为了：右 -> 左 -> 根

如果2： 我们将遍历的顺序由从左到右修改为从右到左，配合如果1

那么结果链表就变为了：左 -> 右 -> 根

这刚好是后序遍历的顺序

基于这两个思路，我们想一下如何处理：

修改前序遍历代码中，节点写入结果链表的代码，将插入队尾修改为插入队首

修改前序遍历代码中，每次先查看左节点再查看右节点的逻辑，变为先查看右节点再查看左节点

想清楚了逻辑，就可以开始编写代码了，详细代码和逻辑注释如下：

Scala

import scala.collection.mutable
object BinaryTreeRightSideView {
  // 二叉树的后序遍历
  def postorderTraversal(root: TreeNode): List[Int] = {
    val stack = new mutable.Stack[TreeNode]()
    val result = new mutable.ListBuffer[Int]()
    var temp = root
    while(temp != null || stack.nonEmpty) {
      if (temp != null) {
        // 对应处理1，每次前序遍历时，都将节点写入结果链表头，而不是尾
        result.+=:(temp.value)
        stack.push(temp)
        // 对应处理2，每次先遍历右节点，再遍历左节点
        temp = temp.right
      } else {
        val node = stack.pop()
        // 对应处理2，每次先遍历右节点，再遍历左节点
        temp = node.left
      }
    }

    result.toList
  }
}
复杂度分析

时间复杂度：O(n)O(n)

我们需要遍历树的每一个节点，树一共有 nn 个节点，所以时间复杂度为 nn

空间复杂度：O(n)O(n)

因为是迭代遍历，需要一个stack空间存储中间节点，还需要一个result空间存储结果，所以空间复杂度为 2n2n，也就是 nn。

作者：18211010139
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/die-dai-jie-fa-shi-jian-fu-za-du-onkong-jian-fu-za/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 从「根-左-右」---> 「右-左-根」---> 「左-右-根」的模型提取; 40ms

class Solution:
    def postorderTraversal(self, root):
        res, stack = [], []
        p = root

        while p or stack:
            while p:
                res.insert(0, p.val)
                stack.append(p)
                p = p.right

            p = stack.pop().left

        return res


'''
让我们先看后序遍历的顺序
left right root

接着来看前序遍历的顺序
root left right

如果我们把后序遍历翻转，将会得到：
root right left

相比较前序遍历，仅仅改变了left 和 right的顺序：
所以本题思路将会是：在前序遍历中，把left 和 right的顺序调换，然后输出反转的树即可。

作者：harris-han
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/python3-er-cha-shu-hou-xu-bian-li-die-dai-fang-fa-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[root]
        res=[]
        while stack:
            s=stack.pop()
            res.append(s.val)
            if s.left:#与前序遍历相反
                stack.append(s.left)
            if s.right:
                stack.append(s.right)
        return res[::-1]


'''
如果你只想掌握其中某一种遍历大可去找那些奇技淫巧的题解（一会判断指针一会儿判断栈就问你怕不怕？面试的时候你能想起来？）；如果你想统一掌握三种遍历，并且希望思路清晰，我强烈建议你阅读下去！因为这里介绍的是递归转迭代的思路，而不仅仅是用迭代的形式完成题目。本题解也是双100%哦！

老思路链接
新思路

递归的本质就是压栈，了解递归本质后就完全可以按照递归的思路来迭代。
怎么压，压什么？压的当然是待执行的内容，后面的语句先进栈，所以进栈顺序就决定了前中后序。
我们需要一个标志区分每个递归调用栈，这里使用nullptr来表示。
具体直接看注释，可以参考文章最后“和递归写法的对比”。先序遍历看懂了，中序和后序也就秒懂。

先序遍历

C++

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;  //保存结果
        stack<TreeNode*> call;  //调用栈
        if(root!=nullptr) call.push(root);  //首先介入root节点
        while(!call.empty()){
            TreeNode *t = call.top();
            call.pop();  //访问过的节点弹出
            if(t!=nullptr){
                if(t->right) call.push(t->right);  //右节点先压栈，最后处理
                if(t->left) call.push(t->left);
                call.push(t);  //当前节点重新压栈（留着以后处理），因为先序遍历所以最后压栈
                call.push(nullptr);  //在当前节点之前加入一个空节点表示已经访问过了
            }else{  //空节点表示之前已经访问过了，现在需要处理除了递归之外的内容
                res.push_back(call.top()->val);  //call.top()是nullptr之前压栈的一个节点，也就是上面call.push(t)中的那个t
                call.pop();  //处理完了，第二次弹出节点（彻底从栈中移除）
            }
        }
        return res;
    }
};
后序遍历
你没看错，只有注释部分改变了顺序，父>右>左。

C++

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> call;
        if(root!=nullptr) call.push(root);
        while(!call.empty()){
            TreeNode *t = call.top();
            call.pop();
            if(t!=nullptr){
                call.push(t);  //在右节点之前重新插入该节点，以便在最后处理（访问值）
                call.push(nullptr); //nullptr跟随t插入，标识已经访问过，还没有被处理
                if(t->right) call.push(t->right);
                if(t->left) call.push(t->left);
            }else{
                res.push_back(call.top()->val);
                call.pop();
            }
        }
        return res;   
    }
};
中序遍历
你没看错，只有注释部分改变了顺序，右>父>左。其他和前序遍历“一 模 一 样”

C++

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> call;
        if(root!=nullptr) call.push(root);
        while(!call.empty()){
            TreeNode *t = call.top();
            call.pop();
            if(t!=nullptr){
                if(t->right) call.push(t->right);
                call.push(t);  //在左节点之前重新插入该节点，以便在左节点之后处理（访问值）
                call.push(nullptr); //nullptr跟随t插入，标识已经访问过，还没有被处理
                if(t->left) call.push(t->left);
            }else{
                res.push_back(call.top()->val);
                call.pop();
            }
        }
        return res;
    }
};
对比中序遍历的递归写法


void dfs(t){ //进入函数表示“访问过”，将t从栈中弹出

    dfs(t->left);   //因为要访问t->left, 所以我先把函数中下面的信息都存到栈里。
                //依次call.push(t->right), call.push(t)【t第二次入栈】, call.push(nullptr)【标识t二次入栈】, call.push(t->left)。
                //此时t并没有被处理（卖萌）。栈顶是t->left, 所以现在进入t->left的递归中。

    //res.push_back(t->val)
    t.卖萌();   //t->left 处理完了，t->left被彻底弹出栈。
                //此时栈顶是nullptr, 表示t是已经访问过的。那么我现在需要真正的处理t了（即，执行卖萌操作）。
                //卖萌结束后，t 就被彻底弹出栈了。
    

    dfs(t->right); 
}

作者：sonp
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/mo-fang-di-gui-zhi-bian-yi-xing-by-sonp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None: return []
    result = []
    stack = [root]
    while stack:
        p = stack.pop()
        if p is None:
            p = stack.pop()
            result.append(p.val)
        else:
            if p.right: stack.append(p.right)  # 先append的最后访问
            if p.left: stack.append(p.left)
            stack.append(p)
            stack.append(None)
    return result