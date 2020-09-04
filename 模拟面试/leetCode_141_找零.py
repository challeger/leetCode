"""
day: 2020-09-04
url: https://leetcode-cn.com/problems/lemonade-change/
题目名: 找零
在柠檬水摊上,每一杯柠檬水的售价为5美元,顾客排队购买你的产品,(按账单bills支付的顺序)
一次购买一杯.每位顾客只买一杯柠檬水,然后向你支付5美元,10美元或者20美元,你必须给每位顾客正确找零
也就是说净交易是每位顾客向你支付5美元.
如果你能给每位顾客正确找零,返回true,否则返回false
示例:
    输入: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
    输出: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
思路:
如果是5元,那么5元钱币+1
如果是10元,那么5元钱币-1,10元钱币+1
如果是20元,那么优先尝试10元钱币,10-1,5-1,否则尝试5元钱币,5-3
判断是否透支,存在负数说明透支,返回false
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            else:
                if not ten:
                    five -= 3
                else:
                    five -= 1
                    ten -= 1
            if five < 0 or ten < 0:
                return False
        return True
