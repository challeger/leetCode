"""
day: 2020-08-24
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwnvrj/
题目名: 多数元素
题目描述: 给定一个大小为n的数组,找到其中的多数元素.多数元素是指在数组中出现次数大于 n/2 的元素
可以假定数组是非空的,并且给定的数组总数存在多数元素
示例:
    输入: [3,2,3]
    输出: 3
    输入: [2,2,1,1,1,2,2]
    输出: 2
思路:
1. 哈希表
    遍历数组记录出现的次数,然后返回出现次数最多的数字
2. 排序
    排好序后,因为多数元素的长度超过了一半,所以中点必然是多数元素
3. 投票算法
    用candidate来表示候选人
    用count表示当前候选人的票数
    遍历Nums,若count=0,则将当前的num赋给candidate
    当num == candidate时, count + 1
    否则 count - 1
    因为多数元素的数量超过了数组中的一半,而且每个元素只会投给自己,
    所以最终candidate的count必然是最多的,所以最终的结果也必然是它
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 哈希表
        # from collections import Counter
        # count = Counter(nums)
        # return count.most_common(1)[0][0]
        # 排序
        # nums.sort()
        # return nums[len(nums) // 2]
        # 投票算法
        count = 0
        candidate = None
        for num in nums:
            if not count:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate


if __name__ == "__main__":
    test = [2, 2, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElement(test))
