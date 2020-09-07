"""
day: 2020-09-07
url: https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/
题目名: 验证二叉树的前序序列化
序列化二叉树的一种方法是使用前序遍历.当我们遇到一个非空节点时,我们可以记录下这个节点的值.
如果它是一个空节点,我们可以使用一个标记值记录,例如 #。

给定一串以逗号分隔的序列,验证它是否是正确的二叉树的前序序列化.编写一个在不重构树的条件下的可行算法.
每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#'.
思路:

    对于二叉树,每有一个非空节点,就会增加两个空节点,我们可以计算当前树的槽位,每次遍历到一个节点
    就减去一个槽位, 如果该节点是非空节点,就增加两个槽位,如果槽位在某次遍历中小于0个,那么说明
    是错误的
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        solts = 1
        for node in preorder.split(','):
            solts -= 1
            if solts < 0:
                return False
            if node != '#':
                solts += 2
        return solts == 0


if __name__ == "__main__":
    test = '9,3,4,#,#,1,#,#,2,#,6,#,#'
    s = Solution()
    print(s.isValidSerialization(test))
