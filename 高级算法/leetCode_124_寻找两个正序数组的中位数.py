"""
day: 2020-09-01
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdvy3h/
题目名: 寻找两个正序数组的中位数
给定两个大小为m和n的正序数组nums1和nums2.
请你找出这两个正序数组的中位数,并且要求算法的时间复杂地为O(log(m+n))
你可以假设nums1和nums2不会同时为空
示例:
    输入: nums1 = [1, 3], nums2 = [2]
    输出: 2.0
    输入: nums1 = [1, 2], nums2 = [3, 4]
    输出: 2.5
思路:
1. 二分法
    m: len(nums1)
    n: len(nums2)
    对于该该问题,我们可以理解为找两个数组中的第k个数
    当m+n % 2 == 1时,那么就是找第(m+n+1)/2个数.
    当m+n % 2 == 0时,那么是找第(m+n)//2与第(m+n)//2 + 1个数,然后求他们的平均值.
    因为两个数组都是有序数组,我们可以直接在两个数组中尝试找他们的第k//2个数,然后将两个
    数进行对比,nums1 --> pivot1, nums2 --> pivot2
    若pivot1 <= pivot2,那么说明对于nums1的第k//2个数,在nums1中有k//2-1个数比它小,
    在nums2中则最多有k//2-1个数比他小,所以我们可以将nums1[0:k//2]的数全部排除,因为
    他们都小于或等于pivot1,但pivot1最多是数组中第k-1个数.
    若pivot1 > pivot2,那么就是排除nums2中的0-k//2个数..
    在我们排除数之后,要将k-排除的数量,并且将对应数组的指针指向下一位数字..然后重新开始二分.
    当我们某个数组被全部排除时,那么只需要返回另一个数组的第k个数即可
    当k==1时,那么只需要返回两个数组的首部较小的一个即可.
2. 划分数组
    对于中位数,它左边的数与右边的数总是相等的
    那么对于两个数组的中位数,我们只需要找到某个分割线,使得分割线左边的数总数等于分割线右边的数.
    m: len(nums1)
    n: len(nums2)
    若m+n为奇数,如果我们能将数组划分为 len(left) = len(right) + 1 && max(left) <= min(right)
    那么数组的中位数就是max(left).
    若m+n为偶数,如果我们能将数组划分为len(left) = len(right) && max(left) <= min(right)
    那么数组的中位数就是 (max(left)+min(right)) // 2
    我们设i与j分别是分割线在nums1与nums2的索引,对于i,在它前面有i个nums1的元素,j同理.
    那么对于我们的len(left) = len(right) + 1,我们只需保证 i+j == m-i+n-j(偶数)
    或者 i+j == m-i+n-j+1(奇数).我们使用//,可以得到条件: i+j == (m+n+1)//2
    对于第二个条件,我们需要保证: nums2[j-1] <= nums1[i] && nums1[i-1] <= nums2[j]
    对于i,j的一些极端条件,比如i==0,j==0,i==m,j==n,我们可以设置正无穷与负无穷来进行替换,这样不会
    影响两边数组最大值最小值的取值.所以我们需要在nums1中找到i,使得:
        nums2[j-1] <= nums1[i] && nums1[i-1] <= nums2[j], j = (m+n+1)//2 - i
    这等价于,我们在nums1中找到一个最大的i,使得:
        nums1[i-1] <= nums2[j], j = (m+n+1)//2 - i
    这是因为,如果i是nums1中最大的满足该条件的值,那么对于i+1,它必然不满足该条件,也就是
        nums1[i] > nums2[j-1],这样就满足了上面的条件2.
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_num(k):
            index1 = index2 = 0
            while True:
                # 当某个数组的数已经全部被排除时,那么就返回另一个数组的第k个数即可
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                # 当k为1时,那么只要返回两个数组的首部的最小值即可
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                # 数组中第k//2个数,取m-1是为了防止越界
                new_index1 = min(index1 + k // 2 - 1, m - 1)
                new_index2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[new_index1], nums2[new_index2]
                # 如果pivot1 <= pivot2,那么说明对于nums1中的第 k // 2个数,
                # 两个数组中总共小于等于它的数,最多不会超过 k - 2 个,所以这个数
                # 不可能是我们要找的第k个数,于是就可以将它左边的所有数全部排除
                # 注意要将k减去排除数的数量,然后将对应数组的指针移动到下一位数字上.
                if pivot1 <= pivot2:
                    k -= new_index1 + 1 - index1
                    index1 = new_index1 + 1
                # 情况处理同pivot1 <= pivot2,只是处理的是nums2
                else:
                    k -= new_index2 + 1 - index2
                    index2 = new_index2 + 1

        m = len(nums1)
        n = len(nums2)
        totalLength = m + n
        if totalLength % 2:
            return get_num((totalLength + 1) // 2)
        else:
            return (get_num(totalLength // 2) + get_num(totalLength // 2 + 1)) / 2

    def findMedianSortedArrays_better(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays_better(nums2, nums1)
        inf = float('inf')
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        # median1: 前一部分的最大值
        # median2: 后一部分的最小值
        median1, median2 = 0, 0
        while left <= right:
            # 前一部分包含了nums1[0...i-1],nums2[0...j-1]
            # 后一部分包含了nums1[i...m-1],nums2[j...n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            # inf与-inf是为了处理边界情况,取正无穷大与负无穷大不会影响我们
            # 两边数组最大最小值的取值
            # 表示nums1[i-1]
            nums_i_1 = (-inf if i == 0 else nums1[i-1])
            # 表示nums1[i]
            nums_i = (inf if i == m else nums1[i])
            # 表示nums2[j-1]
            nums_j_1 = (-inf if j == 0 else nums2[j-1])
            # 表示nums2[j]
            nums_j = (inf if j == n else nums2[j])
            # 我们会一直移动左右边界,直到找到nums1中的最大的i
            # 使得nums1[i-1] <= nums2[j]
            # 那么对于这个最大的i, i+1必然不满足上述条件,也就是nums1[i] > nums2[j-1]
            # 此时的分割线就是我们要找的分割线,那么获得左边数组的最大值,与右边数组的最小值
            # 来求数组的中位数
            if nums_i_1 <= nums_j:
                median1, median2 = max(nums_i_1, nums_j_1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1
        # 当数组长度的和为偶数时,中位数的值是左边数组的最小值与右边数组的最大值之和 // 2
        # 当数组长度的和是奇数时,中位数的值就是左边数组的最小值
        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


if __name__ == "__main__":
    test1 = [1, 3, 5, 7, 9]
    test2 = [2, 4, 6, 8]
    s = Solution()
    print(s.findMedianSortedArrays(test1, test2))
