"""
day: 2020-09-02
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd8eai/
题目名: 扁平化嵌套列表迭代器
给你一个嵌套的整型列表.请你设计一个迭代器,使其能够遍历这个整型列表中的所有整数.
列表中的每一项或者为一个整数,或者是另一个列表,其中列表的元素也可能是整数或者其他列表

示例:
    输入: [[1, 1], 2, [1, 1]]
    输出: [1, 1, 2, 1, 1]
    输入: [1, [4, [6]]]
    输出: [1, 4, 6]
"""


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 我们的pop()操作是从右边弹,所以需要将列表反转后入栈
        # 这样栈顶元素才是对应的第一个节点
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # 在hasNext中,我们已经保证了栈顶必然是一个数字,所以直接
        # 弹出栈顶拿到数字即可
        return self.stack.pop().getInteger

    def hasNext(self) -> bool:
        # 如果栈顶节点是列表的话,就将该列表反转,然后推入栈顶
        # 反转同样是为了保证列表的第一个元素在栈顶,循环直到栈顶是一个数字
        while len(self.stack) > 0 and not self.stack[-1].isInteger():
            self.stack.extend(self.stack.pop().getList()[::-1])
        return len(self.stack) > 0


class NestedIterator_iter:
    def __init__(self, nestedList: [NestedInteger]):
        self.elements = self.build_generator(nestedList)

    def build_generator(self, nestedList):
        for x in nestedList:
            # 如果是数字就抛出当前节点
            if x.isInteger():
                yield x.getInteger()
            # 否则将当前节点作为列表继续去找,直到找到数字
            else:
                yield from self.build_generator(x.getList())

    def next(self) -> int:
        return self.v

    def hasNext(self) -> bool:
        try:
            self.v = next(self.elements)
            return True
        # 迭代结束
        except StopIteration:
            return False
