"""
day: 2020-08-29
url: https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
题目名: 数组中的逆序对
在数组中的两个数字,如果前面一个数字大于后面的数字,则这两个数字组成一个逆序对.
输入一个数组,邱这个数组中的逆序对的总数
示例:
    输入: nums = [7,5,6,4]
    输出: 5
思路:
    我们在进行归并排序时,可以分为几种情况:
    left,right数组都没有遍历完时:
        1. left <= right:
            此时,对于left的值,右边数组比left大的元素的个数,相当于当前right往右走的步数,
            比如此时right已经往右走了1步了,那么右边数组中比left大的元素的个数也就是1
        2. right > left:
            此时我们正常将right右移,这样在下次出现情况1时,那么逆序的个数的计算会+1
        3. right遍历完了:
            当right已经全部走完时,那么对于left中剩下的元素,right数组的全部元素都比它小,
            也就是逆序的个数为右边数组的长度right-mid-1
        4. left遍历完了:
            那么就不存在逆序数组了,这时将右边数组的元素全部加到排序的数组中即可.
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def __merge_dichotomize(left, right):
            if left == right:
                return 0
            mid = (left + right) >> 1
            inv_count = __merge_dichotomize(left, mid) + __merge_dichotomize(mid+1, right)
            # 如果左边数组的末尾小于等于右边数组的开头,
            # 那么这一个数组都是有序的,不用进行排序
            return inv_count if nums[mid] <= nums[mid+1] else __merge_sort(left, mid, right, inv_count)

        def __merge_sort(left, mid, right, inv_count):
            nonlocal temp, nums

            # 左边数组的开头
            i = left
            # 右边数组的开头
            j = mid+1
            for k in range(left, right+1):
                # 左边走完了,那么剩下的都是有序的,添加到排序数组后面
                if i > mid:
                    temp[k] = nums[j]
                    j += 1
                # 右边走完了,那么左边剩余的元素,与右边的所有元素都是逆序对
                # 那么这个元素在现在这个数组中的逆序对数就是右边的元素个数
                elif j > right:
                    temp[k] = nums[i]
                    i += 1
                    inv_count += (right - mid)
                # 如果左边的元素小于等于右边的元素
                # 那么对于这个左边元素,右边元素比它小的个数是右边已经走过的步数
                # 那么逆序对数就是步数
                elif nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                    inv_count += (j - mid - 1)
                else:
                    temp[k] = nums[j]
                    j += 1
            nums[left:right+1] = temp[left:right+1]
            return inv_count

        size = len(nums)
        temp = [0 for _ in range(size)]
        return __merge_dichotomize(0, size-1)


if __name__ == "__main__":
    test = [7, 5, 6, 4]
    s = Solution()
    print(s.reversePairs(test))
