"""
day: 2020-09-22
url: https://leetcode-cn.com/problems/binary-tree-cameras/
题目名: 监控二叉树
给定一个二叉树,我们在树的节点上安装摄像头.
节点上的每个摄像头都可以监事其父对象,自身及其直接子对象
计算监控树的所有节点所需的最小摄像头数量.
思路:
    对于一个节点,他会有三种状态:
    1. 自身是监控器
    2. 自身不是监控器,但是可以被监控到
    3. 该节点没有被监控到
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        if root:
            def dfs(node):
                nonlocal ans
                # 表示该节点安装了监视器
                if not node:
                    return 2
                left = dfs(node.left)
                right = dfs(node.right)
                # 如果左节点或右节点任意一个处在
                # 不可监控状态,那么需要将该节点设置为监控节点
                if left == 3 or right == 3:
                    ans += 1
                    return 1
                # 左节点与右节点任意一个为监控节点,那么
                # 当前节点处于状态2,也就是可以被监控到,但是不是监控节点
                elif left == 1 or right == 1:
                    return 2
                # 如果该节点的左右节点都处于状态2, 那么这个节点处于不可监控状态
                return 3

            if dfs(root) == 3:
                ans += 1
        return ans
