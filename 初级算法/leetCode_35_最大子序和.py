"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn3cg3/
题目名: 最大子序和
题目描述: 给定一个整数数组nums, 找到一个具有最大和的连续子数组(子数组最少包含一个元素),返回
其最大和
示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6  [4, -1, 2, 1]
思路:
1. 动态规划
    nums[:i]的最大子序和, 应该是 nums[:i-1]的最大子序和+nums[i]与nums[i]之间的较大值
    所以我们只需遍历数组,每次获取当前的最大子序和,将其保存到result中,最终返回result即可
2. 分治法
    我们定义一个操作get(a, l, r)表示查询a序列[l, r]区间内的最大子序和,那么最终我们要的
    答案就是get(nums, 0, len(nums)-1),我们取m=(l+r)//2,然后对区间[l, m], [m+1, r]分治
    求解,当区间长度缩小到1时,递归开始回升.这时我们需要将[l, m]和[m+1, r]区间的信息合并成
    区间[l, r]的信息

    对于一个区间[l, r],我们可以维护四个量:
        lSum:表示[l, r]内以l为左端点的最大子段和
        rSum:表示[l, r]内以r为右端点的最大子段和
        mSum:表示[l, r]内的最大子段和
        iSum:表示[l, r]的区间和
    设[l, r]为a, [l, m]为b, [m+1, r]为c
    a的iSum就是b的iSum+c的iSum
    a的lSum,要么是b的lSum,要么是b的iSum+c的lSum
    a的rSum,要么是c的rSum,要么是c的iSum+b的rSum
    a的mSum,要么是b的mSum,要么是c的mSum,要么是b的rSum与c的lSum的和,取最大值
"""


class Solution:
    class Status:
        def __init__(self, lSum, rSum, mSum, iSum):
            self.lSum = lSum
            self.rSum = rSum
            self.mSum = mSum
            self.iSum = iSum

    def pushup(self, left: Status, right: Status):
        # a的iSum就是b的iSum+c的iSum
        iSum = left.iSum + right.iSum
        # a的lSum,要么是b的lSum,要么是b的iSum+c的lSum
        lSum = max(left.lSum, left.iSum+right.lSum)
        # a的rSum,要么是c的rSum,要么是c的iSum+b的rSum
        rSum = max(right.rSum, right.iSum+left.rSum)
        # a的mSum,要么是b的mSum,要么是c的mSum,要么是b的rSum与c的lSum的和,取最大值
        mSum = max(max(left.mSum, right.mSum), left.rSum+right.lSum)
        return self.Status(lSum, rSum, mSum, iSum)

    def getInfo(self, a, left, right):
        if left == right:
            return self.Status(a[left], a[left], a[left], a[left])
        m = (left + right) // 2
        lSub = self.getInfo(a, left, m)
        rSub = self.getInfo(a, m+1, right)
        return self.pushup(lSub, rSub)

    def maxSubArray(self, nums: list) -> int:
        return self.getInfo(nums, 0, len(nums)-1).mSum
        # if nums:
        #     prev = 0
        #     result = nums[0]
        #     for i in nums:
        #         prev = max(prev+i, i)
        #         result = max(result, prev)
        #     return result


if __name__ == "__main__":
    s = Solution()
    test = [-2, 1, -3, 4, -1, 2, 1, -3, 4]
    print(s.maxSubArray(test))
