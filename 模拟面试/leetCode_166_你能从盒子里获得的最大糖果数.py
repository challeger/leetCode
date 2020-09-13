"""
day: 2020-09-13
url: https://leetcode-cn.com/problems/maximum-candies-you-can-get-from-boxes/
题目名: 你能从盒子里获得的最大糖果数
给你n个盒子,每个盒子的格式为[status, candies, keys, containedBoxes],其中：

状态字 status[i]：整数,如果box[i]是开的,那么是1,否则是0.
糖果数 candies[i]: 整数,表示 box[i] 中糖果的数目.
钥匙 keys[i]：数组,表示你打开 box[i] 后,可以得到一些盒子的钥匙,每个元素分别为该钥匙对应盒子的下标.
内含的盒子 containedBoxes[i]：整数,表示放在 box[i] 里的盒子所对应的下标.
给你一个 initialBoxes 数组,表示你现在得到的盒子,你可以获得里面的糖果,也可以用盒子里的钥匙打开新的盒子,还可以继续探索从这个盒子里找到的其他盒子.

请你按照上述规则,返回可以获得糖果的 最大数目 

示例:
    输入：status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
    输出：16
    解释：
    一开始你有盒子 0 .你将获得它里面的 7 个糖果和盒子 1 和 2.
    盒子 1 目前状态是关闭的,而且你还没有对应它的钥匙.所以你将会打开盒子 2 ,并得到里面的 4 个糖果和盒子 1 的钥匙.
    在盒子 1 中,你会获得 5 个糖果和盒子 3 ,但是你没法获得盒子 3 的钥匙所以盒子 3 会保持关闭状态.
    你总共可以获得的糖果数目 = 7 + 4 + 5 = 16 个.
思路:
    记录手中有的盒子与钥匙,每次都尝试打开手中的盒子.
    如果某一次遍历没有打开过盒子,说明不能继续往下打开了,就结束.
"""
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # 手上有的盒子
        my_boxes = set(initialBoxes)
        # 手上有的钥匙
        my_keys = set()
        # 已经开掉的盒子
        visited = set()
        res = 0
        # 表示本轮是否开过盒子
        flag = True
        while flag:
            # 一开始先设置为没开过盒子
            flag = False
            # 记录本轮可能得到的新的盒子与钥匙
            new_box = set()
            new_key = set()
            # 先判断有没有能够直接打开的盒子
            for box in my_boxes:
                if box not in visited and status[box]:
                    flag = True
                    res += candies[box]
                    my_keys.update(keys[box])
                    new_box.update(containedBoxes[box])
                    visited.add(box)
            # 再判断有没有钥匙可以打开的盒子
            for key in my_keys:
                if key not in visited and key in my_boxes:
                    flag = True
                    res += candies[key]
                    new_key.update(keys[key])
                    new_box.update(containedBoxes[key])
                    visited.add(key)
            my_boxes.update(new_box)
            my_keys.update(new_key)
        return res
