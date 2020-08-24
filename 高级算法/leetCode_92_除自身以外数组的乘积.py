"""
day: 2020-08-24
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xw8dz6/
题目名: 除自身以外数组的乘积
题目描述: 给定一个长度为n的整数数组nums, 其中n>1, 返回输出数组output, 其中output[i]等于nums中除nums[i]之外
其余各元素的乘积
要求: 不能使用除法,在O(n)时间复杂度内完成此题
示例:
输入：[1, 2, 3, 4]
输出: [24, 12, 8, 6]
思路:
    除它以外的各元素的乘积,也就是它的左边元素的乘积x右边元素的乘积
    那么我们可以定义两个数组,遍历两次来记录索引为i的元素的左边元素
    的乘积与右边元素的乘积.最后再遍历依次把结果放入output数组中

    额外空间O(1)写法:
    用output数组来记录.
    第一次遍历把让数组中的每个元素都是当前索引的左边元素的乘积
    然后第二次遍历,定义一个变量right来记录当前索引右边元素的乘积
    每次遍历,都让right = right * nums[i],这样就可以维护右边元素的乘积
    这样两次遍历即可完成计算
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # left, right, output = [0]*length, [0]*length, [0]*length
        # left[0] = 1
        # for i in range(1, length):
        #     left[i] = nums[i-1] * left[i-1]
        # right[length-1] = 1
        # for i in reversed(range(length-1)):
        #     right[i] = right[i+1] * nums[i+1]
        # for i in range(length):
        #     output[i] = left[i] * right[i]
        # return output
        output = [0]*length
        output[0] = 1
        # 第一次遍历计算各个元素左边的元素的乘积
        for i in range(1, length):
            output[i] = output[i-1] * nums[i-1]
        right = 1
        # 第二次将右边元素的乘积与左边的乘积相乘,并计算下一个元素的右边元素的乘积
        for i in reversed(range(length)):
            output[i] = output[i] * right
            right *= nums[i]
        return output


if __name__ == "__main__":
    test = [1, 2, 3, 4]
    s = Solution()
    print(s.productExceptSelf(test))
