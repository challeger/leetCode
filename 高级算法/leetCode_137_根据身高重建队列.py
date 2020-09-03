"""
day: 2020-09-03
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd6s9j/
题目名: 根据身高重建队列
假设有打乱顺序的一群人站成一个队列,每个人由一个整数对(h, k)表示,其中h是这个人的身高,k是排在这个人前面
且身高大于或等于h的人数.编写一个算法来重建这个队列

总人数少于1100人
示例:
    输入: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    输出: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
思路:
先对数组进行处理,将它按h降序排列,如果有相同的,按k升序排列,然后
按照k依次插入res数组即可.
算法证明:
    因为矮的人并不会影响高的人的顺序,而对于当前的人来说,前面排好序的人都是大于等于它的身高的,
    所以k要求是多少,就插到哪里就行,他前面的k个元素都是比它高或者和他一样的,而再后面插入的元素,
    都是比它矮的,与它没有关系.
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


if __name__ == "__main__":
    test = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    s = Solution()
    print(s.reconstructQueue(test))
