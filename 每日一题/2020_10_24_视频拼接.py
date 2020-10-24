"""
day: 2020-10-24
url: https://leetcode-cn.com/problems/video-stitching/
题目名: 视频拼接
你将会获得一系列视频片段,这些片段来自于一项持续时长为 T 秒的体育赛事.这些片段可能有所重叠,也可能长度不一.

视频片段 clips[i] 都用区间进行表示：
开始于 clips[i][0] 并于 clips[i][1] 结束.我们甚至可以对这些片段自由地再剪辑,例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分.

我们需要将这些片段进行再剪辑,并将剪辑后的内容拼接成覆盖整个运动过程的片段([0, T]).返回所需片段的最小数目,如果无法完成该任务,则返回 -1 .

示例:

    输入: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
    输出: 3
    解释: [0, 2], [1, 9], [8, 10]

    输入: clips = [[0,1],[1,2]], T = 5
    输出: -1
思路:
1. 贪心
    首先将列表按右区间的值从大到小排序,然后依次遍历.
    每次遍历时,如果当前视频的右边区间大于或等于我们要求的区间,那么就尝试更新
    下次的目标区间cur,直到当前视频的右边区间小于目标区间,那么就进行 剪辑
    判断目标区间cur的值是否小于当前的右边区间,是说明可以拼接,那就更新目标区间
    并且使用的区间数+1
    否则不能进行拼接,返回-1

2. 动态规划
    用dp[i]来表示区间[0, i)覆盖所需要的最少自取件的数量
    枚举所有子区间,来计算最少的区间数.


3. 贪心2
    首先遍历列表,以left作为索引, right作为值,更新每个left可以到达的最远的right
    然后再从0到T依次遍历,每次都计算last,也就是当前能走的最远距离.
"""
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(reverse=True, key=lambda x: x[1])  # 按结尾从大到小排序
        cur = T  # 目标区间
        n = len(clips)  # 列表长度
        cnt = 0  # 需要的区间数
        i = 0  # 遍历整个列表的指针
        while T:
            # 每次都找到最小的左边区间
            if i < n and clips[i][1] >= T:
                cur = min(cur, clips[i][0])
                i += 1
            else:
                # 更新区间
                if cur < T:
                    T = cur
                    cnt += 1
                # 如果最小的左边区间和当前T相等,那么说明无法拼接
                else:
                    return -1
        return cnt

    def videoStitching_2(self, clips: List[List[int]], T: int) -> int:
        max_list = [0] * T
        last = res = pre = 0
        # 记录每个left能得到的最远的right
        for left, right in clips:
            if left < T:
                max_list = max(max_list[left], right)

        for i in range(T):
            # 计算下次剪辑能剪的最远距离
            last = max(last, max_list[i])
            # 如果相等,说明不能再往后拼接了.
            if i == last:
                return -1
            # 说明走到了上次剪辑时的末尾
            if i == pre:
                res += 1
                pre = last
        return res

    def videoStitching_dp(self, clips: List[List[int]], T: int) -> int:
        dp = [0] + [float('inf')] * T
        for i in range(1, T+1):
            for left, right in clips:
                if left < i <= right:
                    dp[i] = min(dp[i], dp[left] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]
