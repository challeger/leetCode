"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwqm6c/
题目名: 四数相加II
题目描述: 给定四个包含整数的数组列表A, B, C, D,计算有多少个元组(i, j, k, l),
使得A[i] + B[j] + C[k] + D[l] = 0
所有的A, B, C, D具有相同的长度N
示例:
    输入:
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]

    输出: 2

两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
思路:
    用一个哈希表记录a+b的所有值出现的次数
    然后再遍历C,D,若a+b+c+d=0,呢么a+b=-c-d
    所以我们将字典中所有-c-d的值加起来就是我们的答案
"""
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for a in A:
            for b in B:
                hashmap[a+b] += 1
        count = 0
        for c in C:
            for d in D:
                count += hashmap[-c-d]
        return count


if __name__ == "__main__":
    t1 = [1, 2]
    t2 = [-2, -1]
    t3 = [-1, 2]
    t4 = [0, 2]
    s = Solution()
    print(s.fourSumCount(t1, t2, t3, t4))
