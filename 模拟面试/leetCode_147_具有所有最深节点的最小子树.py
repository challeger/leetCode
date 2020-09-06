"""
day: 2020-09-06
url: https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/submissions/
题目名: 具有所有最深节点的最小子树

给定一个根为 root 的二叉树,每个结点的深度是它到根的最短距离
如果一个结点在整个树的任意结点之间具有最大的深度,则该结点是最深的
一个结点的子树是该结点加上它的所有后代的集合
返回能满足“以该结点为根的子树中包含所有最深的结点”这一条件的具有最大深度的结点

思路:
1. 两次遍历
    第一次遍历记录所有节点的深度,并找到最深深度.
    第二次遍历找节点,
    如果一个节点的左右子树都具有最大深度节点,那么应该返回该节点
    如果一个节点的左右子树都不具有最大深度节点,那么应该返回空
    如果一个节点只有某个左子树或右子树包含最大深度节点,那么应该返回包含最大深度节点的子树
2. 一次遍历
    自底向上递归,底部节点返回0, 每次返回 深度+节点
    如果左节点深度 > 右节点深度: 返回左节点
    如果右节点深度 > 左节点深度: 返回右节点
    相等返回当前节点.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {None: -1}
        max_depth = 0

        def dfs(node, parent=None):
            nonlocal max_depth, depth
            depth[node] = depth[parent] + 1
            max_depth = max(max_depth, depth[node])
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        # 先遍历一次树,将所有节点的深度记录下来
        dfs(root)

        def ans(node):
            if not node or depth[node] == max_depth:
                return node
            left = ans(node.left)
            right = ans(node.right)
            return node if left and right else left or right
        return ans(root)

    def subtreeWithAllDeepest_one(self, root: TreeNode) -> TreeNode:
        import collections
        Result = collections.namedtuple('Result', ['node', 'depth'])

        def dfs(node) -> Result:
            if not node:
                return Result(None, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            if left.depth > right.depth:
                return Result(left.node, left.depth+1)
            if right.depth > left.depth:
                return Result(right.node, right.depth+1)
            return Result(node, left.depth+1)
        return dfs(root).node
