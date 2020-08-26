"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwz4lj/
题目名: 寻找重复数
题目描述: 给定一个包含n+1个整数的数组nums,其数字都在1到n之间(包括1和n),可知至少存在一个重复的整数.
假设只有一个重复的整数,找出这个重复的数
    1. 不能更改原数组
    2. 只能使用额外的O(1)空间
    3. 时间复杂度小于O(n^2)
    4. 数组中只有一个重复的数字,但它可能不止重复出现一次
示例:
    输入: [1, 3, 4, 2, 2]
    输出: 2
思路:
1. 二分法
    对于数组nums[1, 2, 3, 4, 2],它的所有数都在[1, 2, 3, 4]中
    我们二分的依据是对于[1, 2, 3 ,4]中的数字num,在数组中小于等于num
    个数字的个数count.
    我们对[1, 2, 3, 4]进行二分,
    对于数字2,它的count = 3, 重复的元素出现在了[1, 2]中,那么缩小右边界到2
    此时范围为[1, 2]
    对于数字1,它的count = 1,说明重复的元素在1的右边,那么缩小左边界到2
    此时left == right, 所以结果就是2
2. 快慢指针
    对于数组nums[1, 2, 3, 4, 2],我们将它的value看做是指向下一个节点的指针,那么对于
    重复的元素,就会有多个节点指向了同一个节点,也就是形成了环,那么就可以用快慢指针来做,
    他们必然会在环中相遇,相遇后让slow回到原点,然后两个指针同步走,再次相遇的地方就是
    环的入口,也就是答案
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums)
        # left = 1
        # right = n - 1
        # while left < right:
        #     mid = (left + right) >> 1
        #     cut = 0
        #     for num in nums:
        #         if num <= mid:
        #             cut += 1
        #     if cut <= mid:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    test = [2, 2, 3, 2, 2]
    s = Solution()
    print(s.findDuplicate(test))
