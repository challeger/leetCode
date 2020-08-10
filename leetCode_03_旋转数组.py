"""
day: 2020-08-10
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
题目名: 旋转数组
题目描述: 给定数组,将数组中的元素向右移动k个位置,其中k是非负数
示例:
    给定nums = [1, 2, 3, 4, 5], k = 3
    得到结果 [3, 4, 5, 1, 2]
思路:
1. 暴力替换:
    旋转k次数组,每次旋转将所有元素向右移一位,时间复杂度为O(k*n)
2. 三次反转:
    当我们旋转数组K次, k%n个尾部元素会被移动到头部, 剩下的元素会移动到尾部
    所以我们直接先将整个数组反转,然后反转前面的k个元素与后面的n-k个元素
    [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1] -> [3, 4, 5, 2, 1] -> [3, 4, 5, 1, 2]
    就可以得到我们想要的结果
3. 环状替换
    我们直接将每一个数字放到它最后的位置,然后将该位置原来的数字取出来,将这个数字放到最后的位置
    如此循环len(nums)次,数组就旋转完毕了
    数字旋转后的位置的计算方式为 (原位置 + 偏移量) % 数组长度
"""


class Solution(object):
    @staticmethod
    def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length

        # 暴力旋转
        # while k > 0:
        #     a = nums[-1]
        #     nums[1:length] = nums[0:length-1]
        #     nums[0] = a
        #     k -= 1

        # 翻转三次
        # nums[:] = nums[length-k:] + nums[:length-k]

        # 环状替换
        count = 0
        start = 0
        while count < length:
            current = start
            prev = nums[start]
            while True:
                # 得到目标旋转后的位置的索引
                next_index = (current + k) % length
                # 将目标的值放到旋转后的位置,并将位置上原来的值取出来
                nums[next_index], prev = prev, nums[next_index]
                # 下一次循环计算该位置原来的值的旋转后的位置
                current = next_index
                count += 1
                # 当下一次要计算的位置与开始的位置相等时,说明本次替换已经结束,要从下一个数字开始替换
                if start == current:
                    break
            start += 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 4
    Solution.rotate(nums, k)
    print(nums, len(nums))
