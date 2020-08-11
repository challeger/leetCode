"""
day: 2020-08-11
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x21ib6/
题目名: 两个数组的交集
题目描述: 给定两个数组,编写一个函数来计算它们的交集
示例:
    给定nums1 = [1, 2, 2, 1, 5, 4, 4], nums2 = [2, 2, 1, 6]
    得到结果 [2, 2, 1]
思路:
1. 使用哈希表记录数字出现的次数:
    选择长度较小的数组,以数组中的数字为键,出现的次数为值,建立一个字典
    然后遍历另一个数组,如果数组的值在字典的键中,则将值添加到结果中,并且字典键对应的值-1
2. 使用双指针:
    将两个数组排序,然后两个指针分别指向两个数组,
    将指针指向的值进行对比,值较小的一方指针向右移一位
    若值相等,则将值添加到结果中,两个指针都向右移一位
"""


class Solution:
    @staticmethod
    def intersect(nums1, nums2):
        # 哈希表
        def _list_to_dict(nums):
            foo = dict()
            for i in nums:
                if i in foo:
                    foo[i] += 1
                else:
                    foo[i] = 1
            return foo

        def _get_list(dict1, nums):
            foo = []
            for i in nums:
                if i in dict1 and dict1[i] > 0:
                    foo.append(i)
                    dict1[i] -= 1
            return foo

        if len(nums1) > len(nums2):
            return _get_list(_list_to_dict(nums2), nums1)
        else:
            return _get_list(_list_to_dict(nums1), nums2)

        # 双指针

        # nums1.sort()
        # nums2.sort()
        # length1, length2 = len(nums1), len(nums2)
        # result = list()
        # index1 = index2 = 0

        # while index1 < length1 and index2 < length2:
        #     if nums1[index1] < nums2[index2]:
        #         index1 += 1
        #     elif nums1[index1] > nums2[index2]:
        #         index2 += 1
        #     else:
        #         result.append(nums1[index1])
        #         index1 += 1
        #         index2 += 1

        # return result


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1, 5, 4, 4]
    nums2 = [2, 2, 1, 6]
    print(Solution.intersect(nums1, nums2))
