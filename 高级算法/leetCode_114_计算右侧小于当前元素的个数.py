"""
day: 2020-08-29
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdoube/
题目名: 计算右侧小于当前元素的个数
给定一个整数数组nums,按要求返回一个新数组counts,数组counts具有该性质,counts[i]的值是
nums[i]右侧小于nums[i]的元素的数量
示例:
    输入: nums = [5,2,6,1]
    输出: [2, 1, 1, 0]
思路:
1. 索引数组+归并排序
    如果我一个元素在算法执行的过程中位置发生变化,但我们仍想定位它,这时
    可以使用索引数组, 在排序时, 原始数组不会变化, 只会用来比较两个元素的大小
    真正排序的,是他们的索引

    我们在对索引数组进行归并排序时,可以分为几种情况:
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
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        # api解法,bisect.bisect_left可以获取一个数在一个有序数组中
        # 应该插入的位置,对于本题,我们倒序遍历,然后将数插入到有序数组中
        # 它要插入的位置,就是它右边比它小的num的个数
        import bisect
        ans = []
        bst = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(bst, num)
            ans.append(idx)
            bst.insert(idx, num)
        return ans[::-1]
        """

        size = len(nums)
        if not size:
            return []
        elif size == 1:
            return [0]
        temp = [None for _ in range(size)]
        res = [0 for _ in range(size)]
        # 索引数组,进行归并排序时排序的是索引数组
        # 但对比值时对比的是索引对应的nums中的值
        indexes = [i for i in range(size)]
        # 进行归并排序
        self.__merge_and_count_smaller(nums, 0, size-1, temp, indexes, res)
        return res

    def __merge_and_count_smaller(self, nums, left, right, temp, indexes, res):
        if left == right:
            return
        mid = (left + right) >> 1
        # 二分
        self.__merge_and_count_smaller(nums, left, mid, temp, indexes, res)
        self.__merge_and_count_smaller(nums, mid+1, right, temp, indexes, res)
        # 如果左边的数组的尾元素,小于等于右边数组的头元素
        # 因为两边都是升序数组,那么此时整个数组都是有序数组,不用排序
        if nums[indexes[mid]] <= nums[indexes[mid+1]]:
            return
        # 归并
        self.__sort_and_count_smaller(
            nums, left, mid, right, temp, indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        # 复制数组来作为排序的依据
        for i in range(left, right+1):
            temp[i] = indexes[i]
        i = left
        j = mid + 1
        for k in range(left, right+1):
            # 左边先走完
            # 剩余的右边元素都是有序的,添加到数组的末尾.
            if i > mid:
                indexes[k] = temp[j]
                j += 1
            # 如果右边先走完了,那么对于左半边剩余的元素
            # 右边的所有元素都是比它小的
            elif j > right:
                indexes[k] = temp[i]
                res[indexes[k]] += (right - mid)
                i += 1
            # 当左边比右边小时,右边的元素现在走了几个
            # 那么右边数组元素比当前元素小的个数就是几个.
            elif nums[temp[i]] <= nums[temp[j]]:
                indexes[k] = temp[i]
                res[indexes[k]] += (j - mid - 1)
                i += 1
            # 右边元素比左边小,正常走
            else:
                indexes[k] = temp[j]
                j += 1


if __name__ == "__main__":
    test = [5, 2, 6, 1]
    s = Solution()
    print(s.countSmaller(test))
