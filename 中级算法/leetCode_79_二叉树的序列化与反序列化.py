"""
day: 2020-08-22
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwxa3m/
题目名: 二叉树的序列化与反序列化
题目描述: 序列化是将一个数据结构或者对象转换为连续的比特位的操作,进而可以将转换后的数据存储在一个文件或者内存中
同时也可以通过网络传输到另一个计算机环境,采取相反方式重构得到原数据

请设计一个算法来实现二叉树的序列化与反序列化,保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构
示例:
你可以将以下二叉树：
    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
思路:
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def r_serialize(self, root, string):
        if not root:
            string += 'null'
        else:
            string += str(root.val) + ','
            string = self.r_serialize(root.left, string)
            string = self.r_serialize(root.right, string)
        return string

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 前序遍历
        return self.r_serialize(root, '')
        # 层次遍历
        # if not root:
        #     return '[]'
        # res = []
        # level = [root]
        # while level:
        #     size = len(level)
        #     for _ in range(size):
        #         node = level.pop(0)
        #         if node:
        #             res.append(f'{node.val}')
        #             level.append(node.left)
        #             level.append(node.right)
        #         else:
        #             res.append('null')
        # return '[' + ','.join(res) + ']'

    def r_deserialize(self, node_list):
        if node_list[0] == 'null':
            node_list.pop(0)
            return None
        root = TreeNode(int(node_list[0]))
        node_list.pop(0)
        root.left = self.r_deserialize(node_list)
        root.right = self.r_deserialize(node_list)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 前序遍历
        data = data.split(',')
        return self.r_deserialize(data)
        # 层次遍历
        # if data == '[]':
        #     return None
        # data = data[1:-1].split(',')
        # idx = 1
        # root = TreeNode(int(data[0]))
        # level = [root]
        # while level:
        #     node = level.pop(0)
        #     if data[idx] != 'null':
        #         node.left = TreeNode(int(data[idx]))
        #         level.append(node.left)
        #     idx += 1
        #     if data[idx] != 'null':
        #         node.right = TreeNode(int(data[idx]))
        #         level.append(node.right)
        #     idx += 1
        # return root
