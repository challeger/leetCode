"""
day: 2020-08-31
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdnjqd/
题目名: 有序数组中第K小的元素,其中每行和每列均按升序排列,找到矩阵中第k小的元素
示例:
    输入: matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ],
    k = 8,
    输出: 13
思路:
1. 堆排序
    我们维护一个最小堆,首先将每一行的行首建立一个最小堆.
    然后进行k-1次循环,每次循环弹出堆首,并且将堆首的下一个元素放入堆中,完成操作后
    此时的堆首就是我们要找的元素
2. 二分查找
    每次我们选择矩阵的中间元素mid,判断矩阵中,小于或等于mid的元素有多少,
    若比它小的元素的数量num >= k,那么说明我们要找的元素target<=mid,那么收缩右边的范围
    若num < k,说明target > mid,那么此时收缩左边的范围
    因为我们矩阵并不是有序的,所以采用值来作为二分的标准
"""
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(i):
            x, y = n-1, 0
            num = 0
            # 自下而上扫描每一列,计算小于等于mid的数量
            while x >= 0 and y < n:
                if matrix[x][y] <= mid:
                    num += x + 1
                    y += 1
                else:
                    x -= 1
            # 当mid的值小于target时,num的值必然小于k,因为num没有计算target本身,所以target必然在 [mid+1, right]中
            # 当mid的值大于或等于target时,那么num的值大于等于k,mid的值可能不在矩阵中,所以不能直接返回mid作为答案
            # 而是将其作为右边界,继续搜索target
            return num >= k
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        # 循环结束时,left == right, 因为left <= target, right >= target,当他们相等时,结果就是target
        return left

    def kthSmallest_heapq(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        n = len(matrix)
        # 将每一行的行首建立一个最小堆
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        # 弹出k-1次堆首
        # 并将堆首对应的下一个数加入堆中,以此来维护我们的最小堆
        for i in range(k-1):
            value, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y+1], x, y+1))
        # 此时堆首就是我们要找的元素
        return pq[0][0]


if __name__ == "__main__":
    test = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    test_1 = 8
    s = Solution()
    print(s.kthSmallest(test, test_1))
