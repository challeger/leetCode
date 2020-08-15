"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnkq37/
题目名: 最小栈
题目描述: 设计一个支持push, pop, top操作,并能在常数时间内检索到最小元素的栈
    push -> 将元素推入栈中
    pop -> 删除栈顶的元素
    top ->获取栈顶元素
    getMin -> 检索栈中的最小元素
示例:
    输入：
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    输出：
    [null,null,null,null,-3,null,0,-2]

    解释：
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.
思路:
1. 额外使用一个栈
    额外定义一个栈来存放每个栈顶对应的最小元素,每次进行push操作时,
    将最小栈栈顶元素与插入的元素对比,取最小值插入最小栈中
2. 不使用额外栈
    定义一个变量min,用于存放该栈中最小元素
    push:
    栈中存放的元素不是插入的x,而是x与之前栈中最小元素的差值, 在第一次push时,差值为0,最小值为x,
    之后每次push操作,都将push x-min,然后对比min与x,取它们的最小值.
    top:
    在获取栈顶元素时,判断当前栈顶元素是否大于0,大于0说明当前栈顶不是最小元素
    返回栈顶元素与min的和即可,否则说明当前栈顶元素是最小元素,返回min即可
    pop:
    判断弹出的栈顶元素是否小于0,若小于0,说明弹出的栈顶元素在弹出之前是最小元素,所以我们的
    min = min - top,这样就变成了栈顶元素push进来之前的最小元素
"""


# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min = [float('inf')]

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.min.append(min(x, self.min[-1]))

#     def pop(self) -> None:
#         self.stack.pop()
#         self.min.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min[-1]


class MinStack:

    def __init__(self):
        self.diff = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if not self.diff:
            self.diff.append(0)
            self.min = x
        else:
            compare = x - self.min
            self.diff.append(compare)
            self.min = min(x, self.min)

    def pop(self) -> None:
        if self.diff:
            top = self.diff.pop()
            if top < 0:
                self.min = self.min - top

    def top(self) -> int:
        if self.diff:
            top = self.diff[-1]
            return top + self.min if top > 0 else self.min
        return -1

    def getMin(self) -> int:
        return self.min if self.min != float('inf') else -1


if __name__ == "__main__":
    pass
