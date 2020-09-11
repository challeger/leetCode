"""
day: 2020-09-11
url: https://leetcode-cn.com/problems/avoid-flood-in-the-city/
题目名: 避免洪水泛滥
你的国家有无数个湖泊,所有湖泊一开始都是空的.当第 n 个湖泊下雨的时候,如果第 n 个湖泊是空的,那么它就会装满水,否则这个湖泊会发生洪水.
你的目标是避免任意一个湖泊发生洪水.
给你一个整数数组 rains ,其中：
    rains[i] > 0 表示第 i 天时,第 rains[i] 个湖泊会下雨.
    rains[i] == 0 表示第 i 天没有湖泊会下雨,你可以选择 一个 湖泊并 抽干 这个湖泊的水.
请返回一个数组 ans ,满足：
    ans.length == rains.length
如果 rains[i] > 0 ,那么ans[i] == -1 .
如果 rains[i] == 0 ,ans[i] 是你第 i 天选择抽干的湖泊.
如果有多种可行解,请返回它们中的 任意一个 .如果没办法阻止洪水,请返回一个 空的数组 .

请注意,如果你选择抽干一个装满水的湖泊,它会变成一个空的湖泊.但如果你选择抽干一个空的湖泊,那么将无事发生

思路:
    用一个数组sun_days来记录晴天,一个字典full_pools来记录满的湖泊的下雨天数

    当我们在某个下雨天,他要充满的湖泊已经在full_pools中了,那么说明我们需要在这一天之前,在上一次该湖泊下雨的天数之后,抽干这个
    湖泊,那么我们去查找sun_days,尝试找full_pools中记录的下雨天数,在该数组中插入的位置,如果插入的位置在数组的最后面,那么说明
    该数组中没有值比该天大,也就意味着没有哪一天是可以让我们抽干该湖泊的雨水的,所以就返回[]
    否则我们就从数组中删除该天,并在结果数组中将该天的操作设置为抽干该湖泊.
"""
from typing import List
from bisect import bisect_left


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        # 记录可以抽干湖泊的日期
        sun_days = []
        # 以湖泊的索引为键,下雨的天数为值
        full_pools = {}
        for i, val in enumerate(rains):
            if val > 0:
                ans[i] = -1
                # 如果下雨的湖泊在之前已经下过一次
                if val in full_pools:
                    # 利用二分查找法,用离上一次下雨最近的那一天去抽水
                    pos = bisect_left(sun_days, full_pools[val])
                    # 如果要插入的位置在数组的最后面,这两次下雨之间没有抽水的机会,所以就返回[]
                    if pos == len(sun_days):
                        return []
                    # 否则就使用那一天来抽水
                    ans[sun_days.pop(pos)] = val
                # 记录湖泊
                full_pools[val] = i
            else:
                # 记录晴天
                sun_days.append(i)
        return ans
