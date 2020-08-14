"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnumcr/
题目名: 合并两个有序数组
题目描述: 给定两个有序整数数组nums1和nums2,将nums2合并到nums1中,使nums1成为一个有序数组
初始化num1和nums2的元素数量分别为m和n
nums1有足够的空间来保存nums中的元素
示例:
    输入:
    nums1 = [1, 2, 3, 0, 0, 0], m = 3
    nums2 = [2, 5, 6], n = 3
    输出:
    [1, 2, 2, 3, 5, 6]
思路:
1. sorted
    直接组成数组重新排序
2. 双指针 从头开始
    把nums1[:m]取出来放到一个数组temp中,将nums1[:]置空,然后定义双指针
    分别遍历temp和nums2,比较谁的值更小就将谁的值放到nums1中并将指针往右移
    当某个指针移动到尾部时,就将另一个数组剩下的值全部放到nums1中.
3. 三指针 从尾开始
    p->从nums1的尾部开始, p1->从nums1有效数组的尾部开始, p2->从nums2的尾部开始
    将p1与p2指向的值的最大值放到p指向的值中,然后将p与对应的指针向左移
    最后要将nums1[:p2+1]替换为p2[:p2+1]
"""


class Solution:
    @staticmethod
    def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = sorted(nums1[:m] + nums2)

        # temp = nums1[:m]
        # nums1[:] = []
        # p1 = p2 = 0
        # while p1 < m and p2 < n:
        #     if temp[p1] < nums2[p2]:
        #         nums1.append(temp[p1])
        #         p1 += 1
        #     else:
        #         nums1.append(nums2[p2])
        #         p2 += 1
        # else:
        #     nums1.extend(temp[p1:] if p1 < m else nums2[p2:])
        p, p1, p2 = m+n-1, m-1, n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]


if __name__ == "__main__":
    foo1 = [2, 2, 0, 0]
    foo2 = [1, 1]
    Solution.merge(foo1, 2, foo2, 2)
    print(foo1)
