"""
day: 2020-08-18
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvix0d/
题目名: 从前序与中序遍历序列构造二叉树
题目描述: 根据一棵树的前序遍历与中序遍历构造二叉树
示例:
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
    3
   / \
  9  20
    /  \
   15   7
思路:
前序遍历:[根, 左子树的前序遍历结果, 右子树的前序遍历结果]
中序遍历:[左子树的中序遍历结果, 根, 右子树的中序遍历结果]

1. 递归
    先构建根节点,然后构建左子树,最后构建右子树.
    对于前序遍历来说,第一个节点就是根节点,我们可以建立一个中序遍历的 value:index的哈希表
    然后通过前序遍历的根节点的值,定位到中序遍历数组中的根节点所在的位置,那么在根节点左边的就是
    左子树,右边的就是右子树,先构建左子树,所以将左子树的前序遍历数组与中序遍历数组传进去继续构建
    然后构建右子树,将右子树的前序遍历数组与中序遍历数组传进去,当当前根节点没有子节点时,就返回none
    否则返回构建好的根节点

2. 迭代
    构建一个栈stack,存放的是在当前节点的祖先节点中还没有考虑过右孩子的节点.
    定义一个指针inorderIdx,用来表示当前节点不断往左移的最终节点
    对于前序遍历的结果来说,两个连续节点u和v,他们只会有三种关系
    v是u的左孩子;u没有左孩子,v是u的右孩子;v是u的某个祖先节点的右孩子

    当stack[-1]与inorder[inorderIdx]不相等时,说明当前节点还能往左移,
    所以将当前节点添加到栈顶节点的左孩子中,并将该节点入栈.

    当stack[-1]==inorder[inorderIdx]时,说明当前节点不能往左移了,
    stack的出栈顺序与inorder的左子树遍历顺序在遇见右孩子节点时,是一样的.
    所以我们判断栈顶元素是否与inorder[inorderIdx]相等,若相等则将元素弹出,
    并让指针右移,直到两者不相等,说明当前指针指向的节点是一个右孩子节点,而他的
    双亲节点就是上一个栈顶元素,所以我们将当前指针指向的节点添加到上一个栈顶元素的右孩子
    节点中,并将该节点入栈(因为该右孩子节点可能还会有子节点)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        # def helper(preorder_left, preorder_right, inorder_left, inorder_right):
        #     if preorder_left > preorder_right:
        #         return None

        #     # 前序遍历的第一个节点就是根节点
        #     preorder_root = preorder_left
        #     # 根据建立的索引表,找到在中序遍历中根节点的索引
        #     inorder_root = index[preorder[preorder_root]]
        #     # 建立根节点
        #     root = TreeNode(preorder[preorder_root])
        #     # 左子树中的节点数目,就是中序遍历中根节点的索引-第一个节点的索引
        #     size_left_tree = inorder_root - inorder_left
        #     # 递归构造左子树
        #     # 前序遍历中,第一个节点是根节点,然后后面的都是根节点的左子树节点,最后是右子树节点
        #     # 所以我们的范围应该是[根节点+1, 根节点+左子树节点数]
        #     # 而中序遍历则是第一个节点到根节点之前的一个节点
        #     root.left = helper(preorder_left+1, preorder_left+size_left_tree,
        #                        inorder_left, inorder_root-1)
        #     # 递归构造右子树
        #     # 前序遍历中,右子树的范围是[左子树的最后一个节点+1, 尾部]
        #     # 中序遍历中,右子树的范围是[根节点的下一个节点,尾部]
        #     root.right = helper(preorder_left+size_left_tree+1, preorder_right,
        #                         inorder_root+1, inorder_right)
        #     return root

        # n = len(preorder)
        # # 哈希映射,用来定位根节点
        # index = {value: idx for idx, value in enumerate(inorder)}
        # return helper(0, n-1, 0, n-1)

        if not preorder:
            return None

        # 前序遍历的第一个节点是根节点
        root = TreeNode(preorder[0])
        # 栈中保存的是所有未考虑过右节点的节点
        stack = [root]
        # 遍历中序遍历数组的指针
        inorderIndex = 0
        # 遍历前序遍历数组中根节点后的节点
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            # 若栈顶的值与中序遍历中的节点值不相等,说明还没有遍历到前序遍历中的左子树的最后一个左节点
            if node.val != inorder[inorderIndex]:
                # 那么节点的左孩子必然是该节点
                node.left = TreeNode(preorderVal)
                # 将该节点推入栈中
                stack.append(node.left)
            # 当栈顶的值与中序遍历中的节点值相等时,说明我们遇到了一个右孩子节点
            else:
                # 栈的出栈顺序与中序遍历的遍历顺序是一样的,我们让node指向
                # 推出的栈顶节点,一直到栈顶节点不等于中序遍历中的值时,说明
                # 遇到了一个右孩子节点,那么这个右孩子节点就是上一个栈顶节点的右孩子
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                # 我们将这个右孩子赋给node节点,因为node节点指向的是上一个栈顶元素
                # 将这个右孩子推入栈中,因为这个右孩子有可能还有子节点
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root
