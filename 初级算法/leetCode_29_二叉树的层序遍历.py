"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnldjj/
题目名: 二叉树的层序遍历
题目描述: 给定一个二叉树,返回按照层序遍历得到的节点值(逐层,从左到右)
示例:
     2
    / \
   9   10
  / \ / \
 1  3 15  7
   输出: [2, 9, 10, 1, 3, 15, 7]
思路:
1.BFS
    按照层搜索,BFS的模板:
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.pop()
            if cur:
                ....
                queue.append(cur.left)
                queue.append(cur.right)
2.DFS
    先递归左子树,再递归右子树,需要一个level来记录当前节点的深度,
    来确定节点的值该放在哪一个列表中
    当进入一个新的level时,在res中新建一个新列表来保存该level中的所有节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        # result = []
        # if root:
        #     nodes = [root]
        #     while nodes:
        #         size = len(nodes)
        #         nodes_val = []
        #         for _ in range(size):
        #             node = nodes.pop(0)
        #             nodes_val.append(node.val)
        #             if node.left:
        #                 nodes.append(node.left)
        #             if node.right:
        #                 nodes.append(node.right)
        #         result.append(nodes_val)
        # return result
        def level(node, node_level, res):
            if not node:
                return
            # 进入了新的一层
            if len(res) == node_level:
                res.append([])
            res[node_level].append(node.val)
            if node.left:
                level(node.left, node_level+1, res)
            if node.right:
                level(node.right, node_level+1, res)
        result = []
        level(root, 0, result)
        return result
