"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvvuqg/
题目名: 递增的三元子序列
题目描述: 给定一个未排序的数组, 判断这个数组中是否存在长度为3的递增子序列,即:
对于数组nums,存在i,j,k,满足
    0 <= i < j < k < len(nums)
    使得nums[i] < nums[j] < nums[k]
示例:
    输入: [1,2,3,4,5]
    输出: true

    输入: [5, 4, 3, 2, 1]
    输出: false
思路:
    定义两个变量来记录最小值与次小值,每次遍历
    进行对比,
    若i<最小值,则将最小值设为i
    若最小值<i<次小值,则将次小值设为i
    若i>次小值,说明存在递增数列,返回true
    假设在i>次小值之前的一次循环中,替换了最小值,但因为i>次小值,
    且次小值必然大于替换前的最小值,所以没有影响
"""


class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        first = second = float('inf')
        for n in nums:
            if n < first:
                first = n
            elif first < n < second:
                second = n
            elif n > second:
                return True
        return False


if __name__ == "__main__":
    test = [1, 3, 2, 0, 4]
    s = Solution()
    print(s.increasingTriplet(test))
